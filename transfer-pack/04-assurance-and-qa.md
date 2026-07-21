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
