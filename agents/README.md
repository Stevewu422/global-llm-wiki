---
title: Shared Agent Memory
type: index
status: active
updated: 2026-07-23
tags: [agents, memory, github]
---

# Shared Agent Memory

This directory is the portable entry point for Claude, Codex, and Hermes.

## Read order

1. [[agents/shared|Shared operating context]]
2. The current agent adapter:
   - [[agents/claude|Claude]]
   - [[agents/codex|Codex]]
   - [[agents/hermes|Hermes]]
3. [[obsidian-vault/index|Obsidian vault index]]
4. The project or playbook relevant to the current task

## Write path

- Durable, verified knowledge belongs in an existing structured page.
- Unreviewed candidate memory belongs under [[inbox/README|inbox]].
- Agent-specific implementation details belong in the relevant adapter.
- Never store complete chat transcripts, credentials, tokens, private endpoints,
  or personal contact details.

See [[agents/MEMORY_PROTOCOL|Shared memory protocol]] for synchronization and
conflict rules.
