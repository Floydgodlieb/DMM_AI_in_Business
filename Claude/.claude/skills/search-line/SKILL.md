---
name: search-line
description: One search line of Stage 1, run by a source-finder agent in parallel with others. Saves kept sources to library/sources/incoming/ and logs every query. Not for direct use; /find-sources launches it.
user-invocable: false
---

# One search line

You are one of several searchers running at the same time. Your line code (e.g. `VEND`) and brief come from the coordinator. Read `context.md` §1–2 and `docs/03_Assignment2_Writeup.md` §1 (gates G1–G5) — nothing else.

## Steps
1. Run `python .claude/scripts/gates.py library` once. Do not save anything whose URL is already there; prefer publishers not yet in it.
2. Search your line only, in the language(s) the brief gives. Prefer the primary document over any summary of it (G5).
3. For each source you keep, write `library/sources/incoming/<CODE>-<NN>.md` (`VEND-01`, `VEND-02`, …) from `templates/S-000.template.md`, with `id: <CODE>-<NN>`. Excerpts **verbatim**, each with page/section — the live page is compared character by character later.
4. If a page's text looks summarised, garbled, or names things you cannot confirm exist, add a line `FLAG FOR HUMAN REVIEW: <reason>`.
5. Log every query as one table line in `library/sources/incoming/searchlog-<CODE>.md`:
   `| date | engine | exact query | kept (your placeholder ids) | discarded, why |`
6. Stop when two searches in a row give nothing new, or your brief's target is met. At most 6 kept sources per line.

## Rules
- Write only inside `library/sources/incoming/`. Never touch `library/sources/S-*.md`, `searchlog.md` or other agents' files.
- No URL fetched, no source. Never save interview material.
- Return one line per kept file: placeholder id · publisher · type · why it is new.
