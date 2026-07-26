#!/usr/bin/env bash
set -euo pipefail

repository_path="${1:-$HOME/global-llm-wiki}"

if [[ ! -d "$repository_path/.git" ]]; then
  printf 'Not a Git repository: %s\n' "$repository_path" >&2
  exit 1
fi

if [[ -n "$(git -C "$repository_path" status --porcelain)" ]]; then
  printf 'Shared-memory worktree is not clean. Preserve and review local changes before syncing.\n' >&2
  exit 1
fi

git -C "$repository_path" fetch origin main
git -C "$repository_path" merge --ff-only origin/main

required=(
  agents/shared.md
  agents/codex.md
  agents/claude.md
  agents/hermes.md
  agents/MEMORY_PROTOCOL.md
  obsidian-vault/Home.md
  obsidian-vault/00-System/OBSIDIAN_MEMORY_MODE.md
)

for relative_path in "${required[@]}"; do
  if [[ ! -f "$repository_path/$relative_path" ]]; then
    printf 'Missing required memory file: %s\n' "$relative_path" >&2
    exit 1
  fi
done

python3 "$repository_path/tools/check-shared-memory.py"

printf 'Shared memory is current: %s\n' "$repository_path"
