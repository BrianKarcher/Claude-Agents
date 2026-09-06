# Tesla Cybercab — Operating Cost per Mile at Scale

_Analysis date: 2026-09-06. Cybercab only (not retrofitted Model Y). Cash fleet operating
costs only — **excludes** all D&A and capex._

## Scope

**Included:** electricity, charging-site O&M, tires, maintenance/service, cleaning, leased
depot/parking real estate, insurance/liability/claims, teleoperation, fleet ops / dispatch /
field response, connectivity & data, customer support, licensing/permits, local ops management,
and (shown separately) payment processing.

**Excluded (per instruction):** vehicle depreciation, battery-degradation reserve, sensor/compute
hardware amortization, charger hardware, depot construction, wireless-charging pads — all capex or
D&A. Also excluded: R&D / software development, corporate G&A, sales & marketing, financing/interest,
income tax. No driver or safety-monitor cost (there is none in a scaled Cybercab).

## Key assumptions

| Assumption | Value | Note |
|---|---|---|
| Vehicle | 2-seat purpose-built Cybercab, ~50 kWh pack | Light, simple, low frontal area |
| Efficiency (grid-side) | ~4.5 mi/kWh | Tesla claims 5.5+; discounted for city stop-go, year-round HVAC, ~0.5 kW compute/sensor parasitic load, ~10% charging losses |
| Utilization | 50,000 mi/vehicle/yr | ~150 mi/day, ~330 service days. Base case; sensitivity below |
| Duty cycle | ~17 mph avg incl. stops → ~3,000 operating hr/yr | Urban ride-hail |
| "At scale" | Mature ops, >100k-vehicle fleet, software past its steep improvement curve | Not early-deployment economics |
| Metro mix | Blend of Sun Belt (cheap) and some coastal (expensive) | Depot + insurance + wages are metro-driven |

---

## Line-item estimate (base case)

| Bucket | Base $/mi | Range | Basis |
|---|--:|--:|---|
| Electricity (energy) | 0.034 | 0.025–0.050 | 4.5 mi/kWh grid-side × ~$0.14/kWh blended depot rate + demand-charge premium. Energy-only "2.6¢/mi" headlines assume 5.5 mi/kWh and ignore losses + parasitic load |
| Charging-site O&M | 0.008 | 0.005–0.012 | Charger maintenance/downtime, network fees, site utilities. Charger hardware = capex, excluded |
| Tires | 0.020 | 0.015–0.030 | ~35k mi/set in stop-go duty, ~$700/set fleet-priced & installed |
| Maintenance & service (ex-tire) | 0.070 | 0.045–0.095 | Brakes, suspension/steering wear (potholes, curbs), 12V/LV, HVAC, wipers/washer system, glass + sensor recalibration, alignments, cosmetic/body repair to keep fleet presentable, preventive-inspection labor. EV drivetrain holds this well below ICE |
| Cleaning & detailing | 0.045 | 0.030–0.070 | Daily quick interior clean, weekly deep clean, ~2×/wk exterior wash, biohazard/vandalism remediation reserve. Per-*day* cost — dilutes at higher daily mileage |
| Depot / parking / staging (lease) | 0.040 | 0.020–0.065 | Leased land for charging/cleaning/staging + curb, airport and pickup-zone access fees. Owned depots would move to capex/D&A (excluded); treated as lease-equivalent. Very metro-dependent |
| Insurance / liability / claims | 0.060 | 0.040–0.120 | Expected 3rd-party bodily-injury + property-damage claims, litigation, excess/reinsurance premium, reserves, admin. Assumes a materially better-than-human crash rate. **Highest-variance line**; 2–3× higher in early years and in litigious states |
| Teleoperation / remote assist | 0.050 | 0.025–0.100 | Real-time remote intervention/confirmation staff. ~1 operator : 100 vehicles at maturity, 24/7, ~$30/hr loaded. 1:40 early → ~$0.13/mi; long-run 1:200 → ~$0.025/mi |
| Fleet ops / dispatch / field response | 0.045 | 0.035–0.060 | Depot techs (staging, plug-in), field rescue/tow contracts, network operations center, routing/dispatch ops |
| Connectivity / data / maps | 0.030 | 0.020–0.045 | Multi-carrier cellular (teleop video bandwidth), map upkeep, OTA + fleet-ops cloud. Excludes R&D compute |
| Customer support / trust & safety | 0.015 | 0.010–0.025 | In-app/phone rider support, in-ride help-button staffing, lost & found, incident hotline |
| Licensing / permits / compliance | 0.010 | 0.005–0.020 | AV permits, registration, city fees, safety-case reporting & audit staff |
| Local / regional ops management | 0.015 | 0.010–0.025 | Regional managers, facilities, HR for ops headcount. Excludes corporate G&A / R&D / marketing |
| **Subtotal — vehicle operating** | **≈ 0.44** | **≈ 0.31–0.72** | |
| Payment processing | 0.050 | 0.030–0.070 | ~2.75% of gross fare at a ~$1.80/mi fare. Revenue-linked, not mileage-linked — kept separate |
| **Total incl. payment processing** | **≈ 0.49** | **≈ 0.34–0.79** | |

