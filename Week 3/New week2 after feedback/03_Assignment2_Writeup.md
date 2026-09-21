# AIBS week 2 — Assignment 2: search strategy and quality criteria

Team: Aäron Bos, Floyd Godlieb, Ivan van Vreeswijk, Baran Yapici · 17 September 2026

**The question.** Good-quality reports on the geopolitics of the AI race — the United States, China, Europe — as far as they bear on what a Dutch trader with 10–50 staff depends on when it uses AI tooling.

**The bar we hold ourselves to.** Another team could repeat this search from this write-up and land on sources of the same quality.

Written by: [name] · AI-drafted parts: section 3 prompt output · Checked by: [name]

## 1. Our criteria — written before we searched (17 September, 14:00) [adjust time]

A source counts as "good quality" for this question if it passes all five gates and scores at least 6/9 on the scale.

**Gates (pass/fail)**

| Gate | Test |
|------|------|
| G1 Attributable | A named author or institution stands behind it. Anonymous or AI-generated text fails. |
| G2 Dated | A publication date is visible, and it is 2024 or later, unless it is a regulation or a foundational report (Draghi 2024 is in scope). |
| G3 Evidenced | It cites data, documents or named interviews we could in principle open. "Experts say" fails. |
| G4 Ownership disclosed | We can find who owns or funds the publisher. A think tank whose funders are undisclosed is used only as a secondary voice, never for a number. |
| G5 Primary where it matters | For any figure about a vendor (ownership, hosting, revenue, market share) the source is the vendor's own contractual or regulatory filing, or an official statistics body — not a news summary of one. |

**Scale (1–3 each; the same three the tool will use in `appraised.md`)**

| Dimension | 1 | 2 | 3 |
|-----------|---|---|---|
| Credibility | trade press, opinion piece | peer-reviewed, established think tank with disclosed funding, major financial press | regulation text, official statistics (CBS, Eurostat, national statistics bodies), vendor's own contractual documentation, court/regulator filings |
| Relevance | about AI geopolitics in general | about AI vendors, hosting or supply chains | about what a European SME depends on, or about tools this sector actually uses |
| Recency | 2024 | 2025 | 2026 |

**Source diversity rule.** For every claim about who leads or who owns what, we hold at least two sources from each of the three regions' perspectives, at least one of them credibility 3, or we say explicitly that we could not. This is the lesson of assignment 1 written into the method. (Revised week 2: one Chinese source at credibility 2 — S-009, MERICS — was not enough; a second, credibility-3 source — S-018, the State Council's own "AI+" guideline — was added. See appraised.md.)

## 2. Our strategy — how, where, why

**Language.** Dutch first for anything about the Dutch market, the sector or Dutch policy (CBS, KvK, sector bodies, Rijksoverheid, NRC/FD); English for EU, US and Chinese material. Dutch sources are appraised in Dutch, then translated (blueprint seam `claims_en.md`).

**Where we search, in this order, and why**

| Order | Where | Why first / what for |
|-------|-------|----------------------|
| 1 | Regulation and official documents: EUR-Lex (AI Act, GDPR, Regulation 833/2014), European Commission, Draghi report (2024) | The duties in our criterion 3 come from here; highest credibility. |
| 2 | Official statistics: CBS (ICT-gebruik bedrijven 2025), Eurostat (AI use by enterprises) | Sector-level numbers, independently verifiable. |
| 3 | Vendor contractual documentation: terms of service, data-processing agreements, hosting/region pages, trust centres of the tools a trader in this sector would use (translation, AI search / chat, CRM add-ons, sanctions-screening tools) | Criterion 3: hosting location and ownership, from the vendor itself, not from marketing. |
| 4 | Think tanks and research institutes with disclosed funding, one per region at minimum: US (e.g. Stanford HAI AI Index, CSIS), Europe (e.g. Bruegel, Rathenau Instituut, TNO, AWTI), China-focused (e.g. MERICS) | The three-perspective rule. |
| 5 | Financial and quality press (FD, NRC, FT, Reuters) | Only for events (acquisitions, export controls, outages) and only as pointers to a primary source. |
| 6 | Sector press and trader channels (used-truck platforms, sector associations) | Strand 2 of the proposal: what tooling is visible in this trade. |

**Search terms** (log the exact string, the engine or database, and the date for every search)

- NL: `AI-gebruik bedrijven 2025 CBS`, `kunstmatige intelligentie mkb afhankelijkheid leveranciers`, `AI Act verplichtingen mkb`, `sanctiescreening export gebruikte vrachtwagens`, `geopolitiek AI Europa Draghi`
- EN: `AI vendor dependency European SMEs`, `AI Act obligations deployer SME`, `data residency EU AI model providers`, `US export controls AI chips Europe 2026`, `China AI models European market`, `Draghi report AI diffusion Europe`
- Vendor: `<vendor> data processing agreement`, `<vendor> data residency EU`, `<vendor> ownership investors`, `<vendor> sub-processors list`

**Stopping rule.** We stop a search line when two consecutive searches return only sources we already have, or when we hold one primary source per claim plus one per region on the leadership question.

**Log format** (one line per search): date · engine/database · exact query · results kept (source ids) · results discarded and why.

## 3. Then AI, carefully — the first analysis

We run this once, in one conversation, with a tool that is not free-tier, on the appraised sources only. The prompt is reproduced in full so the strategy given to the AI is explicit.

```
You are helping four business students write one page of a handbook for the owner of a
Dutch trader in used commercial vehicles (10–50 staff, no IT function). The page answers:
"Who owns the AI tools I use, and what happens to me if that changes?"

Use ONLY the sources pasted below, each with its id and appraisal rating. Do not add
knowledge of your own. For every statement you make, give the source id and quote the
exact sentence it rests on. If the sources disagree, report the disagreement; do not pick
the bigger number. If a claim about who leads has support from fewer than three regional
perspectives, say so.

Produce:
1. For each of the US, China and Europe: what the sources say the region controls that a
   Dutch SME's AI tooling depends on (models, chips, cloud/hosting, rules).
2. A list of the dependencies that show up in more than one source, and the ones that
   appear in only one.
3. The three claims you are least sure of, and why.
4. Nothing else. No recommendations; those are ours to write.

Sources:
[paste appraised sources, id + rating + text]
```

**Output handling.** The AI's output is a hypothesis list, not content. Each statement in it is checked against the quoted sentence and its source before it becomes a claim in `claims_en.md`. The output, with our checks marked, is attached as Appendix B.

**Appendix A — assignment 1 evidence (three articles + note)**

Attach the three articles (US / China / Europe), each from a separate conversation. Then three or four lines:

- What all three agree on: [fill]
- Where they contradict each other: [fill]
- What none of them cites: [fill]
- Why "ask AI who leads" is not a research method, in our words: [fill]

**Appendix B — the AI's first analysis, with our checks marked** [attach]

**Appendix C — search log**: see `searchlog.md` in this repository (one line per search, as described in section 2).
