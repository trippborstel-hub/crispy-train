# Source Map — The Multi-Source Foundation of the EY Climate AI Agent Pilot (v1)

_Drafted 2026-07-17 · Owner: Tripp · Status: living document — update as sources are adopted_

## Why this document exists

This course is built by research, not by copying. The Kith Climate cohort is its
pedagogical inspiration and one of its sources; this document records the full source
stack, what each source contributes, and the attribution and boundary rules we follow.
It is the evidence of method. Every module we build should be traceable to entries here
(the "source ledger" convention in CLAUDE.md).

## The ethics framework (agreed 2026-07-17)

1. **Idea vs. expression.** The core ideas taught in the Kith course (AI as a system
   rather than a model; context files as institutional knowledge; LLMs as probabilistic
   colleagues rather than software; assurance via documentation and provenance) are
   convergent, field-common ideas that many practitioners have reached independently.
   Ideas are commons. *Expression* — Kith's artifacts, decks, coinages, client
   simulation, sequencing — is Kith's IP and is not reused.
2. **The three tests** that make this research rather than derivation:
   **transformation** (different audience, harness, emphasis, artifacts — Riverbend was
   built from scratch; the arc is restructured; assurance is rebuilt on audit-profession
   primary sources), **attribution** (Kith credited in Week 1 and instructor materials;
   distinctive coinages credited by name if used), and **permission** (Diego's blessing
   to be sought — note his own Week 6 module is titled "Taking Claude Code Back to Your
   Team"; internal propagation is the advertised outcome of his course).
3. **The commercial boundary.** An EY-internal training inspired by Kith is aligned with
   Kith's stated mission. Packaging Kith frameworks into client-sold EY offerings, or
   presenting Kith coinages as EY-original thought leadership, is out of bounds.

## Selection criteria for sources

1. **Complement, don't duplicate** — strongest where Kith is thin: vendor-canonical
   mechanics, organizational change, citable governance standards, formal evaluation.
2. **Audience fit** — built for professionals, not software engineers.
3. **Authority diversity** — at least one each: vendor canon, academic/practitioner,
   standards body, EY-internal.
4. **License/adaptability** — vendor docs and standards are free to build on; commercial
   courses are benchmarked, never copied (same courtesy we extend Kith).
5. **Durability** — concepts that survive a harness change (Cursor → Claude Code).

## The source stack

### 1. Kith Climate 6-week cohort (pedagogical spine)
*What it contributes:* the cohort format (fictional client, weekly deliverable, peer
demos, build–apply–present), the deliverable-first "raise the stakes" pedagogy, and the
strongest conceptual framings (atomic unit, reference-vs-inference, trust ladder,
provenance-as-binding). *How we use it:* structure and concepts re-expressed in our own
materials; zero artifact reuse; attributed. *Materials:* `reference_files/` (private
study copies) + Tripp's and Miranda's firsthand experience.

### 2. Vendor canon — the mechanics layer
- **[Cursor docs](https://cursor.com/docs)** and **[Cursor Learn](https://cursor.com/learn)** —
  required reading; EY's harness. Agent mode, Rules, MCP, models, enterprise controls.
  Feeds: Week 0 setup, Week 1 skills, all live builds.
- **[Anthropic Academy](https://anthropic.skilljar.com/)** (free, certificate-issuing) —
  notably *Claude Code 101* / *[Claude Code in Action](https://anthropic.skilljar.com/claude-code-in-action)*
  and the *AI Fluency* course (its Delegation / Description / Discernment / Diligence
  framework is a ready-made complement to our management-skills thread). Feeds: Weeks 1,
  2, 5; also the future-proofing story for when Claude Code lands at EY.
- **Anthropic's *Building Effective Agents* + Claude Code best-practices guidance** —
  canonical citations for agent patterns, context management, and permission design.
  Feeds: Weeks 1–3.

### 3. Practitioner-conceptual — the "working with it" layer
- **Ethan Mollick** — *Co-Intelligence* (book) and One Useful Thing (newsletter);
  [Wharton exec-ed AI offerings](https://executiveeducation.wharton.upenn.edu/faculty/ethan-mollick/).
  The single best complement to the Kith voice: same territory, academically grounded,
  strong on organizational adoption and the "jagged frontier" of capability. Feeds:
  Week 1 framing, instructor narrative, partner-facing talking points.
- **Simon Willison** (blog) — grounded, skeptical LLM behavior analysis; excellent on
  what models actually do and fail to do. Feeds: Week 2–3 epistemics ("how does it know
  that?").
- **Andrew Ng — agentic design patterns** (reflection, tool use, planning, multi-agent).
  A second, independent taxonomy of the same ideas. Feeds: Weeks 3, 5.

### 4. Course-form benchmarks (study the form, not the content)
- **[DeepLearning.AI: Claude Code — A Highly Agentic Coding Assistant](https://www.deeplearning.ai/courses/claude-code-a-highly-agentic-coding-assistant)**
  (with Anthropic; taught by Elie Schoppik) and
  **[Agent Skills with Anthropic](https://www.deeplearning.ai/courses/agent-skills-with-anthropic)** —
  benchmark for exercise design and hands-on pacing.
- **[Coursera: Claude Code — Software Engineering with GenAI Agents](https://www.coursera.org/learn/claude-code)** —
  benchmark for a university-style treatment.
- **Section, Maven cohort courses** — benchmarks for business-professional AI training
  formats and cohort mechanics.

### 5. Governance & assurance — the layer where EY leads
- **EU AI Act, Article 4 (AI literacy)** — in force since Feb 2025; staff AI-literacy is
  a legal obligation for AI deployers; compliance is process-based and documented. This
  makes the pilot itself part of a compliance story, and it belongs in the Week 0/4
  narrative. ([overview](https://iternal.ai/eu-ai-act-literacy))
- **NIST AI RMF** (+ Generative AI Profile) and **ISO/IEC 42001** (AI management
  systems; clauses 7.2–7.3 map to literacy/competence) — citable scaffolding for Week 4;
  see [framework mapping](https://euaicompass.com/iso-42001-nist-ai-rmf-eu-ai-act-mapping.html).
- **Audit-profession literature on AI assurance** (IAASB/AICPA/ICAEW streams) — Week 4
  is rebuilt on these primary sources, where EY's institutional depth exceeds any
  external course.

### 6. EY-internal — the layer that makes it an EY course
`[EY-NETWORK — Tripp: identify and link the actual assets]`
- EY AI academy/badge offerings (whatever exists internally for GenAI fluency)
- EY responsible-AI framework and GenAI usage policies
- EY climate/sustainability methodology assets (non-client-specific)
Feeds: Week 0 rules, Week 4 governance, and internal legitimacy/credit pathways.

### 7. Domain standards (climate content)
GHG Protocol (scopes, boundaries), TCFD/ISSB (risk framing lineage), California SB 253
(the sandbox trigger event), CDP/PCAF as relevant. Feeds: Weeks 2–4 content accuracy.

### 8. Primary experience (original source material)
Tripp's and Miranda's Kith experience; this repo's session logs; the pilot cohort
itself — the use-case backlog, demo recordings, and student artifacts become the richest
source for cohort 2. Original data, owned outright.

## Week-by-week source mapping

| Week | Kith contributes | Other sources carry |
|---|---|---|
| 0 Pre-flight | Setup-guide concept, privacy-sheet concept | Cursor docs (mechanics), EY policy (rules), EU AI Act Art. 4 (why training is obligatory) |
| 1 Pitch it | Fictional-client kickoff format, stakes-first pedagogy | Cursor Learn (agent basics), Anthropic AI Fluency (delegation/description), Mollick (adoption framing) |
| 2 Ground it | Data-week concepts (context files, directing inference) | Anthropic agents guidance, Willison (model epistemics), GHG Protocol (data quality tiers) |
| 3 Prove it | Trust-ladder framing, dashboard deliverable pattern | Ng patterns (tool use/reflection), GHG Protocol + SB 253 (content), DeepLearning.AI (exercise form) |
| 4 Assure it | Provenance/QA framings | **Primary rebuild:** audit-profession AI assurance literature, NIST AI RMF, ISO 42001, EY responsible-AI framework |
| Demo Day | Demo culture, champions mechanic | Ben's case-competition playbook (attributed), EY internal comms norms |

## Attribution plan

- Week 1 kickoff and the course hub footer: "Modeled on the Kith Climate cohort
  (kithclimate.com), which Tripp and Miranda completed as students. Built with
  additional sources — see the source map."
- Instructor materials: this document travels with the course.
- Named coinages (e.g., "the atomic unit") credited to Diego Espinosa / Kith when used
  by name; otherwise re-derived framings in our own words.
- Pending: Diego's and Ben's blessing (draft note in progress). Guest Demo Day
  appearance to be offered.

## Boundaries (hard rules)

1. No Kith artifacts in student-facing materials: no Northwood, no Kith decks, no Kith
   reference files, no transcript excerpts.
2. Kith's Supabase environment and API keys are never used or distributed.
3. This course is internal-only; it is not packaged into client-facing EY offerings.
4. If any module ends up leaning on a single source, stop and diversify or attribute
   prominently — single-source modules are the failure mode this document exists to prevent.
