# EY Climate — AI Agent Pilot: The 4-Week Arc (v1)

_Drafted 2026-07-16 · Owners: Tripp, Dan Kenney, Miranda Nayyar · Status: draft for co-instructor review_

## The program in one sentence

Four weeks, one fictional client, four compounding deliverables: participants **win the work,
master the data, make the numbers mean something, and make the output trustworthy** — using
Cursor and the agent skills that transfer to any harness, including Claude Code when it arrives.

## Design principles

1. **One engagement, start to finish.** Like Kith's Northwood, everything happens inside a
   single fictional client engagement. Each week's output is the next week's input. The system
   compounds — participants feel it compound.
2. **Demo pressure is the engine.** Presenting your build to peers weekly is what made Kith
   work. Every live session opens with demos. Nobody hides.
3. **The deliverable is the curriculum.** No lecture without a build. Each week pairs one
   agent skill with one climate deliverable a client could actually receive.
4. **Assurance is our home turf.** Kith taught assurance in week 6 as a capstone concept.
   We are EY — traceability, QA, and defensible numbers get a full week and run as a thread
   through every week before it. This is also our differentiator vs. generic AI training.
5. **Bounded time, honest floors.** Target ≤4 hrs/week: 75-min live session + ~2 hr build +
   optional 30-min office hours. Every assignment has a stated **minimum bar** (achievable in
   an hour on a brutal client-work week) and a **full build**. Finishing the minimum bar keeps
   you in the game.
6. **Concepts over buttons.** We teach with Cursor but name the concepts (agent, context,
   rules files, reference files, harness) so the skills survive a harness change.

## The arc at a glance

| Week | Theme | Agent skill | Deliverable (client-ready) | Kith source |
|------|-------|-------------|---------------------------|-------------|
| 0 | Pre-flight | Install, clone, smoke test | Working setup + intro note | W1 setup guide + privacy cheat sheet |
| 1 | **Pitch it** | Operating an agent; rules & reference files; HTML output | Client pitch deck (HTML) | Kith W1 |
| 2 | **Ground it** | Directing inference at messy data; data quality judgment | Data audit memo + structured data ask | Kith W2 |
| 3 | **Prove it** | Agent-written code vs. model guesses; analysis → interactive deliverable | Carbon dashboard + materiality one-pager (ranked by $) | Kith W3 + W4 fused |
| 4 | **Assure it** | QA systems, traceability, error-finding review | Assured capstone package + methodology doc | Kith W6 |
| — | **Demo Day** | — | 5-min demo to invited practice audience | Kith Friday demos, scaled up |

---

## Week 0 — Pre-flight (async, ~45 min, week before kickoff)

**Goal:** Nobody loses Week 1 to IT problems.

- Checklist: Cursor installed and signed in, model access verified (Claude + GPT), EY GitHub
  access confirmed, sandbox repo cloned, one smoke-test prompt run successfully.
- Read: adapted privacy & data-handling cheat sheet (the EY version — what may and may not
  touch these tools; fictional data only in the sandbox).
- Post a 3-line intro + screenshot of the smoke test to the cohort channel. This is the first
  demo — trivially easy, but it establishes the "show your work" norm before Week 1.
- One drop-in office hour during Week 0 for anyone stuck on setup.

## Week 1 — Pitch it

**The move:** Walk in as a consultant, not a student. Session opens in-world: the sandbox
client has sent an engagement inquiry, and the cohort is the team that has to pitch.

**Agent skills:** What an agent is (vs. chat); how the harness reads your workspace; rules
files (`.cursorrules`/`AGENTS.md`) and reference files as encoded institutional knowledge;
iterating on an HTML deliverable; the "you direct, it builds" working posture.

**Live session (75 min):** Kickoff & the client brief (15) · live build: instructor turns a
blank folder + engagement inquiry into the skeleton of a pitch, narrating every prompt
decision (30) · workspace tour: rules files, reference files, why they exist (15) ·
assignment brief & pods (15).

**Assignment:** Build the pitch — what we'd deliver, what data we need, how an AI-native team
works. HTML presentation, firm-branded. *Minimum bar:* 5-slide pitch from the template
workspace. *Full build:* custom scoping, portfolio prioritization, distinctive angle.

