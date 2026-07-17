# Session log — 2026-07-16 — Built the Riverbend sandbox data package

_Participants: Tripp + Claude_

## What happened

1. Tripp approved the sandbox concept but renamed it: **Alderwood Group → Riverbend
   Beverage Group** (more beverage-forward). Leaned into it — now a pure beverage company
   (bottling, acquired craft brands, packaging, cold chain), which tightens the story:
   water stress is existential for a bottler, agri inputs drive Scope 3.
2. Confirmed the Kith `northwood-capital/` folder stays **local-only** (Kith's IP + live
   Supabase key; students never need it — they get Riverbend).
3. Built the full sandbox in `sandbox-client/`:
   - `company-profile.md`, `engagement-inquiry.md` (Rosa Vantia's RFP letter — the Week 1 input)
   - `riverbend-2024-sustainability-highlights.md` (the greenwashing doc — Week 4 fodder)
   - `data/`: facility master list, energy CSV (397 rows), Headwater xlsx (different
     schema/units), fleet export, supplier spend top-50, revenue/headcount, 4 site
     questionnaires, 3 HTML utility bills
4. All 13 seeded flaws implemented and verified; exact locations + expected findings in
   `course-build/instructor-answer-key-v1.md` (**instructor-only, never ships to students**).
5. Data generated deterministically by `course-build/tools/generate-sandbox-data.py`
   (seed 4258) — regenerable and tweakable. Headwater xlsx built with openpyxl
   (installed on Tripp's machine this session).

## Design notes for Dan & Miranda

- Questionnaires carry breadcrumbs for the data flaws (Denise mentions the double October
  submission; Tyler contradicts his own gas data; Sal warns about the insane July reading;
  Priya flags the refrigerant blindspot). Students who *read* the qualitative material get
  rewarded — that's deliberate.
- Two utility bills reconcile with the CSV, one doesn't (transposition) — the Week 4
  provenance exercise.
- Answer key includes "non-flaw texture" (things that look wrong but are right — glass
  furnace gas, Phoenix cooling load, reefer fuel with zero odometer) so instructors don't
  get blindsided in demos.

## Next steps

- [ ] Dan/Miranda: run the Week 2 exercise against this data cold — does an agent-guided
      audit surface flaws at the right difficulty?
- [ ] Build `reference-totals.py` (corrected-data ground truth) for Week 3 grading
- [ ] Port Kith setup guide + privacy cheat sheet → Cursor/EY versions (Week 0 pack)
- [ ] Draft Week 1 kickoff deck (Riverbend edition of Kith's Week 1)
