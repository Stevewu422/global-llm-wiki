# Global LLM Wiki

This is the cross-project LLM Wiki for Codex/Hermes/OpenClaw work on this machine.

## Canonical Paths

- Wiki root: `~/wiki`
- CLI: `~/.codex/tools/llm_wiki_cli.py`

## What It Is For

- Durable knowledge that should survive across repositories and sessions
- External research worth reusing later
- Reusable workflow patterns, tool comparisons, and operating notes
- High-signal implementation summaries that should not stay trapped in chat history

## Quick Commands

```powershell
python ~/.codex/tools/llm_wiki_cli.py status
python ~/.codex/tools/llm_wiki_cli.py queue https://example.com
python ~/.codex/tools/llm_wiki_cli.py lint
```

## Working Model

- `raw/` stores source captures
- `entities/`, `concepts/`, `comparisons/`, and `queries/` store curated pages
- `SCHEMA.md` defines structure
- `purpose.md` defines why the wiki exists
- `index.md` and `log.md` are required maintenance files
- `tools/llm_wiki_cli.py` provides a minimal local CLI for queue, status, and lint