**The Kith trick to keep:** whatever you pitch is what you execute for the next three weeks.
Choose wisely. (Instructors constrain scope in feedback so nobody pitches themselves off a cliff.)

## Week 2 — Ground it

**The move:** The pitch was the easy part. Now the client "sends the data" — and it's messy,
incomplete, and contradictory, because real client data always is. (We build the sandbox data
with deliberate, documented flaws.)

**Agent skills:** Pointing an agent at a folder of mixed files (CSVs, PDFs, questionnaires)
and directing inference; asking the agent to *show you what's there* before telling it what to
make; data-quality grading (the Kith A/B/C: metered / estimated / proxy); knowing when the
agent is reading vs. guessing.

**Live session:** 2–3 pitch demos (15) · concept: the atomic unit — global inference + your
encoded context + a place to act (10) · live build: interrogate the messy dataset, surface
contradictions, grade quality (30) · assignment brief (10) · translate-to-your-work prompt (10).

**Assignment:** Data audit memo — what exists, what's trustworthy, what's broken and the fix,
what's missing — plus a structured data ask back to the client. *Minimum bar:* inventory +
top-5 issues. *Full build:* full quality grading + prioritized remediation + polished ask.

## Week 3 — Prove it

**The move:** From audit to analysis to *meaning*. Fuses Kith's carbon week (W3) and
materiality week (W4) around the through-line both share: **a number without financial context
is a scoreboard; connected to dollars it's a finding.**

