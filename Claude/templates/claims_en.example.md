# claims_en.md — contract between Translate and Draft (example)

week: 2
theme: geopolitics and vendor models
context_version: 1.0

Rules: `original_nl` is verbatim and never edited. `source_id` must exist in `appraised.md` with `decision: use`.
A claim passes Check when `auto_verified` starts with `AUTO-PASS`, or when `verified_by` names the person who
opened the source (context.md §3c). `auto_verified` is written only by verify_claims.py. English sources use the
same block with the original English sentence in `original_nl`.
A claim whose `original_nl` proves not verbatim is never edited: it gets `superseded_by: <new id>` and a new
claim replaces it.

```yaml
- claim_id: W2-001
  source_id: S-001
  location: "<table or page>"
  original_nl: "<verbatim sentence from the source>"
  translation_en: "<English claim as it will appear on the page>"
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: ""          # a person, only if review_queue.md routes this claim to them
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3"   # tool-filled; never a person's name

- claim_id: W2-002
  source_id: S-004
  location: "<section>"
  original_nl: "<verbatim sentence>"
  translation_en: "<English claim>"
  kind: statement
  evidence: company-reported
  scope: case
  translated_by: person    # interview material is always entered by a person
  verified_by: "<name>"
  auto_verified: ""        # interview claims are never auto-verified
```
