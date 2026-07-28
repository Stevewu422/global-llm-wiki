# Wiki Log

> Chronological record of all wiki actions. Append-only.

## [2026-06-25] create | Repo-local LLM Wiki initialized
- Domain: INPAY AI operating system and LLM Wiki implementation patterns
- Created `SCHEMA.md`, `purpose.md`, `index.md`, `log.md`, `inbox.md`, `AGENTS.md`
- Created `raw/`, `entities/`, `concepts/`, `comparisons/`, `queries/`, `_meta/`
- Added seed pages for external LLM Wiki implementations
- Added local CLI: `tools/llm_wiki_cli.py`

## [2026-07-23] import | Public-safe Obsidian AI Agent memory export
- Added `obsidian-vault/` with 45 curated knowledge pages plus export README and index.
- Imported sanitized projects, playbooks, research domains, templates, knowledge map, coverage assessment, and operational timeline.
- Excluded user profile, live context, credentials, private endpoints, IP addresses, workspace state, caches, backups, and server deployment scripts.
- Added the portable Obsidian snapshot convention to `SCHEMA.md`.
- Indexed every exported page in root `index.md`.
## 2026-07-23 — Shared Claude, Codex, and Hermes memory

- Added a common GitHub-backed memory protocol and per-Agent adapters.
- Added a reviewed-memory inbox and a fast-forward-only local sync helper.
- Defined GitHub `main` as portable authority while keeping private and
  machine-specific facts local.

- 2026-07-24 00:24:10: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-24 00:31:39: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-24 06:25:05: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-24 12:25:12: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-24 18:25:19: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-25 00:25:28: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-25 06:25:35: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-25 12:25:41: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-25 18:26:45: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-26 00:26:49: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-26 06:26:57: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-26 12:27:06: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-26 13:10:35: Hermes cron synced public-safe Obsidian memory export (61 files, 2 skipped).

- 2026-07-26 13:11:26: Hermes cron synced public-safe Obsidian memory export (62 files, 2 skipped).

## 2026-07-26 — Harden shared-memory synchronization

- Replaced the retired the legacy snapshot index file route with `obsidian-vault/Home.md`
  across Claude, Codex, Hermes, protocol, and sync adapters.
- Added a read-only publication gate for Wiki links, root-index coverage, legacy
  routes, and common sensitive patterns.
- Kept private `USER.md`, `MEMORY.md`, `CURRENT.md`, Daily, Inbox, credentials,
  endpoints, and server-only facts outside the portable snapshot.
- Required a clean worktree before fast-forward synchronization and retained the
  Linux executable mode for the Bash entry point.

- 2026-07-26 13:48:04: Hermes guarded sync exported public-safe Obsidian memory (62 files, 2 skipped).

- 2026-07-26 14:13:52: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 37 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:14:30: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 36 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:14:55: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 36 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:21:52: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 36 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:22:06: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 36 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:23:33: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 36 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:26:03: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 14:26:10: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-26 20:26:27: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-27 02:26:50: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-27 08:26:58: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-27 14:27:05: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-27 20:27:50: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-28 02:27:56: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-28 08:28:10: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).

- 2026-07-28 14:28:19: Hermes guarded sync exported public-safe Obsidian memory (58 files, 6 skipped, 34 link-sanitized files, 38 EOF-normalized files).
