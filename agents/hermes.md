---
title: Hermes Memory Adapter
type: agent-adapter
status: active
updated: 2026-10-11
tags: [agents, hermes, memory]
---

# Hermes Memory Adapter

## Startup

1. Run `bash tools/sync-agent-memory.sh` from the shared repository. This
   checks for a clean worktree, fetches and fast-forwards `origin/main`, then
   validates required entries, links, index coverage, sensitive patterns and
   Python syntax. Stop on failure; preserve unknown local changes.
2. Read [[agents/shared]] and this adapter, following
   [[agents/MEMORY_PROTOCOL]].
3. Retrieve only relevant pages from [[obsidian-vault/Home]], the canonical
   snapshot entry. The root [[index]] is a catalog, not a second Vault entry.
4. For private context, use the local Vault's user profile, current context
   and memory routing pages. Do not substitute an old public snapshot for
   private or live operational facts.

The startup helper is download-only. A successful sync does not export local
memory, publish changes, update another device, or synchronize ChatGPT memory.

## Local memory boundary

- `~/.hermes/memories/USER.md` contains a compact user profile and retrieval
  pointer.
- `~/.hermes/memories/MEMORY.md` contains a compact operational pointer and
  verified server-local facts.
- The Obsidian vault is the read/write surface; GitHub is the portable shared copy.
- Server-only facts, credentials, and private endpoints must stay local.

## Updates

- Use a branch or [[inbox/README|inbox]] for candidate memory.
- Pull before writing and never force-push.
- Resolve conflicts by preserving both verified facts and recording provenance.
