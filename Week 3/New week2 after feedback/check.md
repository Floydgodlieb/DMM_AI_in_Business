# check.md — week 2 · draft version: 3 (full recheck reopened 2026-09-21, PM decision: all manual checks redone)

**Why reopened:** the week-2 feedback pass (see `open_questions.md`) added the source-decision column below and surfaced a per-row override for S-012/S-014 that did not exist when this file last said PASS. The PM decided the whole Check stage — not just those two sources — goes back to pending: the tool-derivable columns are re-stated below (still true, mechanically re-verified against `sources/`, `claims_en.md` and `appraised.md`), but no row is marked PASS until a person confirms it again.

## Tool checks (one row per [claim-id] in draft.md)
| claim_id | claim exists | quote in source | number/date matches | duty named (crit 3) | labels present (crit 4) | source `decision: use` in appraised.md | pass/fail | note |
|----------|--------------|-----------------|---------------------|---------------------|--------------------------|--------------------------|-----------|------|
| W2-001 | yes | yes (S-001) | yes — draft reads "22.7%... up almost 9 percentage points from 2023", matching the claim | n/a | yes | yes (S-001) | PENDING | `verified_by: "Floyd"` present in claims_en.md, but pending re-check under the reopened Stage 5 |
| W2-002 | yes | yes (S-001) | n/a (draft states direction only) | n/a | yes | yes (S-001) | PENDING | |
| W2-003 | yes | yes (S-002) | n/a (direction only) | n/a | yes | yes (S-002) | PENDING | |
| W2-004 | yes | yes (S-002) | n/a (direction only) | n/a | yes | yes (S-002) | PENDING | |
| W2-005 | yes | yes (S-003) | n/a | yes | yes | yes (S-003) | PENDING | |
| W2-006 | yes | yes (S-004) | n/a | yes | yes | yes (S-004) | PENDING | |
| W2-007 | yes | yes (S-004) | n/a | yes | yes | yes (S-004) | PENDING | |
| W2-008 | yes | yes (S-004) | n/a | yes | yes | yes (S-004) | PENDING | |
| W2-009 (×2: Duties, Rec. 3) | yes | yes (S-005) | n/a | yes | yes | yes (S-005) | PENDING | |
| W2-010 | yes | yes (S-005) | n/a | yes | yes | yes (S-005) | PENDING | |
| W2-011 | yes | yes (S-006) | yes | n/a | yes | yes (S-006) | PENDING | |
| W2-012 | yes | yes (S-006) | n/a | n/a | yes | yes (S-006) | PENDING | |
| W2-013 | yes | yes (S-007) | n/a | n/a | yes | yes (S-007) | PENDING | |
| W2-014 | yes | yes (S-007) | n/a | n/a | yes | yes (S-007) | PENDING | |
| W2-019 | yes | yes (S-010) | n/a | n/a | yes | yes (S-010) | PENDING | S-010 itself carries a content-authenticity flag (sources/S-010.md) — re-open in a browser again as part of this recheck, don't rely on the earlier pass |
| W2-020 (×2: Duties, Rec. 2, Rec. 4) | yes | yes (S-011) | n/a | yes | yes | yes (S-011) | PENDING | |
| W2-021 | yes | yes (S-012) | n/a | n/a | yes | yes (S-012 — per-row override, see appraised.md) | PENDING | override is new this week; needs a person's sign-off, not just the assistant's reasoning |
| W2-022 | yes | yes (S-012) | n/a | n/a | yes | yes (S-012 — per-row override, see appraised.md) | PENDING | as above |
| W2-023 (×2) | yes | yes (S-012) | n/a | n/a (Rec. 3's own duty covered by W2-009) | yes | yes (S-012 — per-row override, see appraised.md) | PENDING | as above |
| W2-024 | yes | yes (S-013) | n/a | n/a | yes | yes (S-013) | PENDING | |
| W2-025 (×2) | yes | yes (S-013) | n/a | yes (Rec. 2 cites W2-020) | yes | yes (S-013) | PENDING | |
| W2-026 | yes | yes (S-014) | n/a | yes | yes | yes (S-014 — per-row override, see appraised.md) | PENDING | override is new this week |
| W2-027 | yes | yes (S-014) | yes ("60%" matches) | yes | yes | yes (S-014 — per-row override, see appraised.md) | PENDING | override is new this week; this is the riskiest row (unverified vendor figure) — recommend a person look at this one first |
| W2-028 | yes | yes (S-015) | n/a | n/a | yes | yes (S-015) | PENDING | `verified_by` line is still malformed YAML in claims_en.md: `verified_by: ""Floyd` — needs a person to fix directly, not the assistant |
| W2-029 | yes | yes (S-015) | n/a | n/a | yes | yes (S-015) | PENDING | |
| W2-030 | yes | yes (S-015) | n/a | n/a | yes | yes (S-015) | PENDING | |
| W2-031 | yes | yes (S-016) | n/a | n/a | yes | yes (S-016) | PENDING | |

**Summary: 27 claim rows, all PENDING re-check** (0 confirmed PASS, 0 FAIL). The columns up to and including the new source-decision one are the tool's own re-verification against `sources/`, `claims_en.md` and `appraised.md`, and are unchanged from before; only the final pass/fail verdict was reset, because that verdict is Check's human sign-off, not something the assistant can restore on its own say-so.

## Second reader: Floyd (not the author)
| criterion | pass/fail | one line |
|-----------|-----------|----------|
| 1 names a step, not a tool | PENDING | |
| 2 time-saving vs customer-touching, stated | PENDING | |
| 5 complexity label per recommendation | PENDING | |
| 6 one next step: owner, cost, 3-month check | PENDING | |

Five statements opened against the original source: `[claim-id]` × 5 — **TODO, Floyd to fill.** (Week-2 feedback: it was not known which five statements the second reader opened; the assistant cannot record what it did not do.) → result: PENDING

## Final: PENDING re-check (Stage 5 reopened 2026-09-21) · was: publish, decided by Floyd, 17-09-2026 · reopened by: PM decision, 2026-09-21
