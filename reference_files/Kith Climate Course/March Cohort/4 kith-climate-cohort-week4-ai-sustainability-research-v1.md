# AI's Environmental Footprint: Research Reference

**For:** Kith Climate Cohort | **Audience:** Sustainability professionals
**Series:** Sustainability Professional Series — Session 1
**Version:** 2.0
**Date:** April 2026

This document consolidates the research base for the AI Environmental Footprint presentation and mini-curriculum. It draws on three source documents: the presentation brief (v3), the four-session curriculum, and Watershed's *AI Emissions: A Practical Guide for Corporate Sustainability Leaders* (2025). All claims are sourced; where sources disagree, both figures are presented with context.

*v2.0 update:* Added Section 13 — Slide-by-Slide Source Map, mapping every factual claim in the v4 presentation to its source.

---

## 1. The AI Lifecycle: A Whole-Life Carbon Assessment

AI's environmental footprint spans six stages, mirroring the whole-life carbon assessment framework used in the built environment. The first five are directly measurable (with varying difficulty); the sixth is systemic and largely unquantified.

### 1.1 Raw material extraction

The hardware that powers AI depends on mining and refining operations concentrated in a small number of countries:

- **Silicon** — the base substrate for all semiconductor wafers
- **Rare earth elements** — used in magnets, polishing compounds, and electronic components. China refines approximately 90% of rare earths globally and leads in refining 19 of 20 key energy-related minerals
- **Gallium** — 95% sourced from China; critical for compound semiconductors
- **Germanium** — used in infrared optics and high-frequency electronics
- **Cobalt and copper** — cobalt for energy storage, copper for heatsinks, wiring, and interconnects
- **Tantalum** — used in capacitors within server power supplies

Both CO2 emissions and water consumption are implicated at the extraction stage, though this is the least-quantified part of the AI lifecycle in current literature.

### 1.2 Chip fabrication

Semiconductor fabrication is the most data-rich stage of embodied emissions. Key figures:

| Metric | Figure | Source |
|--------|--------|--------|
| Energy per 300mm wafer | >800 kWh (EUV lithography alone ~300 kWh) | ASML, 2023 |
| 3nm vs 5nm energy increase | +18% electricity per wafer | TSMC |
| Good GPU dies per wafer | 28-65 (H100, ~814 mm2 die size) | Industry estimates |
| Wafer cost (3nm node) | ~$18,000-$20,000 per wafer | Tom's Hardware / analysts |
| TSMC total electricity (2024) | 25.55 billion kWh | TSMC |
| TSMC share of Taiwan grid | 8.9% (2023), projected 24% by 2030 | CommonWealth Magazine |
| Taiwan grid carbon intensity | ~474 g CO2/kWh | Taiwan MOEA, 2024 |
| Ultrapure water per 300mm wafer | ~5,700 litres | IDTechEx |
| City water needed to produce UPW | 6,000 litres per 3,800 litres of UPW (37% waste) | IDTechEx |
| TSMC total water (2023) | 101 billion litres | TSMC |

**Fluorinated process gases** are a major but often overlooked emissions source. These gases are used in etching and chamber cleaning and have extreme global warming potentials:

| Gas | GWP (100-year) | Atmospheric lifetime |
|-----|---------------|---------------------|
| CF4 | 6,630x CO2 | ~50,000 years |
| NF3 | 16,100x CO2 | 500 years |
| SF6 | 23,500x CO2 | 3,200 years |

These account for 80-90% of direct fab emissions. The semiconductor sector produces over 15 Mt CO2 annually, expected to double by 2030.

### 1.3 Data centre construction

Data centres are industrial facilities with embodied carbon profiles significantly exceeding conventional commercial buildings:

- Up to **4,500 t CO2e per MW** of IT capacity
- **5x the embodied carbon** of an office building per m2 (8,000-10,000 kg CO2e/m2 vs ~1,300 for office)
- Concrete accounts for up to 80% of building embodied carbon
- **Scope 3 accounts for 38-69%** of total lifetime emissions (Schneider Electric White Paper 99)
- Microsoft reports Scope 3 = 97% of total footprint; its mass timber approach cuts embodied carbon by 65%
- AWS has built 43 data centres with lower-carbon concrete/steel (doubled from 2022), achieving ~30% embodied carbon reduction vs benchmarks

**Scale of construction:** The largest data centres now average 224 acres per site — a 144% increase since 2022. Hyperscaler capex is projected at $736 billion for 2025-2026.

### 1.4 Model training

Training is a one-time but massive GPU compute event per model version. The energy cost depends entirely on grid carbon intensity at the time and location of training. See Section 4 for detailed training energy data by model.

### 1.5 Inference (every query)

Inference — the process of running a trained model to answer queries — is continuous, cumulative, and now the dominant share of AI's total energy spend. See Section 3 for the training-to-inference shift and Section 5 for per-query data.

### 1.6 System-level effects

The downstream consequences of AI deployment represent the largest potential impact — positive or negative — but are the least studied and most difficult to quantify.

**The Kaack framework (Nature Climate Change, 2022):**

Kaack et al. established the three-tier framework now cited by IPCC AR6 WGIII:

1. **Direct effects** — energy and carbon of compute itself (Stages 1-5 above)
2. **Indirect effects** — application-level changes. AI optimising an energy grid = positive indirect effect. AI optimising oil extraction = negative indirect effect
3. **System-level effects** — rebound, structural change, lock-in, behavioural shifts. The largest in magnitude but least studied

**Estimates of AI-enabled emissions reductions:**

- IEA estimates AI-enabled emissions reductions could reach **1,400 Mt CO2 by 2035** — 3x larger than total data centre emissions — but notes "there is currently no momentum" ensuring this happens
- BCG/Google (2023-2024) estimates AI could help reduce **5-10% of global GHG emissions** (2.6-5.3 Gt CO2e annually). Highest potential sectors: energy/power (15-20%), buildings (10-20%), transport (10-15%)

**Rebound effects:**

- Luccioni (FAccT 2025) published a Jevons' Paradox framework identifying 7 types of rebound effects specific to AI
- Energy economics literature estimates rebound effects of **20-60%** for efficiency improvements. For transformative general-purpose technologies, some studies suggest backfire (>100% rebound) is possible
- The Watershed guide frames this as the core climate risk: "The climate risk is not per-query emissions. It's system-wide energy growth outpacing clean supply"

**Accounting gap:** No established methodology exists for net assessment. The GHG Protocol has no "Scope 4." SBTi explicitly excludes avoided emissions from targets (BVCM is supplementary only).

**The provocation:** The carbon footprint of an AI model is not its electricity bill — it is what the model makes happen in the world.

