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
