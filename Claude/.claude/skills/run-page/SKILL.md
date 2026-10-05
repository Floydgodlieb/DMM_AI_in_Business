---
name: run-page
description: Run the handbook pipeline stage by stage, stopping at every point a person must act. Run only when the product manager asks for it.
disable-model-invocation: true
argument-hint: "[stage to start from, 1-5; default: the first with work left]"
---

# Run one handbook page

You are the boss's assistant, not the boss: the product manager decides when a stage moves on. Read `context.md` first.

Start with `python .claude/scripts/gates.py todo` — it shows which stages have work left. Start at stage `$ARGUMENTS`, or the first stage with work. Run one stage, report, stop at its gate, and ask before the next.

| Stage | Who runs it | Gate before the next stage (a person) |
|---|---|---|
| 1 Find | `/find-sources`: several `source-finder` agents at once, then `gates.py intake` | Person checks URL and date of each new source. |
| 2 Appraise | `appraiser` agent (new sources only) | Person reads only new credibility 1–2 rows; sets overrides and `discard`. |
| 3 Translate | `translator` agent (it runs `verify_claims.py --write --changed` itself) | Person works through `review_queue.md`. FAIL claims back to `translator` first. |
| 4 Draft | `drafter` agent (precheck clean before handing over) | Person sets the angle before, edits after. |
| 5 Check | `checker` agent | Second reader (not the author) fills criteria 1, 2, 5, 6; PM decides publish/return. |
| 6 Publish | none — `/publish-prep` by the deployer, then by hand | — |

After each stage, remind the person to log time with `/log-time`.

Never skip a gate because its file looks complete, and never run stage 6.
