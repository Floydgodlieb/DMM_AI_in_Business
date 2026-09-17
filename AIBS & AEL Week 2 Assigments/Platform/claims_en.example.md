# claims_en.md — contract between Translate and Draft (example)

week: 2
theme: geopolitics and vendor models
context_version: 1.0

Rules: `original_nl` is verbatim and never edited. `source_id` must exist in `appraised.md` with `decision: use`.
A `number` or `quote` claim without `verified_by` fails at Check. English sources use the same block with the
original English sentence in `original_nl`.

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
  verified_by: ""          # fill in before Check; empty = fails

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
```
