---
title: Hermes Memory Adapter
type: agent-adapter
status: active
updated: 2026-07-23
tags: [agents, hermes, memory]
---

# Hermes Memory Adapter

## Startup

1. Update the server clone with `git pull --ff-only`.
2. Read [[agents/shared]] and this adapter.
3. Retrieve only the relevant pages from [[obsidian-vault/Home]].

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
