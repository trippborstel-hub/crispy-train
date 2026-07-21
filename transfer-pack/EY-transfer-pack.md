# EY Agentic Work — Transfer Pack (single-file edition)

One markdown file containing the complete pack. Each original file begins at a
`FILE:` divider — to re-split into separate files, ask an agent:
"Split this document into its original files at the FILE: dividers."

Contents: `README.md` · `AGENTS-template.md` · `01-principles-of-agentic-work.md` · `02-working-methods.md` · `03-reference-file-method.md` · `04-assurance-and-qa.md` · `05-glossary.md` · `the-dyad-and-the-deliverable.md`


---

**`FILE: README.md`**

---

# EY Agentic Work — Transfer Pack

Plain-markdown knowledge pack for seeding an AI-agent working environment at EY.
Everything here is text: no code to run, no dependencies, no external links required.
Copy the folder (or paste file contents) into any workspace.

## What this is

A distillation of working knowledge about AI coding agents — synthesized from the Kith
Climate cohort (Diego Espinosa, Ben Hillier), vendor documentation (Anthropic, Cursor),
and our own practice — expressed in our own words and packaged the way agent knowledge
should be packaged: as reference files an agent reads.

## How to install (Cursor)

1. Create a folder for your agent workspace (local, not inside OneDrive).
2. Copy this pack into it. Rename `AGENTS-template.md` to `AGENTS.md` (Cursor reads
   that name automatically; Claude Code reads `CLAUDE.md` — same file, either name).
3. Open the folder in Cursor, open the agent panel (Agent mode), and run this prompt:

   > Read every file in this folder, starting with AGENTS.md and README.md. Then give
   > me: (1) a one-paragraph summary of how we work here, (2) the three rules you
   > consider most binding, and (3) one question about anything ambiguous.

   If the answers are good, the transfer worked. That prompt is also the demo to show
   a colleague.

## Reading order (humans)

| # | File | What it is |
|---|------|-----------|
| 1 | `01-principles-of-agentic-work.md` | The eight core ideas, one page each idea |
| 2 | `02-working-methods.md` | The day-to-day management playbook |
| 3 | `03-reference-file-method.md` | How to grow your own reference files |
| 4 | `04-assurance-and-qa.md` | Making agent output defensible (the EY edge) |
| 5 | `05-glossary.md` | The vocabulary, named precisely |
| 6 | `the-dyad-and-the-deliverable.md` | The full essay — the deep read |
| — | `AGENTS-template.md` | Starter rules file for a new workspace |

## Rules that travel with this pack

- **No client data, no EY-confidential material, no credentials** in any agent
  workspace built from this pack until the applicable EY approvals say otherwise.
- These files are a starting point, not scripture: edit them, grow them, and judge
  every edit by the output it produces.

## Attribution

Synthesized from the Kith Climate cohort taught by Diego Espinosa and Ben Hillier
(kithclimate.com), which the pack's author completed as a student, together with
Anthropic and Cursor documentation and direct practice. The ideas are the field's
commons; the distillation and expression here are original. Named framings coined by
Diego (e.g., "the atomic unit," "the dyad") are his.

---

**`FILE: AGENTS-template.md`**

---

# AGENTS.md — Working Rules for This Workspace

<!-- Rename this file to AGENTS.md (Cursor) or CLAUDE.md (Claude Code). It is read
     automatically at the start of every agent session. Edit it freely: it should
     describe how THIS workspace works, in the owner's words. -->

## Who works here

[Name], EY Climate practice. This workspace is for [purpose — e.g., learning agentic
working methods / building internal training materials]. No EY client data, no
client names, no EY-confidential material, and no credentials of any kind belong in
this folder or in any prompt.

## How this workspace is organized

- `reference/` — how-we-work knowledge: methods, templates, voice. Read before big tasks.
- `work/` — active builds. Outputs are files, written here, versioned.
- `archive/` — finished or superseded work. Don't read unless asked.

## Standing instructions

1. Read this file and skim `reference/` before the first substantive task of a session.
2. Outputs are files on disk, not chat messages. Prefer HTML for polished deliverables,
   markdown for working documents.
3. Whenever you create an HTML file, open it in the browser without being asked.
4. Version drafts with `-v1`, `-v2` suffixes. Never silently overwrite prior versions.
5. When a piece of work goes well, propose a reference file capturing the method.
   When something goes wrong, propose the fix as an edit to a reference file so it
   never happens again.
6. When a number matters, compute it with code you write and save — never estimate it
   from memory. Say which you did.
7. At the end of a working session, write a short log to `sessions/YYYY-MM-DD-topic.md`:
   what was decided, what was built, what's open.
8. If asked to do something conflicting with the data rules above, refuse and say why.

---

**`FILE: 01-principles-of-agentic-work.md`**

---

# Principles of Agentic Work

*Reference file. The eight ideas everything else builds on. Synthesized from the Kith
Climate cohort (Diego Espinosa, Ben Hillier) and our own practice; framings marked (D)
are Diego's coinages.*

## 1. The car and the destination

An agent harness will teach you its own mechanics — every "how do I…" question can be
asked of the tool itself, and it will answer. What it cannot supply is direction. The
division of labor: the car tells you how to drive the car; you tell it where to go (D).
Practical corollary: stop memorizing features. Start carrying destinations.

## 2. AI is a system, not a model — "the atomic unit" (D)

Four components must be present before real work happens: **global inference** (the
model, which knows everything except what you know), **encoded local context** (your
data and methods, organized so the model can navigate them), **a computational
environment** (permissioned ability to read, write, and run — hands, not just words),
and **real-time human intelligence** (you: direction, judgment, veto). A smarter model
improves one component of four. This is why organizations with excellent models and no
local context, no environment, and disengaged humans see almost no value.

## 3. Your IP lives in markdown