---

## Scenario summary

| Scenario | Conditions | $/mi (ex-payment) | $/mi (incl. payment) |
|---|---|--:|--:|
| **Lean / mature (2030+)** | 65–75k mi/yr, teleop 1:150+, clean safety record trims insurance to ~$0.04, cheap Sun Belt metros, cleaning diluted | ~0.28–0.33 | ~0.32–0.38 |
| **Base (realistic mature mix)** | assumptions above | ~0.44 | ~0.49 |
| **Early-scale / high-cost (2027–29)** | 35–45k mi/yr, teleop 1:40–60, insurance $0.10–0.12, expensive coastal metros, immature ops | ~0.68–0.80 | ~0.72–0.86 |

### Utilization sensitivity

Fixed-ish buckets (depot, insurance base, teleop, fleet-ops core, connectivity, support, licensing,
local mgmt) ≈ **$12,000 / vehicle / year**. Variable buckets ≈ **$0.20/mi**.

| Miles/yr | Fixed $/mi | Total $/mi (ex-payment) |
|--:|--:|--:|
| 35,000 | 0.34 | ~0.54–0.60 |
| 50,000 | 0.24 | ~0.44 |
| 70,000 | 0.17 | ~0.37 |

Utilization is the single biggest lever Tesla actually controls.

---

## How this compares

| Source | Figure | Notes |
|---|--:|---|
| **This estimate (ex-D&A)** | base **~$0.44–0.49/mi**; lean ~$0.30; early ~$0.75 | |
| Musk ("We, Robot", Oct 2024; reaffirmed Sept 2026) | "~$0.20/mi" operating cost; fare "30–40¢/mi"; Robovan "5–10¢/mi per passenger" | Stage claim, no published line-item model — see "Provenance" below |
| ARK *Big Ideas 2026* | $0.20/mi fully-loaded at scale by 2030 (Waymo Gen 6: $0.40) | Effectively energy + maintenance + thin ops/insurance slice |
| Morgan Stanley | Tesla **~$0.74/mi** incl. depreciation, cleaning, maintenance, charging, mobile operators, insurance, parking (Waymo $1.36) | Strip ~$0.08–0.12 depreciation → **~$0.62–0.66/mi ex-D&A** |
| Analyst est. of Tesla's *current* (2026) cost | ~$0.81/mi | Sub-scale, immature |

**Why the base here ($0.44) sits above Musk/ARK's $0.20:** those figures under-weight cleaning,
leased depot real estate, teleoperation and field response at realistic staffing ratios, customer
support, payment processing, and a realistic insurance load. They are achievable only post-2030,
at large scale, with a clean safety record — and even then $0.20 looks optimistic once payment
processing and a full insurance/claims load are included. Morgan Stanley's ~$0.62–0.66/mi ex-D&A
is the more defensible near-term number; this estimate is somewhat leaner because it assumes higher
utilization and a more mature teleop ratio.

### Provenance of Musk's $0.20/mi target

