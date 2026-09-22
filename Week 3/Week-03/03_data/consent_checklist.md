# Consent checklist — field research / own data intake

**Nothing in stage 3 (Own Data Intake) runs, and nobody on the team approaches the SME partner,
until every item below is checked and signed.** This mirrors the course's own hard rule: consent
and anonymisation are settled before contact, not after.

## Before the visit

- [ ] The SME contact has been told, in plain language, what the research is for and how the
      material will be used (the handbook page, the platform documents, the portfolio).
- [ ] The SME contact has been told who will see the raw material (the team) and who will not
      (nobody outside the team sees anything before it's anonymized).
- [ ] The SME contact has agreed to be interviewed.
- [ ] The SME contact has agreed to the interview being **recorded**.
- [ ] The SME contact has agreed to the recording being **transcribed and translated**, and knows
      the chain that happens to it (see below) — this is its own line item, not implied by
      "recorded."
- [ ] Company permission has been obtained for AI processing of any company data or materials
      referenced in the interview (not just the interviewee's personal consent).
- [ ] The SME contact knows they can withdraw consent, or ask for their data to be deleted, at any
      point — and who to tell if they want to.

## What actually happens to the recording — tell the SME contact this, don't just do it

1. The recording is transcribed **locally** (`faster-whisper` / `openai-whisper`, running on
   Floyd's own laptop). The audio never leaves the laptop and never goes through a free-tier AI
   tool or any cloud transcription service.
2. The raw transcript is written to `03_data/private/` — never read by any pipeline agent.
3. `scripts/anonymize.py` runs on it — local, no AI — replacing names and identifying terms from a
   mapping file, writing the result to `03_data/anonymized/`.
4. Only the **anonymized** transcript is translated, via Claude on Floyd's paid plan. The raw
   transcript is never sent anywhere.
5. The original-language text is kept alongside the translation in `03_data/anonymized/` — not
   replaced by it — so a claim can still be checked against what was actually said.
6. Stage 3 (`data-intake`) reads only from `03_data/anonymized/`, and flags anything that still
   looks identifying before it goes any further.

## Sign-off

| Role | Name (or "declined to be named") | Date |
|---|---|---|
| SME contact / interviewee | | |
| Team member obtaining consent | | |

**This checklist must be fully checked, and both sign-off rows filled in, before the interview
happens — not after.** `data-intake` (stage 3) and `transcribe_translate.py` both refuse to
proceed on an incomplete checklist; that check is manual until phase 5 builds it into the script.

## Manual fallback

If a script can't run, the same chain happens by hand: transcribe from the recording by ear
(still locally — no cloud dictation tool), anonymize by find-and-replace against the mapping file,
then translate the anonymized text by hand or by pasting the anonymized-only text into an AI tool.
The order (transcribe → anonymize → translate) does not change.