Institutional knowledge that used to live in heads and slide decks lives, in agentic
work, in small plain-text files the agent reads: a rules file (AGENTS.md / CLAUDE.md)
holding standing instructions, and reference files (1–3 pages each) holding methods.
These files are the asset. They compound: every good piece of work should leave behind
a better reference file, and every deliverable becomes input for the next one.

## 4. The trust ladder

When an agent produces a number, ask how it got there. Three rungs: (1) the model
*predicted* it — pattern completion; a wrong answer looks exactly as confident as a
right one; (2) the model *wrote and ran code* — the logic can be wrong, the arithmetic
cannot; (3) the code is *saved where you can read and rerun it* — the only rung that
survives review. Climb the ladder as consequences rise. Guessed and computed look
identical on the page; the difference is everything.

## 5. Brilliant and stupid in the same conversation

Agents are inconsistent at genius level — capable of expert-grade work and basic
blunders in the same session. This is not a defect to be cured; it is the operating
characteristic to be managed. Manage it like you'd manage a brilliant, erratic junior:
clear intent, broad-then-narrow direction, review proportionate to stakes, and
corrections encoded in reference files rather than repeated in person.

## 6. It's not software (D)

Software is deterministic: bugs get fixed, behavior repeats, reliability is the
engineer's job. An agent is neither software nor colleague — fallible like a person,
tireless like a machine, with novel failure modes of its own. Treating it as software
("configure it once, trust it forever") and treating it as magic ("it said so") are
the two classic errors. The working posture is management: delegation with
verification.

## 7. The harness and the app

The **harness** (Cursor, Claude Code) is where a skilled operator does open-ended
work: it closes the loop of data in → reasoning → files out. The **app** is what you
build *with* the harness for people who will never open it: a codified workflow with
fixed inputs and consistent outputs. The harness is where you work; the app is what
you leave behind. When someone says "I don't trust AI for this, I'd want a tool" —
the tool is what the AI builds.

## 8. The dyad (D)

The unit of value is not the AI; it is the human-plus-AI pair. Output no human has
judged is a tree falling in an empty forest. The model has no stakes — nothing matters
to it — so the human seat in the system is not a courtesy; it is where value gets
determined. One person's judgment, amplified by an agent, against another person's
judgment, amplified by an agent: the judgment is still what differs, and it is still
what's scarce. The strongest evidence: give the same assignment, model, and data to
twenty-eight people and you get twenty-eight meaningfully different deliverables.
The variance is the human contribution, made visible.

---

**`FILE: 02-working-methods.md`**

---

# Working Methods — The Day-to-Day Playbook

*Reference file. How to actually run sessions with an agent. Synthesized from the Kith
Climate cohort and our own practice.*

## Directing

