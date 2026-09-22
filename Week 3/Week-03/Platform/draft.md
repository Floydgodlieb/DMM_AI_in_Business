<!--
PROCESS NOTE (not page content). This draft was produced by the assistant in one pass:
research (searchlog.md), appraisal (appraised.md), translation (claims_en.md) and this draft,
without the team's own second-reader step (blueprint §1, part 5). Every substantive sentence
below carries a claim-id taken only from claims_en.md. verified_by is empty on every claim used
(claims_en.md's own note) — this page cannot pass Check until a person on the team re-opens each
source and confirms it, and a second reader has not yet opened the five statements Check
requires. Do not publish this page as-is.
-->

# Can I trust this AI tool — with my data, its answers and my people?

*How much checking has been done on this page: none yet by a second human reader — see the
process note above. Every quote and number below traces to a real, dated source in
`sources/` (search trail: `searchlog.md`); nothing is drawn from memory.*

Week 2 asked who owns the AI tools you use. This week asks the question that actually decides
whether you use them: can you trust what they do with your data, whether to trust what they
tell your customers, and whether you even know what your own people are doing with them?

## What leaves the building — and could you run it yourself?

Using an AI tool almost always means sending something outside your own walls, even when the
tool's marketing says "hosted in the EU." Microsoft's own documentation shows why that phrase
needs a second look: it operates an "EU Data Boundary" meant to keep EU customer traffic inside
the EU — but one of the models available through it, supplied by Anthropic, is currently
excluded from that boundary [W3-015, company-reported, sector]. "Hosted in the EU" can have
named exceptions, model by model, not just vendor by vendor. DeepL, a translation tool this
trade plausibly uses for buyer-facing quotes, is similar: its own contract terms allow it to
process your text on its own servers or on other companies' cloud infrastructure, with no fixed
location guaranteed unless you negotiate one [W3-014, company-reported, sector]. Nationally,
the Dutch central bank and financial regulator warn that leaning on a small number of
non-European IT suppliers is a growing, real risk [W3-012, independently-verifiable, sector] —
written about banks, but the mechanism (everyone ends up on the same few providers) is the one
this page is about.

Whatever a supplier processes on your behalf, the GDPR duty is the same and does not depend on
what kind of AI tool it is: get a data-processing agreement in place before it ever sees a real
customer record [W3-013, independently-verifiable, sector].

Could you avoid this entirely by running the model yourself, on your own hardware? It is a real,
discussed option in 2026 [W3-016, company-reported, sector] — but the only source found for it
this week was a vendor-tier blog with no independently checkable cost figures, so treat any price
you see quoted as a starting point for your own enquiry, not a fact. For a trader with no IT
function, this is closer to BAS World's own in-house-built pricing tools than to something to
copy first.

## When can it act for you, and when should it only advise?

Ask this two ways and you get two different answers. Asked as "what can AI agents do for my
business," the search results are mostly optimistic and generic: faster replies, drafts instead
of blank pages. Asked as "who pays when the AI agent gets it wrong," the answer sharpens
immediately: a Canadian tribunal held an airline liable for negligent misrepresentation because
its own customer-facing chatbot gave a customer wrong information about a fare refund — the
airline argued it could not be responsible for what its own tool said, and lost
[W3-010, independently-verifiable, sector]. A named legal analysis explains why this keeps
happening: ordinary employer-liability law assumes a human employee is acting, and a fully
autonomous AI agent does not fit that assumption cleanly, so the law here is still catching up
[W3-009, independently-verifiable, sector]. In practice, that gap does not protect you — it
means you are answerable for what your AI tells a customer whether or not any AI-specific
regulation happens to cover that tool. The lesson for how you ask your own questions about AI is
the same one this page's method used: "how can it help me" and "who pays when it fails" are not
the same question, and only one of them protects you.

The EU AI Act's own answer to "when should a person be able to step in" is Article 14: a
system must be built so a named person can override what it produced in a specific case, and can
stop it altogether [W3-005, W3-006, independently-verifiable, sector]. That duty is legally
binding only for AI systems classed "high-risk" — a sales-chat or translation tool is very
unlikely to be one — and a July 2026 EU reform ("Digital Omnibus") has in any case pushed the
compliance date for that whole category back to 2 December 2027, while adding lighter,
size-adjusted rules for small and mid-cap firms once it does apply
[W3-007, W3-008, independently-verifiable, sector]. So: not yet a binding duty for most tools
this reader would use — but a cheap habit to adopt anyway, because the Air Canada case did not
need the AI Act to bite.

## What happens when staff use AI and do not say so?

A 2025 study of 600 organisations, fieldwork by the independent Ponemon Institute, found that
"shadow AI" — staff downloading or using tools the business never approved — added an extra
$670,000 to the average cost of a data breach, and caused one in five of the breaches studied
outright [W3-001, W3-002, independently-verifiable, sector]. A Dutch trend report puts local
unapproved use at 78% of AI-using employees [W3-003, independently-verifiable, sector] — a
different study, a different country, the same shape of problem.

"We never approved that tool" is not a defence. Under the AI Act's own definition, a business
counts as a "deployer" of an AI system just by using it under its authority for work — there is
no separate test for whether management signed off on it [W3-004, independently-verifiable,
sector]. The GDPR duty above follows the same logic: it attaches to the data, not to who bought
the software.

## What this looks like as recommendations

Each one names a step in the lead → quotation → contract → payment → export document chain,
says whether it saves time or touches the customer, and how complex it is.

1. **Lead / quotation step — an AI chat or search tool answering customers directly.**
   *Customer-touching.* Complexity: **named process owner**. Someone decides, in writing, which
   kinds of answer a person must check before it reaches a customer — the Air Canada case is
   the reason this matters even though nothing in current law requires it yet for this class of
   tool [W3-010, W3-005].

2. **Quotation step — translating listings and quotes for non-EU buyers.**
   *Customer-touching.* Complexity: **bought tooling**. Before relying on any translation tool
   for a commercially sensitive quote, confirm in its contract where your text is actually
   processed [W3-014] and get the GDPR data-processing agreement signed first [W3-013].

3. **Every step, before the others work — a one-page, named AI-use policy.** *Not
   customer-touching; a governance step, not a saving.* Complexity: **named process owner**.
   States which AI tools staff may use anywhere in the lead-to-export-document chain and what
   may never go into them. Criterion 1 asks for one chain step per recommendation; this one is
   named as an exception on purpose, because the disclosure numbers above show the problem is
   not any single step — it is not knowing which tools are already touching all of them
   [W3-001, W3-003].

4. **Contract step — the data-processing agreement itself.** *Not customer-touching.*
   Complexity: **named process owner**. One person, named, responsible for a signed GDPR
   Article 28 agreement with every AI supplier that touches customer or contract data
   [W3-013], and for checking whether any high-risk-classed tool's Article 14 duties apply once
   the 2027 deadline arrives [W3-007, W3-008].

## Next step

- **Owner:** the commercial manager, for the AI-use policy (recommendation 3) — the one step on
  this list that needs no new tool and no budget approval to start.
- **Rough cost:** a half-day to draft the policy plus one team meeting to agree it.
- **Three-month check:** ask staff which AI tools they actually used against what the policy
  names, and check whether any customer-facing AI answer went out without a person reviewing it
  first.

## Disclaimer

This page offers inspiration and starting points, not commercial advice or guarantees.
Educational, not consultancy. Decisions about your firm remain your own.
