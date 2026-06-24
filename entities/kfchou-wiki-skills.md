---
title: kfchou/wiki-skills
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm-wiki, skill, codex, tooling, ingest, query, lint, audit]
sources: [raw/articles/2026-06-25-llm-wiki-landscape.md]
confidence: medium
---

# kfchou/wiki-skills

`kfchou/wiki-skills` is a Claude Code-oriented implementation of the [[llm-wiki-pattern]]
that splits the workflow into explicit reusable skills such as init, ingest, query,
lint, update, and audit.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

Its strongest idea is the operational decomposition: instead of one giant instruction
set, the wiki lifecycle becomes a set of named actions that are easier to invoke,
test, and reason about.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

Compared with [[ndjordjevic-pin-llm-wiki]], it is less queue-centric. Compared with
[[nashsu-llm-wiki]], it is much lighter and more harness-native.
