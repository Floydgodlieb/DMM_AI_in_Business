---
name: verify-claims
description: End of Stage 3. Mechanically verify claims in claims_en.md against the saved excerpt and the live source document, write auto_verified per claim, and build review_queue.md with the only sources a person must open (context.md §3c). Use after Translate, before Draft, and whenever claims or sources change.
allowed-tools: Bash(python .claude/scripts/verify_claims.py:*), Read
---

# Verify claims

Run from `platform/` — no agent needed, this is one command:

`python .claude/scripts/verify_claims.py --write --changed`

`--changed` re-fetches only claims whose claim, excerpt or rating changed since the last run (or whose page could not be read last time). Use `--write` without `--changed` for a full live re-check, e.g. at the start of a week; Check always does a full one.

Report the summary line, every `PERSON` source in `review_queue.md` with its trigger (the person's whole checking job), and every `FAIL` (back to `/translate`).

## Rules
- The script routes; you never re-route. Never write `verified_by`, never put a name in `auto_verified`.
- If the script cannot run, say so and stop. Do not verify by reading pages yourself.
- `--offline` routes every claim to a person; only when there is no network, and say so.
