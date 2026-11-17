---
title: Shared Memory Protocol
type: protocol
status: active
updated: 2026-11-15
tags: [agents, memory, synchronization]
---

# Shared Memory Protocol

## Authority model

- The Obsidian vault is the read/write surface for humans and agents.
- GitHub `main` is the canonical portable shared copy and synchronization source.
- Local Agent files are small routing layers and may contain private,
  machine-specific facts.
- Obsidian is the human-readable authoring and review surface.

## Read cycle

1. `git pull --ff-only`
2. Read [[agents/shared]] and the current Agent adapter.
3. Retrieve only task-relevant linked pages.
4. Match scope, source reliability and validity before replacing a conflicting statement. A newer file modification date alone does not establish authority.

## Write cycle

1. Classify the candidate as durable, temporary, private, or uncertain.
2. Discard temporary chatter.
3. Keep private facts local.
4. Put uncertain portable facts in [[inbox/README|inbox]].
5. Update an existing page when possible.
6. Update [[obsidian-vault/Home]] and [[log]].
7. Run lint, link, index, and sensitive-data checks.
8. Pull/rebase, then publish only with the required authorization.

## Conflict policy

- Never force-push shared memory.
- Do not silently overwrite a contradictory verified fact.
- Record source and date when facts are time-sensitive.
- If a conflict changes user intent or an external action, ask the user.

## Safety boundary

Do not commit secrets, passwords, access tokens, cookies, private keys, private
endpoints, raw conversation archives, or personal contact/payment identifiers.

- A local Vault may intentionally be non-versioned. An empty Git shell with no
  `HEAD` and zero tracked files is not, by itself, an unsafe worktree; validate
  the Vault through its authority contract, required entries, conflict scan,
  links, sensitive scan, backup, and readback.
- Only the portable shared repository and server clone require Git worktree
  cleanliness. Preserve and review unknown changes on either side.
- Python bytecode and `__pycache__` are generated artifacts, never shared
  memory. Ignore them and use AST-based syntax checks that do not create caches.

## Private bridge and multiple computers

- Private Page references and private snapshots stay outside this public repository. Never use a Git commit ID as proof of private content equality.
- A Page must actually be read in the conversation. Its existence does not change account-level memory or prove mobile reading.
- New computers start as readers. Designate one workstation for scheduled merges unless a real cross-machine lock and conflict protocol have been implemented.
- A clean worktree, catalog inclusion or successful health check is not publication authorization. Prepare the batch and verification evidence, obtain the required confirmation, then commit and publish.
- Download-only helpers do not publish. Exporters must honor the applicable publication authorization before committing or pushing; do not execute an unattended publisher merely to diagnose status.
- Report no-content-change, failed preflight, pending approval and published changes separately. Never generate a commit merely to refresh a timestamp.