---

## 2. Embodied Emissions: The Invisible Carbon Cost

Embodied emissions = all CO2e generated before a model runs a single query. This includes raw material extraction, chip manufacturing, server assembly, and data centre construction.

### 2.1 The emissions split

The Watershed guide provides a high-level breakdown of total AI system lifecycle emissions:

| Component | Share of total | Source |
|-----------|---------------|--------|
| Electricity for GPU operation | 80.9% | Tomlinson et al., 2024 |
| Electricity for data centre overhead | 17.8% | AFL, assuming PUE 1.2 |
| GPU manufacturing | 1.3% | Tomlinson et al., 2024 |

This 80.9% / 17.8% / 1.3% split represents the full lifecycle including inference. The embodied share appears small because inference dominates at scale. However, at the individual model level (particularly for models on clean grids), embodied emissions can be 22-35% of total lifecycle impact.

The Luccioni et al. BLOOM study (2023, JMLR) found embodied carbon accounted for approximately **22% of BLOOM's total lifecycle footprint** — 11.2 tonnes CO2e from hardware alone. This high share was precisely because BLOOM trained on France's largely nuclear grid (~57 g CO2/kWh). A model running on a coal-heavy grid would show embodied emissions as a smaller share simply because operational emissions are so large. This is the **clean grid paradox** — identical to the phenomenon in buildings where a highly insulated low-energy building still carries significant embodied carbon from its materials.

### 2.2 NVIDIA H100 — the first vendor-level product carbon footprint

NVIDIA published the first vendor-level Product Carbon Footprint (PCF) for the HGX H100 baseboard in 2025:

- **Total:** 1,312 kg CO2e per 8-GPU baseboard (cradle-to-gate)
- **Per card:** ~164 kg CO2e per individual H100 SXM card

**Component breakdown:**

| Component | Share | Estimated kg CO2e |
|-----------|-------|-------------------|
| HBM Memory | 42% | ~551 |
| GPU dies (integrated circuits) | 25% | ~328 |
| Thermal components | 18% | ~236 |
| Electromechanical + PCB + other | 15% | ~197 |

**Lifecycle phase:** Materials & components 91%, assembly 8.6%, transportation 0.4%

**B200 generation:** 24% lower carbon intensity per exaflop vs H100. Each new GPU generation shows roughly 3x improvement in carbon efficiency per compute unit (confirmed by Google TPU data: v4i to v6e showed 3x CCI improvement).

Sources: NVIDIA HGX H100 PCF Summary, 2025; NVIDIA HGX B200 PCF Summary, 2025

### 2.3 Why HBM memory dominates (42%)

High Bandwidth Memory is the single largest contributor to GPU embodied carbon because of its extreme manufacturing complexity:

- Manufacturing requires ~19 additional materials engineering steps beyond conventional DRAM
- Through-silicon vias (TSVs) require etching, deposition, plating, grinding, and bonding
- HBM3 stacks 8 DRAM dies; HBM3e stacks 8-12 dies. A defect in any layer can waste the entire stack
- Each HBM stack requires multiple full wafer processes
- The H100 has 80 GB of HBM3 across 5 stacks; H200 increases to 141 GB (6 stacks)
- **Scaling concern:** As models demand more memory, HBM's share of embodied carbon will grow

### 2.4 Additional hardware embodied emissions data

| Hardware | Embodied CO2e | Notes | Source |
|----------|--------------|-------|--------|
| NVIDIA A100 GPU | 141 kg per card (cradle-to-grave) | GPU chip alone: 81.8% of manufacturing climate impact. Copper heatsink: 3.8% of climate impact but 91% of human toxicity (cancer) | Falk et al., 2025 |
| Google TPU v5p machine | 2,277 kg total | Accelerator tray + host tray + transport | Google, 2025 |
| Standard enterprise server | ~922 kg per unit | | Industry data |
| Industry GPU lifetime assumption | 3-5 years | AWS uses 6-year amortisation | Various |

Google TPU data shows manufacturing + construction = ~30% of lifecycle emissions (market-based); operational = ~70%. With 90% clean energy, manufacturing becomes a larger share — another manifestation of the clean grid paradox.

### 2.5 The built environment parallel

| Built environment concept | AI equivalent |
|---------------------------|---------------|
| Embodied carbon in materials | Chip fabrication + data centre construction |
| Operational energy in use | Inference energy per query |
| Whole-life carbon assessment | LCA across training, deployment, hardware EOL |
| Energy Performance Certificate | AI energy label (proposed by Luccioni, Nature 2024) |
| Grid carbon intensity | Data centre location and PPA coverage |

---

## 3. The Training-to-Inference Shift

### 3.1 The story in three moments

- **Pre-2022:** Training dominates the research discussion. Models trained infrequently by a small number of labs. Inference costs negligible relative to training
- **2022-2023:** ChatGPT launches (November 2022). Inference scales to millions of users. Cumulative inference cost begins to rival training costs
- **2024-present:** Inference accounts for 60-70% of total AI electricity (IEA, 2025). Some providers report inference at >90% of their AI energy spend (AWS, 2024). Training remains large but is amortised across billions of queries

### 3.2 The data

**IEA (2025):**
- Inference = 60-70% of total AI electricity consumption as of 2024
- Projected to reach approximately two-thirds by 2026

**Watershed guide:**
- Inference accounts for >90% of total lifecycle emissions of an AI system (citing Tomlinson et al., 2024; Niu et al., 2025; Jegham et al., 2025)
- "Training happens once; inference happens constantly. Over a model's lifetime, less than 10% of emissions come from training"

**Note on the discrepancy:** The IEA figure (60-70%) measures electricity allocation across the AI sector at a point in time (including new models still in training). The Watershed/Tomlinson figure (>90%) measures a single model's lifetime emissions allocation. Both can be true simultaneously — the difference is boundary and timeframe.

### 3.3 Scale of inference

ChatGPT alone processes roughly **2.5 billion queries per day** (Watershed guide, 2025). This volume is why cumulative inference emissions dwarf training, even though individual queries are small.

**Implication for participants:** Every query run in the course of professional work is now the live, ongoing contribution to AI's carbon footprint. Training happened once. Inference is continuous, and every user is part of it.

---

## 4. Training Energy by Model

### 4.1 Historical training costs

