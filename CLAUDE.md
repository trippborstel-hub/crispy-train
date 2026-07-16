# crispy-train — EY Climate AI Agent Training Build

## What this project is

We are building a training program to teach EY Climate practice colleagues how to use
AI coding agents (Cursor + Claude/GPT today; Claude Code possibly later). The program is
modeled on the Kith Climate 6-week cohort, whose materials live in `reference_files/`.

## Who is working here

- **Tripp** (Managing Director, EY Climate) — project lead, Kith Climate graduate
- **Miranda Nayyar** — co-instructor, Kith Climate graduate
- **Dan Kenney** — co-instructor

All three collaborate asynchronously on this repo from personal machines. No EY client
or proprietary data may ever be committed here — the training uses a fictional client
sandbox instead.

## Design decisions to date

See `course-build/project-brief.md` for the current plan and rationale. Read it before
proposing changes to the program design.

## Repo layout

- `reference_files/` — Kith Climate course materials (source content; read-only, do not edit)
- `course-build/` — the training program we are building (briefs, curriculum, session plans)
- `sandbox-client/` — fictional client workspace participants will work in (Northwood-style, EY-flavored)
- `sessions/` — session logs: summaries of AI working sessions, one file per session

## Conventions for every AI agent working in this repo

1. **End-of-session log.** Before a working session ends, write a summary to
   `sessions/YYYY-MM-DD-<topic>.md`: decisions made, rationale, artifacts created/changed,
   open questions, next steps. This is how the three collaborators stay in sync — write it
   for a colleague who wasn't there.
2. **Catch up before starting.** At the start of a session, read the two or three most
   recent files in `sessions/` so you know what your collaborators decided.
3. **Versioning.** Drafts are files with `-v1`, `-v2` suffixes. Never overwrite a version
   another collaborator may be reviewing; add a new one.
4. **Commit and push at the end of every session** so the others can see the work.
   Commit messages should say what changed and why in one line.
5. **No client data, no real names of EY clients, no EY-internal material.** Fictional
   sandbox content only.
