---
title: Codex Memory Adapter
type: agent-adapter
status: active
updated: 2026-07-23
tags: [agents, codex, memory]
---

# Codex Memory Adapter

## Startup

For non-trivial work related to prior projects or user preferences:

1. Pull the local clone with fast-forward only.
2. Read [[agents/shared]].
3. Read the smallest relevant set of pages from [[obsidian-vault/Home]].

## Updates

- Treat local Codex memory as a routing cache, not a competing knowledge store.
- Promote only verified and reusable knowledge to this repository.
- Put uncertain candidates in [[inbox/README|inbox]].
- Run the repository lint and safety checks before committing.

## Local entry point

The machine-level `~/.codex/AGENTS.md` should point to this adapter and the
shared context file.