- **Origin: Tesla's "We, Robot" event, 10 Oct 2024.** Musk said on stage the Cybercab's operating
  cost would be "about 20 cents a mile," with the rider price landing "around 30 or 40 cents a mile"
  after taxes. He floated 5–10¢/mi per passenger for the (concept) Robovan.
- **Stated justification was an analogy, not a model.** His comparison: a city bus costs
  "about a dollar a mile" to operate, so a Cybercab at 20¢ is "individualized mass transit."
  Tesla has never published a bottoms-up line-item derivation of the number.
- **The nearest thing to a derivation is ARK Invest's** *Big Ideas 2026* report, which
  independently models ~$0.20/mi **fully loaded (including depreciation)** at scale by 2030, vs.
  ~$0.40/mi for Waymo's Gen 6. ARK's build leans on: 5.5–6 mi/kWh at ~$0.15/kWh (<$0.03/mi energy),
  low EV maintenance, low-downtime robotic cleaning, and — the biggest lever — amortizing a
  ~$25–30k vehicle over **100,000+ miles/year** of utilization so per-mile depreciation stays small.
- **Caveats for using it against this file:** (a) it began as an unmodeled stage assertion;
  (b) ARK's version *includes* D&A, so it is not scope-comparable to the ex-D&A numbers here;
  (c) ARK assumes ~2× this file's base utilization (100k vs 50k mi/yr); (d) both Musk's and ARK's
  figures carry only a thin insurance/teleop/support allocation. Treat $0.20/mi as a
  best-case 2030+ marketing target, not a planning number.

## Biggest uncertainties

1. **Insurance / claims** — swings $0.04 to $0.12+/mi on the realized crash rate and the tort
   environment. Could be the largest single line or a minor one.
2. **Teleoperation ratio** — $0.025 to $0.13/mi across plausible operator:vehicle ratios.
3. **Utilization** — see table; ±$0.10/mi.
4. **Metro mix** — depot lease, insurance and wages roughly double from Phoenix to San Francisco.

This is a cost estimate only — it is not a margin or profitability statement; fares and revenue
are not modeled here beyond the payment-processing line.

## Sources

- Musk / ARK / analyst cost-per-mile figures — https://www.autoblog.com/news/tesla-cybercab-could-cost-just-2-6-per-mile-to-run
- Musk touts Cybercab cost edge over Waymo (launch remarks) — https://eletric-vehicles.com/tesla/musk-touts-cybercab-cost-edge-over-waymo-ojai-hours-before-launch-event/
- Cybercab cost-per-mile discussion — https://aaronsmet.medium.com/tesla-cybercabs-cost-per-mile-how-autonomous-transportation-could-become-cheaper-than-car-a450452c3ea6
- Robotaxi fleet cost breakdown (energy/maintenance/insurance/remote-ops components) — https://tahaabbasi.com/blog/taha-abbasi-robotaxi-economics-cost-per-mile-autonomous-fleet-analysis-feb-2026
- Morgan Stanley Waymo $1.36 vs Tesla $0.74 per mile — https://www.nextbigfuture.com/2025/01/estimating-per-car-robotaxi-revenue-and-expenses.html
- Robotaxi cost components / depots / cleaning / remote ops — https://unchartedterritories.tomaspueyo.com/p/robotaxis-are-here
- "We, Robot" event (Oct 2024): Cybercab 20¢/mi, bus ~$1/mi analogy, Robovan 5–10¢/mi — https://techcrunch.com/2024/10/10/tesla-reveals-20-cybercabs-at-we-robot-event/
- Musk says it's "probably true" Cybercab could cost less than $0.20/mi (Sept 2026) — https://eletric-vehicles.com/tesla/musk-says-its-probably-true-cybercab-could-cost-less-than-0-20-per-mile/
- ARK-derived $0.20/mi (energy, maintenance, cleaning, depreciation via 100k+ mi/yr) — https://ilovetesla.com/tesla-cybercab-elon-musk-confirms-0-20-per-mile-operating-cost-the-future-of-affordable-robotaxis-is-here/
