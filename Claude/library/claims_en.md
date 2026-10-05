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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:5a941ffd8b|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:cfc92b7e4f|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:2438782e6c|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:f06c905f69|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:3b1f353252|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:e147a7aae0|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:4d08028e29|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:027840d096|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:f9394ccf78|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:964ce6eec3|live:NO MATCH]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 FAIL: malformed YAML quoting in: original_nl [h:78b735911c|live:NO MATCH]"   # tool-filled; never a person's name
  superseded_by: W4-001

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:4d22919e23|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:de92dfa751|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:5edb342578|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T2 number not in the quoted sentence: 2025; T1 credibility 2 [h:4a807f21a6|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:0973f9a4d9|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:cf84faf8ae|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:54d9b92823|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T2 number not in the quoted sentence: 2026; T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:f81572c3e1|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:4cb9904653|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:21d90cf4d9|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:6472cd4071|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:8e4e53c4bc|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:0f9cc39a5f|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:c4744ed9d0|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:84df0fc832|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:8dd9a6c69d|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:921470f140|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:85615c545d|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:5d7702df18|live:match]"   # tool-filled; never a person's name

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
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:e76ffc96e4|live:match]"   # tool-filled; never a person's name

- claim_id: W4-001
  source_id: S-006
  location: "page body, report title and date"
  original_nl: '"The future of European competitiveness – A competitiveness strategy for Europe", published "9 September 2024"'
  translation_en: "The Draghi report, 'The future of European competitiveness – A competitiveness strategy for Europe', was published on 9 September 2024."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:a33b0bd3e5|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-002
  source_id: S-018
  location: "quoted sentence on the 2027 target"
  original_nl: "By 2027, China aims to achieve significant progress in the deep integration of AI in six key sectors, with the penetration rate of new-generation intelligent terminals and AI agents expected to surpass 70 percent."
  translation_en: "China's State Council says that by 2027 it aims for significant progress in integrating AI into six key sectors, with new-generation intelligent terminals and AI agents expected to pass 70 percent penetration."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 AUTO-PASS: excerpt+live match, numbers ok, credibility 3 [h:634322f9d9|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-003
  source_id: S-019
  location: "section 'Definitions of article 4 and the AI Act'"
  original_nl: "Article 4(1) of the AI Act requires providers and deployers of AI systems to take measures to support the development of AI literacy of their staff and other persons dealing with the operation and use of AI systems on their behalf."
  translation_en: "Under Article 4(1) of the EU AI Act, a business that provides or uses AI systems must take measures to build AI literacy among its staff and others who run or use the systems for it."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:cc63b9c05d|live:match]"   # tool-filled; never a person's name

- claim_id: W4-004
  source_id: S-019
  location: "section 'Definitions of article 4 and the AI Act'"
  original_nl: "Article 4(2) requires the Commission and Member States to support and facilitate the efforts of providers and deployers of AI systems, in particular SMEs, to fulfil their obligations."
  translation_en: "Under Article 4(2) of the EU AI Act, the Commission and Member States must support businesses that provide or use AI systems, in particular SMEs, in meeting their obligations."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:85e0032297|live:match]"   # tool-filled; never a person's name

- claim_id: W4-005
  source_id: S-019
  location: "section 'Compliance with article 4'"
  original_nl: "Article 4 of the AI Act does not entail an obligation to measure the knowledge of AI of employees."
  translation_en: "Article 4 of the EU AI Act does not oblige a business to measure its employees' knowledge of AI."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:fb8de70780|live:match]"   # tool-filled; never a person's name

- claim_id: W4-006
  source_id: S-019
  location: "section 'Enforcement of article 4'"
  original_nl: "Article 4 of the AI Act entered into application on 2 February 2025, therefore the obligation to take measures to support the development of AI literacy of their staff already applies. The supervision and enforcement rules apply from 3 August 2026 onwards."
  translation_en: "The AI literacy duty in Article 4 of the EU AI Act has applied since 2 February 2025. The supervision and enforcement rules apply from 3 August 2026 onwards."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:55a46a6ca7|live:match]"   # tool-filled; never a person's name

