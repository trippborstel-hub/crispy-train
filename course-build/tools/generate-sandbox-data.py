#!/usr/bin/env python3
"""Generate the Riverbend Beverage Group sandbox data package.

Deterministic (fixed seed). Seeds the flaws documented in
course-build/instructor-answer-key-v1.md — if you change a flaw here,
update the answer key, and vice versa.

Usage: python3 generate-sandbox-data.py  (writes into sandbox-client/data/)
"""
import csv, math, random, os

random.seed(4258)  # Riverbend founded 1958 + 42. Do not change: answer key depends on values.

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sandbox-client", "data")
os.makedirs(ROOT, exist_ok=True)
MONTHS = list(range(1, 13))

def seasonal(base, month, summer_peak=0.15, noise=0.05):
    """Monthly value with sinusoidal seasonality (peak July) and noise."""
    s = 1 + summer_peak * math.sin((month - 4) / 12 * 2 * math.pi)
    return base * s * (1 + random.uniform(-noise, noise))

def winter(base, month, winter_peak=0.5, noise=0.06):
    """Monthly value peaking in winter (heating loads)."""
    s = 1 + winter_peak * math.cos((month - 1) / 12 * 2 * math.pi)
    return base * s * (1 + random.uniform(-noise, noise))

# ---------------------------------------------------------------- master list
FACILITIES = [
    # id, name, division, city, state, ownership, sqft, status
    ("RBC-01", "Portland Bottling Plant",   "Riverbend Bottling Co.", "Portland",    "OR", "Owned",  412000, "Operating"),
    ("RBC-02", "Sacramento Bottling Plant", "Riverbend Bottling Co.", "Sacramento",  "CA", "Owned",  355000, "Operating"),
    ("RBC-03", "Boise Bottling Plant",      "Riverbend Bottling Co.", "Boise",       "ID", "Owned",  248000, "Operating"),
    ("RBC-04", "Spokane Canning Plant",     "Riverbend Bottling Co.", "Spokane",     "WA", "Owned",  221000, "Operating"),
    ("RBC-05", "Reno Bottling Plant",       "Riverbend Bottling Co.", "Reno",        "NV", "Owned",  198000, "Operating"),
    # FLAW 2a: RBC-06 Medford appears in the energy CSV (Jan-Aug) but NOT here (sold Aug 2025, master updated, energy file not)
    ("HWB-01", "Bend Brewery & Bottling",   "Headwater Brands",       "Bend",        "OR", "Owned",  132000, "Operating"),
    ("HWB-02", "Fort Collins Plant",        "Headwater Brands",       "Fort Collins","CO", "Owned",  118000, "Operating"),
    ("HWB-03", "Salt Lake City Plant",      "Headwater Brands",       "Salt Lake City","UT","Owned", 104000, "Operating"),
    ("RPS-01", "Tacoma Glass Plant",        "Riverbend Packaging Solutions", "Tacoma",   "WA", "Owned", 389000, "Operating"),
    ("RPS-02", "Fresno Can Sheet Plant",    "Riverbend Packaging Solutions", "Fresno",   "CA", "Owned", 301000, "Operating"),
    ("RPS-03", "Salem Corrugated Plant",    "Riverbend Packaging Solutions", "Salem",    "OR", "Owned", 264000, "Operating"),
    ("RPS-04", "Vancouver PET Preform Plant","Riverbend Packaging Solutions","Vancouver","WA", "Owned", 176000, "Operating"),
    # FLAW 2b: RPS-05 exists here, marked Operating, but has zero rows in the energy CSV
    ("RPS-05", "Boise Can Sheet Plant",     "Riverbend Packaging Solutions", "Boise",   "ID", "Owned", 155000, "Operating"),
    ("CDL-01", "Portland Distribution Center",   "Coldstream Distribution & Logistics", "Portland",   "OR", "Owned", 285000, "Operating"),
    ("CDL-02", "Sacramento Distribution Center", "Coldstream Distribution & Logistics", "Sacramento", "CA", "Owned", 240000, "Operating"),
    ("CDL-03", "Seattle Distribution Center",    "Coldstream Distribution & Logistics", "Seattle",    "WA", "Owned", 262000, "Operating"),
    ("CDL-04", "Denver Distribution Center",     "Coldstream Distribution & Logistics", "Denver",     "CO", "Owned", 214000, "Operating"),
    ("CDL-05", "Phoenix Distribution Center",    "Coldstream Distribution & Logistics", "Phoenix",    "AZ", "Owned", 231000, "Operating"),
    ("COR-01", "Corporate Headquarters",    "Corporate", "Portland",  "OR", "Owned",   88000, "Operating"),
    ("COR-02", "R&D and Pilot Lab",         "Corporate", "Hillsboro", "OR", "Owned",   31000, "Operating"),
    # FLAW 10: leased offices in scope question — no energy data anywhere
    ("COR-03", "Chicago Sales Office",      "Corporate", "Chicago",   "IL", "Leased",   9500, "Operating"),
    ("COR-04", "Dallas Sales Office",       "Corporate", "Dallas",    "TX", "Leased",   7200, "Operating"),
    ("COR-05", "Atlanta Sales Office",      "Corporate", "Atlanta",   "GA", "Leased",   6800, "Operating"),
]

