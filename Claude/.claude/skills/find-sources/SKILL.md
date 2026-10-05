---
name: find-sources
description: Stage 1 of the handbook pipeline, as coordinator. Checks the source library, splits the search into lines, runs several source-finder agents at the same time, then merges their results into library/sources/. Use when asked to find or add sources for the week's question.
argument-hint: "[optional: a single URL to save, or line codes to run, e.g. VEND TT-CN]"
---

# Stage 1 — Find sources (coordinator)

Read `context.md`, `question.md` and `docs/03_Assignment2_Writeup.md` §2.

## A single URL
If `$ARGUMENTS` is one URL: launch one `source-finder` with line `URL` and that address. Then run intake (step 4).

## The parallel search
1. **Library first.** Run `python .claude/scripts/gates.py library`. The library carries over between weeks: regulation, statistics and vendor-contract sources stay valid (Check re-fetches them live every week). Do not search again for what it already covers.
2. **Pick the lines with a gap** for this week's question. Default set (writeup §2 order, think tanks split by region so each perspective gets its own searcher — that is where the diversity rule needs two sources):

   | Code | Line | Language |
   |---|---|---|
   | REG | Regulation and official documents (EUR-Lex, Commission, Rijksoverheid, Douane) | NL + EN |
   | STAT | Official statistics (CBS, Eurostat, national bodies) | NL first |
   | VEND | Vendor contract docs: DPA, hosting/region, sub-processors, ownership — tools this sector uses | EN |
   | TT-US | Think tanks / institutes, US perspective | EN |
   | TT-EU | Think tanks / institutes, European and Dutch perspective | NL + EN |
   | TT-CN | China perspective: official documents and China-focused institutes | EN |
   | SECT | Sector: trader channels, sector bodies (strand 2); press only for events, as pointer to a primary | NL first |

   Skip a line whose gap is already filled (stop rule: one primary source per claim, two per region with one at credibility 3).
3. **Launch all chosen lines in one message**, one `source-finder` agent each, so they run at the same time. Give each: its code, the line, its search terms from writeup §2 plus terms for this week's question, and the publishers already in the library for that line (so it looks for *different* ones).
4. **Merge.** When all have returned, run `python .claude/scripts/gates.py intake`. It gives the new files their final ids, sets aside duplicates two searchers both found, and adds their searchlog lines.
5. **Report** the new ids per line, the duplicates, and any `FLAG FOR HUMAN REVIEW`. Gate: a person checks URL and date of each new source.

Never write source files yourself in this mode; only the searchers do, into `library/sources/incoming/`.
