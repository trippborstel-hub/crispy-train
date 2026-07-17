# Session log — 2026-07-16 — Sandbox client concept: "Alderwood Group"

_Participants: Tripp + Claude_

## What happened

1. Decided the Kith `northwood-capital/` workspace stays **local-only** (never committed):
   it's Kith's course IP and contains their live Supabase key. Our students never need it —
   we're building our own sandbox. `.gitignore` already blocks `*api-keys.md` as a backstop.
2. Drafted the sandbox client concept: `course-build/sandbox-client-design-v1.md`.

## The concept in brief

**Alderwood Group** — fictional $1.1B family-held food & beverage / packaging / cold-chain
company, ~40 sites, 4 divisions. Engagement trigger: SB 253 + top customer demanding CDP
data + sustainability-linked loan + an unsubstantiated "carbon neutral by 2030" marketing
claim the audit committee is scared of. Deliberately NOT a Northwood clone: corporate (not
PE) because that's EY's actual client shape; we keep the pedagogy (multi-entity, messy
data, skeptical CFO, metrics→dollars) and none of the content.

Key calls awaiting Dan/Miranda/Tripp sign-off:
- Files-only data package, no Supabase (zero infrastructure for pilot)
- 13-flaw seeded data catalog, each flaw mapped to a week's lesson; instructor answer key
  never ships to students
- Students get a separate clean repo at launch; crispy-train stays instructor-only

## Next steps

- [ ] Team green-light on Alderwood (or alternatives B/C in the doc)
- [ ] Generate the data package + engagement inquiry + company profile
- [ ] Write instructor answer key alongside data generation
