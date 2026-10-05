# Scope note (added by the pipeline build, not part of the original repo)

This directory is a clone of `github.com/datadrivendecisions/ai-in-business`
(the public source behind `https://datadrivendecisions.github.io/ai-in-business/`),
kept here for provenance.

**Only `site/` is input for the pipeline's skills.** That's the published
course site — the same content the crawler in `scripts/scrape_course_site.py`
would otherwise have fetched page by page.

Everything else in this clone (`work/`, `project-documentation/`,
`experiment_service/`, `.claude/`, `.github/`, root `CLAUDE.md`, etc.) is the
instructor/build-side repository for the course, not the public site. It is
kept for reference only and must not be fed into skills.

`site/tool-bias-experiment.html` was deleted from this clone. The course
owner must do that experiment unprepared, and this repo also contains
design/pilot material for the same experiment elsewhere (decision records
`work/decisions/0016-experiment-service.md` and
`0017-experiment-as-homework.md`, `work/drafts/week-03-information-seeking-experiment.md`,
`project-documentation/week-03-experiment-manual.md`,
`project-documentation/test-fixtures/pilot-log.md`, and the
`experiment_service/` backend) — none of that was read or summarized while
building this pipeline, and none of it should be treated as skill input either.

`site/integrated-lrd.html` was also deleted from this clone (2026-09-21, phase 3
of the pipeline build). The source repo's own `CLAUDE.md`/`instructor-view.md`
say this page is instructor-only and — by the repo's own tracked issue #3 —
publicly reachable only by mistake, carrying the Socratic AI tutor's hidden
grading rubric and scores. It was not read (a background research pass read
around it for gate/assessment *mechanics* only, deliberately stopping short of
the rubric itself). Excluded on the course owner's explicit instruction, same
treatment as the bias-experiment page. May be reinstated later if the course
owner confirms it's safe to.