| Model | Year | Parameters | Architecture | Training energy (est.) | CO2e (est.) | Notes |
|-------|------|-----------|-------------|----------------------|-------------|-------|
| BERT-base | 2018 | 110M | Dense | ~1.5 MWh | ~0.6 t | Strubell et al. |
| GPT-2 | 2019 | 1.5B | Dense | ~27 MWh | ~13 t | Patterson et al. |
| T5-11B | 2019 | 11B | Dense | ~86 MWh | ~47 t | Google; Patterson et al. |
| GPT-3 | 2020 | 175B | Dense | ~1,300 MWh | ~552 t | Patterson et al. |
| OPT-175B | 2022 | 175B | Dense | ~324 MWh | ~75 t | Meta; ~992 MWh incl. experiments |
| BLOOM 176B | 2022 | 176B | Dense | ~433 MWh | ~25 t | French nuclear grid (~57 g/kWh). Lifecycle incl. hardware: ~50 t |
| Stable Diffusion v1 | 2022 | -- | Diffusion | ~150 MWh | ~15 t | Luccioni et al.; ~150k A100-hours |
| Llama 2 7B | 2023 | 7B | Dense | ~184 MWh | ~31 t | Meta model card |
| Llama 2 70B | 2023 | 70B | Dense | ~1,720 MWh | ~291 t | Meta; total Llama 2 family: ~539 t |
| GPT-4 (est.) | 2023 | ~1.8T (MoE?) | MoE (est.) | ~50,000-62,000 MWh | Not disclosed | Epoch AI triangulations |
| Llama 3 8B | 2024 | 8B | Dense | ~1,300 MWh | ~390 t | Meta; 1.3M GPU-hours on H100 |
| Llama 3 70B | 2024 | 70B | Dense | ~6,400 MWh | ~1,920 t | Meta; 6.4M GPU-hours on H100 |
| Llama 3.1 405B | 2024 | 405B | Dense | ~27,500 MWh | ~11,390 t | Meta; 30.84M GPU-hours on H100 |
| DeepSeek-V3 | 2024 | 671B (37B active) | MoE | ~5,543 MWh | Not disclosed | 2.788M H800 GPU-hours. Claimed ~$5.6M training cost |

### 4.2 The transparency gap

Anthropic (Claude) and Google (Gemini) have published **no training energy or emissions figures** for any model. No credible third-party estimates exist either, because neither company discloses parameter counts, training hardware, token counts, or duration. Mistral, Qwen, and Yi are similarly undisclosed.

### 4.3 Key trend

Training compute has been growing at roughly **4-5x per year** (Epoch AI), far faster than hardware efficiency improvements (~2x per 2-3 years). Absolute training energy has been growing rapidly despite per-FLOP efficiency gains.

---

## 5. Inference Energy and Per-Query Emissions

### 5.1 Task type matters more than model size

From "Power Hungry Processing" (Luccioni, Jernite & Strubell, FAccT 2024), testing 88 models across 10 tasks on consistent hardware (single A100, CodeCarbon):

| Task type | Avg energy (Wh/inference) | Relative cost |
|-----------|--------------------------|---------------|
| Text classification | 0.002 | 1x (baseline) |
| Token classification / NER | 0.003 | 1.5x |
| Extractive QA | 0.005 | 2.5x |
| Image classification | 0.007 | 3.5x |
| Object detection | 0.04 | 20x |
| Text generation | 0.047 | 24x |
| Summarisation | 0.049 | 25x |
| Image captioning | 0.05 | 25x |
| Image generation | 2.907 | 1,450x |

**What you ask the model to do matters as much as which model you use.** Within text generation alone, model size creates a further ~10-100x variation (125M params: ~2 Wh/1k queries to 175B params: ~50-200 Wh/1k queries). Combined, the cheapest operation vs most expensive can differ by **1,000x or more**.

### 5.2 Per-query energy figures (2024-2025)

| Model | Type | Energy (Wh/query) | CO2e (g/query) | Source | Date |
|-------|------|-------------------|----------------|--------|------|
| GPT-4o (typical) | Closed | ~0.3 | ~0.13 | Epoch AI | 2025 |
| ChatGPT (average) | Closed | ~0.34 | ~0.15 | OpenAI (Altman) | Jun 2025 |
| Google Gemini (median text) | Closed | ~0.24 | ~0.03* | Google | Aug 2025 |
| Claude 3 Haiku | Closed | ~0.22 | ~0.10 | Hannah Ritchie | 2025 |
| Claude 3 Sonnet | Closed | ~0.5-1.5 | ~0.25-0.75 | EcoLogits (est.) | 2025 |
| Claude 3 Opus | Closed | ~4.05 | ~1.80 | Hannah Ritchie | 2025 |
| Mistral 7B (self-hosted) | Open | ~0.05-0.15 | ~0.025-0.075 | EcoLogits (est.) | 2025 |
| Llama 3 70B (self-hosted) | Open | ~0.4-1.0 | ~0.2-0.5 | EcoLogits (est.) | 2025 |
| GPT-3.5 Turbo | Closed | ~0.3-0.5 | ~0.15-0.25 | EcoLogits (est.) | 2024 |
| GPT-4 | Closed | ~3.0-7.0 | ~1.5-3.5 | EcoLogits (est.) | 2024 |
| o3 / DeepSeek-R1 (long prompt) | Reasoning | >33 | varies | "How Hungry is AI?" | May 2025 |
| GPT-5 (medium prompt) | Reasoning | ~18.9 avg | varies | Univ. of Rhode Island | Aug 2025 |

\* Google's very low-carbon grid drives the low CO2e figure.

**Watershed's figure:** A single LLM query uses approximately 0.24 Wh of electricity, translating to roughly 0.1-0.3 g CO2e per query on the average US grid. A heavy user running 100 queries per day generates about 3 kg CO2e per year — less than the emissions from half a kilogram of beef.

**The widely cited "10x a Google search" figure** (2.9 Wh per ChatGPT query, from EPRI/IEA) is now considered an overestimate for standard text queries on current models. Epoch AI and OpenAI's own figures converge around 0.3-0.34 Wh for a typical GPT-4o query. However, reasoning models (o3, GPT-5) can consume 10-100x more than this baseline, creating an enormous range.

### 5.3 Why estimates vary by ~200x across studies

- **Methodology:** Inference-only vs lifecycle including amortised training and embodied hardware
- **Model version:** GPT-3.5 vs GPT-4o vs GPT-5
- **Query complexity:** Short classification vs long reasoning chain
- **Grid carbon intensity:** Google's clean grid vs global average
- **PUE assumptions:** 1.1-1.2 for hyperscalers vs 1.5-2.0 for enterprise

### 5.4 Reasoning models: a new energy tier

Reasoning models (o1, o3, DeepSeek-R1) generate 5-50x more tokens internally via chain-of-thought before producing the final answer:

