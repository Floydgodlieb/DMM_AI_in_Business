---
name: check
description: Stage 5 of the handbook pipeline. Generate the tool part of check.md with a fresh live verification run, then judge only the duty-per-recommendation rows (criterion 3). Use when asked to check the draft.
allowed-tools: Bash(python .claude/scripts/verify_claims.py:*), Read, Edit, Grep, Glob
---

# Stage 5 — Check

Read `context.md` §3. The by-hand version is `templates/check.manual.md`.

1. Run `python .claude/scripts/verify_claims.py --draft draft.md --check-md check.md`.
   It re-fetches every live document and writes the whole claim table, the review-queue count and an empty duty table. It keeps the second-reader section and final line if a person already filled them. Do not change anything it wrote.
2. Fill the **duty table only**, one row per recommendation, from the draft text:
   - duty named with claim-id: which duty (AI Act / GDPR / sanctions) and its `[claim-id]`, or `none`;
   - supplier hosting: the location named, `not known` if the draft says so, or `missing`;
   - pass if a duty with claim-id is named and hosting is named or explicitly `not known`; otherwise fail, one short reason.
3. Report: claim rows passing (the script's count), duty rows passing, open review-queue sources. Any fail → return to draft.

## Never
- Fill the second-reader criteria (1, 2, 5, 6), the final decision, or `verified_by`.
- Change a claim, a row the script wrote, or any file but `check.md`.
