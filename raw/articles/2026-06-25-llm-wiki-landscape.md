---
source_url: local://2026-06-25-llm-wiki-landscape
ingested: 2026-06-25
sha256: e76086f8fa8a08c8a1474255df74a626ec1cd88f5c7931ab4764f5025665296c
---

# 2026-06-25 LLM Wiki implementation landscape

This local source records the implementation landscape reviewed on 2026-06-25.

- Karpathy LLM Wiki pattern: persistent markdown wiki instead of re-deriving from raw RAG every time.
- `kfchou/wiki-skills`: explicit `wiki-init`, `wiki-ingest`, `wiki-query`, `wiki-lint`, `wiki-update`, `wiki-audit` skill split.
- `ndjordjevic/pin-llm-wiki`: queue-driven ingest with `inbox.md`, `AGENTS.md`, `raw/`, and `wiki/`.
- `lewislulu/llm-wiki-skill`: OpenClaw / Codex-oriented implementation with audit plugin and local web viewer.
- `nashsu/llm_wiki`: desktop application version with UI, graph, queue, MCP, local API, and agent skill support.

This file is intentionally short and acts as the initial seed source for the wiki.
