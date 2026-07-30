param(
    [string]$RepositoryPath = (Join-Path $HOME 'global-llm-wiki')
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath (Join-Path $RepositoryPath '.git'))) {
    throw "Not a Git repository: $RepositoryPath"
}

$worktreeState = @(git -C $RepositoryPath status --porcelain)
if ($LASTEXITCODE -ne 0) { throw 'git status failed' }
if ($worktreeState.Count -gt 0) {
    throw 'Shared-memory worktree is not clean. Preserve and review local changes before syncing.'
}

git -C $RepositoryPath fetch origin main
if ($LASTEXITCODE -ne 0) { throw 'git fetch failed' }

git -C $RepositoryPath merge --ff-only origin/main
if ($LASTEXITCODE -ne 0) {
    throw 'Fast-forward update failed. Preserve local work and resolve it on a branch.'
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

Write-Output "Shared memory is current: $RepositoryPath"
