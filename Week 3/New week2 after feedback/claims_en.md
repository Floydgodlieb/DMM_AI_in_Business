# claims_en.md — contract between Translate and Draft

week: 2
theme: geopolitics and vendor models
context_version: 1.0

Rules: `original_nl` is verbatim and never edited. `source_id` must exist in `appraised.md` with `decision: use`.
A `number` or `quote` claim without `verified_by` fails at Check. English sources use the same block with the
original English sentence in `original_nl`.

```yaml
- claim_id: W2-001
  source_id: S-001
  location: "opening paragraph"
  original_nl: "In 2024 gebruikte 22,7 procent van de bedrijven met 10 of meer werkzame personen een of meer AI-technologieën. Dit was een toename van bijna 9 procentpunt ten opzichte van 2023."
  translation_en: "In 2024, 22.7% of Dutch businesses with 10 or more employees used one or more AI technologies — up almost 9 percentage points from 2023."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-002
  source_id: S-001
  location: "section 'Vooral grote bedrijven'"
  original_nl: "Grote bedrijven maakten in 2024 vaker gebruik van AI-technologie dan kleinere bedrijven. Het gebruik van AI-technologie was het hoogst onder bedrijven met 500 en meer werkzame personen (59,2 procent) en het laagst onder bedrijven met 10 tot en met 19 werkzame personen (17,8 procent)."
  translation_en: "AI use in 2024 was highest among businesses with 500+ employees (59.2%) and lowest among businesses with 10-19 employees (17.8%)."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-003
  source_id: S-002
  location: "company-size breakdown"
  original_nl: "Bedrijven die AI-technologie gebruikten waren juist minder vaak een klein bedrijf (10-49 werkzame personen) dan bedrijven die dit niet deden (65 tegen 81 procent)."
  translation_en: "Among businesses with 10+ employees, 65% of AI users were small businesses (10-49 employees), against 81% of non-users — small businesses this reader's size are under-represented among AI adopters."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-004
  source_id: S-002
  location: "sector breakdown"
  original_nl: "Het grootste deel van de bedrijven met 10 of meer werkzame personen die in 2024 AI-technologie gebruikten waren actief in de bedrijfstak G (Handel, 24 procent)."
  translation_en: "Of businesses with 10+ employees using AI technology in 2024, the largest share (24%) was in trade (bedrijfstak G, Handel) — the sector this trader belongs to."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-005
  source_id: S-003
  location: "body text"
  original_nl: "Soms is de uitvoer van bepaalde goederen naar bepaalde landen verboden, of alleen toegestaan met een vergunning."
  translation_en: "Export of certain goods to certain countries is sometimes prohibited, or only allowed with a permit (Dutch Customs)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-006
  source_id: S-004
  location: "export-ban list"
  original_nl: "Dual-use goods and advanced technology items that can contribute to Russia's defence and security capabilities (e.g. quantum computers and advanced semiconductors, electronic components and software)"
  translation_en: "The EU sanctions regime bans export to Russia of dual-use goods and advanced technology items that could contribute to its defence and security capabilities, including semiconductors and software."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-007
  source_id: S-004
  location: "export-ban list"
  original_nl: "Transportation equipment, goods used in aviation, space industry and maritime navigation"
  translation_en: "The same EU sanctions regime restricts export of transportation equipment and goods used in aviation, space and maritime navigation."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-008
  source_id: S-004
  location: "legal basis, repeated on page"
  original_nl: "Council Regulation (EU) No 833/2014"
  translation_en: "The legal basis for the EU's export bans on Russia is Council Regulation (EU) No 833/2014."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-009
  source_id: S-005
  location: "Article 26"
  original_nl: "Deployers of high-risk AI systems shall take appropriate technical and organisational measures to ensure they use such systems in accordance with the instructions for use"
  translation_en: "Under the EU AI Act (Article 26), a business deploying a high-risk AI system must take appropriate technical and organisational measures to use it according to the provider's instructions."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-010
  source_id: S-005
  location: "Article 26"
  original_nl: "Deployers of high-risk AI systems...shall inform the natural persons that they are subject to the use of the high-risk AI system"
  translation_en: "Under the EU AI Act (Article 26), a deployer of a high-risk AI system must tell people when they are subject to its use."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-011
  source_id: S-006
  location: "page body, report title and date"
  original_nl: "The future of European competitiveness – A competitiveness strategy for Europe", published "9 September 2024"
  translation_en: "The Draghi report, 'The future of European competitiveness — A competitiveness strategy for Europe', was published on 9 September 2024."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-012
  source_id: S-006
  location: "page body"
  original_nl: "Slowing productivity, demographic challenges, rising energy costs, and increased global competition are putting pressure on Europe's long-term prosperity."
  translation_en: "The Draghi report finds that slowing productivity, demographic challenges, rising energy costs and increased global competition are pressuring Europe's long-term prosperity."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-013
  source_id: S-007
  location: "body text"
  original_nl: "De financiële sector loopt een groeiend risico door zijn toenemende afhankelijkheid van een klein aantal niet-Europese IT-leveranciers."
  translation_en: "The Dutch financial sector faces a growing risk from its increasing dependence on a small number of non-European IT suppliers (DNB/AFM; about the financial sector, not the vehicle trade)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-014
  source_id: S-007
  location: "body text"
  original_nl: "Doordat instellingen veelal gebruikmaken van dezelfde aanbieders en infrastructuren zijn concentratie- en systeemrisico's ontstaan."
  translation_en: "Because institutions largely rely on the same providers and infrastructure, concentration and systemic risks have emerged."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-015
  source_id: S-008
  location: "Finding 2"
  original_nl: "The United States continues to lead in global private AI investment, committing 23 times more than China."
  translation_en: "The US leads global private AI investment, committing 23 times more than China (Stanford AI Index, 2026 report, 2025 figures)."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-016
  source_id: S-008
  location: "Economy chapter, investment section"
  original_nl: "private investment figures likely understate China's total AI spending, as government guidance funds have deployed an estimated $184 billion into AI firms between 2000 and 2023."
  translation_en: "Private-investment figures likely understate China's total AI spending: Chinese government guidance funds are estimated to have put $184 billion into AI firms between 2000 and 2023."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-017
  source_id: S-009
  location: "penetration goal"
  original_nl: "penetration of AI-powered 'intelligent terminals' and AI agents to exceed 70 percent across key sectors by 2027"
  translation_en: "China's 'AI+' plan targets AI-powered 'intelligent terminals' and AI agents exceeding 70% penetration across key sectors by 2027."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-018
  source_id: S-009
  location: "risk to Europe"
  original_nl: "could give China an edge in areas where Europe has traditionally excelled, like industrial automation."
  translation_en: "MERICS assesses that China's AI+ push could give it an edge in areas where Europe has traditionally excelled, such as industrial automation."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-019
  source_id: S-010
  location: "on allied dependence — SOURCE FLAGGED, verify in browser before Check (see sources/S-010.md)"
  original_nl: "Everyone else lives in managed dependence. The Fable and Mythos directive has made that clear."
  translation_en: "Bruegel: outside the US and China, countries and companies live in 'managed dependence' on foreign AI providers — illustrated, the authors say, by a June 2026 US directive restricting non-US access to certain AI models."
  kind: quote
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-020
  source_id: S-011
  location: "document title on page"
  original_nl: "Commission Implementing Decision on standard contractual clauses between controllers and processors under Article 28 (7) of Regulation (EU) 2016/679"
  translation_en: "The European Commission has adopted standard contractual clauses for use between data controllers and processors under Article 28(7) GDPR."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-021
  source_id: S-012
  location: "hosting"
  original_nl: "Een modulair, vendor-agnostisch fundament op AWS"
  translation_en: "BAS World's AI agents run on a modular, vendor-agnostic foundation hosted on AWS."
  kind: statement
  evidence: company-reported
  scope: case
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-022
  source_id: S-012
  location: "LLM flexibility"
  original_nl: "Volledig modulair & LLM-agnostisch (ChatGPT, Gemini, Claude plug-and-play)"
  translation_en: "BAS World's setup is fully modular and model-agnostic, with ChatGPT, Gemini and Claude available as plug-and-play models."
  kind: statement
  evidence: company-reported
  scope: case
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-023
  source_id: S-012
  location: "architecture"
  original_nl: "Alle agents draaien op Incentro's AI Building Block: een modulaire agent-architectuur gebaseerd op onder andere LangChain en LangGraph... waardoor BAS World ook na dit traject zelf kan doorontwikkelen — zonder afhankelijk te zijn van Incentro."
  translation_en: "All of BAS World's agents run on Incentro's AI Building Block, a modular agent architecture built on LangChain and LangGraph among others, designed so BAS World can keep developing it further itself afterwards, without depending on Incentro."
  kind: statement
  evidence: company-reported
  scope: case
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-024
  source_id: S-013
  location: "legal entity"
  original_nl: "DeepL SE, Maarweg 165, 50825 Cologne, Germany"
  translation_en: "DeepL's contracting entity, DeepL SE, is headquartered in Cologne, Germany."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-025
  source_id: S-013
  location: "data processing location"
  original_nl: "may process Content, Processed Content and Customer Training Data on its servers as well as on technical infrastructure owned and/or operated by third party cloud providers"
  translation_en: "DeepL's contract terms allow it to process customer data on its own servers or on infrastructure owned or operated by third-party cloud providers, with no fixed geographic restriction by default."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-026
  source_id: S-014
  location: "product description"
  original_nl: "Automate screening processes and integrate with your business systems"
  translation_en: "Descartes' Denied Party Screening product automates checks of trading partners against government watchlists and integrates with a company's own business systems."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-027
  source_id: S-014
  location: "AI feature"
  original_nl: "AI Assist for Trade Compliance ... Reduce screening false positives by 60%"
  translation_en: "Descartes markets an 'AI Assist for Trade Compliance' feature it says reduces screening false positives by 60% — a vendor-reported figure, not independently verified."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-028
  source_id: S-015
  location: "Microsoft Copilot and the EU Data Boundary"
  original_nl: "Microsoft Copilot calls to the LLM are routed to the closest data centers in the region, but also can call into other regions where capacity is available during high utilization periods."
  translation_en: "Microsoft Copilot's calls to the AI model are normally routed to the nearest regional data centre, but can be routed to other regions when regional capacity runs out at peak demand."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-029
  source_id: S-015
  location: "Microsoft Copilot and the EU Data Boundary"
  original_nl: "For European Union (EU) users, we have additional safeguards to comply with the EU Data Boundary. EU traffic stays within the EU Data Boundary while worldwide traffic can be sent to the EU and other countries or regions for LLM processing."
  translation_en: "For EU users, Microsoft applies extra safeguards so EU traffic stays inside the EU Data Boundary, while traffic from outside the EU can be routed into the EU or elsewhere for AI processing."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-030
  source_id: S-015
  location: "Microsoft Copilot and the EU Data Boundary, note"
  original_nl: "Models provided by Anthropic as a subprocessor are currently excluded from the EU Data Boundary."
  translation_en: "Models supplied by Anthropic as a subprocessor within Microsoft Copilot are currently excluded from the EU Data Boundary, so that specific model's processing is not guaranteed to stay inside the EU."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"

- claim_id: W2-031
  source_id: S-016
  location: "body text"
  original_nl: "publieke organisaties in allerlei sectoren van de samenleving in toenemende mate afhankelijk zijn van de diensten van enkele grote Amerikaanse techbedrijven: naast clouddiensten ook software, AI-tools en apparatuur. Dit maakt de samenleving kwetsbaar."
  translation_en: "Rathenau Instituut: public organisations across many sectors of Dutch society are increasingly dependent on a handful of large American tech companies — not just cloud services but also software, AI tools and equipment — which makes society vulnerable. (About the Dutch public sector generally, not this trade sector.)"
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
```
