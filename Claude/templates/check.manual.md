# check.manual.md — doing Stage 5 by hand (the back-up for Check)

Use this when the assistant or the verification script cannot run. It produces the same `check.md` (shape: `templates/check.template.md`). Read `context.md` §3 first. Time: about 2–3 minutes per claim; skip nothing.

## Before you start
- Open `draft.md`, `claims_en.md`, `appraised.md`, `review_queue.md` side by side.
- Write down every `[W..-...]` in `draft.md`, in order. Each one is a row.

## For each claim-id
1. **Claim exists.** Search `claims_en.md` for the id. Not there → fail.
2. **Source is usable.** Find its `source_id` in `appraised.md`. `decision` must be `use`. Note the credibility.
3. **Quote in saved source.** Open `library/sources/S-xxx.md`. Ctrl+F a distinctive 5–6 word stretch of `original_nl`. It must be in `excerpt:` word for word.
4. **Live document.**
   - Credibility 3, no `FLAG` in the source file, and `auto_verified` says `AUTO-PASS` from this week → write `auto`; you may skip opening the page.
   - Otherwise (or if there is no `auto_verified`): open the URL in a browser, Ctrl+F the same stretch. Found → write your name in `verified_by` and `person: <you>`. Not found, page gone or blocked → fail, note why.
5. **Numbers.** Every number in the draft sentence must be in `original_nl` (decimal comma becomes a point: 22,7 = 22.7). Any other number → fail.
6. **Labels (crit 4).** The draft bracket must show the claim's `evidence` and `scope` exactly.
7. Row passes only if 1–6 all pass.

## For each numbered recommendation (crit 3)
Is the AI Act, GDPR or sanctions duty named with a claim-id, and the supplier's hosting location named (or "not known")? Fill one row of the duty table; no → fail.

## Then
- Count `review_queue.md` rows with result `ok`. Write the line under "Person source checks".
- Hand the file to the second reader for criteria 1, 2, 5, 6. Any fail anywhere → back to Draft. The PM settles disagreements.
- Log the minutes in `timelog.csv` with `done_by: hand`.
