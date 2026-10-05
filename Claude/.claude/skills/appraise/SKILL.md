---
name: appraise
description: Stage 2 of the handbook pipeline. Rate the sources not yet in appraised.md on credibility, relevance and recency (1-3), keeping every existing row and human override. Use when asked to rate, appraise or judge sources.
---

# Stage 2 — Appraise (new sources only)

Read `context.md` first (§3c decides who reads which rating). Scale: `docs/03_Assignment2_Writeup.md` §1. Shape: `templates/appraised.template.md`.

## Steps
1. Run `python .claude/scripts/gates.py todo`. Rate **only** the sources on the "rate only these (new)" line, plus any on the "credibility 3 not allowed" line. Every other row stays exactly as it is — the library is appraised once.
2. For each, score credibility, relevance, recency 1–3 and write one-line reason. Note any gate (G1–G5) it fails.
3. **Credibility 3 only if** type is `regulation`, `statistics` or `vendor-contract-doc` **and** the URL is the issuer's own domain **and** the excerpt is contract/regulation/statistics text, not marketing. A mirror, summary or product page is at most 2. When unsure, score 2 — a 2 costs one person check; a wrong 3 skips it. (The type part is enforced by the script; the domain and marketing part is yours.)
4. A source file with `FLAG FOR HUMAN REVIEW` keeps its flag; mention it in the reason.
5. Default `decision: use`. Never discard on your own — a person sets `discard`.
6. Append the new rows to the table in id order. Never change a row whose `human_override` is filled.

## Hand-off
Report only: the new rows at credibility 1–2 — the only ratings a person must read (context.md §3c).
