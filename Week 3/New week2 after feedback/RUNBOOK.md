# RUNBOOK — producing one handbook page (week 2, by hand)

Boss this week: the product manager. One person drives the CLI assistant; the others work on the same files in parallel.
Every stage: (1) start the timer, (2) do the stage, (3) stop the timer and log it in `timelog.csv`, (4) commit.

## Day 1 — set up (30 min)
1. Unzip `platform.zip` so the files sit directly in
   `C:\Users\floyd\Desktop\DDM-AI in business repository\platform`
   (i.e. `...\platform\context.md`, not `...\platform\platform\context.md`). Open a terminal in that `platform` folder and start the CLI assistant there, so the folder boundary of door 2 is the folder it can see. The interview recording never goes in this repository.
2. Rename `ASSISTANT.md` to whatever your CLI assistant reads first (`CLAUDE.md` for Claude Code, `AGENTS.md` for others). It tells the assistant to read `context.md` and obey the stage rules.
3. Fill `question.md` (already drafted for week 2 — check it).
4. Every team member: open `timelog.csv` and log from the first minute.

## Stage 1 — Find sources (developer, ~2 h)
- Run the searches in `03_Assignment2_Writeup.md` §2, in that order, NL first. Log every query in `searchlog.md`.
- For each source you keep, ask the assistant: *"Create sources/S-0xx.md from this URL using the source.md template."* Check URL and date yourself.
- Stop rule: two searches in a row give nothing new, or one primary source per claim + one per region on the leadership question.
- Output: 15–25 `sources/S-0xx.md` files.

## Stage 2 — Appraise (tester, ~1 h)
- Ask the assistant: *"Rate every file in sources/ on credibility, relevance, recency (1–3) using the scale in 03_Assignment2_Writeup.md §1 and write appraised.md. One-line reason each. Do not discard anything."*
- You read every rating (this week: all of them — that is open question 2, and reading all is how you find out how long it takes). Change what you disagree with; fill `human_override`. Set `decision: use/discard`.

## Stage 3 — Translate (developer + one verifier, ~2 h)
- Ask: *"For every source with decision: use, extract the sentences we will rely on into claims_en.md using claims_en.example.md. original_nl verbatim. Set kind, evidence, scope. Leave verified_by empty."*
- A second person opens each source and fills `verified_by` for every `number` and `quote` claim. No sampling.
- Interview claims (if the visit has happened): a person types them in directly, `translated_by: person`.

## Stage 4 — Draft (author, ~2 h)
- Ask: *"Write draft.md following 04_Handbook_Page_Week2_Draft.md. Fill each [CLAIM] slot only from claims_en.md, appending the claim-id in brackets. Leave a slot empty if no claim supports it."*
- You choose the angle and edit the text. Do not add a sentence the assistant can't tie to a claim-id.

## Stage 5 — Check (tester + second reader, ~1.5 h)
- Ask: *"Produce check.md from the template: for each [claim-id] in draft.md confirm the claim exists, the quote appears in the saved source, numbers match, a duty is named where the sentence makes a recommendation, and evidence/scope labels are present."*
- The second reader (never the author, rotates) answers criteria 1, 2, 5, 6 pass/fail with one line, and opens the original source for five statements of their choice.
- Any fail → back to Stage 4. PM arbitrates disagreements.

## Stage 6 — Publish (deployer, ~1 h)
- Copy the approved `draft.md` to `page.md`; add version, date and the checking note ("x of y statements opened by second reader; all numbers checked").
- Publish on the course site by the route the session gave (branch → pull request → link check → merge). No direct push.
- Post in Teams: the page link, `01_Technical_Blueprint_v1.1.md`, `02_PRD_v2.1.md`, and the assignment 2 write-up wherever the session said.

## After
- Total the hours per stage from `timelog.csv`. Put the number in PRD §8 ("what we have now"). That is your baseline.
- Each person: write portfolio entry 2 after the gates answer (Mon 21 Sept).
