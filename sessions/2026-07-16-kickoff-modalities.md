# Session log — 2026-07-16 — Kickoff: repo setup & training modality decisions

_Participants: Tripp + Claude_

## What happened

1. Committed the Kith Climate course reference files to the repo (July, March, May
   cohorts — 42 files). Note: the `northwood-capital/` sandbox workspace from the May
   cohort was deleted locally before commit (it contained a live-looking Supabase
   API key in `_secrets/api-keys.md`), so it is NOT in the repo. We will rebuild an
   EY-flavored equivalent from scratch anyway.
2. Brainstormed training modalities. Options considered: full 6-week Kith clone,
   compressed 4-week cohort, 1–2 day bootcamp + labs, case competition, flipped
   self-paced + live labs, champions/train-the-trainer.
3. **Decision: sequence, don't choose.** Starter kit → 4-week pilot cohort (10–15
   hand-picked) → practice-wide case competition → ongoing monthly office hours.
   Full rationale in `course-build/project-brief.md`.
4. Set up the collaboration machinery: `CLAUDE.md` with shared conventions,
   `course-build/` for program assets, `sessions/` for these logs.

## Key context for Dan & Miranda

- Tripp (MD) provides authority; no formal L&D integration to start — scrappy first.
- Build happens on personal machines in this repo; no EY client/proprietary data ever.
- EY has Cursor + LLM suite + EY GitHub, not Claude Code (may change in coming months).
  We teach agent concepts with Cursor as the vehicle.
- The two most useful reference files for program design:
  - `6 Taking Claude Code Back to Your Team — Kith Climate.html` (rollout playbook)
  - `6 Running an Internal AI Case Competition — Kith Climate.html` (competition playbook)

## Next steps

- [ ] Tripp: add Dan & Miranda as repo collaborators; consider making repo private
- [ ] Draft the 4-week pilot arc (which Kith weeks fuse) — `course-build/`
- [ ] Design the fictional sandbox client (name, sector, scenario, datasets)
- [ ] Port the Kith setup guide to a Cursor setup guide
