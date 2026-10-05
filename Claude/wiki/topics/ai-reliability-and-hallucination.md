---
title: AI reliability and hallucination
type: topic
summary: Language models state false things with confidence, even with document lookup, and AI use outside its competence lowers correctness
updated: 2026-10-05
sources: S-052, S-053, S-069, S-072, S-049
---

# AI reliability and hallucination

Language models can produce plausible but false content, and the evidence shows people using them outside what they do well get worse results. For quotations, contracts and export documents, a person has to check the output.

## The picture

- Large language models are prone to hallucination: plausible yet nonfactual content [W4-101].
- Misleading output can directly influence decisions, spread false beliefs or cause harm [W4-102].
- Systems that retrieve documents before answering (RAG) still suffer from hallucinations [W4-103]. This matters for firms that rely on a search assistant over their own data.
- In a legal test, models made things up in 58% (ChatGPT 4) to 88% (Llama 2) of direct questions about real US court cases [W4-105]; the authors say theirs is the first systematic evidence for public-facing models and caution against unsupervised use [W4-104] [W4-106]. The setting is legal, not business documents, and the models are those tested at the time [W4-105].
- Outside the frontier of AI capability, consultants using AI were 19 percentage points less likely to produce correct solutions [W4-165]; inside the frontier they were faster and better [W4-164]. See [[genai-productivity-at-work]].
- SMEs themselves report accuracy, harmful content and legal uncertainty as issues [W4-182].
- For high-risk systems the AI Act requires human oversight by people with competence, training and authority [W4-094].

## Contradictions and tensions

> [!contradiction] W4-164 vs W4-165: AI makes consultants better inside the frontier and worse outside it
> Both findings are from the same working paper (with BCG) [W4-166]. The difficulty for a user is that the frontier is not visible in advance; this is the paper's own point [W4-166].

## Gaps

- No claim measures hallucination in translation, quotation drafting or customs-document tasks.
- The hallucination rates come from older models and a legal setting; no claim gives current rates for business text.

## Sources

[[S-052]] · [[S-053]] · [[S-069]] · [[S-072]] · [[S-049]] · see also [[ai-risk-management]], [[ai-act]]