- claim_id: W4-007
  source_id: S-019
  location: "section 'Enforcement of article 4'"
  original_nl: "The supervision and enforcement of Article 4 of the AI Act is not with the AI Office, but it is under the remit of national market surveillance authorities."
  translation_en: "Article 4 of the EU AI Act is supervised and enforced by national market surveillance authorities, not by the AI Office."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:5e2e9d0804|live:match]"   # tool-filled; never a person's name

- claim_id: W4-008
  source_id: S-020
  location: "section 'Vereiste'"
  original_nl: "Personeel en gebruikers zijn voldoende AI-geletterd."
  translation_en: "The Dutch government's algorithm framework requires that staff and users are sufficiently AI-literate (written for government organisations; the same duty comes from the AI Act)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:73f22146c2|live:match]"   # tool-filled; never a person's name

- claim_id: W4-009
  source_id: S-020
  location: "section 'Wat te doen'"
  original_nl: "Zorg voor bewustwording en voldoende opleidingen over de risico's en kansen van algoritmes en AI"
  translation_en: "The framework advises making sure there is awareness and enough training on the risks and opportunities of algorithms and AI."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:600ce3076e|live:match]"   # tool-filled; never a person's name

- claim_id: W4-010
  source_id: S-020
  location: "section 'Wat te doen'"
  original_nl: "Laat de aanbieder aangeven welke mate van opleiding en ondersteuning bij de implementatie nodig is"
  translation_en: "The framework advises asking the supplier of an AI system what level of training and support is needed for implementation."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:60376d66ed|live:match]"   # tool-filled; never a person's name

- claim_id: W4-011
  source_id: S-021
  location: "section 'Wat is de AI-verordening?'"
  original_nl: "De AI-verordening stelt plichten voor aanbieders en gebruiksverantwoordelijken van AI-systemen in Europa."
  translation_en: "The AI Act sets duties for providers and for users (deployers) of AI systems in Europe."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:0e7bfb8689|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-012
  source_id: S-022
  location: "section 'Hub description'"
  original_nl: "Digital Hub Northwest Netherlands (DHNWN) is the European Digital Innovation Hub for North Holland, Utrecht, and Flevoland, supporting SMEs and PSOs in accelerating their digital transformation, with a focus on the sectors Smart Industry, Smart Food, Smart Health, and Creative Industries."
  translation_en: "Digital Hub Northwest Netherlands says it is the European Digital Innovation Hub for North Holland, Utrecht and Flevoland, helping SMEs and public organisations with digital transformation, focused on Smart Industry, Smart Food, Smart Health and Creative Industries (not trade, and not Brabant)."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:31303f7046|live:match]"   # tool-filled; never a person's name

- claim_id: W4-013
  source_id: S-025
  location: "section 'Kernuitspraken'"
  original_nl: "Toch heeft slechts zeven procent een concreet AI-beleid ontwikkeld."
  translation_en: "Only seven percent has developed a concrete AI policy (evofenedex survey of trade and logistics companies)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:5a0249f333|live:match]"   # tool-filled; never a person's name

- claim_id: W4-014
  source_id: S-025
  location: "section 'Kernuitspraken'"
  original_nl: "het gebrek aan kennis en vaardigheden in de organisatie. Deze worden genoemd door bijna twee derde van de bedrijven."
  translation_en: "The lack of knowledge and skills in the organisation is named by almost two thirds of the companies (evofenedex survey of trade and logistics companies)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:50af9e0451|live:match]"   # tool-filled; never a person's name

- claim_id: W4-015
  source_id: S-025
  location: "section 'Kernuitspraken'"
  original_nl: "Slechts 42 procent van de bedrijven heeft zijn interne data grotendeels op orde; bij een derde is dit zelfs beperkt."
  translation_en: "Only 42 percent of the companies have their internal data largely in order; for a third it is even limited (evofenedex survey of trade and logistics companies)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:fb433740d9|live:match]"   # tool-filled; never a person's name

- claim_id: W4-016
  source_id: S-025
  location: "section 'Advies N. Schriek'"
  original_nl: "Maar het is wél belangrijk om hier een gedegen plan voor te maken en klein te beginnen."
  translation_en: "An evofenedex adviser says it is important to make a sound plan for this and to start small."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:fe99a7dd16|live:match]"   # tool-filled; never a person's name

