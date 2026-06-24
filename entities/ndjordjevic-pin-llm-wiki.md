---
title: ndjordjevic/pin-llm-wiki
created: 2026-06-25
updated: 2026-06-25
type: entity
tags: [llm-wiki, skill, ingest, operations, obsidian, tooling]
sources: [raw/articles/2026-06-25-llm-wiki-landscape.md]
confidence: medium
---

# ndjordjevic/pin-llm-wiki

`pin-llm-wiki` packages the [[llm-wiki-pattern]] as a queue-driven source ingestion
workflow. Its distinctive pieces are `inbox.md`, `AGENTS.md`, `raw/`, and `wiki/`,
which together make source collection and later ingestion easy to stage.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

This pattern is especially useful when humans or agents keep finding links during the
day and want to defer full processing until a later ingest pass.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

Compared with [[kfchou-wiki-skills]], it is more pipeline-shaped. Compared with
[[lewislulu-llm-wiki-skill]], it spends less emphasis on feedback tooling.
