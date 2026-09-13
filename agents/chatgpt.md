---
title: ChatGPT Memory Adapter
type: agent-adapter
status: proposed-local
updated: 2026-09-13
tags: [agents, chatgpt, desktop, mobile, memory]
---

# ChatGPT Memory Adapter

## Scope and boundary

- ChatGPT desktop and mobile can share account-level conversations and Projects,
  but that alone does not prove they have read or written the Obsidian Vault.
- The Vault remains the only durable human-and-agent memory surface; GitHub
  `main` remains its portable, public-safe copy.
- Native ChatGPT must not treat its chat history or product memory as a second
  source of truth. It has no automatic local-Vault read/write permission.

## Desktop and mobile project setup

Use the same signed-in OpenAI account and one Project named `Shared Memory` on
both devices. Add this adapter and the current public-safe shared snapshot to
that Project whenever a refreshed version is approved. In the Project
instructions, require that task work relying on prior context first uses the
provided shared snapshot and asks for a refresh when its version/date is absent
or stale.

## Retrieval and handoff

1. Start from the supplied public-safe snapshot, then retrieve only the pages
   relevant to the request.
2. Do not infer access to local files, private pages, credentials, operational
   data, or another conversation's full history.
3. For a durable observation, emit a compact `MEMORY_CANDIDATE` containing the
   proposed fact, source, date, confidence, privacy classification, and target
   Vault page.
4. A Claude, Codex, or Hermes run verifies, deduplicates, and writes qualified
   candidates through the Vault workflow. ChatGPT does not claim completion
   until that readback is available.

## Safety

Never place private operational facts, credentials, payment or customer data,
complete conversation transcripts, or private local paths in the Project or
portable repository. Publication still requires the current authorization.
