# Riverbend Sandbox — Instructor Answer Key (v1)

**INSTRUCTOR ONLY — never ships to the student repo.**
Authoritative catalog of seeded flaws with exact locations and expected findings.
Data is generated deterministically by `course-build/tools/generate-sandbox-data.py`
(seed 4258). If you regenerate with a changed script, re-verify this key.

## Flaw ledger

| # | Flaw | Exact location | Expected student finding | Week |
|---|------|---------------|--------------------------|------|
| 1 | MWh in a kWh-labeled column | `headwater-brands-energy-2025.xlsx`: all HWB-01 ELEC rows are ~280–340 (MWh) while HWB-02/03 are ~180k–250k; UOM column says kWh for all | HWB-01 electricity is ~1000× too small vs. comparable plants; questionnaire HWB-02 Q7 breadcrumbs a billing-provider unit change. Correct treatment: ×1,000 the HWB-01 values, document the assumption | W2 |
| 2a | Facility in energy data but not master list | `energy-consumption-2025.csv` has RBC-06 (Jan–Aug only); absent from `facility-master-list.csv` | Medford plant sold Aug 2025 — master updated, energy file not. Raises boundary question: does a divested site's Jan–Aug consumption belong in the 2025 inventory? (Yes, for the ownership period — good discussion) | W2 |
| 2b | Facility in master list with zero energy data | `facility-master-list.csv` row RPS-05 Boise Can Sheet Plant, status Operating; no rows in energy CSV | Data gap at an operating plant — belongs on the data ask, not silently ignored. (In-world truth: site reports through a regional office that never received the request) | W2 |
| 3 | Duplicate month | `energy-consumption-2025.csv`: RBC-01 2025-10 electricity AND gas rows appear twice (identical values) | Dedup before totals; breadcrumbed in RBC-01 questionnaire Q7 ("submitted twice… portal migration") | W2 |
| 4 | Missing months | RBC-04 Spokane: no rows for 2025-03/04/05 | Gap ≠ zero. Estimate (interpolation or same-months prior-year logic), tag as estimated | W2/W3 |
| 5 | Questionnaire contradicts data | HWB-02 questionnaire Q3: "fully electric facility, no gas service on site" vs. xlsx NATGAS rows ~3,300–5,900 therms/mo for HWB-02 | Source-trust hierarchy: metered/billed data beats testimony; but the contradiction itself must be surfaced and resolved with the client, not silently picked | W2 |
| 6 | Extra digit / outlier month | `energy-consumption-2025.csv`: RPS-01 2025-07 electricity = **4,741,390** kWh (true value 474,139) | ~10× every other month; breadcrumbed in RPS-01 questionnaire Q2/Q7 (meter replacement, "one reading I don't believe myself"). Correct: flag, correct with documented basis, or exclude with note | W2/W3 |
| 7 | Refrigerants absent everywhere | No file contains refrigerant quantities; CDL-03 questionnaire Q4 mentions ammonia top-offs ×2, R-507A, R-404A reefer units; RBC-01 mentions R-134a recharge after a leak | Absence-of-data as a material finding: fugitive emissions from a cold-chain business are a known Scope 1 category, currently unquantifiable. Belongs in data ask + inventory boundary notes | W2/W3 |
| 8 | Mislabeled fuel unit | `fleet-fuel-export-2025.csv` column `FUEL_GAL` contains **liters** | Plausibility check: TRACTOR ~11,800 km/veh/mo with FUEL_GAL read as gallons implies ~7.4 mpg… actually ~35 L/100km — only sensible as liters. Convert in code; document | W3 |
| 9 | Bill ≠ CSV | `utility-bills/RBC-01-electric-2025-03.html` shows **268,400 kWh**; CSV row RBC-01 2025-03 Electricity = **246,800** (digit transposition). April bill + RPS-01 Feb gas bill reconcile exactly | Provenance lesson: a figure is only as good as its binding to source. The other two bills prove reconciliation is possible; this one fails it | W4 |
| 10 | Leased-office boundary | COR-03/04/05 in master list (Leased), no energy rows anywhere | Organizational boundary judgment (operational control): include or exclude leased sales offices, state the choice, estimate if included (~small). The point is the documented decision, not the number | W3 |
| 11 | Unsubstantiated claim | `riverbend-2024-sustainability-highlights.md`: "carbon neutral by 2030" citing Pacific Timberlands offsets "(2021 vintage)" retired already; zero inventory basis; "100% — our commitment" fluff | W4 capstone: no baseline inventory existed when claim was made; already-retired 2021-vintage forest offsets can't cover 2030 operational emissions; claim as stated is unsupportable → recommend withdraw/restate + what substantiation would require | W4 |
| 12 | Supplier duplicate | `supplier-spend-top50.csv`: "Cascade Malting Co." ($6.2M, Malted barley) + "Cascade Malting Company LLC" ($3.9M, Brewing malts) | Entity resolution before spend-based Scope 3 estimates; combined ~$10.1M makes it a top-10 supplier | W2 stretch |
| 13 | Fiscal vs. calendar year | `revenue-headcount-by-division.csv` comment line: FY = Jul 2024–Jun 2025; energy data is CY2025 | Intensity denominators misaligned by 6 months; either note the limitation or request CY revenue. Catching the comment line is itself the lesson (agents skip comments if you let them) | W3 |

## Non-flaw texture (things that look odd but are correct)

- RPS-01 gas dwarfs everything (~104k therms/mo): correct — glass furnace. Teaches "big ≠ wrong."
- CDL-05 Phoenix electricity is the highest of the DCs: correct — cooling load in Phoenix.
- REEFER_TRL rows have ODO_KM = 0 but nonzero fuel: correct — trailers don't have odometers; reefer units burn diesel while parked. (Subtle Scope 1 completeness point for strong students.)
- Summit Industrial Gases sells beverage-grade CO2: fun discussion — the product literally contains CO2; is dissolved product CO2 an emission? (Yes, eventually — GHG Protocol treats it under Scope 1 or 3 depending on sourcing; instructor can keep this as a stretch tangent.)

## Reconciliation totals (for grading Week 3 inventories)

After correcting flaws 1, 3, 6 (and excluding nothing else), approximate CY2025 totals:
- Corporate energy CSV + Headwater: ~48–50 GWh electricity; ~1.9–2.0M therms gas
  (glass plant is ~60% of all gas).
- Compute exact reference totals with a corrected-data script before the pilot; store
  alongside this key. (TODO — build `course-build/tools/reference-totals.py` when we
  build the Week 3 instructor materials.)

## Answer-key hygiene

- Student repo gets `sandbox-client/` ONLY. This file, the generator script, and
  reference totals stay in `course-build/`.
- If a student finds an *unseeded* anomaly that survives scrutiny, it's a generator bug:
  log it here, fix or adopt it (some of the best flaws will be accidents).
