# Wiki Agent Guide

## First Read

Before modifying this wiki, read:
1. `SCHEMA.md`
2. `purpose.md`
3. `index.md`
4. Recent entries in `log.md`

## Operating Rules

- Treat `raw/` as immutable source capture.
- Prefer updating existing pages over creating duplicates.
- Add every new page to `index.md`.
- Append meaningful actions to `log.md`.
- Use `[[wikilinks]]` generously so pages do not become isolated.
- Do not store secrets, credentials, or private endpoints in this wiki.

## Local Helper

Use the local CLI:

```powershell
python ~/.codex/tools/llm_wiki_cli.py status
python ~/.codex/tools/llm_wiki_cli.py queue https://example.com
python ~/.codex/tools/llm_wiki_cli.py lint
```

## Cross-project Rule

- This wiki is global and should be reused across projects.
- Project-local notes can reference it, but the canonical long-term memory lives here.
- When a repo needs durable knowledge, add raw sources or structured pages here first.

## Shared Agent Memory

- Claude, Codex, and Hermes share this repository as their portable long-term memory.
- Start with `agents/shared.md`, then read the current adapter under `agents/`.
- Retrieve only task-relevant pages from `obsidian-vault/Home.md`.
- Follow `agents/MEMORY_PROTOCOL.md` for writes and conflict handling.
- Keep credentials, private endpoints, and machine-specific private facts local.
