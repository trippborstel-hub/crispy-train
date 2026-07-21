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
