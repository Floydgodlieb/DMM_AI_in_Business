# to_download.md — week 3

Per `lead-researcher`'s stage description: start with OpenAlex/Semantic Scholar/Crossref, then —
per `search-strategy`'s own "when three academic databases aren't enough" section — search
directly wherever the topic isn't academic literature. Both halves were actually run, not
assumed; results below.

## Step 1 — academic databases (2026-09-22)

| database | search string | candidates found | kept |
|---|---|---|---|
| OpenAlex | `shadow AI employee unauthorized use data breach` | 5 results; 4 off-topic (generative AI broadly, privacy/analytics, explainable AI for digital twins), 1 on-topic | S-028 |
| OpenAlex | `AI agent liability autonomous business decision` | 2 results (Dwivedi et al. 2019, Floridi et al. 2018), both broad AI-governance surveys, neither about agent liability specifically | none |
| Crossref | `EU AI Act deployer obligations small medium enterprise` | 5 results, all 2026 SSRN working papers (not peer-reviewed) on AI Act deployer duties; most relevant: Clark, "Deployer Obligations under the EU AI Act: Article 26..." (SSRN, 12 Feb 2026) | not kept — see note |

**S-028** (Puthal, Mishra, Mohanty, Longo & Yeun, "Shadow AI: Cyber Security Implications,
Opportunities and Challenges in the Unseen Frontier," *SN Computer Science* 6:405, 2025,
DOI `10.1007/s42979-025-03962-x`) is genuinely open-access — full text fetched and read
directly (see `Platform/sources/S-028.md`, `Platform/appraised.md`). No download/Zotero step
needed for a source read directly from its own DOI landing page.

**Not kept: Clark (SSRN, 2026), "Deployer Obligations under the EU AI Act."** Found via Crossref,
directly relevant on paper (Article 26's eleven paragraphs, deployer governance), but SSRN
returned HTTP 403 to the fetch tool — the abstract's own claims were readable via the search
snippet, but the pipeline's own rule 5 (never quote from memory, never from what the search
snippet showed) rules out using it without the actual text in front of the assistant. Logged
here as a candidate for Floyd to fetch directly (SSRN downloads are free, no HAN paywall
involved — this is a fetch-tool limitation, not an access-rights one) if stage 4 wants a second
legal-analysis source alongside `S-025` (Clifford Chance) for the act-or-advise section.

**No paywalled/HAN-access items this week.** Nothing found required Zotero, Unpaywall, or HAN
library access — everything either had genuinely open full text (S-028, and every regulation/
official page in the set) or was a live web page fetched directly. `scripts/sync_sources.py` and
`scripts/extract_text.py` were not run this stage; nothing in `02_sources/pdf/` to sync.

## Step 2 — direct web search (2026-09-22)

Not academic literature: EU regulation and its official reform history, a tribunal decision,
vendor contractual documentation, an industry breach-cost study, and two national
adoption/prevalence surveys. Full search log, gates, and the deliberate rephrasing test:
`Platform/searchlog.md` and `Platform/question.md` — not duplicated here; this file points to
that one rather than forking the record into two versions that could drift apart.
