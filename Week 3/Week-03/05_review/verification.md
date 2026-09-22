# verification.md — week 3, draft_v1.md

**Hand-built, not script-generated.** `scripts/verify_quotes.py` requires
`02_sources/text/<source>/page_NNNN.txt`, written by `extract_text.py` from a Zotero-synced PDF.
None of this week's sources are PDFs — `02_sources/pdf/` and `02_sources/text/` are both empty
(confirmed via `to_download.md`: everything this week was a live web page or a directly-fetched
open-access article, not a Zotero item). A real attempt was run to confirm this rather than
assumed:

```
$ python scripts/verify_quotes.py --quote "Deployers of high-risk AI systems shall take appropriate technical and organisational measures" --source S-023 --page 1
ERROR: no extracted text for S-023 page 1 (run extract_text.py first; ...\02_sources\text\S-023 does not exist)
```

Per `reviewer-factchecker`'s own manual fallback ("check each quote against its stated page... if
`verify_quotes.py` can't run"), adapted for web sources: each citation below is checked by hand
against the actual excerpt captured in `Platform/sources/S-0NN.md` at the time it was fetched —
not against a PDF page, since none exists, and not from memory.

| Claim (draft_v1.md) | Source file | Page | Match | Issue |
|---|---|---|---|---|
| Microsoft's EU Data Boundary excludes one model supplier | `Platform/sources/S-015.md` | n/a (web) | match | — |
| GDPR duty: data-processing agreement before a supplier sees customer data | `Platform/sources/S-011.md` | n/a (web) | match | — |
| Self-hosting is a real, if low-IT-priority, 2026 option | `Platform/sources/S-027.md` | n/a (web) | match | — |
| Tribunal held an airline liable for its chatbot's wrong answer | `Platform/sources/S-026.md` | n/a (web) | match | — |
| AI Act Art. 14: named person can override/stop the system | `Platform/sources/S-023.md` | n/a (web) | match | — |
| Digital Omnibus pushes high-risk rules back to Dec 2027 | `Platform/sources/S-024.md` | n/a (web) | match | — |
| Shadow AI added $670K to breach cost, caused 1 in 5 breaches | `Platform/sources/S-019.md` | n/a (web) | match | — |
| "a pattern a peer-reviewed survey confirms as real" | `Platform/sources/S-028.md` | n/a (web) | no-match | See issue_log.md I7 — `S-028` confirms shadow AI is a recognised risk category, not the specific $670K/20% figures the sentence sits next to; as phrased this overstates what the source supports |
| AI Act counts a business as "deployer" regardless of approval | `Platform/sources/S-022.md` | n/a (web) | match | — |
| Rec. 1 rationale: check AI answers before they reach a customer | `Platform/sources/S-026.md` | n/a (web) | match | Reasonable inference from the case, not a direct quote presented as one — draft doesn't claim the case itself prescribes this |
| Rec. 2: check contract for processing location, sign DPA | `Platform/sources/S-011.md`, `S-015.md` | n/a (web) | match | — |
| Rec. 3 rationale: AI-use policy answers the disclosure numbers | `Platform/sources/S-019.md`, `S-022.md` | n/a (web) | match | — |

**Summary: 12 claims checked, 11 match, 1 no-match (I7).**
