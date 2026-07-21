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