- o3 / DeepSeek-R1 on long prompts: **>33 Wh per query** — 70x more than GPT-4.1 nano (0.42 Wh)
- o3 "high compute" setting: up to **100x the compute** of a standard GPT-4 query on hard problems
- GPT-5 on medium prompts: ~18.9 Wh average
- Chain-of-thought prompting increases output tokens by 2-10x, proportionally increasing energy. The key cost driver is **output tokens**, not input

### 5.5 Open source vs closed: efficiency implications

- For equivalent capability, API inference from a major cloud provider is generally **more energy-efficient** than self-hosting (better utilisation, batching, PUE 1.1-1.2 vs typical 1.5-2.0)
- However, the biggest energy win comes from **using a smaller model sufficient for the task** — easier with open-source models
- A 4-bit quantised Llama 70B uses roughly the same energy as a full-precision 13-20B model
- Quantisation savings: INT8 = ~30-50% energy reduction; INT4 = ~50-70% energy reduction; minimal quality loss (<1-3% accuracy)

---

## 6. Efficiency Gains and Counter-Narratives

### 6.1 Per-query efficiency is improving rapidly

- Google reported a **33x reduction** in energy per Gemini prompt within a single year (combination of TPU improvements, software, and algorithmic advances)
- Google also reports a **44x carbon reduction** per Gemini prompt in the same period
- Algorithmic efficiency has been **halving compute requirements every 16 months** for a given benchmark (Hernandez & Brown, 2020; Epoch AI confirms this continues)
- "Model efficiency improvements are the single most important thing you can do to reduce the environmental costs of AI" — Neil Thompson, MIT, 2025

### 6.2 2025 vs 2020 for the same task

For a standardised task (~200 token factual response):

| Model (Year) | Approx energy/query | Relative efficiency |
|-------------|--------------------|--------------------|
| GPT-3 (2020) | ~3-5 Wh | 1x (baseline) |
| GPT-3.5 Turbo (2022) | ~0.4-0.7 Wh | ~5-10x more efficient |
| GPT-4o-mini (2024) | ~0.2-0.5 Wh | ~8-15x more efficient |
| Llama 3 8B Q4 (2024) | ~0.1-0.3 Wh | ~15-30x more efficient |
| Phi-3-mini (2024) | ~0.05-0.15 Wh | ~30-60x more efficient |

For equivalent quality on simple tasks, 2024/2025 models are roughly **10-30x more efficient** than 2020-era models.

### 6.3 Mixture-of-Experts (MoE) — structural efficiency

| Architecture | Total params | Active params/token | Inference cost vs dense equivalent |
|-------------|-------------|--------------------|------------------------------------|
| Dense 70B | 70B | 70B | 1x |
| Mixtral 8x7B | 46.7B | ~13B | ~0.2-0.3x of dense 46.7B |
| DeepSeek-V2 | 236B | 21B | ~0.1x of dense 236B |
| DeepSeek-V3 | 671B | 37B | ~0.05x of dense 671B |
| GPT-4 (est.) | ~1.8T | ~220B | ~0.12x of hypothetical dense 1.8T |

MoE routes each token to only a subset of "expert" networks. DeepSeek-V3 reportedly trained for ~$5.6M in compute — roughly 10-20x cheaper than estimated GPT-4 training costs.

### 6.4 Post-Chinchilla training strategy

Industry now "over-trains" small models on far more data than compute-optimal, specifically to maximise inference efficiency. Llama 3 8B was trained on 15T tokens (far above Chinchilla-optimal). The logic: spend more at training time to make every inference query cheaper.

### 6.5 The Jevons Paradox problem

Efficiency gains are real, but they drive adoption. This is the central tension:

- As AI gets cheaper and more efficient per query, usage grows — more people, more tasks, more often
- Per-query footprint drops, but aggregate footprint rises
- Data centre electricity is projected to more than double by 2030 even as per-query efficiency improves dramatically
- The Watershed guide frames this directly: "This is the Jevons Paradox in action: Efficiency improvements make something cheaper and more accessible, driving greater adoption — ultimately using more of that resource and overwhelming the rate of efficiency gains"
- Energy economics literature estimates rebound effects of 20-60% for efficiency improvements
- The parallel from climate economics: LED lighting, internal combustion engines, and air travel all followed the same pattern

---

## 7. Water in the AI Lifecycle

### 7.1 Operational cooling water

Data centres use water in cooling towers and chilled water systems, measured as Water Usage Effectiveness (WUE): litres of water per kWh of IT load.

**Key figures:**

- Training GPT-3 consumed approximately **700,000 litres** of water
- Microsoft reported global data centre water consumption rose **34% between 2021 and 2022**
- Google's data centres consumed **~6 billion gallons total** in 2024, up 8% year-on-year. The Council Bluffs, Iowa facility alone consumed **1 billion gallons**
- **78% of Google's data centre water withdrawal** in 2024 was potable (drinking) water
- US data centres consumed **17 billion gallons** of water directly for cooling in 2023, projected to double or quadruple by 2028

**Per-query water estimates (conflicting):**

| Source | Estimate | Notes |
|--------|----------|-------|
| University of California, Riverside | ~519 mL per 100-word prompt | ~1 standard water bottle |
| Google (self-reported) | 0.26 mL per median Gemini text prompt | ~2,000x lower than UCR figure |

The gap between these figures illustrates the transparency challenge. Methodology, boundary conditions, and cooling technology vary enormously.

**Water-stressed locations:** Roughly 40% of US data centres are located in the most water-stressed areas of the country.

### 7.2 Embodied water — chip fabrication

- ~5,700 litres of ultrapure water (UPW) per 300mm wafer
- 6,000 litres of city water required to produce 3,800 litres of UPW (37% waste ratio)
- TSMC total water consumption: **101 billion litres** (2023)
- TSMC missed its 2023 unit water reduction target; unit water consumption **increased 25.2%**
- Taiwan water stress: droughts have directly threatened fab operations
- This water cost is entirely invisible in most AI emissions reporting

**Takeaway:** WUE is the AI equivalent of water intensity metrics sustainability professionals already track in supply chains. It should be demanded from providers the same way.

---

## 8. Global AI Energy Demand: Scale and Trajectory

### 8.1 Current state (2024)

- Global data centres consumed **415 TWh** in 2024 (~1.5% of global electricity) — IEA, April 2025
- US data centres: **180 TWh** in 2024 (44% of global total)
- AI servers consumed **23% of total US data centre electricity** in 2024
- AI share of global data centre demand: **14%** (2024) — Goldman Sachs
- For context: 415 TWh is roughly the annual electricity consumption of France

### 8.2 Projections