- claim_id: W4-017
  source_id: S-026
  location: "section 'Digiwerkplaats MKB'"
  original_nl: "De Digiwerkplaats mkb helpt ondernemers met een digitaliseringsvraag in zowel de regio West-Brabant als Noordoost-Brabant."
  translation_en: "Avans's Digiwerkplaats mkb helps business owners with a digitalisation question in both West-Brabant and Noordoost-Brabant."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:90ae96971b|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-018
  source_id: S-027
  location: "main text, paragraph 1"
  original_nl: "Mkb-maakbedrijven uit Zeeland, Noord-Brabant en Limburg kunnen vanaf vandaag voor ondersteuning bij hun digitalisering aankloppen bij EDIH Zuid-Nederland (EDIHZNL)."
  translation_en: "BOM announced that small and medium-sized manufacturing firms from Zeeland, Noord-Brabant and Limburg can turn to EDIH Zuid-Nederland for help with digitalisation (launch announcement, 2023)."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 number not in the quoted sentence: 2023; T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:ce97d96344|live:match]"   # tool-filled; never a person's name

- claim_id: W4-019
  source_id: S-027
  location: "main text, paragraph 3"
  original_nl: "EDIH Zuid-Nederland is er voor de mkb-maakindustrie, inclusief de toeleverindustrie en onderhoudsbedrijven in sectoren als agrifood, procesindustrie, semicon, medical systems, machinebouw en de automotive industrie."
  translation_en: "EDIH Zuid-Nederland is meant for the small and medium-sized manufacturing industry, including suppliers and maintenance firms in sectors such as agrifood, process industry, semiconductors, medical systems, machine building and automotive; a used-vehicle trader may not qualify."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:194651fb39|live:match]"   # tool-filled; never a person's name

- claim_id: W4-020
  source_id: S-028
  location: "section 'Privacy'"
  original_nl: "Als je persoonsgegevens of gevoelige bedrijfsinformatie invoert in een AI-tool, is deze informatie mogelijk niet beschermd."
  translation_en: "KVK warns that if you enter personal data or sensitive business information into an AI tool, that information may not be protected."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:5c13a9cd90|live:match]"   # tool-filled; never a person's name

- claim_id: W4-021
  source_id: S-028
  location: "section 'Onbetrouwbare inhoud'"
  original_nl: "Teksten die je met een AI-tool maakt, bevatten mogelijk onjuiste informatie."
  translation_en: "KVK warns that texts you make with an AI tool may contain incorrect information."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:4ea61f6364|live:match]"   # tool-filled; never a person's name

- claim_id: W4-022
  source_id: S-029
  location: "section 'Reasons for not using AI technologies'"
  original_nl: "In 2025, among EU enterprises who had ever considered using AI technologies, the most common reason for not using AI technologies was the lack of relevant expertise (70.89%), followed by lack of clarity about the legal consequences (52.52%), and concerns regarding violation of data protection and privacy (48.83%)."
  translation_en: "In 2025, among EU firms that had ever considered using AI, the most common reason for not using it was lack of relevant expertise (70.89%), then lack of clarity about the legal consequences (52.52%), then data protection and privacy concerns (48.83%). EU-wide, not Dutch."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW [h:bfacaa6f26|live:match]"   # tool-filled; never a person's name

- claim_id: W4-023
  source_id: S-030
  location: "chapter 6 'Redenen geen AI-technologie'"
  original_nl: "Voor microbedrijven die het gebruik van AI-technologie in 2025 hebben overwogen en toch besloten er geen gebruik van te maken was 'gebrek aan ervaring' veruit de belangrijkste reden (71,6 procent)."
  translation_en: "Among Dutch micro-businesses that considered using AI in 2025 and decided against it, 'lack of experience' was by far the main reason (71.6%). Micro-businesses are smaller than this reader's firm."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW [h:1d944dcb39|live:match]"   # tool-filled; never a person's name

- claim_id: W4-024
  source_id: S-030
  location: "chapter 6 'Redenen geen AI-technologie'"
  original_nl: "Ongeveer de helft van de microbedrijven noemde privacy als een reden om geen AI-technologie te gebruiken."
  translation_en: "About half of the Dutch micro-businesses named privacy as a reason not to use AI technology."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW [h:9b7787ab11|live:match]"   # tool-filled; never a person's name

