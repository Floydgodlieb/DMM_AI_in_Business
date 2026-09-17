# Who owns the AI tools I use, and what happens to my business if that changes?

version: 1.0 · 17-09-2026
checking note: second reader passed all 4 criteria (steps named, time-saving vs
customer-touching stated, complexity labelled, one next step given) and spot-checked 5
statements against their original source, per check.md — the individual statements checked
were not named in check.md, so this note can't say which five.

## Why this question matters for a trader like you

In 2024, 22.7% of Dutch businesses with 10 or more staff used one or more AI technologies — up
almost 9 percentage points from 2023 [W2-001, independently-verifiable, sector]. AI use is highest at large companies and lowest at
the smallest ones [W2-002, independently-verifiable, sector], and businesses that already use AI
skew larger than the 10-49 staff bracket most traders in this sector sit in
[W2-003, independently-verifiable, sector]. Trade is the single largest sector among AI-using
businesses [W2-004, independently-verifiable, sector] — so this is already happening in
businesses like yours, not just at the frontier.

BAS World, a much larger Dutch trader in the same kind of goods, is that frontier case: its AI
agents for sales, pricing and customer service run on a modular setup hosted on AWS
[W2-021, company-reported, case], built to be model-agnostic — ChatGPT, Gemini and Claude are
all interchangeable [W2-022, company-reported, case] — and designed so BAS World is not stuck
depending on the implementation partner that built it [W2-023, company-reported, case]. That
"not stuck depending on" design choice is itself the answer to this page's question: it is
possible to reduce lock-in, but it has to be designed in, not assumed.

## What you depend on, and why it can change

When you use an AI tool, you are usually depending on a foreign supplier for the software, and
often for where your d
- Microsoft's own documentation says Copilot normally sends your prompts to the nearest regional
  data centre, but can send them to another region if the regional data centre is full
  [W2-028, company-reported, sector]. For EU customers, Microsoft says EU traffic is kept inside
  an "EU Data Boundary" [W2-029, company-reported, sector] — but Microsoft also states that one
  of its AI models, supplied by Anthropic, is currently excluded from that EU boundary
  [W2-030, company-reported, sector]. In other words: "hosted in the EU" can have exceptions, and
  they can be model-specific.
- DeepL, a translation tool, is a German company [W2-024, company-reported, sector], but its own
  contract terms allow it to process your text on servers run by other cloud companies, with no
  fixed location guaranteed unless you negotiate one [W2-025, company-reported, sector].
- Nationally, the Dutch central bank and financial regulator have separately warned that a
  sector that leans on a small number of non-European IT suppliers takes on a real, growing risk
  [W2-013, independently-verifiable, sector], precisely because everyone ends up on the same
  handful of providers and infrastructure [W2-014, independently-verifiable, sector]. That
  warning was written about banks, not vehicle traders — but the mechanism it describes
  (concentration on a few non-EU suppliers) is the same one this page is about.
- The Rathenau Instituut, an independent Dutch research institute, makes the same point about
  Dutch public organis
- On the "what happens if it changes" question directly: a Bruegel commentary describes everyone
  outside the US and China as living in "managed dependence" on foreign AI providers, and points
  to a directive restricting non-US access to certain AI models as an example of what that
  dependence can mean in practice [W2-019, independently-verifiable, sector].

## The duties that apply

- **AI Act.** If a tool you use counts as "high-risk" under the EU AI Act, the law requires you,
  as the business using it (the "deployer"), to use it according to the supplier's instructions
  [W2-009, independently-verifiable, sector], and to tell people when they are subject to it
  [W2-010, independently-verifiable, sector].
- **GDPR.** If a supplier processes personal data on your behalf (most cloud AI tools do), the
  European Commission has published standard contract clauses for exactly this relationship,
  under Article 28(7) of the GDPR [W2-020, independently-verifiable, sector]. You need one of
  these (or an equivalent) signed with every such supplier.
- **Sanctions screening / export documents.** Dutch Customs states plainly that export of some
  goods to some countries is banned outright, or allowed only with a permit
  [W2-005, independently-verifiable, sector]. At EU level, the sanctions regime on Russia (legal
  basis: Council Regul

Each recommendation below names one step in your sales or documentation chain
(lead → quotation → contract → payment → export document), says whether it saves you time or
touches the customer, and how complex it is to adopt.

1. **Export document step — screening trading partners against sanctions lists.**
   *Time-saving automation, not customer-touching.* Complexity: **bought tooling**. Products
   such as Descartes' Denied Party Screening automate checking a trading partner against
   government watchlists and plug into your own systems
   [W2-026, company-reported, sector]. Descartes itself claims an AI feature that cuts false
   positives by 60% [W2-027, company-reported, sector] — that is the vendor's own figure, not
   independently checked, so treat it as a starting point for a demo, not a guarantee.

2. **Lead / quotation step — translating listings and quotes for non-EU buyers.**
   *Customer-touching automation* (the buyer sees the translated text directly). Complexity:
   **bought tooling**. A translation tool is a plausible fit here, but confirm in its contract
   where your text is actually processed before you rely on it for anything commercially
   sensitive [W2-025, company-reported, sector] — "translation vendor" is not automatically
   "EU-hosted." The duty that applies is the same one as in the Duties section above: get a
   GDPR Article 28 data-processing agreement with this supplier too, before it ever sees a real
   customer quote [W2-020, independently-verifiable, sector].

3. **Quotation step — AI-assisted pricing.** *Time-saving automation, not customer-touching* (it
   informs a price your staff still sets). Complexity: **in-house build — flagged as a
   warning**. BAS World's pricing agent is a custom, purpose-built system on a modular
   architecture [W2-023, company-reported, case]. That took a much larger company, with an IT
   partner, to build. For a 10-50 staff trader with no IT function, copying this approach
   directly is very unlikely to be the right first step; treat it as evidence of what is
   possible at scale, not a template to copy. The duty to check before adopting anything like
   this is the same AI Act deployer duty named above: confirm with whoever builds or sells you
   the tool whether it counts as high-risk, and if so, that you can meet the instructions-for-use
   and oversight duty it carries [W2-009, independently-verifiable, sector].

4. **Contract step — the data-processing agreement itself.** *Not customer-touching; a compliance
   step, not a saving.* Complexity: **named process owner**. Someone in the business — named, not
   "whoever has time" — should be responsible for getting a GDPR Article 28 data-processing
   agreement signed with every AI supplier that touches customer or contract data
   [W2-020, independently-verifiable, sector], and for checking each supplier's AI Act deployer
   obligations apply and are met [W2-009, independently-verifiable, sector].