**Agent skills:** The trust ladder — model *predicts* a number vs. model *writes and runs code*
vs. code *you own and can rerun* (this is the single most important slide in the course for an
EY audience — it's the difference between a demo and a defensible deliverable); building an
interactive HTML dashboard; intensity metrics and cross-referencing datasets; simulating
plausible data where gaps exist and *labeling it as simulated*.

**Live session:** demos (15) · concept: guessed vs. computed, and why only owned code survives
an auditor (15) · live build: CSV + emission factors → calculated inventory → dashboard
skeleton (30) · assignment brief: dashboards feed decisions, so ship the one-pager too (15).

**Assignment:** Scope 1+2 carbon dashboard (interactive HTML: portfolio view, entity
breakdown, data-quality layer, Scope 3 flags) **plus** the materiality one-pager: top issue and
top initiative per entity, ranked by $ exposure — capex, payback, risk avoided. *Minimum bar:*
calculated inventory + static dashboard + 3-row one-pager. *Full build:* drilldowns, intensity
metrics, initiative NPVs.

This is the heaviest week and it's deliberate — it's also the week the "wow" lands. Office
hours are actively pushed here, and pods are told to pair-build.

## Week 4 — Assure it

**The move:** The client's audit committee asks: *"How do we know any of this is right?"*
Answer it. This is where EY's DNA becomes the curriculum: the week that turns AI output from
impressive to defensible — and the week that most directly differentiates this program from
every generic prompt-engineering course.

**Agent skills:** Error-finding QA (ask the agent to *find errors*, never to confirm
correctness); external referents (check against source docs and deterministic calcs, not the
model's own opinion); provenance as a binding — every figure traceable to a stored source;
tagging estimates and documenting assumptions; random error vs. systematic bias, and where
each can live in an AI workflow.

**Live session:** demos (15) · concept: assurance of AI-built work — estimation was always
the process; the bar is methodology, reasonableness, documentation (20) · live build: run an
error-finding QA pass over Week 3's dashboard, watch it catch things, fix and document (25) ·
capstone & Demo Day brief (15).

**Assignment:** The assured capstone package — Week 3's deliverables upgraded with: a QA log
(what was checked, what was caught, what was fixed), a methodology note (sources, factors,
assumptions, estimate tags), and traceability from every headline figure to its source file.
*Minimum bar:* QA pass + methodology note on the dashboard. *Full build:* full package with
per-figure trace references.

## Demo Day (week 5, one session — the graduation and the launchpad)

- Every participant (or pod) gets 5 minutes: show the capstone, tell one "it caught me by
  surprise" story, name the real engagement task they'll apply this to first.
- **Invite the practice:** leadership plus the curious. This is the recruiting event for the
  Phase 3 case competition and the internal evidence base for a Claude Code business case.
- Close with the ask: each graduate runs one show-and-tell for their own team in the next
  month (the champions mechanic from the Kith rollout playbook).

---

## Cadence and roles

- **Tuesday live session, 75 min** (concept + live build + demos). Recorded.
- **Thursday office hours, 30 min, optional** — drop-in, pod-based.
- **Pods of 4–5**, one anchored by each instructor (Tripp, Dan, Miranda). Pods are the peer
  accountability layer: demo rotation, pair-building in Week 3, first line of unblocking.
- **Cohort channel** (Teams) for async — questions, screenshots, small wins. Instructors seed
  it daily in weeks 1–2; it usually becomes self-sustaining by week 3.
- **The use-case backlog:** every week, each participant adds one line to a shared doc —
  "a task on my real engagement this week's skill would change." By Demo Day this is a
  practice-wide inventory of AI-applicable work: fuel for Phase 3 and hard evidence for tooling
  conversations with EY leadership.

## What we cut from Kith's six weeks, and why

- **Week 5 (The App)** → cut to a stretch goal / alumni session. The dashboard in our Week 3
  already delivers the core lesson (build things non-users can use); a full app with API calls
  is the first thing to break across varied EY Cursor setups, and it's the least
  immediately-billable skill. When Claude Code lands, this is the natural "alumni week 5."
- **Carbon and materiality as separate weeks** → fused. The Kith materials themselves frame
  materiality as "what last week's number means" — one arc, one week, one two-part deliverable.
- **Saturday community sessions, Discord** → replaced by pods + Teams channel. Scrappy.
- **Nothing else is cut** — setup, data, assurance, and demo culture all survive intact.

## Reference-file reuse map

| Build task | Source in `reference_files/` |
|---|---|
| Week 0 setup guide (port to Cursor) | July Cohort: Claude Code Setup Guide |
| Week 0 data-handling cheat sheet (EY version) | July Cohort: Privacy & Data Security Cheat Sheet |
| Week 1 kickoff deck + engagement inquiry | May Cohort W1 kickoff + northwood-engagement-inquiry.md |
| Week 2 concepts + messy-data design | May Cohort W2: Data |
| Week 3 carbon mechanics + trust ladder | March Cohort W3: Carbon |
| Week 3 materiality one-pager framing | May Cohort W4: Materiality |
| Week 4 assurance concepts | May Cohort W6: Assurance Concepts + Disclosure |
| Demo Day / champions mechanics | May Cohort W6: Taking Claude Code Back to Your Team |
| Phase 3 design (later) | May Cohort W6: Running an Internal AI Case Competition |
| Sandbox client (rebuild, EY-flavored) | Northwood structure (from memory — workspace not in repo) |

## Success metrics for the pilot

1. **Completion:** ≥80% present a capstone at Demo Day.
2. **Application:** within 30 days, ≥half of graduates have used the skills on a real
   engagement task (self-reported, collected at the +30 day check-in).
3. **Multiplication:** ≥half of graduates run a team show-and-tell within a month.
4. **Evidence:** use-case backlog has 40+ entries by Demo Day.
5. **Demand:** a waitlist exists for cohort 2 without us advertising.

## Risks and mitigations

- **Billable crunch → dropout.** Minimum-bar assignments; recorded sessions; pods chase
  stragglers; MD air-cover explicit at kickoff ("I expect you to protect these 4 hours").
- **Cursor environment inconsistency at EY.** Week 0 exists precisely for this; Dan/Miranda
  test the full arc on an EY machine before kickoff; every build has a no-API, files-only path.
- **Skill spread across the cohort.** Pods mix levels; minimum bar keeps beginners shipping;
  full build + stretch goals keep the fast people hungry.
- **Someone puts client data in the sandbox.** Week 0 cheat sheet + rules-file guardrails +
  kickoff statement; fictional-only is a hard rule with MD weight behind it.

## Open items

- [ ] Sandbox client design — name, sector mix, data package with documented flaws (next build task)
- [ ] Dan + Miranda review this arc; each adopts a week to own (suggest: Miranda W2 or W4 given
      Kith experience; Dan per his strengths)
- [ ] Dry-run each live-build segment on an EY Cursor machine
- [ ] Pick pilot start date and participant list (10–15)
- [ ] Working title for the program (current placeholder: **"The Build Cohort"** — better ideas welcome)
