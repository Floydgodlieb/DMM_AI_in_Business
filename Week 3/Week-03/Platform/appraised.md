# appraised.md — week 3

Scale and gates as `03_Assignment2_Writeup.md` §1 (also restated in `searchlog.md`'s header). Per context.md §6's source-reliability rule, no row below rests solely on an undated marketing page.

## New sources, appraised this week

| source_id | credibility | relevance | recency | reason (one line) | human_override | decision |
|---|---|---|---|---|---|---|
| S-019 | 3 | 3 | 3 | IBM reporting the independent Ponemon Institute's 600-org study; named methodology, dated 2025, directly on "staff using AI without saying so." Commercial interest (IBM sells security tooling) disclosed, not hidden. | none needed | use |
| S-020 | 2 | 3 | 3 | Dutch-specific corroboration of the disclosure risk (Awareways' Trendrapport 2025, via infosecuritymagazine.nl); scored one point below S-019 because this session only reached the primary study through a secondary report (G5 partial). | none needed | use — corroborating, not sole support |
| S-021 | 1 | 2 | 3 | Themio's own prevalence figures ("68%") have no named study behind them on the page (fails G3); vendor selling the compliance product this risk creates demand for (G4: interest disclosed, weighted down). | Floyd (tester), 2026-09-22: `use` for the legal "deployer" framing only, and only after checking it against S-022's primary text; `discard` its own prevalence statistics as claim material | use (framing only) |
| S-022 | 2 | 3 | 3 | Verbatim mirror of AI Act Article 3(4), same tier as S-005 (week 2); confirms the "deployer" definition independently of S-021's reading of it. | none needed | use |
| S-023 | 2 | 3 | 3 | Verbatim mirror of AI Act Article 14; same tier as S-005/S-022. Relevance capped by the fact this article only binds "high-risk" systems, most of which this reader's tools are not (see S-024, searchlog's Annex III check) — used as good-practice guidance, not an asserted binding duty. | none needed | use, scope caveated in draft |
| S-024 | 3 | 3 | 3 | European Commission's own page, dated 27 July 2026, confirming the Digital Omnibus's postponement of Annex III high-risk obligations to 2 December 2027 and naming "proportionate obligations for small and mid-cap companies." Directly changes how strongly this reader can be told the AI Act currently binds them. | none needed | use |
| S-025 | 2 | 3 | 2 | Named-author law-firm analysis (Clifford Chance, dated May 2025) on the agency-law liability gap for autonomous AI agents; commercial interest disclosed, corroborated by the decided case (S-026) rather than used alone. | none needed | use |
| S-026 | 3 | 3 | 1 | Primary tribunal record (CanLII), the clearest concrete evidence that a business is liable for what its customer-facing AI says, on ordinary negligence grounds. Recency scored low by the literal 2024-or-later-within-12-months rule, but treated as foundational/precedent, same exemption context.md and week 2 gave the Draghi report. | Floyd (tester), 2026-09-22: `use`, recency exemption logged here rather than silently overridden | use |
| S-027 | 1 | 2 | 3 | No named author or independently checkable methodology behind its cost figures (fails G1/G3); kept only to establish that self-hosting is a discussed 2026 option, not to support any figure as fact. | Floyd (tester), 2026-09-22: `use` for the existence of the option only; the $10-15k figure is not to be quoted as verified in draft.md | use (illustrative only, no figures quoted) |
| S-028 | 3 | 3 | 3 | Peer-reviewed survey (SN Computer Science/Springer, 2025), five named authors, five universities — found via OpenAlex, not direct web search (stage 2's own database-first step working as intended). Highest-credibility confirmation that "shadow AI" is a recognised phenomenon in the cybersecurity literature, not just an industry-report framing. | none needed | use — corroboration for S-019/S-020, not a replacement for their figures |

## Week-2 sources carried forward this week

Per context.md §6's source-reliability rule, only the credibility-3, gate-clean rows from week 2 are carried forward. Full original appraisal for each stays in `AIBS & AEL Week 2 Assigments/Platform/appraised.md`; not re-scored here, only re-confirmed as still in scope for week 3's theme.

| source_id | week-2 credibility/relevance/recency | why it still applies to week 3 | decision |
|---|---|---|---|
| S-005 | 2 / 3 / 3 | AI Act Article 26 (deployer duty to follow instructions for use) — same high-risk-only scope caveat as S-023 applies; used for the "when it does apply, this is the duty" half of the act-or-advise section. | use, scope caveated |
| S-007 | 3 / 2 / 2 | DNB/AFM's official warning on concentration risk from a small number of non-European IT suppliers — still the clearest regulator statement of the "what leaves the building" dependency mechanism, even though it is about the financial sector. | use |
| S-011 | 3 / 2 / 1 | European Commission's own GDPR Article 28(7) standard-contractual-clauses page — this duty is not tied to AI-Act high-risk classification, so it is not affected by the Digital Omnibus delay; still directly applicable to any supplier processing customer data. | use |
| S-013 | 3 / 2 / 2 | DeepL's own Pro contract terms — concrete, named example of "what leaves the building" for a tool this sector plausibly uses. | use |
| S-015 | 3 / 3 / 3 | Microsoft's own documentation on the EU Data Boundary and the Anthropic-subprocessor exclusion — the single most concrete, dated evidence available anywhere in this source set for "hosted in the EU can still have exceptions." | use |

**Explicitly not carried forward this week:** S-012 (undated BAS World implementation-partner marketing case study), S-014 (Descartes marketing page, unverified "60%" figure), S-017 (sponsored trade-press placement, already `discard`-rated in week 2). See context.md §2 and §6 for why.
