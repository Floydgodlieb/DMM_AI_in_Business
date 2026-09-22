# source_bank.md — week 3

Per `format.md`'s resolved citation-style decision, this follows the team's own already-
implemented convention (source id + credibility/relevance/recency 1–3 + G1–G5 gate notes),
**not** this pipeline's generic APA-7/High-Medium-Low default. Full excerpts, verbatim quotes,
and gate-by-gate reasoning live in `Platform/sources/S-0NN.md` and `Platform/appraised.md` —
this file is the reconciled index `academic-writer` reads from, not a second copy of the same
text (one source of truth; the two are kept in sync by hand, not duplicated line-for-line).

Scale/gates: see `01_requirements/source_criteria.md`. Quote/location/translation for every
claim actually usable in the draft: `Platform/claims_en.md`.

## New sources this week (10)

| id | citation | type | credibility/relevance/recency | decision |
|---|---|---|---|---|
| S-019 | IBM (X-Force), "2025 Cost of a Data Breach Report: Navigating the AI rush without sidelining security," reporting Ponemon Institute fieldwork (600 orgs), 2025 | vendor research report | 3/3/3 | use |
| S-020 | Awareways, "Trendrapport 2025 — De opmars van de onzichtbare collega – Shadow AI," via InfosecurityMagazine.nl, 2025/2026 | press (secondary, naming a primary study) | 2/3/3 | use — corroboration only |
| S-021 | Themio, "Shadow AI in European SMEs: The 2026 Compliance Risk," 4 Sept 2026 | vendor blog | 1/2/3 | use — legal framing only, not its own prevalence stats |
| S-022 | Future of Life Institute (AI Act Explorer), Regulation (EU) 2024/1689 Article 3(4) text mirror | verbatim-legal-text mirror | 2/3/3 | use |
| S-023 | Future of Life Institute (AI Act Explorer), Regulation (EU) 2024/1689 Article 14 text mirror | verbatim-legal-text mirror | 2/3/3 | use, high-risk-only scope caveated |
| S-024 | European Commission (Digital Strategy), "AI Omnibus enters into force," 27 July 2026 | official/regulatory | 3/3/3 | use |
| S-025 | Clifford Chance LLP (Kewley, Cramer, Gordon, Lutz, Navarro, Swaniker, Kidney), "Who's Responsible for Agentic AI?", 22 May 2025 | law-firm thought leadership | 2/3/2 | use |
| S-026 | Civil Resolution Tribunal of British Columbia, *Moffatt v. Air Canada*, 2024 BCCRT 149, 14 Feb 2024, via CanLII | primary legal record | 3/3/1 (recency exempted — foundational precedent) | use |
| S-027 | Digital Applied, "Self-Hosting Open-Weight LLMs: 2026 Decision Guide" | vendor/consultancy blog | 1/2/3 | use — existence of the option only, no figures quoted |
| S-028 | Puthal, Mishra, Mohanty, Longo & Yeun, "Shadow AI: Cyber Security Implications, Opportunities and Challenges in the Unseen Frontier," *SN Computer Science* 6:405, 2025, DOI 10.1007/s42979-025-03962-x | peer-reviewed journal article | 3/3/3 | use — corroboration |

## Week-2 sources carried forward this week (5)

Per `context.md` §6's source-reliability rule, only the credibility-3, gate-clean week-2 rows.
Full original appraisal: `AIBS & AEL Week 2 Assigments/Platform/appraised.md` (the team's real
repo, not duplicated into this one).

| id | citation | type | credibility/relevance/recency | why it applies to week 3 |
|---|---|---|---|---|
| S-005 | Future of Life Institute (AI Act Explorer), Regulation (EU) 2024/1689 Article 26 text mirror | verbatim-legal-text mirror | 2/3/3 | deployer duty when a tool does count as high-risk — same scope caveat as S-023 |
| S-007 | De Nederlandsche Bank / AFM, official warning on IT/cloud concentration risk | official/regulatory | 3/2/2 | clearest regulator statement of the dependency mechanism |
| S-011 | European Commission, GDPR Art. 28(7) standard contractual clauses page | official/regulatory | 3/2/1 | not tied to AI Act high-risk status — unaffected by the Digital Omnibus delay |
| S-013 | DeepL SE, Pro contract terms | primary vendor documentation | 3/2/2 | concrete "what leaves the building" example |
| S-015 | Microsoft, Copilot/EU Data Boundary documentation | primary vendor documentation | 3/3/3 | the Anthropic-subprocessor-excluded detail — most concrete evidence in the set |

## Explicitly not carried forward / not used

- **S-012, S-014, S-017** (week 2) — undated marketing case study, unverified vendor "60%"
  claim, and a discarded sponsored placement. `context.md` §2/§6.
- **Clark, "Deployer Obligations under the EU AI Act" (SSRN, 2026)** — found via Crossref,
  directly relevant, but full text returned HTTP 403 to the fetch tool this session; not used
  without a verified quote in hand (rule 5). Logged in `to_download.md` for Floyd to fetch
  directly if wanted for stage 4.

## What each part of the page can actually draw on

- **Part 1 (what leaves the building / self-hosting):** S-015, S-013, S-007, S-011, S-027.
- **Part 2 (act or only advise):** S-023, S-024, S-005, S-025, S-026.
- **Part 3 (staff using AI without saying so):** S-019, S-020, S-028, S-022, S-021 (framing).

At the ~485-word stage-4 budget (`checklist.md`), each part supports roughly 90–140 words —
enough for one strong, well-evidenced claim per part plus one supporting detail, not a full
survey of everything in this table. Selecting which one or two sources per part carries the
final page is stage 4's own job (`academic-writer` "chooses the angle"), not decided here.