- claim_id: W4-025
  source_id: S-032
  location: "section 'Bijna eenderde bedrijven heeft ICT-specialisten in loondienst'"
  original_nl: "In 2021 had 31 procent van de bedrijven met 10 of meer werkzame personen één of meer ICT-specialisten in loondienst"
  translation_en: "In 2021, 31 percent of Dutch companies with 10 or more employees had one or more ICT specialists on the payroll, so most did not."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW [h:8c8ca39b0e|live:match]"   # tool-filled; never a person's name

- claim_id: W4-026
  source_id: S-032
  location: "section 'Meer bedrijven bieden ICT-cursussen aan'"
  original_nl: "In 2022 bood 21 procent van de bedrijven hun eigen ICT-specialisten de mogelijkheid een opleiding of cursus te volgen"
  translation_en: "In 2022, 21 percent of Dutch companies let their own ICT specialists follow training or a course."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW [h:e67a83fcfe|live:match]"   # tool-filled; never a person's name

- claim_id: W4-027
  source_id: S-033
  location: "project page, section 'Bevindingen'"
  original_nl: "Mkb'ers geven aan met name drempels te ervaren m.b.t. inzicht in AI en de mogelijkheden ervan voor hún bedrijf"
  translation_en: "Dialogic found that small and medium-sized business owners mainly report barriers in understanding AI and what it can do for their own business."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:1af6609c89|live:match]"   # tool-filled; never a person's name

- claim_id: W4-028
  source_id: S-033
  location: "project page, section 'Bevindingen'"
  original_nl: "Efficiëntieoverwegingen zijn voor het mkb de belangrijkste motivatie voor de inzet van AI"
  translation_en: "Dialogic found that efficiency is the main reason small and medium-sized businesses give for using AI."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:7b8797f7de|live:match]"   # tool-filled; never a person's name

- claim_id: W4-029
  source_id: S-033
  location: "project page, section 'Bevindingen'"
  original_nl: "Het mkb geeft aan vooral behoefte te hebben aan praktische kennis, voorlichting, begeleiding en financiële steun"
  translation_en: "Dialogic found that small and medium-sized businesses say they mainly need practical knowledge, information, guidance and financial support."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:cd492de450|live:match]"   # tool-filled; never a person's name

- claim_id: W4-030
  source_id: S-034
  location: "advice page, recommendations section"
  original_nl: "De SER adviseert om het midden- en kleinbedrijf, waar AI nog beperkt wordt toegepast, praktisch te ondersteunen."
  translation_en: "The Social and Economic Council (SER) advises giving practical support to small and medium-sized businesses, where AI is still used only to a limited extent."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:630df918b2|live:match]"   # tool-filled; never a person's name

- claim_id: W4-031
  source_id: S-034
  location: "advice page, recommendations section"
  original_nl: "De overheid moet zorgen dat bedrijven in een netwerk met elkaar ervaringen en kennis uitwisselen."
  translation_en: "The SER says the government must make sure companies can share experience and knowledge with each other in a network."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:9e37a37b87|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-032
  source_id: S-034
  location: "advice page, recommendations section"
  original_nl: "Overheid, onderwijs en werkgevers moeten samen actiever aan de slag met scholing, bijscholing en een leven lang ontwikkelen."
  translation_en: "The SER says government, education and employers must work together more actively on training, retraining and lifelong learning."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:91efb84f3f|live:match]"   # tool-filled; never a person's name

- claim_id: W4-033
  source_id: S-035
  location: "news announcement"
  original_nl: "By September 2024, the European Digital Innovation Hubs had organised over 5 000 events reaching more than 200 000 participants and had delivered over 18 000 services."
  translation_en: "By September 2024, the European Digital Innovation Hubs had organised over 5 000 events reaching more than 200 000 participants and delivered over 18 000 services (EU-wide)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:65a69b8eec|live:match]"   # tool-filled; never a person's name

- claim_id: W4-034
  source_id: S-035
  location: "news announcement"
  original_nl: "JRC findings show that European Digital Innovation Hubs helped 90% of users to improve their digital maturity."
  translation_en: "The Commission's Joint Research Centre reports that European Digital Innovation Hubs helped 90% of users improve their digital maturity (EU-wide, based on the network's own monitoring)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:5fcdd92dc7|live:match]"   # tool-filled; never a person's name

