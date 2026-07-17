# Session log — 2026-07-16 — Week 0 pack, Week 1 kickoff deck, grading ground truth

_Participants: Tripp + Claude_

## What happened

1. **Week 0 pack** (`course-build/week0/`), ported from the Kith July-cohort guides:
   - `cursor-setup-guide-v1.md` — Cursor edition of the Claude Code setup guide
   - `data-handling-cheat-sheet-v1.md` — EY edition of the privacy cheat sheet; leads
     with three non-negotiable pilot rules (fictional data only, no secrets, course
     tools for course work)
2. **Week 1 kickoff deck** (`course-build/week1/kickoff-deck-v1.html`) — Riverbend
   edition of Kith's Week 1 kickoff: 11 slides, arrow-key HTML deck, EY-yellow styling.
   Ends on Kith's best trick: "whatever you propose is what you'll execute."
3. **Grading ground truth** — `tools/reference-totals.py` computes corrected CY2025
   energy totals (applies answer-key corrections for flaws 1/3/6/9) →
   `course-build/reference-totals-2025.md`. Re-run after any data regeneration.

## Important: EY-network placeholders

**Tripp will revise both Week 0 docs to handle EY internal network nuances.** Every spot
needing that detail is marked **`[EY-NETWORK]`** in the two files: Cursor
licensing/install path, model availability, student repo URL + proxy/cert issues for git,
EY Cursor privacy configuration (Privacy Mode, retention, codebase indexing), Risk
Management policy references, and the real-engagement approval path. Until resolved, the
cheat sheet's Section 1 rules govern.

## For Dan & Miranda

- Open `course-build/week1/kickoff-deck-v1.html` in a browser (arrow keys to navigate) —
  reactions welcome, especially on tone.
- The setup guide's smoke test doubles as the Week 0 deliverable (screenshot + 3-line
  intro to the cohort channel) — establishes the demo norm before Week 1.

## Next steps

- [ ] Tripp: fill `[EY-NETWORK]` placeholders (some need Risk Management input)
- [ ] Build the student-repo template (AGENTS.md/.cursorrules for the Riverbend workspace)
- [ ] Week 2-4 session materials (concept slides + live-build scripts)
- [ ] Dan/Miranda cold-run of Week 2 exercise against the sandbox data
