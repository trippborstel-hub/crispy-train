# EY Climate — AI Coding Agent Training: Project Brief (v1)

_Last updated: 2026-07-16 · Owner: Tripp_

## Goal

Equip EY Climate practice colleagues with the foundational concepts and techniques to
work productively with AI coding agents, using the tools EY has today (Cursor, the LLM
suite within it, EY GitHub), with a structure that transfers cleanly if/when Claude Code
becomes available.

## Context

- The program is modeled on the Kith Climate 6-week cohort (materials in `reference_files/`),
  which Tripp and Miranda completed. What made it work: a fictional client, a deliverable
  every week, live peer demos, and a build–apply–present cadence. All of that is
  harness-agnostic.
- EY Climate practice: ~250 people. Smart, ambitious, curious — but no internal training
  for this exists.
- Tripp is MD and provides the authority/air-cover. No formal L&D/CPD integration to
  start — too admin-heavy. Scrappy first, broaden later. Participants will commit time
  because they see the products of Tripp's work.

## Instructors

Tripp, Dan Kenney, Miranda Nayyar (Kith Climate graduate).

## Phased plan (agreed 2026-07-16)

1. **Phase 1 — Starter kit (now).** Build the assets every later phase consumes:
   - Fictional client sandbox workspace (Northwood-style, EY-climate-flavored) in `sandbox-client/`
   - Cursor setup guide (port of the Kith Claude Code setup guide)
   - Rules-file templates (`.cursorrules` / `AGENTS.md` — the CLAUDE.md equivalent)
2. **Phase 2 — Pilot cohort.** ~4 weeks (compressed from Kith's 6), 10–15 hand-picked
   participants Tripp knows, weekly deliverable, demo sessions. Proves the model,
   produces champions.
3. **Phase 3 — Case competition** across the practice, cohort grads as team anchors.
   Playbook: `reference_files/.../6 Running an Internal AI Case Competition — Kith Climate.html`.
4. **Ongoing — monthly office hours** (Kith alumni-session pattern).

## Key constraints

- **Harness translation:** Kith taught Claude Code; EY has Cursor. Concepts map ~1:1
  (CLAUDE.md → .cursorrules/AGENTS.md; agent mode; reference files; repo workflow).
  Course must teach the *concepts* with Cursor as the vehicle.
- **Data safety:** built on personal machines first; zero EY client/proprietary data.
  The fictional sandbox is what makes hands-on work safe. Port to EY GitHub later is
  just a clone.
- **Time budget:** participants are billable. Kith's 5–7 hrs/week won't fly for a
  broad rollout; pilot targets a tighter footprint (live session + bounded homework).

## Open questions

- Exact week-by-week arc for the 4-week pilot (which Kith weeks fuse?)
- Name for the fictional sandbox client and its scenario
- Pilot participant list and start date
- Repo visibility (should crispy-train be private given Kith course materials are in it?)