- claim_id: W4-035
  source_id: S-035
  location: "news announcement"
  original_nl: "AI adoption and automation are among the areas that improved the most, accounting for 35% of performance increase."
  translation_en: "AI adoption and automation are among the areas that improved the most, accounting for 35% of the performance increase (EU-wide, based on the hub network's own monitoring)."
  kind: number
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:beb086c7ce|live:match]"   # tool-filled; never a person's name

- claim_id: W4-036
  source_id: S-036
  location: "press release, key findings"
  original_nl: "The share of firms in the European Union deploying generative AI is 37% compared with 36% of businesses in the US."
  translation_en: "The share of EU firms deploying generative AI is 37%, compared with 36% of US businesses (EIB Investment Survey 2025; all firms, not only SMEs)."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:de11062685|live:match]"   # tool-filled; never a person's name

- claim_id: W4-037
  source_id: S-037
  location: "project page, intro text"
  original_nl: "Ondernemers kunnen er kosteloos terecht voor advies, een concreet product, praktische ondersteuning en training."
  translation_en: "At the Digiwerkplaats MKB West-Brabant (a regional programme page hosted by NXT Moerdijk; it covers West-Brabant, not Veghel or Noordoost-Brabant), business owners can get advice, a concrete product, practical support and training free of charge."
  kind: statement
  evidence: company-reported
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 FAIL: S-037 decision is 'discard' [h:daf16785c6|live:match]"   # tool-filled; never a person's name

- claim_id: W4-038
  source_id: S-038
  location: "news item, body text"
  original_nl: "Bestuurders moeten het onderwerp agenderen, budgetteren en actief ondersteunen."
  translation_en: "A Rijksoverheid news item (Digitale Overheid) reporting the Dutch Data Protection Authority's (AP) guidance on AI literacy says managers and directors must put the topic on the agenda, budget for it and actively support it."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:7503581a44|live:match]"   # tool-filled; never a person's name

- claim_id: W4-039
  source_id: S-038
  location: "news item, body text"
  original_nl: "De AP roept organisaties op om AI-geletterdheid niet alleen bottom-up, maar ook top-down te organiseren."
  translation_en: "A Rijksoverheid news item (Digitale Overheid) reports that the Dutch Data Protection Authority (AP) calls on organisations to organise AI literacy not only bottom-up but also top-down."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:3a4b0af5a6|live:match]"   # tool-filled; never a person's name

- claim_id: W4-040
  source_id: S-038
  location: "news item, body text"
  original_nl: "Organisaties die AI-systemen ontwikkelen of gebruiken, zijn wettelijk verplicht om te zorgen dat medewerkers en opdrachtnemers voldoende kennis en vaardigheden hebben om AI verantwoord in te zetten."
  translation_en: "A Rijksoverheid news item (Digitale Overheid) reporting the Dutch Data Protection Authority's guidance says organisations that develop or use AI systems are legally required to make sure staff and contractors have enough knowledge and skills to use AI responsibly."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 source file carries a FLAG FOR HUMAN REVIEW; T1 credibility 2 [h:64b2399f7c|live:match]"   # tool-filled; never a person's name

