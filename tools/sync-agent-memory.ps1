param(
    [string]$RepositoryPath = (Join-Path $HOME 'global-llm-wiki')
)

# Read-side refresh for the shared memory copy. This script never commits,
# stashes, resets or pushes. Exit codes:
#   0  readable: SYNC_STATUS=updated | current | current-local-pending
#   2  blocked: remote has new commits while local changes are pending review
#   1  any other failure (fetch, diverged history, missing files, gates)

$ErrorActionPreference = 'Stop'

function Invoke-Git {
    $output = & git -C $RepositoryPath @args
    if ($LASTEXITCODE -ne 0) { throw "git $($args -join ' ') failed with exit code $LASTEXITCODE" }
    return $output
}

if (-not (Test-Path -LiteralPath (Join-Path $RepositoryPath '.git'))) {
    throw "Not a Git repository: $RepositoryPath"
}

# --no-optional-locks keeps status from rewriting .git/index, so the
# common "already current" path needs no write access to the repository
# (sandboxed agents may only have read/execute there).
$pending = @(Invoke-Git --no-optional-locks status --porcelain)

$remoteSha = ([string](Invoke-Git ls-remote origin refs/heads/main)).Trim() -split '\s+' | Select-Object -First 1
$headSha = ([string](Invoke-Git rev-parse HEAD)).Trim()
if ([string]::IsNullOrWhiteSpace($remoteSha)) { throw 'origin has no refs/heads/main' }

if ($remoteSha -eq $headSha) {
    $ahead = 0
    $behind = 0
}
else {
    # Remote differs: fetch (updates remote-tracking refs only, never the worktree).
    try {
        Invoke-Git fetch --quiet origin main | Out-Null
    }
    catch {
        Write-Output "SYNC_STATUS=blocked-fetch-failed head=$($headSha.Substring(0,7)) remote=$($remoteSha.Substring(0,7))"
        Write-Output 'Remote main differs from HEAD and fetch failed (network, or no write access to .git in a sandbox).'
        exit 1
    }
    $counts = ([string](Invoke-Git rev-list --left-right --count 'HEAD...origin/main')).Trim() -split '\s+'
    $ahead = [int]$counts[0]
    $behind = [int]$counts[1]
}

if ($behind -gt 0) {
    if ($pending.Count -gt 0) {
        Write-Output "SYNC_STATUS=blocked-dirty-behind ahead=$ahead behind=$behind pending_files=$($pending.Count)"
        Write-Output 'Remote has new commits but local changes are pending review. Worktree left untouched:'
        $pending | ForEach-Object { Write-Output "  $_" }
        exit 2
    }
    $null = Invoke-Git merge --ff-only --quiet origin/main
    $syncStatus = 'updated'
}
elseif ($pending.Count -gt 0) {
    $syncStatus = 'current-local-pending'
}
else {
    $syncStatus = 'current'
}

$required = @(
    'agents/shared.md',
    'agents/codex.md',
    'agents/claude.md',
    'agents/hermes.md',
    'agents/MEMORY_PROTOCOL.md',
    'obsidian-vault/Home.md',
    'obsidian-vault/00-System/OBSIDIAN_MEMORY_MODE.md',
    'tools/check-python-syntax.py'
)

foreach ($relativePath in $required) {
    $fullPath = Join-Path $RepositoryPath $relativePath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        throw "Missing required memory file: $relativePath"
    }
}

$checker = Join-Path $RepositoryPath 'tools\check-shared-memory.py'
if (-not (Test-Path -LiteralPath $checker)) {
    throw 'Missing shared-memory publication checker'
}

$env:PYTHONDONTWRITEBYTECODE = '1'
python -B $checker
if ($LASTEXITCODE -ne 0) { throw 'Shared-memory publication gates failed' }

$syntaxChecker = Join-Path $RepositoryPath 'tools\check-python-syntax.py'
python -B $syntaxChecker
if ($LASTEXITCODE -ne 0) { throw 'Python syntax gates failed' }

Write-Output "SYNC_STATUS=$syncStatus ahead=$ahead behind_before=$behind pending_files=$($pending.Count)"
if ($ahead -gt 0) {
    Write-Output "Local commits not on origin/main: $ahead (unpublished)."
}
if ($pending.Count -gt 0) {
    Write-Output 'PENDING_LOCAL_CHANGES (read-only; needs owner review and batch approval before any commit or push):'
    $pending | ForEach-Object { Write-Output "  $_" }
}
Write-Output "Shared memory is current: $RepositoryPath"
exit 0
