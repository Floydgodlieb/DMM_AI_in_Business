# check.md — week 2 · draft version: 2 (after W2-001 rewrite, Rec.2/Rec.3 duty fixes, verified_by filled)

## Tool checks (one row per [claim-id] in draft.md)
| claim_id | claim exists | quote in source | number/date matches | duty named (crit 3) | labels present (crit 4) | pass/fail | note |
|----------|--------------|-----------------|---------------------|---------------------|--------------------------|-----------|------|
| W2-001 | yes | yes (S-001) | yes — draft now reads "22.7%... up almost 9 percentage points from 2023", matching the claim | n/a | yes | PASS | rewritten; `verified_by: "Floyd"` now present |
| W2-002 | yes | yes (S-001) | n/a (draft states direction only) | n/a | yes | PASS | `verified_by: "Floyd"` |
| W2-003 | yes | yes (S-002) | n/a (direction only) | n/a | yes | PASS | `verified_by: "Floyd"` |
| W2-004 | yes | yes (S-002) | n/a (direction only) | n/a | yes | PASS | `verified_by: "Floyd"` |
| W2-005 | yes | yes (S-003) | n/a | yes | yes | PASS | `verified_by: "Ivan"` |
| W2-006 | yes | yes (S-004) | n/a | yes | yes | PASS | `verified_by: "Ivan"` |
| W2-007 | yes | yes (S-004) | n/a | yes | yes | PASS | `verified_by: "Ivan"` |
| W2-008 | yes | yes (S-004) | n/a | yes | yes | PASS | `verified_by: "Ivan"` |
| W2-009 (×2: Duties, Rec. 3) | yes | yes (S-005) | n/a | yes | yes | PASS | `verified_by: "Floyd"`; Rec. 3 now names this duty explicitly |
| W2-010 | yes | yes (S-005) | n/a | yes | yes | PASS | `verified_by: "Floyd"` |
| W2-011 | yes | yes (S-006) | yes | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-012 | yes | yes (S-006) | n/a | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-013 | yes | yes (S-007) | n/a | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-014 | yes | yes (S-007) | n/a | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-019 | yes | yes (S-010) | n/a | n/a | yes | PASS | `verified_by: "Floyd"`; user confirms S-010 was opened directly in a browser and confirmed genuine, separately from the blanket verification pass |
| W2-020 (×2: Duties, Rec. 2, Rec. 4) | yes | yes (S-011) | n/a | yes | yes | PASS | Rec. 2 now names this duty explicitly |
| W2-021 | yes | yes (S-012) | n/a | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-022 | yes | yes (S-012) | n/a | n/a | yes | PASS | `verified_by: "Ivan"` |
| W2-023 (×2) | yes | yes (S-012) | n/a | n/a (Rec. 3's own duty now covered by W2-009) | yes | PASS | `verified_by: "Ivan"`; usesage of terms changed|
| W2-024 | yes | yes (S-013) | n/a | n/a | yes | PASS | |
| W2-025 (×2) | yes | yes (S-013) | n/a | yes (Rec. 2 now cites W2-020) | yes | PASS | |
| W2-026 | yes | yes (S-014) | n/a | yes | yes | PASS | |
| W2-027 | yes | yes (S-014) | yes ("60%" matches) | yes | yes | PASS | `verified_by: "Floyd"`; still correctly labelled as a vendor-reported figure |
| W2-028 | yes | yes (S-015) | n/a | n/a | yes | **note** | `verified_by` line is malformed YAML: `verified_by: ""Floyd` (stray leading quote, no closing quote). Was already PASS before verification (statement kind), so this doesn't block Check, but it should be corrected to `verified_by: "Floyd"` for a clean file — a person should fix this directly in claims_en.md, not me |
| W2-029 | yes | yes (S-015) | n/a | n/a | yes | PASS | |
| W2-030 | yes | yes (S-015) | n/a | n/a | yes | PASS | |
| W2-031 | yes | yes (S-016) | n/a | n/a | yes | PASS | |

**Summary: all 27 claim rows now PASS.** One cosmetic data-integrity issue remains (W2-028's malformed `verified_by` line) — doesn't affect the pass/fail outcome but should be corrected before this file is considered clean.

## Second reader: Floyd (not the author)
| criterion | pass/fail | one line |
|-----------|-----------|----------|
| 1 names a step, not a tool | pass | |
| 2 time-saving vs customer-touching, stated | pass | |
| 5 complexity label per recommendation | pass | |
| 6 one next step: owner, cost, 3-month check | pass | |

Five statements opened against the original source: pass, pass, pass, pass, pass → result: pass

## Final: publish · decided by: Floyd · date: 17-09-2026
