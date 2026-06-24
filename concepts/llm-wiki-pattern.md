---
title: LLM Wiki Pattern
created: 2026-06-25
updated: 2026-06-25
type: concept
tags: [llm-wiki, knowledge-base, rag-alternative, research, tooling]
sources: [raw/articles/2026-06-25-llm-wiki-landscape.md]
confidence: medium
---

# LLM Wiki Pattern

The LLM Wiki pattern is a way to turn raw documents into a persistent, interlinked
Markdown knowledge base instead of re-reading everything from scratch on each query.
It keeps knowledge compiled, structured, and incrementally updated over time.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

In practice, the pattern usually separates three layers: raw source capture, generated
wiki pages, and schema/rules for how the wiki should evolve. The most common operations
are ingest, query, and lint or audit.^[raw/articles/2026-06-25-llm-wiki-landscape.md]

This concept is the foundation behind [[kfchou-wiki-skills]], [[ndjordjevic-pin-llm-wiki]],
[[lewislulu-llm-wiki-skill]], and [[nashsu-llm-wiki]]. For the implementation split in
this repo, also see [[llm-wiki-implementations]].
