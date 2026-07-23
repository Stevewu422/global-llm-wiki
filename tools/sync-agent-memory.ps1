param(
    [string]$RepositoryPath = (Join-Path $HOME 'global-llm-wiki')
)

$ErrorActionPreference = 'Stop'

if (-not (Test-Path -LiteralPath (Join-Path $RepositoryPath '.git'))) {
    throw "Not a Git repository: $RepositoryPath"
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
    'obsidian-vault/index.md'
)

foreach ($relativePath in $required) {
    $fullPath = Join-Path $RepositoryPath $relativePath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        throw "Missing required memory file: $relativePath"
    }
}

Write-Output "Shared memory is current: $RepositoryPath"
