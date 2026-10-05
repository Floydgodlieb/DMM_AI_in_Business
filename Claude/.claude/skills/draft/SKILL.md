---
name: draft
description: Stage 4 of the handbook pipeline. Write draft.md from draft.template.md, filling every [CLAIM] slot only from claims_en.md with the claim-id and its labels, and self-check before handing over. Use when asked to draft or redraft the handbook page.
argument-hint: "[optional: the angle the author chose]"
---

# Stage 4 — Draft

Read `context.md` first (§1 reader, §3b criteria, §5 house style). Shape: `templates/draft.template.md`. Claims: `claims_en.md` only — including claims from earlier weeks; they are verified the same way. To find claims by topic you may read `wiki/` (`wiki/index.md`, then topic pages); the wiki only points to claims, so copy every label from `claims_en.md`, never from a wiki page.

## Steps
1. Use the angle the person gave. If none was given, ask for it — the angle is the author's choice, not yours.
2. Follow the template section by section. Every sentence that states a fact ends with `[claim-id, evidence, scope]`, copied exactly from the claim block.
3. Use only claims whose `auto_verified` starts with a date and `AUTO-PASS`, or whose `verified_by` names a person. A claim routed `PERSON` without `verified_by` may enter only with `(awaiting source check)` right after its bracket; a `FAIL` claim never enters.
4. No claim for a slot → `[no claim found: <what was looked for>]`. Never fill it from your own knowledge.
5. Each recommendation is a numbered line starting `1. **<chain step> — <what>.**`, names one step (lead → quotation → contract → payment → export document), says time-saving or customer-touching, carries one complexity label, and names the duty with its claim-id and the supplier's hosting location (or "not known").

## Self-check before handing over (saves a Check → Draft round)
Run `python .claude/scripts/verify_claims.py --draft draft.md --precheck` (no network, seconds). Fix every `FIX:` line and run it again until it reports 0 problems. Then re-read each recommendation against step 5.

Output only `draft.md`. If `check.md` has fails, fix exactly those lines and leave the rest.
