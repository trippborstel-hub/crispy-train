# AI Agent Data Handling Cheat Sheet — EY Climate AI Agent Pilot (v1)

*Read before Week 1. This is the document that keeps you, the client, and the firm safe.
Adapted from the Kith Climate "Claude Privacy & Data Security Cheat Sheet."*

> **⚠ Placeholders marked `[EY-NETWORK]` require confirmation against EY's actual Cursor
> deployment and Risk Management guidance — Tripp to complete before distribution.
> Until every placeholder is resolved, the conservative rules in Section 1 govern.**

---

## 1. The rules for this course (non-negotiable)

1. **Fictional data only.** The course workspace contains Riverbend Beverage Group — an
   invented company. Nothing real goes in: no client names, no client data, no EY-internal
   documents, no personal data, not even "anonymized" client material. If you're unsure
   whether something counts, it counts. Leave it out and ask.
2. **No secrets, ever.** No passwords, API keys, tokens, or credentials in any file the
   agent can read, in any prompt, in any tool. Use placeholders (`<API_KEY>`). Assume
   anything in the workspace gets transmitted (see Section 2 — it does).
3. **Course tools for course work.** Don't point your course setup at engagement files
   "just to try it" — the path from these skills to real client work exists, but it runs
   through Risk Management, not through enthusiasm. Week 4 and Demo Day cover the road map.

These three rules are the whole compliance story *for the pilot*. Everything below is
understanding — which you need, because your clients will ask you these questions.

## 2. The core mental model: everything the agent reads is sent

An agent harness is not a local tool that occasionally phones home. **Every file the agent
reads, every prompt, and every piece of context is transmitted to the model provider's
servers for processing.** That's how inference works. Consequences:

- The agent's file access = your data-disclosure surface. Opening a folder in Cursor
  makes its contents *readable*, and anything it reads in a session is *sent*.
- This is far more surface area than a chat window, where you paste things deliberately.
  With an agent, a stray file in the workspace goes along for the ride.
- Corollary: **curating the workspace folder is a security control**, not housekeeping.

## 3. Consumer vs. enterprise — the distinction that decides everything

The Kith course taught this for Claude; it's true across every provider:

| | Consumer account (personal Pro plan) | Enterprise deployment (EY's Cursor) |
|---|---|---|
| Training on your data | Opt-out toggle, easy to miss | Contractually excluded |
| Retention | Up to 5 years (training on) / 30 days | Short, contract-defined `[EY-NETWORK: confirm EY's terms]` |
| Admin controls | None | Org-level policy, model allowlists |
| Appropriate for work data | **No** | Per EY policy `[EY-NETWORK: cite it]` |

The practical takeaway your clients need to hear from you: *"a Pro plan sounds
professional but is a consumer account."* Enterprise terms — not the model, not the
price — are what make a deployment business-grade.

`[EY-NETWORK — Tripp: confirm EY Cursor specifics — is Privacy Mode enforced org-wide?
What is the contractual retention with Cursor and with the underlying model providers?
Is codebase indexing (embeddings of your files on Cursor's servers) enabled or disabled?]`

## 4. Where your data lives locally

Agent harnesses keep local session history — prompts, responses, file contents — in
plaintext on your machine (Cursor stores chat/agent history per workspace; Claude Code
stores JSONL transcripts under `~/.claude/`). Two implications:

- Anyone with access to your machine can read past sessions. Standard EY device security
  is your control here — it's why course work happens on managed devices.
- Deleting a chat from the UI and deleting local history are different things.

## 5. EY-specific obligations

This section is what makes this sheet EY's rather than anyone's.

`[EY-NETWORK — Tripp, with Risk Management: confirm and complete —`
- `Which EY policy documents govern generative-AI tool use (names + links)?`
- `Client confidentiality: what may touch an approved AI tool even under enterprise
  terms — and what never may (audit clients? PII? material non-public information)?`
- `Independence: any restrictions arising from EY's audit relationships (e.g., using AI
  tools in ways that create self-review threats on assurance clients)?`
- `Approval path: who signs off before AI-agent use on a real engagement, and what does
  the request look like?]`

Until completed: the Section 1 rules make the question moot for the pilot — nothing real
enters the tools.

## 6. Quick reference checklist

- ☐ I'm signed into **EY's** Cursor, not a personal account
- ☐ My course workspace contains only the cloned course repo
- ☐ No real client, EY-internal, or personal data anywhere in the workspace
- ☐ No credentials or secrets in any file or prompt — placeholders only
- ☐ I understand everything the agent reads is transmitted for inference
- ☐ I know the path to using this on real work runs through `[EY-NETWORK: approval path]`
  — not through my own judgment alone

## 7. Why we teach this in week zero

Because it's the first question every partner, every client, and every skeptic asks — and
because the honest, precise answer ("here is exactly where the data goes, here are the
contractual terms, here is what we never put in") is *the* trust-building move that
separates professionals using AI from enthusiasts playing with it. You're learning the
answer now so you can give it confidently for the rest of your career.