- claim_id: W4-041
  source_id: S-039
  location: "p. 1, Abstract"
  original_nl: "In particular, we make use of a randomized controlled trial to analyze the effect of a nationwide innovation voucher scheme in the United Kingdom that grants SMEs across all industries financial support of up to 5,000 GBP for engaging the services of experts, e.g., from universities, research institutes or IP advisors, when pursuing an innovation-related project."
  translation_en: "A peer-reviewed study (in Research Policy) ran a randomized controlled trial of a UK government voucher worth up to 5,000 GBP that lets small firms in any industry pay for outside expert advice (for example from universities, research institutes or IP advisors) on an innovation project. This is a subsidy for buying expert advice, not an AI tool."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:5e678a0e36|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-042
  source_id: S-039
  location: "p. 1, Abstract"
  original_nl: "However, we also observe that these results fade out quite quickly, i.e., two years after the intervention many effects caused by the innovation voucher program have disappeared."
  translation_en: "The same study of the UK expert-advice voucher (not an AI programme) found that the gains faded quickly: two years after the voucher, many of its effects had disappeared."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:080444eea2|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-043
  source_id: S-039
  location: "p. 4, section 3.1 Context and program"
  original_nl: "The program provided up to 5,000 GBP to enable innovative small and medium-sized businesses to engage the services of experts they had not worked with before to gain new knowledge that could help their business to innovate and grow."
  translation_en: "The study describes the UK voucher as up to 5,000 GBP that let small and medium-sized firms hire outside experts they had not worked with before, to gain new knowledge for innovating and growing. It is a voucher for expert advice, not for AI."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:682fff69c0|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-044
  source_id: S-039
  location: "p. 4, section 3.1 Context and program"
  original_nl: "Given the relatively small amount of support, the scheme was mainly targeted at small-scale projects, for example leading to an improved IP protection and product, service, or process development, rather than breakthrough innovations."
  translation_en: "Because the UK voucher for outside expert advice was small, it was mainly aimed at small projects, such as better IP protection or improved products, services or processes, rather than breakthrough innovations."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:2a71d5dcfd|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-045
  source_id: S-039
  location: "p. 10, section 5.1 Descriptive statistics and comparison of means"
  original_nl: "Firms that responded to the first survey round were on average 6 years old, had on average 7 employees at the date of voucher application, and were mostly active in the service industry (72%)."
  translation_en: "In the study of the UK expert-advice voucher, the firms that answered the first survey were on average 6 years old, had on average 7 employees when they applied, and were mostly in services (72%). These are very small firms, much smaller than the traders this page is for."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:921fd2b0dd|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-046
  source_id: S-039
  location: "p. 14, section 6 Discussion and conclusion"
  original_nl: "Thus, it seems that while the voucher provides an effective stimulus to reduce knowledge constraints for SMEs for a specific project, it does not seem to help SMEs resolve knowledge constraints in the long run."
  translation_en: "The study concludes that the UK expert-advice voucher helped small firms close a knowledge gap for one specific project, but does not seem to help them close such gaps in the long run."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:b697deb375|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-047
  source_id: S-040
  location: "p. 1, Abstract"
  original_nl: "We conducted an empirical study encompassing 12,108 SMEs, based on survey data of the Flash Eurobarometer database from the European Union."
  translation_en: "A peer-reviewed study (in Technology in Society) analysed survey data on 12,108 small and medium-sized firms from the EU's Flash Eurobarometer. The survey was fielded in spring, before generative AI became common (the survey dates are in a separate claim)."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: NO MATCH; T1 credibility 2 [h:7f0b01cea0|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-048
  source_id: S-040
  location: "p. 1, Abstract"
  original_nl: "However, internal capabilities exert a greater influence on AI adoption in SMEs compared to business environmental support."
  translation_en: "The study finds that a firm's own capabilities matter more for adopting AI than outside support from the business environment (survey data from before generative AI)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:101d580b6f|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-049
  source_id: S-040
  location: "p. 1, Introduction"
  original_nl: "These challenges include financial constraints [10], a lack of expertise and skills [8,11], resistance to change, and difficulties in integrating AI with existing systems [12]."
  translation_en: "The study lists the challenges small firms face with AI as money limits, a lack of expertise and skills, resistance to change, and difficulty fitting AI into existing systems."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:ee0cd569af|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-050
  source_id: S-040
  location: "p. 6, 4.1"
  original_nl: "This survey, conducted between February and May 2020, explores diverse topics, including innovation and digital technologies."
  translation_en: "The survey behind the study was conducted between February and May 2020, so its AI findings predate generative AI tools."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:a6e5cf5289|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-051
  source_id: S-040
  location: "p. 6, 4.3"
  original_nl: "Regarding size, we categorized the companies into three groups: from 0 to 9 employees as micro-enterprises; from 10 to 49 employees as small enterprises; and from 50 to 250 employees as medium-sized enterprises."
  translation_en: "The study sorts firms into micro (0 to 9 employees), small (10 to 49) and medium-sized (50 to 250). A trader with 10 to 50 staff falls in the small and lower medium bands."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:6581a65d98|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-052
  source_id: S-040
  location: "p. 8, 5"
  original_nl: "It is evident that digitalisation capabilities have the most significant impact on AI (digitalisation: .730; 100 % normalized value), followed by innovation capabilities (innovation: .195; 26.7 % normalized value), with business environmental support having the least impact on the probability of adopting AI (digitalisation: .075; 10.3 % normalized value)."
  translation_en: "In the pre-generative-AI survey data, a firm's digital capabilities had the biggest effect on whether it adopted AI, then its innovation capabilities (26.7% of the digital effect), and outside business support had the least (10.3% of the digital effect)."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:b05348808c|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-053
  source_id: S-040
  location: "p. 9, 5"
  original_nl: "Moreover, when we examine node 5 combined with node 15, we observe a synergistic effect between the variables of digital capabilities and innovation capabilities."
  translation_en: "The study also finds that digital capabilities and innovation capabilities reinforce each other in raising the chance that a small firm adopts AI (survey data from before generative AI)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:268ebd5727|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-054
  source_id: S-041
  location: "p. 719, Abstract"
  original_nl: "Furthermore, internal characteristics, such as internationalization and firm size, and external factors, such as the availability of digital skills and infrastructure, are significant drivers of digitalization at the firm level."
  translation_en: "A peer-reviewed study of European small firms (in Small Business Economics) finds that internal traits such as internationalisation and firm size, and outside factors such as the availability of digital skills and infrastructure, are significant drivers of digitalisation. Its data is a survey from before generative AI."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: NO MATCH; T1 credibility 2 [h:a86a0b8c47|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-055
  source_id: S-041
  location: "p. 734, section 6 Conclusions"
  original_nl: "Despite the potential benefits from digitalisation, European firms, and in particular SMEs, are lagging in the adoption of ADTs due to associated complexity and costs."
  translation_en: "The study concludes that European firms, especially small and medium-sized ones, lag in adopting advanced digital technologies (which include AI) because of their complexity and cost (survey data from before generative AI)."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:f25c21e1fa|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-056
  source_id: S-041
  location: "p. 722, section 2.1 (skills and training)"
  original_nl: "Hence, for successful adoption, firms must develop complementary skills, adapt them to non-digital environments and techniques, train the workforce, align previous production methods and, in essence, modify their organisational culture by developing a whole range of secondary innovations (Ciarli et al., 2021)."
  translation_en: "The study says, citing Ciarli et al. (2021), that for adoption to succeed firms must build complementary skills, train their workforce, align earlier ways of working and change their organisational culture."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:47d0495844|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-057
  source_id: S-041
  location: "p. 722, section 2.1 (skills scarce)"
  original_nl: "ADTs require complex, often costly, skills that are scarce in the labour market (Shapiro & Mandelman, 2021)."
  translation_en: "The study says, citing Shapiro and Mandelman (2021), that advanced digital technologies need complex and often costly skills that are scarce in the labour market."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:a4ff368e6c|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-058
  source_id: S-041
  location: "p. 724, section 2.3"
  original_nl: "Therefore, firms need to invest in generating learning effects and to train their workforce."
  translation_en: "The study argues that firms need to invest in learning and in training their workforce."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:8e5c9aabd9|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-059
  source_id: S-041
  location: "p. 725, section 3.1 The database (sample)"
  original_nl: "The survey was carried out between February 19th and May 5th, 2020, and covers all European countries in addition to Bosnia and Herzegovina, Brazil, Canada, Croatia, Great Britain, Iceland, Japan, Kosovo, Makedonia, Norway, Serbia, Turkey and USA, with a sample of 16,365 firms."
  translation_en: "The survey behind the study ran from 19 February to 5 May 2020 and covers all European countries plus several others, with a sample of 16,365 firms. It predates the generative AI wave."
  kind: number
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:57b6e4716c|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-060
  source_id: S-041
  location: "p. 729, footnote 13 (Netherlands)"
  original_nl: "Here, Western European countries are Austria, Belgium, Germany, France, Ireland, Luxembourg and the Netherlands."
  translation_en: "The study groups the Netherlands with Austria, Belgium, Germany, France, Ireland and Luxembourg as 'Western European'. It reports no Netherlands-only result."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:d8e98a43aa|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-061
  source_id: S-041
  location: "p. 727, section 3.2 (size classes)"
  original_nl: "Similarly, the largest firms have the highest adoption rates for all technologies, while the smallest ones present lower rates of adoption."
  translation_en: "In the pre-generative-AI survey data the largest firms have the highest adoption rates for all the technologies studied (including AI), while the smallest firms adopt less."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T1 credibility 2 [h:05ad8b7dd7|live:NO MATCH]"   # tool-filled; never a person's name

- claim_id: W4-062
  source_id: S-042
  location: "p. 1299"
  original_nl: "It is essential to note, however, that overly complex AI applications may not be feasible for SMEs because of their cost and complexity (Moeuf et al., 2020)."
  translation_en: "A systematic review of studies on AI in small firms reports, citing Moeuf et al. (2020), that overly complex AI applications may not be feasible for small firms because of their cost and complexity."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:9955b7ce7b|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-063
  source_id: S-042
  location: "p. 1309, Knowledge/Resources"
  original_nl: "SMEs may face hindrances due to poor technical expertise, inadequate skills, or improper management styles due to limited AI education (Liu, 2023)."
  translation_en: "A systematic review reports, citing Liu (2023), that small firms may be held back by poor technical expertise, inadequate skills or unsuitable management styles caused by limited AI education."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:f2c6a8001e|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-064
  source_id: S-042
  location: "p. 1309, Knowledge/Resources"
  original_nl: "Furthermore, the lack of AI specialists limits the potential for AI in SMEs (Lemos et al., 2022)."
  translation_en: "A systematic review reports, citing Lemos et al. (2022), that the lack of AI specialists limits what AI can do for small firms."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:cbde62a2bf|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-065
  source_id: S-042
  location: "p. 1309, Resources"
  original_nl: "In addition, with limited financial resources, SMEs often acknowledge the benefits of AI systems but fear the associated costs (Dörr et al., 2023)."
  translation_en: "A systematic review reports, citing Dörr et al. (2023), that small firms with limited money often see the benefits of AI systems but fear the costs."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:2f95521717|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-066
  source_id: S-042
  location: "p. 1310, Culture"
  original_nl: "Comprehensive education and practical training empower SME workers, allaying apprehensions and facilitating perceived ease of use (Hamdan et al., 2022)."
  translation_en: "A systematic review reports, citing Hamdan et al. (2022), that thorough education and practical training give small-firm staff confidence, ease their worries and make AI seem easier to use."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:68699321e3|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-067
  source_id: S-042
  location: "p. 1312, Ecosystem"
  original_nl: "Due to limited innovative resources and capabilities, SMEs often partner with external organizations for collaborative R&D (Qu et al., 2021)."
  translation_en: "A systematic review reports, citing Qu et al. (2021), that because their own resources and capabilities are limited, small firms often partner with outside organisations for joint research and development."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:f0ca236979|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-068
  source_id: S-042
  location: "p. 1312, Ecosystem"
  original_nl: "Moreover, SMEs leverage external support to foster innovation, with networks serving as key sources of innovation (Hermawati & Gunawan, 2021)."
  translation_en: "A systematic review reports, citing Hermawati and Gunawan (2021), that small firms use outside support to innovate, with networks as key sources of innovation."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:fb65f37914|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-069
  source_id: S-042
  location: "p. 1315, Discussion"
  original_nl: "While limited resources are seen as one of the most hindering factors, management commitment can compensate for that negative, as it strengthens communication between experts, driving an innovative and progressive mindset within the company (Rojas-Córdova et al., 2020)."
  translation_en: "A systematic review reports, citing Rojas-Córdova et al. (2020), that limited resources are among the most hindering factors, but management commitment can offset this by strengthening communication between experts and driving an innovative mindset."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:238c6c4f59|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name

- claim_id: W4-070
  source_id: S-042
  location: "p. 1316, Managerial relevance"
  original_nl: "Decision-makers should foster a learning culture, invest in the workforce, engage in transparent communication, and practice adaptable leadership."
  translation_en: "The review's advice to decision-makers is to foster a learning culture, invest in the workforce, communicate openly and lead adaptably."
  kind: statement
  evidence: independently-verifiable
  scope: sector
  translated_by: tool
  verified_by: "Floyd"
  auto_verified: "2026-10-01 PERSON: T2 live document: fetch failed: HTTPError 403; T1 credibility 2 [h:cf6e532a53|live:fetch failed: HTTPError 403]"   # tool-filled; never a person's name
```