| Metric | Projection | Source |
|--------|-----------|--------|
| Global DC electricity by 2030 | ~945 TWh (~3% of global electricity) — 2.3x increase | IEA, April 2025 |
| DC electricity growth rate | 15% per year — 4x faster than all other sectors | IEA, 2025 |
| AI-optimised DC demand by 2030 | Quadruples | IEA |
| AI share of US DC electricity by 2028 | 70-80% | US DC Energy Usage Report, 2024 |
| AI share of global DC demand by 2030 | 39% | Goldman Sachs |
| AI-specific DC power demand (2030) | 89.9 GW (from 14 GW in 2025) | McKinsey |
| AI-specific CO2 by 2030 | 24-44 million metric tonnes annually | Cornell University |
| All DC growth CO2 addition | ~220 million tonnes (60% from fossil fuels) | Goldman Sachs, Aug 2025 |
| Combined AI infrastructure spending | $320 billion in 2025 (doubled from $151B in 2023) | Watershed guide |

**Critical note on the Goldman Sachs figure:** The 220 Mt CO2 covers **all data centre growth**, not AI alone. Must be labelled clearly to avoid conflation with the AI-specific Cornell figure.

### 8.3 Energy supply constraints

The Watershed guide highlights a structural mismatch between AI demand growth and clean energy supply:

- **1,891 energy projects (266 GW) were cancelled in 2025** — 93% of cancelled capacity was clean energy
- This is equivalent to scrapping Texas's entire power grid in one year
- Interconnection costs can now reach ~50% of total project cost
- US renewable energy queue times: wind 40 months, solar 34 months, solar+battery 27 months, battery 24 months
- Goldman Sachs projects **60% of new data centre power this decade will come from natural gas**

### 8.4 The major providers (2024-2025 reports)

| Provider | Total GHG | Key trend | Source |
|----------|----------|-----------|--------|
| **Google** | 15.2 Mt (2024). DC emissions -12% YoY (first decrease since 2019). But Scope 3 +22%. DC electricity: 30.8 TWh (doubled since 2020). 66% carbon-free energy (hourly match) | Operational improving, supply chain worsening. Total +51% vs 2019 | Google 2025 Environmental Report |
| **Microsoft** | 14.86 Mt (FY2024). -1.8% YoY (first decrease). Scope 1+2 down 30% vs 2020. But Scope 3 (97% of total) up 26%. Energy use +168% since 2020 | Significant decoupling (energy +168%, emissions +23%) but insufficient for 2030 carbon-negative target | Microsoft 2025 Sustainability Report |
| **Amazon** | 68.25 Mt (2024). +6% YoY. Scope 1 +162% since 2019 (when Climate Pledge announced). 100% renewable energy match (annual PPAs) | Emissions still rising despite 100% renewable claim. Direct emissions tripled in 5 years | Amazon 2024 Sustainability Report |
| **Meta** | 8.2 Mt net (2024). Scope 3 = 99%. Capital goods = 63% of Scope 3. $38-40B capex. 100% clean energy match | Rapidly building AI infrastructure; Scope 3 dominated by construction | Meta 2025 Sustainability Report |

**Market-based vs location-based accounting:** Google highlights a 12% reduction in "data centre energy emissions" via market-based accounting, while actual data centre electricity use rose 27% in a single year. The gap is filled by renewable energy certificate (REC) purchasing. Microsoft's location-based Scope 2 emissions more than doubled even as market-based figures improved. Sustainability professionals should apply the same scrutiny to these claims as they would to any supplier's ESG reporting.

**Renewable energy commitments:**
- **Google:** Pursuing 24/7 carbon-free energy on every grid by 2030. Signed ~8 GW of clean energy contracts in 2024 (a record). Achieves 90% hourly CFE matching at five data centres. Acquired Intersect Power for $4.75 billion (December 2025)
- **Microsoft:** Matched 100% of global electricity consumption with renewable energy by 2025 (confirmed February 2026)
- **Amazon:** World's largest corporate renewable energy purchaser with 20 GW contracted
- **Meta:** Committed to 100% renewable energy for operations

**"Matched" vs "24/7" — the critical distinction:** Traditional annual matching (via PPAs and RECs) does not guarantee hourly carbon-free operations. A data centre can buy wind credits from West Texas to "offset" coal-powered consumption in Virginia. 24/7 CFE measures hourly correlation — ensuring actual clean power is available when and where it is consumed. This distinction is immediately transferable to participants' own clients' renewable energy claims.

---

## 9. Provider Disclosure and Transparency

### 9.1 What providers typically disclose

- **PUE** (Power Usage Effectiveness) — widely reported, but a measure of efficiency not absolute impact
- **Renewable energy percentage** — often via annual PPAs which do not guarantee time-matched clean power
- **Total Scope 1 and 2 emissions** — reported by Google, Microsoft, Amazon in annual sustainability reports

### 9.2 What is rarely or never disclosed