with open(os.path.join(ROOT, "facility-master-list.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["facility_id","facility_name","division","city","state","ownership","floor_area_sqft","status"])
    w.writerows(FACILITIES)

# ------------------------------------------------------- energy consumption
# (elec base kWh/mo, gas base therms/mo). HWB excluded — separate Headwater export.
ENERGY_SITES = {
    "RBC-01": (392000, 14500), "RBC-02": (341000, 11200), "RBC-03": (236000,  9800),
    "RBC-04": (208000,  8900), "RBC-05": (191000,  7600),
    "RBC-06": (118000,  5200),   # FLAW 2a: Medford — sold Aug 2025, not in master list
    "RPS-01": (415000, 104000),  # glass furnace: gas-dominated
    "RPS-02": (524000,  6100), "RPS-03": (183000, 21500), "RPS-04": (352000,  2100),
    "CDL-01": (168000,  2400), "CDL-02": (172000,  1900), "CDL-03": (159000,  2200),
    "CDL-04": (144000,  3800), "CDL-05": (258000,   900),
    "COR-01": ( 38000,  1600), "COR-02": ( 22000,   420),
}

rows = []
for fid, (eb, gb) in ENERGY_SITES.items():
    for m in MONTHS:
        if fid == "RBC-06" and m > 8:      # sold — data simply stops
            continue
        if fid == "RBC-04" and m in (3, 4, 5):   # FLAW 4: missing months, Mar-May
            continue
        e = round(seasonal(eb, m, summer_peak=0.22 if fid.startswith("CDL") else 0.12))
        g = round(winter(gb, m, winter_peak=0.10 if fid == "RPS-01" else 0.55))
        if fid == "RPS-01" and m == 7:
            e = e * 10                      # FLAW 6: extra digit, July electricity
        if fid == "RBC-01" and m == 3:
            e = 246800                      # FLAW 9: bill says 268,400 (transposition)
        rows.append([fid, f"2025-{m:02d}", "Electricity", e, "kWh"])
        rows.append([fid, f"2025-{m:02d}", "Natural Gas", g, "therms"])
        if fid == "RBC-01" and m == 10:     # FLAW 3: October re-submitted (portal migration)
            rows.append([fid, f"2025-{m:02d}", "Electricity", e, "kWh"])
            rows.append([fid, f"2025-{m:02d}", "Natural Gas", g, "therms"])

with open(os.path.join(ROOT, "energy-consumption-2025.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["facility_id","month","energy_type","consumption","unit"])
    w.writerows(rows)

# ---------------------------------------------------- Headwater export (CSV here; converted to xlsx separately)
# FLAW 1: HWB-01 electricity values are MWh though the column header says kWh
# FLAW 5: HWB-02 reports natural gas despite questionnaire claiming all-electric
HWB = {
    "HWB-01": (312, 4100, "MWH_AS_KWH"),   # values ~312 in a kWh-labeled column
    "HWB-02": (238000, 3800, "OK"),
    "HWB-03": (187000, 5100, "OK"),
}
hwb_rows = []
for fid, (eb, gb, mode) in HWB.items():
    for m in MONTHS:
        e = seasonal(eb, m, summer_peak=0.10)
        e = round(e, 1) if mode == "MWH_AS_KWH" else round(e)
        g = round(winter(gb, m))
        hwb_rows.append([fid, f"{m:02d}/2025", "ELEC", e, "kWh"])
        hwb_rows.append([fid, f"{m:02d}/2025", "NATGAS", g, "therms"])

with open(os.path.join(ROOT, "headwater-brands-energy-2025.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["SITE","PERIOD","COMMODITY","QTY","UOM"])   # note: different schema than corporate file
    w.writerows(hwb_rows)

# ------------------------------------------------------------- fleet export
# FLAW 8: FUEL_GAL column actually contains LITERS (plausibility check: L/100km ~ 32-38 for tractors)
FLEET = [
    ("TRACTOR",      62, 11800, 35.0),  # class, count, km/veh/mo, L/100km
    ("STRAIGHT_TRK", 88,  3400, 24.0),
    ("REEFER_TRL",  115,     0,  0.0),  # reefer diesel burn tracked (poorly) below
    ("YARD_SWITCH",   9,   600, 55.0),
]
fleet_rows = []
for m in MONTHS:
    for cls, cnt, km, lper in FLEET:
        if cls == "REEFER_TRL":
            fuel = round(cnt * seasonal(410, m, summer_peak=0.35))  # liters, cooling peaks in summer
            kms = 0
        else:
            kms = round(cnt * seasonal(km, m, summer_peak=0.08))
            fuel = round(kms * lper / 100)
        fleet_rows.append([f"2025-{m:02d}", cls, cnt, kms, fuel])

with open(os.path.join(ROOT, "fleet-fuel-export-2025.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["RPT_PD","VEH_CLS","VEH_CNT","ODO_KM","FUEL_GAL"])  # FUEL_GAL is actually liters
    w.writerows(fleet_rows)

# --------------------------------------------------------- supplier spend
SUPPLIERS = [
    ("Western Cane & Sweetener Corp",   "Cane sugar",              41.2),
    ("AgriSweet Processing LLC",        "High-fructose corn syrup",28.7),
    ("Cascade Malting Co.",             "Malted barley",            6.2),   # FLAW 12a
    ("Cascade Malting Company LLC",     "Brewing malts",            3.9),   # FLAW 12b: same supplier
    ("Valley Sun Fruit Concentrates",   "Fruit concentrate",       19.4),
    ("Pacific Citrus Cooperative",      "Citrus concentrate",      11.8),
    ("Alumax Rolling Products",         "Aluminum can sheet",      52.6),
    ("CanWest Container Corp",          "Finished aluminum cans",  33.1),
    ("Northwest Cullet Supply",         "Recycled glass cullet",    7.3),
    ("SilicaSource Minerals",           "Glass raw materials",      9.1),
    ("PolyOne Pacific Resins",          "PET resin",               24.9),
    ("Evergreen Corrugated Supply",     "Corrugate & board",       13.5),
    ("Summit Industrial Gases",         "Beverage-grade CO2",       8.8),
    ("Cap & Closure Industries",        "Caps and closures",        6.7),
    ("FlavorCraft Botanicals",          "Flavors & extracts",      12.2),
    ("Rainier Refrigeration Services",  "Refrigeration maintenance",2.1),
    ("Cascade Mechanical Contractors",  "HVAC & chiller service",   1.8),
    ("Interstate Freight Partners",     "Contract freight (dry)",  17.6),
    ("ColdLink Carriers Inc",           "Contract freight (reefer)",14.3),
    ("Pacific Pallet Pool",             "Pallets & returnables",    3.4),
    ("LabelWorks Printing",             "Labels & shrink sleeves",  5.9),
    ("AquaPure Treatment Systems",      "Water treatment chemicals",2.6),
    ("Pacific Power Solutions",         "Electrical contracting",   1.4),
    ("Bighorn Cleaning Systems",        "CIP & sanitation chemicals",4.8),
    ("TruckPro Fleet Services",         "Fleet maintenance",        5.2),
]
# pad to top-50 with plausible tail suppliers
TAIL_CATS = ["MRO supplies","IT services","Packaging film","Lab services","Uniforms & PPE",
             "Waste hauling","Security services","Staffing services","Marketing services",
             "Equipment leasing","Insurance services","Travel services","Facilities services",
             "Consulting services","Telecom","Office supplies","Landscaping","Catering",
             "Legal services","Training services","Printing services","Sensors & controls",
             "Spare parts","Safety equipment","Calibration services"]
TAIL_NAMES = ["Meridian","Bluepine","Stonegate","Larkspur","Redpoint","Silverbow","Kestrel",
              "Foxglove","Ironwood","Clearwater","Sagebrush","Timberline","Westgate","Nighthawk",
              "Goldbeam","Riverstone","Bridgeport","Halcyon","Juniper","Madrona","Obsidian",
              "Pinnacle","Quartzite","Sundown","Tamarack"]
for i, cat in enumerate(TAIL_CATS):
    SUPPLIERS.append((f"{TAIL_NAMES[i]} {cat.split()[0].title()} Co.", cat, round(random.uniform(0.4, 1.9), 1)))

with open(os.path.join(ROOT, "supplier-spend-top50.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["supplier_name","category","spend_2025_usd_m"])
    for name, cat, spend in sorted(SUPPLIERS, key=lambda x: -x[2])[:50]:
        w.writerow([name, cat, spend])

# --------------------------------------------- revenue & headcount (FLAW 13: fiscal year)
with open(os.path.join(ROOT, "revenue-headcount-by-division.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["division","revenue_fy2025_usd_m","avg_headcount_fy2025"])
    f.write("# Fiscal year: 1 July 2024 - 30 June 2025 (Riverbend FY basis)\n")
    for div, rev, hc in [
        ("Riverbend Bottling Co.", 571, 2180),
        ("Headwater Brands", 198, 640),
        ("Riverbend Packaging Solutions", 209, 1120),
        ("Coldstream Distribution & Logistics", 121, 760),
        ("Corporate", 0, 115),
    ]:
        w.writerow([div, rev, hc])

print("Sandbox data generated into", os.path.normpath(ROOT))
