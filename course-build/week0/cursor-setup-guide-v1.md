# Getting Started with Cursor — EY Climate AI Agent Pilot (v1)

*Complete these steps before the Week 1 session. Most take under 5 minutes. If you hit a
snag, Step 6 has troubleshooting — and one drop-in office hour runs during Week 0 for
anyone stuck.*

*Adapted from the Kith Climate "Claude Code Setup Guide." Concepts are identical; the
harness is Cursor.*

> **⚠ Placeholders marked `[EY-NETWORK]` need EY-specific detail (license requests, proxy,
> GitHub URLs) — Tripp to complete before distribution.**

---

## 1. Get Cursor

Cursor is the AI coding agent harness EY provides. You need it installed and signed in.

`[EY-NETWORK — Tripp: exact steps to request/install Cursor at EY — software portal name,
license/approval flow, expected turnaround, who to chase if it stalls.]`

Once installed, open Cursor and sign in with your EY-provisioned account (not a personal
account — the enterprise deployment is what makes this appropriate for work use).

## 2. Know your two modes

Cursor has an inline autocomplete mode and a **chat/agent panel** (`Cmd+L` / `Ctrl+L`).
Inside the panel, the mode selector matters:

- **Ask** — answers questions, touches nothing. Safe reconnaissance.
- **Agent** — reads files, writes files, runs commands, works in multi-step loops.
  **This is the mode this course is about.** When we say "the agent," we mean this.

Try both once before Week 1 so the difference is concrete, not theoretical.

## 3. Pick your model

Cursor gives you a choice of underlying models (Claude, GPT). For this course:

- Default to the most capable **Claude** model available in your model picker — the
  course materials and reference patterns were developed against Claude models.
- The skill you're building is *directing* a model, not worshipping one. If a model is
  unavailable or slow, switch and carry on. Noticing how models differ is course content.

`[EY-NETWORK — Tripp: confirm which models EY's Cursor deployment exposes and any usage
guidance/limits IT has set.]`

## 4. Get the course repo

Your workspace for the course is a Git repository containing the Riverbend Beverage Group
engagement (your fictional client — see the data-handling cheat sheet: **fictional data
only** lives here).

`[EY-NETWORK — Tripp: student repo URL on EY GitHub + access request process + any
proxy/credential-manager steps needed for git clone to work on the EY network.]`

Clone it to a **local, non-synced location**:

```
# macOS
git clone <STUDENT_REPO_URL> ~/agent-course

# Windows (PowerShell)
git clone <STUDENT_REPO_URL> "$env:USERPROFILE\agent-course"
```

**Why not Documents/Desktop/OneDrive?** Two reasons, both learned the hard way: cloud
sync chokes on the many small files agent work generates (your machine will crawl), and a
synced folder can propagate files somewhere you didn't intend. Keep the workspace at your
user home, *next to* your sync folders, never inside them.

## 5. Open the folder and meet the rules file

In Cursor: **File → Open Folder → `agent-course`**. The folder you open is the agent's
world — it can see what's inside and nothing else. That's a feature: it's your containment
boundary as much as its capability boundary.

In the repo root you'll find an **`AGENTS.md`** (and `.cursorrules`) file. This is the
agent's standing instructions — who the client is, how files are organized, output
conventions. The agent reads it automatically at the start of every session. By Week 2
you'll be editing it; by Week 4 you'll understand why it's where a firm's IP actually
lives. (Kith equivalent: `CLAUDE.md` — same concept, different filename.)

## 6. Smoke test

Open the agent panel, select Agent mode, and run:

```
Read the engagement-inquiry.md in this folder and give me: (1) who the client is,
(2) their four asks, in one line each, and (3) the one sentence in the letter that
should scare a consulting team the most. Then create a file called hello.md
containing today's date and your model name.
```

If you get a sensible summary **and** `hello.md` appears in your folder, you're
operational. Post a screenshot of both to the cohort channel with a 3-line intro —
that's your Week 0 deliverable, and the course's first demo.

## 7. Troubleshooting

First move whenever anything errors: **paste the error into the agent (Ask mode) and ask
it to diagnose.** Learning to debug with the tool is course content, not a workaround.

Common EY-machine issues:

`[EY-NETWORK — Tripp: the real list — proxy/SSL certificate errors on git or model
calls, admin rights for install, VPN interactions, credential manager quirks. Add the
known fixes for each.]`

Still stuck after 20 minutes? Stop burning time — post in the cohort channel or bring it
to the Week 0 office hour. Setup problems are boring; we clear them fast and together.

## FAQ

**Do I need to know how to code?** No. You need to be able to read a folder structure and
be willing to let the agent show you the rest. The course teaches direction, not syntax.

**Can I use this setup on client work right away?** Not yet — read the data-handling
cheat sheet. Course work uses fictional Riverbend data only. Applying the *skills* to real
engagements comes with its own guardrails, which we cover in Week 4 and at Demo Day.

**What if Claude Code becomes available at EY?** Everything here transfers: `AGENTS.md` ↔
`CLAUDE.md`, agent mode ↔ Claude Code sessions, same repo, same working method. You'd be
productive in under an hour. That's deliberate — we teach concepts, Cursor is the vehicle.