- Per-model or per-query energy consumption
- Inference vs training split of operational emissions
- Water consumption at facility level (improving but inconsistent)
- Embodied emissions from hardware supply chains at model level (Meta omitted them from Llama 2's published figures)
- Carbon intensity of specific data centres used for specific workloads

### 9.3 The closed-model problem

Claude, GPT-4, Gemini, and other frontier proprietary models are black boxes in the research literature. All comparative studies use open-weight models (BLOOM, Llama, etc.) where researchers can directly measure energy.

Anthropic has not disclosed: parameter counts, training hardware, training token counts, or training duration for any Claude model. Google has not published per-model training energy for any Gemini variant. The same is true for most commercial providers.

### 9.4 Available data for measurement

The Watershed guide identifies the most useful data points for corporate AI emissions accounting:

| Data point | Utility for carbon accounting | Availability |
|-----------|-------------------------------|-------------|
| Region / location | Critical — grid carbon intensity varies by region | Mixed |
| Model ID | Critical — different models require very different compute | High |
| Token count (input/output) | Medium-high — good proxy for work performed | High |
| Spend ($) | Low-medium — useful fallback when activity data unavailable | High |
| Latency (duration) | Low — does not reliably reflect actual compute | Low |

### 9.5 Proposed solutions

- Luccioni et al. (Nature, 2024) proposed **mandatory AI energy labels** — analogous to EU appliance energy efficiency ratings
- The European Commission is exploring an AI energy and emissions label
- A review clause in the EU AI Act requires assessment of voluntary environmental codes by August 2028

**Takeaway:** Participants should be asking AI providers the same questions they would ask any supplier in a Scope 3 assessment. The fact that answers are unavailable is itself a material finding.

---

## 10. What Sustainability Professionals Can Do

### 10.1 Individual usage decisions

**The decision hierarchy:**

1. **Do I need AI for this task at all?** — The avoided-use question
2. **What is the smallest adequate model?** — Right-sizing is the most effective individual lever. Haiku vs Opus for a simple task: ~0.22 Wh vs ~4.05 Wh
3. **What type of task am I running?** — 1,450x range from classification to image generation
4. **How am I prompting?** — Shorter, clearer prompts reduce token usage and energy. Avoid "context stuffing" (sending unnecessary documents). Use retrieval tools (RAG) to pull only relevant information before sending to a model
5. **Am I regenerating unnecessarily?** — "Try again" when the output was close multiplies the cost

### 10.2 Organisational levers

- **Cloud region selection:** Grid carbon intensity varies from ~2.2 g CO2/kWh (Norway) to 800-1,000+ g CO2/kWh (coal-heavy grids). Selecting a lower-carbon region can reduce operational AI emissions by **30-80% instantly** (Watershed guide)
- **Provider sustainability criteria in procurement:** Annual vs hourly renewable matching, quality of procurement (PPAs vs unbundled RECs), clean energy investment, carbon removal purchases
- **AI usage policies:** Most companies have AI policies focused on security and data privacy, but almost none include environmental considerations
- **Include AI in carbon inventories:** AI usage is Scope 3 for most organisations. The SCI (Software Carbon Intensity) standard from the Green Software Foundation provides a framework

### 10.3 The proportionality test

- Using AI to identify $2M in energy savings across a building portfolio? High proportionality
- Using AI to reformat a memo that could be done in Word? Low proportionality
- Using AI to build a carbon inventory that would take weeks manually? High proportionality
- Regenerating the same output five times for minor phrasing? Low proportionality

### 10.4 Procurement as climate strategy

The Watershed guide frames procurement as the strongest lever sustainability leaders have. When evaluating AI or cloud providers, focus on three areas:

1. **Infrastructure transparency** — Can the provider disclose region-level emissions factors, market vs location-based Scope 2, and clear methodology?
2. **Clean energy strategy** — Annual vs hourly matching? PPAs vs unbundled RECs?
3. **Long-term climate commitments** — Clean energy procurement, carbon removal purchases, data centre efficiency improvements

---

## 11. Environmental Justice and Social Dimensions

### 11.1 Where data centres get built

- Nearly half of ~700 US data centres reviewed are in census tracts with above-median environmental burdens (air pollution, water pollution, limited park access)
- 40% of US data centres are in the most water-stressed areas
- The largest data centres now average 224 acres per site — a 144% increase since 2022

### 11.2 Community opposition

- More than **$162 billion** in data centre projects were delayed or cancelled between May 2024 and June 2025 due to organised community opposition
- Concerns: water depletion, loss of farmland, backup diesel generator emissions, noise, industrialisation of residential areas
- **80% of Virginia municipalities surveyed** had NDAs with data centre developers — limiting public transparency
- The NAACP has launched a "Stop Dirty Data Centers" campaign

### 11.3 Global distribution

- AI development is concentrated in a handful of wealthy countries. Environmental costs are distributed more broadly
- Content moderation, data labelling, and training data work is disproportionately performed by workers in lower-income countries, often under poor conditions
- Benefits (productivity gains, economic value) accrue primarily to organisations and geographies that can afford the tools

### 11.4 Hardware lifecycle and e-waste

- GPUs running AI workloads at high utilisation survive an estimated 1-3 years
- NVIDIA releases new chips annually, accelerating obsolescence
- AI-related components could contribute **5-16 million additional tons of e-waste** by 2030
- Circular strategies: older GPUs repurposed from training to inference ("value cascade"), but hardware turnover pace is outrunning circular economy efforts

---

## 12. Governance and Regulation

### 12.1 EU AI Act (entered force August 2024)

- Original drafts contained stronger environmental provisions; negotiations weakened them
- Encourages voluntary codes of conduct covering environmental sustainability — does not mandate hard environmental limits
- The AI Office can demand technical documentation on energy consumption from major model providers
- The European Commission is exploring an AI energy and emissions label
- A review clause requires assessment of voluntary environmental codes by August 2028

### 12.2 US — fragmented

- No federal AI environmental regulation
- California's data centre energy/water disclosure bills have largely failed (only a study bill passed)
- California's broader climate disclosure laws (SB 253, SB 261) require large companies to report GHG emissions, which indirectly captures data centre operators
- The regulatory landscape is patchwork — mostly voluntary, mostly absent

### 12.3 The measurement gap

There is no globally accepted standard for measuring AI emissions. Key challenges:

- No agreed unit (per token? per query? per model?)
- Training energy allocation across millions of users
- Embodied carbon from GPUs and data centres
- Limited transparency from model providers

The GHG Protocol does not yet have an AI-specific module. That gap will close. Organisations that develop robust AI emissions accounting methodologies ahead of regulation will be better positioned when mandatory disclosure arrives.

---

## 13. Slide-by-Slide Source Map

This section maps every factual claim in the v4 presentation to its source. Use it to verify claims, trace methodology, or prepare for participant questions. Where sources conflict or figures are estimates, a note is included.

### Slide 2 — AI Lifecycle

- China refines ~90% of rare earths globally → **Source:** IEA, *Critical Minerals Market Review* (2023)
- 800+ kWh per wafer → **Source:** ASML (2023), wafer energy estimates
- 5,700 L ultrapure water per wafer → **Source:** IDTechEx, semiconductor water usage analysis
- 4,500 t CO2e per MW of data centre capacity → **Source:** Schneider Electric White Paper 99 (Data Centre Scope 3)
- 5x the embodied carbon of an equivalent office building → **Source:** Schneider Electric White Paper 99
- Training energy growing 4-5x per year → **Source:** Epoch AI (2025), compute trends analysis
- >90% of model lifetime emissions come from inference → **Source:** Tomlinson et al. (2024); Niu et al. (2025); Jegham et al. (2025). *Note: the exact split varies by model size and deployment scale, but all three studies converge on inference dominance.*
- Kaack et al. system-level framework for AI climate impacts → **Source:** Kaack et al., *Nature Climate Change* (2022)

### Slide 3 — Embodied Emissions

- H100: 1,312 kg CO2e per 8-GPU baseboard → **Source:** NVIDIA HGX H100 Product Carbon Footprint Summary (2025)
- HBM 42%, Processor 25%, Thermal 18%, Other 15% → **Source:** NVIDIA HGX H100 PCF Summary (2025)
- B200: 24% lower embodied carbon per exaflop → **Source:** NVIDIA HGX B200 PCF Summary (2025)
- ~3x generational improvement in embodied carbon per unit compute → **Source:** NVIDIA PCF Summaries (H100 + B200) combined with Google TPU Life-Cycle Emissions LCA (2025). *Note: the 3x figure is a cross-vendor approximation; exact ratios depend on workload and comparison baseline.*
- 28-65 dies per wafer → **Source:** Industry estimates. *Note: varies by die size, process node, and yield; no single canonical source.*
- SF6 has 23,500x GWP; NF3 has 16,100x GWP → **Source:** IPCC AR5/AR6
- 80-90% of direct fab emissions come from process gases → **Source:** Semiconductor industry reports (aggregated). *Note: exact percentage varies by fab and process node.*
- Data centre Scope 3 represents 38-69% of total lifecycle emissions → **Source:** Schneider Electric White Paper 99
- AWS achieved 30% reduction in embodied emissions → **Source:** Amazon 2024 Sustainability Report
- 224 acre average data centre land footprint, up 144% → **Source:** World Resources Institute
- BLOOM: 22% of total footprint from embodied emissions → **Source:** Luccioni et al., "Estimating the Carbon Footprint of BLOOM," JMLR (2023)

### Slide 4 — The Shift (Training vs. Inference)

- 80.9% GPU electricity / 17.8% data centre overhead / 1.3% manufacturing → **Source:** Tomlinson et al. (2024)
- >90% of lifetime emissions from inference → **Source:** Tomlinson et al. (2024); Niu et al. (2025)
- 60-70% of sector-wide AI compute used for inference in 2024 → **Source:** IEA, "Energy and AI" (April 2025)
- 65-70% inference share projected by IEA for 2026 → **Source:** IEA, "Energy and AI" (April 2025)
- Training energy rising 4-5x per year → **Source:** Epoch AI (2025)
- 81% of AI emissions from electricity, which is decarbonisable → **Source:** Tomlinson et al. (2024); Watershed (2025)

### Slide 5 — Model Energy Over Time

- BERT: 1.5 MWh → **Source:** Strubell, Ganesh & McCallum (2019)
- GPT-2: 27 MWh → **Source:** Patterson et al. (2021)
- GPT-3: 1,300 MWh → **Source:** Patterson et al. (2021)
- OPT-175B: 324 MWh → **Source:** Meta (2022), OPT model card
- BLOOM: 433 MWh → **Source:** Luccioni et al., JMLR (2023)
- Llama 3 8B: 1,300 MWh → **Source:** Meta model card (2024)
- DeepSeek-V3: 5,543 MWh → **Source:** DeepSeek technical report (2024)
- Llama 3.1 405B: 27,500 MWh → **Source:** Meta model card (2024)
- GPT-4: 50,000-62,000 MWh → **Source:** Epoch AI triangulation. *Note: OpenAI has not disclosed GPT-4 training energy; this is a third-party estimate based on reported compute and hardware assumptions.*
- 33x efficiency improvement (Gemini) → **Source:** Google Cloud Blog (2025)
- 16-month halving time for compute needed to reach a fixed performance level → **Source:** Hernandez & Brown (2020)
- 10-30x efficiency improvement over time → **Source:** Multiple: Epoch AI, Google, MIT. *Note: range reflects different benchmarks, time horizons, and definitions of "efficiency."*
- MoE architecture: DeepSeek-V3 trained for $5.6M → **Source:** DeepSeek technical report (2024)

### Slide 6a — Task-Type Selection

- All task-type energy data (text generation, summarisation, classification, etc.) → **Source:** Luccioni, Jernite & Strubell, "Power Hungry Processing," ACM FAccT (2024). 88 models, 10 tasks, measured on a single A100 GPU.
- Reasoning models consume 3-100x more energy than standard inference → **Source:** "How Hungry is AI?" arxiv:2505.09598 (2025)
- GPT-5: 18.9 Wh per query → **Source:** University of Rhode Island (2025)

### Slide 6b — Model Selection (Per-Query Energy)

- Mistral 7B: ~0.1 Wh → **Source:** EcoLogits (2025), GenAI Impact
- Claude Haiku: ~0.22 Wh → **Source:** Hannah Ritchie (2025)
- Gemini: ~0.24 Wh → **Source:** Google (August 2025)
- GPT-4o: ~0.3 Wh → **Source:** Epoch AI (2025)
- Claude Sonnet: ~0.5-1.5 Wh → **Source:** EcoLogits estimates (2025). *Note: range reflects different prompt lengths and response sizes.*
- Llama 3 70B: ~0.7 Wh → **Source:** EcoLogits estimates (2025)
- Claude Opus: ~4.05 Wh → **Source:** Hannah Ritchie (2025)
- GPT-5/o3: 18-33+ Wh → **Source:** "How Hungry is AI?" arxiv:2505.09598 (2025); University of Rhode Island (2025). *Note: these are early estimates for reasoning-heavy models; actual figures may vary significantly by query complexity.*
- INT4 quantisation yields 50-70% energy savings → **Source:** Multiple ML compression studies. *Note: exact savings depend on model architecture, hardware, and acceptable accuracy loss.*

### Slide 7 — Water

- Google consumed 6 billion gallons, 78% potable → **Source:** Google 2025 Environmental Report
- US data centres consumed 17 billion gallons → **Source:** Lawrence Berkeley National Lab
- 5,700 L ultrapure water per wafer → **Source:** IDTechEx
- TSMC consumed 101 billion litres, missed reduction target → **Source:** TSMC 2024 sustainability disclosures
- 40% of data centres located in water-stressed areas → **Source:** Watershed (2025); World Resources Institute
- 519 mL of water per ChatGPT prompt → **Source:** University of California, Riverside; Li et al. (2023). *Note: this figure includes both direct cooling water and indirect water for electricity generation; direct cooling water alone is substantially lower.*
- 0.26 mL per Gemini query → **Source:** Google (August 2025). *Note: Google's figure may use a narrower boundary than the Li et al. estimate, which partly explains the large difference.*

### Slide 8 — Energy, Grids & Renewables

- Global data centre electricity demand: 415 TWh rising to 945 TWh, growing ~15%/year → **Source:** IEA, "Energy and AI" (April 2025)
- $320 billion in hyperscaler capital spending → **Source:** Watershed (2025)
- 1,891 renewable/grid projects cancelled, representing 266 GW → **Source:** Watershed (2025), citing Lawrence Berkeley National Lab interconnection queue data
- Grid carbon intensity: Norway ~2 g CO2/kWh, France ~57 g, US ~386 g → **Source:** Electricity Maps; MOEA (Norway); EPA eGRID (US)
- 30-80% emissions reduction achievable through region selection → **Source:** Watershed (2025)
- 60% of new US power generation from gas → **Source:** Goldman Sachs (August 2025)
- 24/7 Carbon-Free Energy (CFE): Google achieved 90% at 5 sites → **Source:** Google 2025 Environmental Report
- Jevons Paradox: 20-60% rebound effect → **Source:** Energy economics literature; Luccioni, ACM FAccT (2025). *Note: rebound estimates are highly uncertain and context-dependent; the range reflects different sectors and time horizons.*

### Slide 9 — Your AI Footprint (Personal Calculation)

- ~21 kg CO2e annual footprint for a typical professional AI user → **Source:** Own estimate, synthesised from Ritchie (2025) per-query energy data, EcoLogits model measurements, and EPA eGRID grid intensity factors. *Note: this is an illustrative estimate, not a peer-reviewed figure. Actual footprint depends on model choice, query volume, and grid region.*
- Beef: 27 kg CO2e per kg → **Source:** Poore & Nemecek, *Science* (2018)
- Driving: 404 g CO2 per mile → **Source:** EPA
- Netflix streaming: ~36 g CO2 per hour → **Source:** IEA / Carbon Trust (2023)
- One transatlantic flight: ~1,000 kg CO2 → **Source:** ICAO Carbon Emissions Calculator
- US average annual footprint: 16,000 kg CO2e → **Source:** EPA (2024)

### Slide 10 — Provider Disclosure & Transparency

- 200x variation in methodology across provider disclosures → **Source:** Multiple sources comparison. *Note: refers to differences in boundary definitions, allocation methods, and reporting scopes across providers.*
- Model throttling/shrinkflation (providers silently reducing model quality) → **Source:** Industry observation; no single peer-reviewed source
- Training cost allocation gap (how to allocate training emissions across millions of users) → **Source:** Watershed (2025)
- Meta omitted embodied emissions from Llama 2 model card → **Source:** Meta Llama 2 model card (2023)
- NVIDIA H100 PCF was the first major GPU product carbon footprint disclosure → **Source:** NVIDIA (2025)
- Google reported 12% absolute emissions increase but 27% increase when adjusting for methodology changes → **Source:** Google 2025 Environmental Report
- Proposal for AI energy labels → **Source:** Luccioni et al., *Nature* (2024)

### Slide 11 — Estimating Emissions (Practitioner Tools)

- Grid carbon intensity is the single largest variable in AI emissions estimates → **Source:** Watershed (2025); Electricity Maps
- Claude Haiku 0.22 Wh vs. Claude Opus 4.05 Wh (18x difference within one provider) → **Source:** Hannah Ritchie (2025)
- EcoLogits: open-source tool for estimating LLM energy consumption → **Source:** GenAI Impact (EcoLogits project)
- CodeCarbon: Python library for tracking compute emissions → **Source:** CodeCarbon project
- SCI Standard (Software Carbon Intensity) → **Source:** Green Software Foundation

### Appendix — Personal Footprint Calculation Methodology

- Claude Sonnet per-query energy range: 0.5-1.5 Wh → **Source:** Hannah Ritchie (2025); EcoLogits (2025)
- US average grid intensity: 386 g CO2/kWh → **Source:** EPA eGRID (2024)
- All comparison figures (beef, driving, Netflix, flights, annual average) use sources already cited in Slide 9 above

---

## Sources

### Foundational research
- Luccioni et al. (2023), "Estimating the Carbon Footprint of BLOOM," JMLR
- Luccioni, Jernite & Strubell (2024), "Power Hungry Processing," ACM FAccT
- Luccioni et al. (2024), Nature — AI energy labels proposal
- Luccioni (2025), Jevons' Paradox framework, ACM FAccT
- Kaack et al. (2022), Nature Climate Change — system-level impacts framework
- Strubell, Ganesh & McCallum (2019), "Energy and Policy Considerations for NLP"
- Patterson et al. (2021), "Carbon Emissions and Large Neural Networks" (Google)
- Hernandez & Brown (2020), "Measuring Algorithmic Efficiency"
- Hoffmann et al. (2022), "Chinchilla" — compute-optimal training

### Hardware and embodied emissions
- NVIDIA HGX H100 PCF Summary (2025)
- NVIDIA HGX B200 PCF Summary (2025)
- Falk et al. (2025), "More than Carbon" — A100 LCA, arxiv 2509.00093
- Google (2025), TPU Life-Cycle Emissions LCA, arxiv 2502.01671
- Schneider Electric White Paper 99 — Data Centre Scope 3
- ASML (2023), wafer energy estimates
- TSMC (2024), sustainability disclosures
- IDTechEx, semiconductor water usage
- Tomlinson et al. (2024), AI lifecycle emissions breakdown

### Energy and demand
- IEA (April 2025), "Energy and AI" report
- U.S. Data Center Energy Usage Report (2024)
- Cornell University AI emissions projection
- Goldman Sachs Research (Aug 2025), data centre energy forecast
- McKinsey (2025), AI DC power demand projections
- Gartner (Nov 2025), DC electricity forecast

### Per-query and inference
- Epoch AI (2025), "How much energy does ChatGPT use?"
- OpenAI / Sam Altman (Jun 2025), per-query energy disclosure
- Google (Aug 2025), Gemini energy per prompt
- Hannah Ritchie (Aug 2025), AI carbon footprint analysis
- "How Hungry is AI?" (May 2025), arxiv:2505.09598
- University of Rhode Island (Aug 2025), GPT-5 energy study
- Neil Thompson, MIT (2025) — model efficiency research
- Niu et al. (2025), TokenPowerBench, arxiv:2512.03024
- Jegham et al. (2025), "How Hungry is AI?", arxiv:2505.09598
- EcoLogits / GenAI Impact — LLM inference emissions estimator

### Provider reports
- Google 2025 Environmental Report
- Microsoft 2025 Sustainability Report
- Amazon 2024 Sustainability Report
- Meta 2025 Sustainability Report

### Wider context
- BCG & Google (2023-2024), AI climate reduction potential
- Li et al. (2023), "Making AI Less 'Thirsty'"
- Watershed (2025), "AI Emissions: A Practical Guide for Corporate Sustainability Leaders"
- Lawrence Berkeley National Lab — US data centre water consumption
- University of California, Riverside — per-query water estimates
- World Resources Institute — data centre community impacts
- NAACP — "Stop Dirty Data Centers" campaign
- Heinrich Boll Stiftung — EU AI Act environmental provisions analysis

### Policy and governance
- EU AI Act (2024)
- California SB 253 / SB 261
- Green Software Foundation — SCI standard
