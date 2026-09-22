# claims_en.md — contract between Translate and Draft (week 3)

week: 3
theme: trust and AI safety
context_version: 2.0

Rules: `original_nl` is verbatim and never edited. `source_id` must exist in `appraised.md` with `decision: use`.
A `number` or `quote` claim without `verified_by` fails at Check. English sources use the same block with the
original English sentence in `original_nl`.

**Note on `verified_by`:** every claim below was drafted by the assistant in one pass, without the team's own
second-reader step (blueprint §1, part 5). `verified_by` is left empty on every claim, honestly, the same way
week 2's `draft.md` left it empty when Check had not yet run — **this page cannot pass Check until a person on
the team re-opens each source and fills it in.**

```yaml
- claim_id: W3-001
  source_id: S-019
  location: "headline figure"
  original_nl: "Shadow AI—where workers download or use unapproved internet-based AI tools—added an extra USD 670,000 to the global average breach cost."
  translation_en: "IBM's 2025 study (fieldwork by the independent Ponemon Institute, 600 organisations) found that 'shadow AI' — staff downloading or using AI tools the business never approved — added an extra $670,000 to the average cost of a data breach."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-002
  source_id: S-019
  location: "prevalence"
  original_nl: "In 2025, 20% of organizations studied reported a breach that was caused by shadow AI usage"
  translation_en: "One in five of the 600 organisations in the same study had a data breach caused specifically by shadow AI."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-003
  source_id: S-020
  location: "article title"
  original_nl: "Shadow AI groeit explosief: 78% van medewerkers gebruikt AI zonder toestemming van IT"
  translation_en: "A Dutch trend report (Awareways, 2025, reported via InfosecurityMagazine.nl) puts the figure at 78% of employees who use AI doing so without IT's permission — the Dutch-specific counterpart to the international IBM/Ponemon figure above."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-004
  source_id: S-022
  location: "Article 3(4)"
  original_nl: "'deployer' means a natural or legal person, public authority, agency or other body using an AI system under its authority except where the AI system is used in the course of a personal non-professional activity"
  translation_en: "Under the AI Act's own definition, a business counts as a 'deployer' of an AI system just by using it under its authority for work — there is no separate test for whether the business formally approved or bought the tool."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-005
  source_id: S-023
  location: "Article 14(1)"
  original_nl: "High-risk AI systems shall be designed and developed in such a way, including with appropriate human-machine interface tools, that they can be effectively overseen by natural persons during the period in which they are in use."
  translation_en: "The AI Act's human-oversight rule (Article 14) requires that a high-risk AI system can be effectively overseen by a person while it is in use."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-006
  source_id: S-023
  location: "Article 14(4)(d) and (e)"
  original_nl: "decide, in any particular situation, not to use the high-risk AI system or to otherwise disregard, override or reverse the output ... intervene in the operation of the high-risk AI system or interrupt the system through a 'stop' button or a similar procedure"
  translation_en: "In practice, Article 14 means a named person can override or reverse what the AI system produced in a given case, and can stop the system altogether."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-007
  source_id: S-024
  location: "postponed dates"
  original_nl: "High-risk AI systems in Annex III: Rules apply starting 2 December 2027"
  translation_en: "The European Commission confirms that the AI Act's binding rules for 'high-risk' AI systems (the category Article 14's oversight duty applies to) were pushed back, by the 'Digital Omnibus' reform, to 2 December 2027 — they are not yet in force."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-008
  source_id: S-024
  location: "SME-relevant change"
  original_nl: "Proportionate obligations for small and mid-cap companies"
  translation_en: "The same reform explicitly adds lighter, size-adjusted obligations for small and mid-cap companies once the high-risk rules do apply."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-009
  source_id: S-025
  location: "the liability gap"
  original_nl: "the laws of agency and vicarious liability require there first to be a human agent...before their employer...can be held responsible"
  translation_en: "A major law firm's own analysis notes that ordinary employer-liability law was built around a human employee acting — a fully autonomous AI agent does not fit that model cleanly, which is part of why the legal picture here is still unsettled."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-010
  source_id: S-026
  location: "tribunal finding"
  original_nl: "did not take reasonable care to ensure its chatbot was accurate"
  translation_en: "In a decided case, a Canadian tribunal found an airline liable for negligent misrepresentation because its own customer-facing chatbot gave a customer wrong information — the business was liable for what its AI told the customer, full stop, regardless of any AI-specific regulation."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-011
  source_id: S-005
  location: "Article 26"
  original_nl: "Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use"
  translation_en: "When a tool does count as 'high-risk' under the AI Act, the deployer duty is to use it strictly according to the supplier's own instructions for use — not to improvise with it."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-012
  source_id: S-007
  location: "body text"
  original_nl: "De financiële sector loopt een groeiend risico door zijn toenemende afhankelijkheid van een klein aantal niet-Europese IT-leveranciers."
  translation_en: "The Dutch central bank and financial regulator warn that concentrating on a small number of non-European IT suppliers is a growing, real risk (written about the financial sector, not the vehicle trade, but the mechanism — everyone ends up on the same few providers — is the same one this page is about)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-013
  source_id: S-011
  location: "document title on page"
  original_nl: "Commission Implementing Decision on standard contractual clauses between controllers and processors under Article 28 (7) of Regulation (EU) 2016/679"
  translation_en: "The GDPR duty to have a data-processing agreement with any AI supplier that handles customer data is separate from the AI Act's high-risk rules, so it is not affected by the Digital Omnibus delay — it applies now."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-014
  source_id: S-013
  location: "data processing location"
  original_nl: "may process Content, Processed Content and Customer Training Data on its servers as well as on technical infrastructure owned and/or operated by third party cloud providers"
  translation_en: "DeepL's own contract terms allow it to process a customer's text on its own servers or on other companies' cloud infrastructure, with no fixed location guaranteed by default — a concrete example of data leaving the building further than a business might assume."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-015
  source_id: S-015
  location: "Microsoft Copilot and the EU Data Boundary, note"
  original_nl: "Models provided by Anthropic as a subprocessor are currently excluded from the EU Data Boundary."
  translation_en: "Even Microsoft's own EU Data Boundary, designed to keep EU customer data inside the EU, currently excludes one specific model supplier — meaning 'hosted in the EU' can have named exceptions, model by model, not just vendor by vendor."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-017
  source_id: S-028
  location: "Introduction"
  original_nl: "Such deployment and usage of AI tools, models, or systems by employees of an organization without explicit endorsement, supervision, or management by IT and cyber security departments is defined as Shadow AI"
  translation_en: "A peer-reviewed 2025 cybersecurity survey (five authors, five universities) confirms 'shadow AI' as a recognised term for exactly this: employees using AI tools their IT and security teams never endorsed or supervised."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: person
  verified_by: ""

- claim_id: W3-016
  source_id: S-027
  location: "the option exists"
  original_nl: "Self-hosting an LLM in 2026 is no longer a research experiment but a workable production option for organizations that need control over their data, costs and performance."
  translation_en: "Running an AI model on the firm's own hardware, so nothing leaves the building at all, is a genuine option in 2026 — though the source for this is a vendor-tier blog with no independently checkable cost figures, so no specific price is claimed here."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: person
  verified_by: ""
```