- **Start broad, then narrow.** Over-specifying up front wastes the intelligence — you
  get exactly what you asked for, which is rarely what you wanted. Open with intent
  ("here's the situation, here's what I'm trying to achieve — how would you approach
  it?"), then tighten.
- **Prompting is not engineering.** The useful mental model: you are asking a very
  smart person who knows almost everything an open-ended question. The leverage is in
  the context you've built and the judgment you apply, not in magic phrasing.
- **Give it a deliverable.** Aimless exploration teaches you little. A concrete thing
  you're trying to produce activates your critical thinking and gives the agent a
  target. If you're stuck on how to learn something, assign yourself an artifact.

## Correcting

- **Say less.** "I noticed the deck was incomplete" outperforms a paragraph of
  instructions — let the agent self-diagnose, then confirm. Micromanaged corrections
  produce compliant, worse work.
- **Encode fixes.** When the same correction happens twice, it belongs in AGENTS.md or
  a reference file ("whenever you create an HTML file, open it"). The discipline:
  never make the same correction three times.
- **Express friction.** "This is tedious — is there a better way?" is a legitimate and
  productive prompt. The agent often knows a faster path and won't volunteer it.

## Sessions

- **Thinking sessions and doing sessions.** Keep one long-lived conversation for
  direction-setting on a workstream, and spin up fresh, disposable sessions for
  execution tasks. Don't burn a rich context on file conversions.
- **Don't fall in love with sessions.** Archive ruthlessly. The durable memory is the
  file system and the reference files, never the chat history.
- **New session = fresh reviewer.** A clean session reading your draft cold is a
  cheap, surprisingly effective independent review.

## Reviewing

- **Beware the polish.** Beautiful output suppresses questioning. A wall of charts can
  be the opposite of rigor. Review the substance with the same skepticism you'd apply
  to a dazzling junior's work — that skepticism is the job, not an insult.
- **Ask "how does it know that?"** When output is surprisingly specific, entertain two
  possibilities every time: it stitched a genuine inference across patterns, or it
  made it up. Both wear the same confidence. Check which, before it ships.
- **Fight AI indigestion.** The volume of output tempts you to wave it through
  ("great, I'll read it later" — you won't). Take yourself up a level: demand
  distillation. "Plain English. One paragraph. The three things the client needs."
  Synthesis is the only unit your judgment can actually inspect.

## Scaling yourself

- **Ask for tools.** If the agent says it can't do something, ask "is there a tool for
  this you could install or use?" It often won't volunteer capabilities it has.
- **No work is ever lost.** Every artifact spawns adjacent artifacts: a plan becomes a
  tracker becomes a status report becomes next week's plan. Before starting anything
  from scratch, ask what existing output it could be derived from.
- **Recalibrate your clock.** Work that took a day may take minutes. The freed time
  has a proper destination: the questions that used to belong to partners — what are
  we doing, why, for whom, and what makes it valuable.

---

**`FILE: 03-reference-file-method.md`**

---

# The Reference File Method

*Reference file about reference files. The craft of encoding how you work so an agent
can follow it. Synthesized from the Kith Climate cohort and our own practice.*

## What a reference file is

A short markdown document (1–3 pages) that captures one method: how we do a data
audit, how we structure a client memo, what our house voice sounds like, how our
scoring framework works. The agent reads it before doing that kind of work. A folder
of these files is, functionally, your firm's operating manual — and your moat, because
generic context produces generic output.

## The rules of the craft

1. **Never write one by hand.** Generate them through iteration: do the work with the
   agent, get it right, then say "write a reference file capturing how we did this so
   we can repeat it." Editing happens the same way — through the agent.
2. **Judge by output, not by reading.** The test of a reference file is whether it
   keeps producing good work, not whether it reads well to you. If output is
   consistently good, the file works.
3. **One method per file.** A file that covers three methods gets half-read three
   ways. Split it.
4. **Mind the reference–inference spectrum.** Too little encoded and results vary
   wildly session to session. Too much and the rigidity strangles the model's
   intelligence — and an over-instructed model will follow a bad rule off a cliff,
   then imply it would have known better if you hadn't insisted. Find the middle
   empirically: encode what must be constant, leave room where judgment helps.
5. **Reference prior work by path.** "See `work/2026-06-audit-v2.html` for a model of
   the expected quality" is worth a page of description. Examples beat instructions.
6. **Capture failures too.** The best reference files contain "never do X, because Y
   happened" lines earned from real mistakes. That's how the same mistake stops
   recurring across sessions — and across colleagues.
7. **QA the file itself.** Periodically ask a fresh session: "Read this reference
   file. Is there anything in it that would lead to incorrect or low-quality output?
   What's ambiguous?" The agent is a competent editor of its own instructions.

## The lifecycle

```
do work well  →  "write a reference file for this"  →  use it next time
     ↑                                                        |
     └── output degrades or errs → fix through the agent ←────┘
```

## Starter set for a new EY Climate workspace

Grow these as the work happens — do not write them speculatively:

- `voice-and-style.md` — how our documents sound; what AI-flavored writing to avoid
- `deliverable-standards.md` — what "client-ready" means here; format defaults
- `data-audit-method.md` — after the first real data audit goes well
- `qa-method.md` — see `04-assurance-and-qa.md` for the seed
- One per recurring deliverable type, earned through use

## The strategic point

Skills marketplaces and pre-packaged prompts are reference files with training wheels:
useful for speed, but the value is in the encoding experience — the iteration where
your judgment about what makes your work distinctive gets written down. That cannot be
bought or transferred. It has to be earned once, per team. Then it compounds.

---

**`FILE: 04-assurance-and-qa.md`**

---

# Assurance and QA for Agent-Built Work

*Reference file. How to make agent output defensible — the layer that separates
professional use from enthusiasm. Synthesized from the Kith Climate cohort, assurance
practice, and our own methods.*

## The reframe that unlocks everything

Estimation was always the process. Carbon accounting — like most professional
analysis — has never been exact; assurance has never attested that a number is
precisely correct. It attests that the **methodology is sound**, the **estimates are
reasonable**, and the **assumptions are documented**. So the question about AI is not
"does it introduce uncertainty into precise work" — the question is whether its
figures are *testable*. That is an architecture question, and architecture is
buildable.

## Two kinds of error — treat them differently

- **Random error** is non-directional, doesn't reproduce, and washes out. Spot-checks
  and sampling catch it. Boring.
- **Systematic bias** is directional, recurs for the same reason, and accumulates.
  Re-running doesn't remove it. This is the real threat, so locate where it can live:
  1. **Source data** — the client's documents are wrong. Same exposure as any manual
     process; not an AI question.
  2. **Orchestration** — a shared instruction tilts all output the same way. Real,
     but correctable: instructions can be read, audited, and fixed (unlike the
     unwritten biases of a team's culture).
  3. **The model itself** — when it fills a data gap, its prior does the work, and
     priors regress toward the typical. For an atypical client that's a directional
     skew. This is the honest carve-out — and exactly the sub-task a well-built
     process tags as an estimate and routes to human judgment.

## The four working rules

1. **Compute, don't recall.** Any number that matters is produced by code the agent
   writes and saves — never by the model's memory. Saved code can be read, tested,
   and rerun; a remembered number cannot. (The trust ladder, rule of the house.)
2. **QA passes hunt errors; they never confirm correctness.** "Find the errors in
   this" produces findings; "is this correct?" produces reassurance. Frame every
   review as error-finding — for agents and, frankly, for people.
3. **Independence means outside the model.** A second agent checking the first shares
   its priors; that is redundancy, not independence. Real checks bind to external
   referents: the stored source document, the published factor, the deterministic
   calculation, the human who owns the assertion.
4. **Provenance is a binding, not an assertion.** Don't accept the model's *claim*
   about where a figure came from; require a link to a stored source that any process
   can verify. A fabricated figure has nothing to bind to — it fails the check
   automatically. This turns hallucination from a philosophical worry into a failed
   test with a line number.

## The minimum QA kit for a deliverable

- **Methodology note** — sources used, methods applied, assumptions made, estimates
  tagged as estimates. One page. Written by the agent, owned by a named human.
- **QA log** — what was checked, what was found, what was fixed. Error-finding
  framing throughout.
- **Trace check** — every headline figure traceable to a source file or saved
  calculation. Sample-test the traces; a figure that traces to nothing gets removed
  or tagged.
- **Fresh-session review** — a clean session, no shared context, prompted to refute:
  "Here is a deliverable. Find what's wrong with it."

## The posture

A well-architected process doesn't eliminate error — nothing ever has. It makes every
figure testable: traceable to source, independently recomputable, checkable for the
one thing that actually threatens an analysis. That standard is one many manual
processes never met. Hold agent work to it, and say so out loud when you present:
precision about where the numbers came from is the trust-building move.

---

**`FILE: 05-glossary.md`**

---

# Glossary — Naming the Concepts

*Reference file. Precise names for the things we work with, so conversations and
prompts stay sharp. Concepts survive tool changes; buttons don't.*

**Agent** — an AI model given tools (read, write, run, search) and the autonomy to
chain steps toward a goal. Distinct from a chatbot, which only talks. Also used for
disposable sub-workers a harness spins up for a bounded task — cheap to create,
discard freely.

**Harness** — the execution environment wrapping the model with tools, memory, and
autonomy (Cursor's agent mode; Claude Code). What makes a harness valuable is being
*workflow-complete*: data in → reasoning → files out, loop closed. Currently the
harness often matters more than the model inside it.

**Model** — the underlying LLM (Claude, GPT). Swappable inside a harness. Capability
varies by tier and version; behavior can change under you — plan for it.

**Context** — everything the model can see for the current task: your prompt, the
files it has read, the rules and reference files, prior turns. Finite. Curating it is
the operator's core skill ("context engineering," which replaced "prompt engineering"
for good reason).

**Rules file** — `AGENTS.md` (Cursor) / `CLAUDE.md` (Claude Code). Standing
instructions read automatically at session start. The workspace's constitution.

**Reference file** — a 1–3 page markdown document capturing one method or standard,
read before doing that kind of work. The unit of encoded institutional knowledge. See
`03-reference-file-method.md`.

**Workspace** — the folder a harness is opened on. The agent can see inside it and
nothing else: simultaneously its capability boundary and your containment boundary.
Curating the workspace is a security control.

**Session** — one conversation with the harness. Ephemeral; ends, gets archived. The
durable memory is files, never chat history.

**MCP (Model Context Protocol)** — a standard for connecting a harness to external
tools and services (databases, browsers, SaaS). Think universal adapter. Ask the
agent what's available before assuming something can't be done.

**API key** — a credential granting programmatic access to a model or service. Never
appears in a workspace, a prompt, or a file. Ever.

**The trust ladder** — predicted number → model-run code → code you own. See
`01-principles-of-agentic-work.md` §4.

**The atomic unit** (Diego Espinosa's coinage) — the four-part system (model + local
context + computational environment + human) that constitutes working AI. The
diagnostic for why adoption stalls.

**The dyad** (Diego Espinosa's coinage) — the human-AI pair as the unit of value.
Output without human judgment is a tree falling in an empty forest.

**App** — a codified workflow with fixed inputs and consistent outputs, built with
the harness for people who don't use the harness. The harness is where you work; the
app is what you leave behind.

**Hallucination / fabrication** — confident output with no grounding. The failure
mode unique to generative systems, and the one most directly defeated by
architecture: provenance bindings, external referents, computed-not-recalled numbers.
See `04-assurance-and-qa.md`.

---

**`FILE: the-dyad-and-the-deliverable.md`**

---

# The Dyad and the Deliverable

*What six weeks of building with Claude Code was actually about*

> Synthesized from Diego Espinosa's live lectures and office hours (March 2026 cohort), with contributions from Ben Hillier noted throughout. Written in Diego's teaching voice as a study aid by Tripp (with Claude) from session transcripts and course decks. Diego did not author or review this document; where it sings, the credit is his, and where it stumbles, the transcription is ours.## 01 · First, get in the car

Okay, so before anything else, I want you to adopt a mindset, and the mindset is a general tolerance for ambiguity. Very little in AI is completely ironed out. Anthropic has raised billions and billions of dollars and it is still shipping stuff every week, changing the rate limits, renaming the buttons, moving your cheese. If you need the ground to be solid before you take a step, this field is going to be a miserable experience for you. If you can treat the wobble as part of the terrain, you're going to be fine. Better than fine.

The first week of the cohort was, on the surface, about installation. Terminals, curl commands, the Pro plan, the folder, the bright arrow. And I stand by what I said in that first session: the bright arrow is really the most important thing about that whole hour. But none of that was the actual lesson. The actual lesson was a metaphor I kept coming back to all six weeks, so let me put it at the top where it belongs:

> **When you're a Claude Code newbie, the thing you need to understand is that the car will tell you how to drive the car. But you need to tell it where you want to go.**

Every mechanical question you had in week one (how do I convert this file, how do I connect this thing, what does this error mean) had the same answer: ask the car. The tool explains itself, troubleshoots itself, installs its own missing parts if you ask it to. What the tool cannot do, ever, is want something. Destination is your department. That division of labor is the entire course in one sentence, and everything else I taught you is elaboration.

Which is why we did the thing that people throw tomatoes at me for: we gave you a client pitch due on Friday of week one, before you knew how to do anything. I call it learning by raising the stakes. We all learn very, very quickly when the stakes are high; nobody learns to swim from a deck chair. The natural response was "I don't know how to do this," and that response was the point, because it forced you into immediate, honest dialogue with the tool about what you knew and what you didn't. You had a purpose. And that's the critical thing about learning to collaborate with AI: a deliverable you're trying to reach is what opens the work up to your critical thinking. Wandering around a chatbot asking it trivia teaches you nothing about collaboration. Having a pitch due Friday for a skeptical ex-McKinsey COO named Sarah teaches you everything.

And do you remember what happened? Twenty-eight people got the same assignment, the same data, the same tool, and produced twenty-eight meaningfully different pitches. Cheryl said it out loud: "I was surprised how different it was from how I did it." Hold on to that surprise. We're going to come back to it at the end, because it turns out to be the most important empirical fact the cohort produced.

One more thing from week one that I want preserved, because it's easy to lose under all the frameworks: this is supposed to feel empowering. After a while you get a little bit lazy in a specific way; I don't go to Finder to find things anymore, I ask. I started with two files and eight weeks later I had 2,700. But notice the direction of the laziness: I stopped doing the clerical part. I am still the one who steers, who determines where to look and how. The power moved toward me, and it will move toward you. When people say AI is going to make us dumber I say: how? We have to up our game every single time it gets smarter. As critical thinkers, I don't think we have ever been challenged as much as this thing is going to challenge us. Good. Bring it on.


## 02 · The atomic unit, or why smarter models change nothing

Now let me get a little theoretical with you. Just a little, okay? I nerd out on this stuff, forgive me, and if you ever want the full philosophical conversation touching human cognition, sociability, and computer science, you know where to find me.

Here's the radical redefinition I need you to carry out of this course: AI is not a large language model. AI is a *system by which humans get things done*, and the model is one component of it. When someone shows you a model and calls it AI, they're showing you an engine on a workbench and calling it a car. The atomic unit of AI, the smallest configuration that actually produces work, has four parts, and if you're missing any one of them you're not doing AI adoption, you're just fooling around.

> *[Figure 1 · The atomic unit. Four components, one output. Remove any component and what remains is not AI adoption; it's a demo. The interaction produces something none of the parts contain individually.]*

*Global inference* is the model: trained on virtually all recorded human knowledge, all possible patterns identified and encoded. When you use Claude you're not searching data, you're searching patterns, and because it holds pretty much all of them it can do things no human could ever come close to doing. But, and write this down, it doesn't know what you know. *Encoded local context* is the answer to that: your files, your methodologies, your client's mess, organized so the model can navigate it. *The computational environment* is the innovation Anthropic actually shipped with Claude Code: permissioned control of your computer, so the intelligence can grab a file, do the work, and put a new file in the folder. And *real-time human intelligence* is you, in the loop, steering, judging, vetoing. The interaction of the four produces something none of them contains individually.

This framework explains the thing that puzzles every executive I talk to. The people at Anthropic can keep making smarter models all day long, and they will. Meanwhile the vast majority of firms have much smarter models than they did six months ago, and what's happening? Practically nothing. They're at a standstill, because a smarter engine on the workbench is still an engine on the workbench. They bought global inference and skipped the other three components. When you see an enterprise AI initiative stall, run the checklist: where's the local context? Where's the environment where it can act? Where's the human with a deliverable and veto power? Somewhere in that list you'll find the missing part.

It also explains why I don't believe in prompt engineering. I find it, as a concept, to be flat. Really flat. The premise of prompt engineering is that the leverage lives in the incantation, in phrasing the request just so. No, no, no. The leverage lives in everything you bring to the table: the data, the context, the judgment, the veto power. The best description I can give you of good prompting is this: you're asking a really smart person who knows almost everything an open-ended question. That's it. You don't need an engineering discipline for that. You need to know what you want, and you need to have built the context that makes your situation legible. Which brings us to markdown.


## 03 · Your IP lives in markdown

If the atomic unit is the theory, here is the practice, and I mean this literally: for a consulting firm operating this way, the intellectual property is a folder of markdown files. Ben called these files the gold dust, and Ben is right, and I want you to understand exactly why something so humble is worth so much.

Start with what markdown is to the model: almost nothing. Kilobytes. A Word file makes Claude Code slow down and wade through formatting junk, all the bolds and headings encoded as XML; a markdown file is pure information, and it makes short work of it. I don't love how markdown looks. I've made my peace with the hashtags. The trade is worth it, because these little files are where the system's memory lives.

There's a hierarchy. At the top sits CLAUDE.md, the macro instructions, the file the harness reads before your first message of every session, its guiding light. Whatever you definitely want it to do, every time, goes there: how the firm works, how to format output, "whenever you create an HTML file, launch it for God's sakes" (that one entered my CLAUDE.md after about the fortieth time I typed it manually). Below that sit the reference files: one to three pages each, one per methodology or repeatable task. How we do a data audit. How we structure an IC memo. What our voice sounds like. What our client's scoring framework means. When a piece of work goes well, the move, always, is: "That was great. Write a reference file so we know how to do this next time." When it goes badly: "Something went wrong. How do we correct it? Let's put it in a reference file and make sure that never happens again."

Now the confession, which I made to you in week six and which I'll repeat here: I have never written a reference file manually. Never. And sometimes I don't even read them. I judge reference files by the output. If the output is great and keeps being great, then whatever is in there works. Some of you might say, that sounds dangerous, Diego, that's riding the bike with no hands. And I accept a piece of that. But it reflects something real about the medium: what you're tuning is a combination of reference and inference, and there's a spectrum. Too little written down and you get variance every time; too much written down and the rigidity starts to strangle the inference, and the model, which is always trying to please, will follow a bad instruction off a cliff and then, implicitly, tell you what every intern tells you: *I would have known not to do that, but you told me to do it.* The craft is the middle of that spectrum, and you find the middle empirically, by output, not by rereading your own instructions and admiring them.

This is also why we stripped our own reference files out of the simulation before giving it to you, and why I told you skill files, the pre-packaged ones, are reference files with training wheels. It would have been cheating to hand them over. The value isn't the file; it's the encoding process, the iteration where your judgment about what makes your work yours gets written into something a machine can read. That experience cannot be transferred. It has to be earned, once, by each firm, and then it compounds forever.

And compounding is the word. Every deliverable you ship becomes data for the next inference. The pitch scaffolds the audit, the audit scaffolds the inventory, this week scaffolds next week, this client scaffolds the next client, this cohort, and I say this with love, scaffolds the next cohort. I went from two files to thousands in a couple of months, and that isn't clutter, that's a balance sheet. Meanwhile notice what this architecture does to the software industry: your data layer, your inference layer, and your deliverables layer all live with you, and the model reads structured data, unstructured documents, and code with total indifference. All data is just data for Claude Code. The market noticed. They called it the SaaSpocalypse, all those vertically siloed systems of record down fifty, eighty percent. That's a market verdict on where this is going, and you, with your folder of markdown, are on the right side of it.

> *[Figure 2 · The determinism spectrum for getting a number into your work. Move right as the stakes rise. An emission factor from Supabase via AI-written code is an IT department; an emission factor from the model's memory is a confident colleague who might be reminiscing.]*


## 04 · The number and the meaning

Carbon week is where the course stopped being about the tool and started being about the profession, so let me reconstruct the argument carefully, because I was proposing something mildly heretical and I'd rather you inherit the argument than the conclusion. Tomatoes welcome, as always.

The traditional frame says: comprehensiveness is the virtue of a carbon inventory. Every source, every scope, every facility, accounted. And comprehensiveness *is* important, in a specific situation: when stakeholders are holding you to account for taking the footprint from X to Y within a certain time. Accountable for the accounting. But ask the question I asked you: how many of our clients actually live in that world? And even for the ones that do, is the value in X and Y, or in what happens *between* X and Y? The money, the risk, the insurance premiums, the exit multiples, the customers won and lost: all of that lives in between. So we reframed: think of it as inventory week, and treat carbon as a placeholder for a process. The inventory is the first step of a risk exercise, which, if you go read your TCFD history, Carney and Bloomberg and the financial-stability crowd, is what it was always supposed to be. What does Sarah want? Ninety percent of the answer in half the time, directionally correct, decision-ready. Our practice is whatever the client wants. That shouldn't be a controversial statement for consultants who intend to stay in business.

Then, inside that reframe, sits the single most load-bearing technical idea of the entire six weeks. When an AI gives you a number, there are three ways it can have gotten there, and they are not created equal.

> *[Figure 3 · The trust ladder. Climb it as consequence rises. Note the honest fine print on rung three: code guarantees the arithmetic, not that you picked the right factor or the right unit. That part is still on you. It was always on you.]*

Guessed or computed, the answer *looks* the same either way; that's what makes this dangerous and why I made you sit with it. The model predicting "0.371" from pattern is fine for a sanity check. The model writing Python that evaluates to 0.371 is a real product. The Python living in your folder, where you can read it, rerun it, and hand it to a skeptic, is a defensible product. And defensibility is the family business, so this ladder is not optional equipment for you.

The other thing carbon-and-materiality fortnight did was break your clock. You'd have told me the deliverable list was hopelessly behind schedule, and then you answered the questions in ten or fifteen minutes with Claude Code, and then came the vertigo. I told you to expect it: you have to recalibrate your own notion of how long things take, and it is a genuinely weird feeling when work that used to take your whole week gets done inside a coffee. But the vertigo has a productive form, which is the question I wanted ringing in your ears: *what is the work, then?* Here's my answer, and it's the cart-before-the-horse exercise from week two in different clothes. The difference between a project leader and a partner is that a partner can walk into a situation and commit: what it costs, how long it takes, what it's worth. When execution collapses to minutes, what remains, what appreciates, is exactly that partner judgment: what are we doing, why, for whom, and what would make it valuable. The tool forces all of us to think like partners. Most professions won't get an invitation like that for decades. Sustainability got it first. I keep telling you: my goal is for climate people to be seen as the pioneers of AI in their organizations. Pure knowledge work, lean teams, nothing to cut and everything to prove. You've got to generate some CO2 to get there, I'm sorry, that's what it is.


## 05 · Brilliant and stupid in the same conversation

Now we come to management, and I need to prepare you for the strangest fact about your new colleague. It can be brilliant and stupid in the same conversation. Usually we don't deal with that when we deal with intelligence. Humans are consistent at their level; the model is not, and the sooner you stop being scandalized by that, the sooner you can manage around it, and even through it: ask it to write the instructions that prevent last hour's stupidity and those instructions will be brilliant. It doesn't happen with interns.

The management playbook we assembled over the weeks fits on a page. Don't over-specify. The best metaphor I have is the really smart, talented young person you micromanaged, who comes back with something you didn't want and says: but that's what you asked me for, right? Start broad, then get narrow; if you start narrow you never rent out the full intelligence. Say less when correcting: "I noticed the deck was incomplete" out-performs a paragraph of specification, because it lets the thing self-diagnose. Express frustration productively; it's information. Ask "is there a tool for this?" when it claims it can't do something, because a lot of times it doesn't know, or pretends not to know, that it can install things. Keep a long-lived thinking session for direction and spin up disposable doing sessions for execution, and don't fall in love with your sessions; be a little ruthless, archive, move on. And stop with "you are an expert in climate" role-priming. Very 2025. I dropped it and I don't miss it.

Underneath the playbook are two psychological hazards, and I've suffered both, so this section is me referring to myself, okay? The first I named in week four: AI indigestion. It produces so much that you start waving it through. Awesome job, I'll look at it this weekend. You never come back to it. The volume is a feature economically and a hazard cognitively, and the failure mode is subtle: you're still there, still nodding, but you've taken yourself out of the process. The discipline is to take yourself up a level. You're the briefer being briefed. Tell me in plain English. One paragraph. The three things Sarah needs to know. Distill and distill until synthesis, because synthesis is the only unit of output your judgment can actually inspect. It's kind of weird walking around with an entourage of tireless analysts pressing work into your hands, and what the entourage trains, if you let it, is assertiveness. We have a great working relationship, Claude and I. Also, I'm the boss.

The second hazard is the seduction of polish. Nil said it best, and bravely: it's looking so beautiful, so perfect, it's damaging my confidence, like losing control of it. Beautiful output suppresses questioning; a wall of charts feels like rigor while being, sometimes, the opposite. So let me give you the epistemics in miniature. When the model produces something eerily specific, ask my favorite question: how does it know that? Sometimes the answer is that it stitched an inference across adjacent patterns, which is why it's so scary smart. Sometimes it's making it up. We have to entertain both possibilities, every time, and be on the lookout, because a fabrication is dressed in the same confidence as a discovery. It reminds me of when my kids were little and I had the answer to everything, and if I'd had to be specific, I'd probably have made it up. Don't tell my kids. This is a little bit of the way AI is. And if you ask it to explain how it knew, be aware it can hallucinate the explanation too. The posture isn't paranoia and it isn't faith. It's the same professional skepticism you'd apply to a dazzling expert, which, I pointed out to you more than once, is not an insult to the expert. It's the job.


## 06 · It's not software

Week five I put a sentence on the screen that I consider the paradigm break of the whole program, so here it is again: *it's not software.* Software, to a certain degree, is supposed to work. The engineers fixed the bugs; it does a certain thing and we count on it doing that thing one hundred percent of the time. We don't work that way with people, and we don't work that way with AI. This thing lives in a funny in-between zone, fallible like a person, tireless like a machine, with some brand-new ways to screw up that neither has, and the 2025 style of adoption, "I'm going to beat it until it behaves like software," is a category error. That's not AI. That's something different, and worse.

Once you accept that, the architecture vocabulary sorts itself out. The *harness* is the execution environment wrapped around the model's intelligence: the memory (CLAUDE.md, the reference files, the whole file tree), the tools (read, write, query, call, spawn), and the autonomy to chain steps without you clicking approve every ten seconds. People say, and I'm apparently one of them, that the harness right now matters more than the model. What makes a harness valuable is that it is workflow complete: it closes the loop. Data comes in, the model reasons over it with your context active, files come out, and the files are the work, versioned, in your folder, feeding the next cycle. Every deliverable you built this course ran through that loop, whether you noticed or not. You were operating the harness. That's the skill on your résumé now, whatever the job title says.

> *[Figure 4 · Workflow complete. The harness closes the loop; the loop, run repeatedly over your growing local context, is the compounding machine. This is also why siloed SaaS lost the market's confidence: it holds one arc of this circle and charges rent on it.]*

But the harness has a limit, and the limit is not capability, it's people. Sarah is never going to open a terminal. The analysts you hand work to, the portco contacts, the client's client: not in the harness, not ever, and open-ended work requires judgment to scope anyway. So week five's question was the design question: what do you want Sarah to be able to *do*? And the answer is an app: a codified workflow with specific inputs and consistent outputs that anyone can run, built by the harness, sometimes with an agent inside it. The harness is where you work; the app is what you leave behind. And I want you to notice the beautiful, slightly absurd logic loop we discovered: when someone says "I don't trust AI to do this, I want an app," the next step of that conversation is, okay, I'll have AI make you the app. It's a little weird to even say it. It's also the honest shape of the future. I didn't use Claude in Excel; I used Claude to *make* an Excel, without opening Excel. That's a huge leap, and once you've made it, a whole aisle of the software store starts to look like training wheels. Agents, by the way, same story: in 2025 Ben and I were all about agents, agents are the future, and now we never talk about them, because the harness makes them the way a box makes Kleenex. A paragraph of instructions and the plumbing to carry it. Disposable. Write reference files instead; the agents will be spun up as needed, and thrown away without ceremony, which is what you do with tissues.

I said something stark in that session and I'll repeat it here because I meant it. I believe the SaaS model of AI adoption is going to fail. Not underperform. Fail. And I believe relatively unconstrained collaboration with AI, as the models keep getting smarter, is the future of this kind of work, and anyone not developing that muscle is at risk of losing whatever they currently do. You're either driving the bus cognitively, pushing it as hard as it will go, or the bus eventually doesn't need your seat. I'm sorry to put it so starkly. Also: 99.5% of professionals have never once pushed an LLM as hard as they can. Until a person has done that, they can't understand any of this, which is why my one diagnostic question for AI readiness is simply: have you ever been rate-limited? If you haven't, try harder. Ganbatte, as they say in Japan. And notice who in your organization has never seen that notice: the CEO hasn't. The CFO hasn't. The head of AI may never have been. That imbalance, the people with the least hands-on hours holding the most decision rights over adoption, is going to be with us for a while, and it's why minds get changed one demo at a time, from below. Very Star Wars: you're the Jedi, IT is the Death Star. Find a way to demo.


## 07 · Make every figure testable

Assurance week is where the two halves of your professional life, the AI half and the EY-shaped half, stop being in tension, so follow the argument closely; it's the one you'll repeat most often to skeptics, regulators, and partners.

Begin with the uncomfortable, liberating truth: carbon accounting is estimation. It has always been estimation. Assurance never attested that a number was exactly correct; it attests that the methodology is sound, the estimates are reasonable, and the assumptions are documented. So the question about AI is not whether it introduces estimation into a precise process. Estimation *was* the process. The benchmark is reasonableness and documentation, and that reframing changes the debate from "can we trust the robot" to "can we test the figures," which is a question professionals actually know how to answer.

Then distinguish two kinds of error, because most AI-risk conversations mash them together. Random error doesn't reproduce; it washes out; sampling and spot-checks catch it; it is boring. Systematic bias is directional, recurs for the same reason, accumulates, and replication does not remove it. That's the real threat, so ask precisely where it can live. In the source data? Then the client's documents are wrong, same exposure as a manual process, not an AI question. In the orchestration? Real, but correctable: a biased shared prompt can be read, found, and fixed, which is more than you can say for a biased culture of analysts. In the weights themselves? That's the honest carve-out: when the system fills a data gap, the model's prior does the work, and priors regress to the mean of the training distribution, which for an atypical client is a directional skew. Notice, though, that this is precisely the sub-task a well-built system tags as an estimate, documents, and routes to human judgment. The claim was never "no bias." The claim is that the only uncorrectable bias lives exactly where the system concentrates its scrutiny. Meanwhile the tasks people worry about most, extraction, classification, calculation, are the least vulnerable: there is no directional way to consistently misread a kWh figure, electricity-to-Scope-2 is settled convention, and the arithmetic is done by a deterministic engine, because the model doesn't do arithmetic; it delegates to something that can't improvise.

Two design principles fall out of this, and they're the ones I most want stitched into your reference files. First: independence is the wrong word for agent B checking agent A, because both share the same priors. Real independence comes from external referents, things outside the model: stored source documents, versioned factor APIs, deterministic calculations. And frame every QA pass as error-finding, never as confirmation, because asking "is this correct?" invites the confirmation reflex, in models and, you may have noticed, in people. Second: provenance is a binding, not an assertion. Not the model's claim about where a value came from, a mechanical link to a stored source that any process can check. A fabricated value has nothing to bind to. It fails the check, automatically, which turns hallucination from a philosophical anxiety into a failed test with a line number. Fabrication is the failure mode unique to generative systems, and it is also the one most directly defeated by architecture.

> *[Figure 5 · Provenance as a binding. The point of the architecture is not that the model never invents; it's that an invention has no source to bind to, so it fails a mechanical check instead of surviving on confidence.]*

I'll append my contrarian coda, clearly labeled as opinion, because it shaped how we taught the final project. I am very suspicious of rigor being imposed on a subjective process. Standards don't improve what we do; they make it comparable, and a "4" under the same methodology is probably not the same "4" across applications; I kind of doubt it, twice. When the rigor of the process exceeds the inherent rigor of the underlying task you get a templated thing nobody believes, and it goes in a drawer. So when Claude produces a score, ask where it came from; when it cites a methodology, ask what the methodology froze; and remember the aphorism from our disclosure discussion: sensitive plus latitude equals silence. The final project made you productize disclosure, decompose the service, encode each task in a reference file, and then price it, because pricing is the forcing function that makes all of this real. If you're going to charge X, it has to be good enough for X. It's not a neat tool. It's not a cool thing you know that no one else knows. It's something that produces work, so let's get serious. And note what I said about the stakes of that exercise: if you'd come back saying "Diego, it's not possible, AI doesn't help, it gets priced the way it's priced today," we'd have learned something extremely valuable. You didn't come back saying that. Nobody has yet. Work doesn't go away; there is no *should* about it; work gets reorganized and repriced, and the people holding the pencil for that repricing will be the ones who understand both the process and the tool. That's you. That was always the plan.


## 08 · The dyad

Let me end where the course actually ended, which is not with a technique but with a picture of who we are in this arrangement, because everything else, the markdown, the ladders, the harness, hangs off this picture.

There are people at the labs who would like nothing more than for AI to be a standalone solution. I don't love that future; let's set it aside, because short of it, AI is always a component in a system, and the minimum system is two: the human and the AI. I call it the dyad. AI by itself is a tree falling in the forest. If there's no human there to say *this is good, this is valuable, this matters*, is it worth anything? Only interpreted through the lens of human judgment does it acquire value, and there is exactly one determinant of whether the work in your local context is valuable. It isn't me, and it isn't Ben. It's you.

Why should that division be stable, even as models improve? Because of what we bring that training can't encode. Human networks are shaped by pleasure and pain, by stakes; the model is the residual of our recorded patterns, brilliant and enormous, but it doesn't know what it is to lose, or to win, or to have something matter, because mattering isn't in the data. That's why I'm not a believer in AGI as advertised, and what do I know, but as I understand it the hard problem is skin in the game, and I just don't know how we get there. In the meantime, the dyad is emergent: two different topographies of intelligence, and the collaboration finds things neither could find alone. When we search, we search for what matters to us. That's the part that doesn't automate.

This is also why I told you, cheerfully, that the users know something the builders don't. Very few people who make LLMs use them as hard as you now do. You are intensive users operating a dyad inside a real profession, and your intuitions, about when it's brilliant, when it confabulates, what the reference-and-inference trade feels like from the driver's seat, are original knowledge. Contribute them. Newsflash: the engineers don't know. And remember the empirical fact I asked you to hold from week one: same assignment, same model, same data, twenty-eight different deliverables. The more difference, the more the human matters. Someone's in the captaincy. The variance *is* the evidence.

So here is the charge, the same one I gave you in the final weeks, with the same affection and the same lack of sugar. This is a high-uncertainty process with a pretty certain end. The only thing I'm sure of is that no one is going to hand it to you: not your firm, not your IT department, not Anthropic, not me. The question was never "how do I do it?" The question is "how are you going to do it, you guys?" Your trajectory has already bent, like a comet that swung close to something massive; four months from now the possibilities will look different again, and you'll adjust, because you've now lived through a model getting smarter, then dumber, then priced differently, and you kept shipping. Be assertive with your entourage. Keep your skepticism warm and your imagination warmer, because the most underrated resource in all of AI is human imagination. Use it freely. Use it freely.

And the very last thing, which I said out loud in week six and meant completely: pretty quickly, Claude Code replaces me and Ben. You just don't need us anymore. The whole design of the course was that you'd realize this at the end and not at the beginning. If you're reading this to refresh yourself before teaching others: that's the trick. Raise the stakes, hand them the keys, and make yourself progressively unnecessary. The car will tell them how to drive the car. You tell them it's worth driving, and you show them, one demo at a time, where it can go.


---

*Synthesized with gratitude from the March 2026 cohort sessions: the Monday lectures, the Wednesday office hours, the Friday demos, the tomatoes offered and thrown. Errors of transcription and emphasis are the synthesizer's. The em-dash count of this document has been kept deliberately low; Diego was a user of them his whole career and gave them up because people thought he was AI. We honor the sacrifice.*