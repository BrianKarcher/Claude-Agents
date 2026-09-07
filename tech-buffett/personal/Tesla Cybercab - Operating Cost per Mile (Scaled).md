# Tesla Cybercab — Cost per Mile at Scale (operating, + depreciation layer)

_Analysis date: 2026-09-06. Cybercab only (not retrofitted Model Y). Primary build is **cash fleet
operating cost, ex-D&A**; a **vehicle depreciation layer** and a **fully-loaded total** are added
in the "Depreciation" section below (added 2026-09-06 revision)._

## Scope

**Included:** electricity, charging-site O&M, tires, maintenance/service, cleaning, leased
depot/parking real estate, insurance/liability/claims, teleoperation, fleet ops / dispatch /
field response, connectivity & data, customer support, licensing/permits, local ops management,
and (shown separately) payment processing.

**Added as a separate layer (see "Depreciation" below):** vehicle depreciation (glider + battery +
onboard autonomy hardware), plus an optional mid-life battery reserve.

**Still excluded:** charger hardware, depot construction, wireless-charging pads, and other
infrastructure capex; R&D / software development; corporate G&A; sales & marketing;
financing / interest; income tax. No driver or safety-monitor cost (there is none in a scaled
Cybercab). Depreciation is an economic (non-cash) charge — the ex-D&A subtotal is still the right
number for a pure cash-cost view.

## Key assumptions

| Assumption | Value | Note |
|---|---|---|
| Vehicle | 2-seat purpose-built Cybercab, ~50 kWh pack | Light, simple, low frontal area |
| Efficiency (grid-side) | ~4.5 mi/kWh | Tesla claims 5.5+; discounted for city stop-go, year-round HVAC, ~0.5 kW compute/sensor parasitic load, ~10% charging losses |
| Utilization | ramps ~40k → ~75k mi/vehicle/yr (see "Annual mileage & utilization" below) | Line-item table below is built at ~50k mi/yr; mature base is ~75k |
| Duty cycle | ~17 mph avg incl. stops; ~350 service days/yr | Urban ride-hail; downtime is for maintenance, not days off |
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
| Insurance / liability / claims | 0.050 | 0.035–0.120 | **Loss-cost basis** — Tesla self-insures via its captive (Tesla Insurance, 13 states incl. TX/FL/AZ/NV/CA — i.e. essentially all near-term robotaxi markets), so this is expected bodily-injury + property-damage losses + in-house claims handling + tail reinsurance above a retention, *without* the ~25–35% expense-and-profit load a third-party commercial insurer adds. Assumes a materially better-than-human crash rate. **Highest-variance line.** High end ($0.10–0.12) = early years / immature loss data / third-party-covered or litigious states; a bad-verdict year hits Tesla's own P&L directly |
| Teleoperation / remote assist | 0.050 | 0.025–0.100 | Real-time remote intervention/confirmation staff. ~1 operator : 100 vehicles at maturity, 24/7, ~$30/hr loaded. 1:40 early → ~$0.13/mi; long-run 1:200 → ~$0.025/mi |
| Fleet ops / dispatch / field response | 0.045 | 0.035–0.060 | Depot techs (staging, plug-in), field rescue/tow contracts, network operations center, routing/dispatch ops |
| Connectivity / data / maps | 0.030 | 0.020–0.045 | Multi-carrier cellular (teleop video bandwidth), map upkeep, OTA + fleet-ops cloud. Excludes R&D compute |
| Customer support / trust & safety | 0.015 | 0.010–0.025 | In-app/phone rider support, in-ride help-button staffing, lost & found, incident hotline |
| Licensing / permits / compliance | 0.010 | 0.005–0.020 | AV permits, registration, city fees, safety-case reporting & audit staff |
| Local / regional ops management | 0.015 | 0.010–0.025 | Regional managers, facilities, HR for ops headcount. Excludes corporate G&A / R&D / marketing |
| **Subtotal — vehicle operating** | **≈ 0.43** | **≈ 0.30–0.72** | *built at ~50k mi/yr; see mileage adjustment below* |
| Payment processing | 0.050 | 0.030–0.070 | ~2.75% of gross fare at a ~$1.80/mi fare. Revenue-linked, not mileage-linked — kept separate |
| **Total incl. payment processing** | **≈ 0.48** | **≈ 0.33–0.79** | *at ~50k mi/yr* |

---

## Annual mileage & utilization estimate

Cost per mile is dominated by annual miles per car, so this is estimated explicitly rather than
assumed flat.

**Benchmark — Waymo (only mature operator, 2026):** ~18–20 paid trips/vehicle/day
(~125 trips/week across a ~4,000-car fleet, 500k paid rides/week), roughly ~90–110 mi/day,
**~30–35k mi/yr**. Waymo is held back by small geofences and premium pricing. Tesla's thesis —
larger service areas, lower fares stimulating demand, more aggressive 24/7 running — should lift
trips/day above Waymo's current level over time. That is an assumption, not a demonstrated fact.

### Base-case ramp (per vehicle)

| Phase | Paid trips/day | Deadhead share of miles | Time utilization¹ | Effective in-service hr/day | **Annual miles** |
|---|--:|--:|--:|--:|--:|
| Early (2027–28) | 16–20 | ~42% | ~32% | ~13 | **~40–48k** |
| Mid (2029–31) | 25–33 | ~38% | ~42% | ~17 | **~55–70k** |
| Mature (2032+) | 35–45 | ~34% | ~50% | ~19 | **~74–90k** |

¹ share of in-service time with a rider aboard. ~350 service days/yr. Avg trip ≈ 3.5 mi paid + ~2 mi deadhead.

### Scenario mileage (mature, 2032+)

| | Annual miles | Basis |
|---|--:|---|
| Bear | ~55k | Geofences stay small, demand thin, Waymo-like |
| Base | ~75k | Larger areas + dynamic pricing filling off-peak |
| Bull | ~95k | Dense network, ~20 hr/day effective, low fares pull heavy demand (≈ ARK's 100k assumption) |

---

## Cost impact of the mileage ramp

Decomposition of the base build: **$0.192/mi** purely variable (energy, charging O&M, tires,
maintenance, self-insured loss cost, field response) + **~$9 / service-day** (cleaning, depot
staging; ≈ $3,150/yr) + **~$9,000 / vehicle-yr** fixed (depot lease, teleoperation, network-ops
core, connectivity, support, licensing, local mgmt). Payment processing (~$0.045–0.05/mi) on top.

| Annual miles | $/mi ex-payment | $/mi incl. payment | Corresponds to |
|--:|--:|--:|---|
| 40,000 | ~0.50 | ~0.54 | early scale — mileage effect only |
| 50,000 | ~0.43 | ~0.48 | prior flat base assumption |
| 60,000 | ~0.39 | ~0.44 | mid scale |
| 70,000 | ~0.36 | ~0.41 | early-mature |
| 75,000 | ~0.35 | ~0.40 | **revised mature base** |
| 95,000 | ~0.32 | ~0.37 | bull / lean mature |

**Effect on the headline:** the mature base moves from the earlier flat-50k figure of ~$0.44
ex-payment down to **~$0.35/mi ex-payment (~$0.40 incl. payment)** — driven mostly by higher
mature utilization (~70–80k mi/yr, not 50k) and helped ~$0.01 by the self-insured loss-cost basis
for insurance. This *replaces* the "$0.44 base" used elsewhere in this file.

### Revised scenario summary

| Scenario | Annual miles | Key conditions | $/mi ex-payment | $/mi incl. payment |
|---|--:|---|--:|--:|
| **Early-scale (2027–29)** | ~40–48k | teleop 1:40–60, insurance $0.10–0.12 (immature loss data, some third-party cover), costly metros | ~0.66–0.83 | ~0.71–0.88 |
| **Mid-scale (2029–31)** | ~55–70k | teleop ~1:80, self-insured loss cost ~$0.06, mixed metros | ~0.40–0.46 | ~0.45–0.51 |
| **Mature base (2032+)** | ~75k | teleop ~1:100, self-insured loss cost ~$0.05, blended metros | **~0.35–0.38** | **~0.40–0.43** |
| **Lean / mature (2033+)** | ~90–95k | teleop 1:150+, self-insured loss cost ~$0.035, cheap Sun Belt metros | ~0.27–0.31 | ~0.31–0.36 |

Utilization / annual miles is the single biggest lever in the whole model: ~$0.50/mi at 40k mi/yr
vs ~$0.32/mi at 95k, before any other change.

---

## Depreciation (added layer)

Economic depreciation of the vehicle itself — glider + battery + onboard vision/compute hardware.
Formula: **capitalized cost × (1 − residual) ÷ lifetime miles.**

**Inputs:**
- **Capitalized cost: revised to $20,000** (2026-09-07, per updated instruction — down from the
  original ~$28–34k estimate). Tesla's *internal build cost* at scale was estimated at ~$25–28k
  (consumer price <$30k) with a fleet unit carrying extra network fit-out and vision/compute stack
  on top — so $20k sits *below* that original build-cost estimate, not just below the fleet-unit
  price. Treat this as a "vehicle gets meaningfully cheaper than originally estimated" case (BOM
  simplification, battery-cost decline, yield improvement) rather than a refinement of the original
  $28–34k figure, unless there's a specific reason to believe $20k is now the better number. The
  original ~$28–34k figures are kept in "How this compares" below for reference.
- **Residual:** ~10% (range 0–20%), unchanged. A purpose-built, no-steering-wheel Cybercab has a thin
  secondary market — mostly parts/scrap plus possible non-US resale.
- **Lifetime:** the binding limit is ~**4.5 years of economic life** (autonomy-hardware generation
  obsolescence and brand/safety standards), or a ~**350k-mile** cap, whichever comes first, unchanged.
  At low early-phase utilization the *time* limit binds, so depreciation per mile is much higher when
  the car is underused — same dynamic as the fixed opex buckets.

| Phase | Annual miles | Lifetime miles (≈4.5 yr or 350k cap) | **Depreciation $/mi** | (at prior $28-34k basis) |
|---|--:|--:|--:|--:|
| Early (2027–28) | ~44k | ~200k | **~0.09** | ~0.13 |
| Mid (2029–31) | ~62k | ~280k | **~0.07** | ~0.10 |
| Mature base (2032+) | ~75k | ~340k | **~0.05** | ~0.08 |
| Lean / bull mature | ~95k | 350k cap (hit in ~3.7 yr) | **~0.04** | ~0.065 |

(New figures = old figures x (20,000/30,000) — capitalized cost scales linearly through the
depreciation formula holding residual % and lifetime miles fixed; $30k is the representative
midpoint the original table's phase values were built from.)

**Optional mid-life battery reserve:** if packs are swapped (~$6–9k, falling) rather than the car
retired, add **~$0.02–0.03/mi** in the mature/lean cases where the car would otherwise outlast its
first pack. Not added to the totals below — noted as a swing factor.

---

## Fully-loaded summary (opex + depreciation)

| Scenario | Opex ex-payment | + Depreciation | **Fully loaded, ex-payment** | **+ payment processing** |
|---|--:|--:|--:|--:|
| Early-scale (2027–29) | ~0.66–0.83 | ~0.09 | **~0.75–0.92** | ~0.80–0.97 |
| Mid-scale (2029–31) | ~0.40–0.46 | ~0.07 | **~0.47–0.53** | ~0.52–0.58 |
| **Mature base (2032+)** | ~0.35–0.38 | ~0.05 | **~0.40–0.43** | **~0.45–0.48** |
| Lean / mature (2033+) | ~0.27–0.31 | ~0.04 | **~0.31–0.35** | ~0.36–0.40 |

**Headline, fully loaded (at $20k capitalized cost):** mature base **~$0.42/mi ex-payment
(~$0.47 incl. payment)**; lean ~$0.33; early-scale ~$0.84. Depreciation now adds only
~$0.04–0.09/mi (was ~$0.08–0.13 at the original $28-34k basis) and is a smaller line relative to
opex than before — still material, no longer the clear second-largest single line at every phase.

---

## How this compares

| Source | Figure | Notes |
|---|--:|---|
| **This estimate — ex-D&A** | mature base **~$0.35/mi** ex-payment (~$0.40 incl.); lean ~$0.29; early-scale ~$0.73 | Cash opex only |
| **This estimate — fully loaded** | mature base **~$0.42/mi** ex-payment (~$0.47 incl.); lean ~$0.33; early-scale ~$0.84 | Opex + ~$0.04–0.09 vehicle depreciation (at $20k capitalized cost). Like-for-like with ARK / MS below |
| Musk ("We, Robot", Oct 2024; reaffirmed Sept 2026) | "~$0.20/mi" operating cost; fare "30–40¢/mi"; Robovan "5–10¢/mi per passenger" | Stage claim, no published line-item model — see "Provenance" below. "Operating cost" framing likely excludes depreciation |
| ARK *Big Ideas 2026* | $0.20/mi **fully loaded** at scale by 2030 (Waymo Gen 6: $0.40) | ~2.2–2.5× below this file's like-for-like fully-loaded mature ~$0.44–0.49. Gap is scope (teleop, support, field response, payment, realistic insurance), not miles or depreciation |
| Morgan Stanley | Tesla **~$0.74/mi** incl. depreciation, cleaning, maintenance, charging, mobile operators, insurance, parking (Waymo $1.36) | ≈ this file's **mid-scale** fully-loaded (~$0.55–0.61 incl. payment) to early-mature — i.e. MS assumes lower utilization / earlier stage than the mature base here |
| Analyst est. of Tesla's *current* (2026) cost | ~$0.81/mi | Sub-scale, immature — ≈ this file's early-scale fully-loaded |

**Why the fully-loaded mature base (~$0.42, at the revised $20k capitalized cost) still sits ~2×
above ARK's $0.20:** the comparison is like-for-like (both fully loaded). It is *not* utilization —
ARK's 100k mi/yr ≈ this file's bull-mature 95k — and now it's not depreciation at all: this file's
mature depreciation (~$0.05/mi, ~$0.04 lean) sits at or below ARK's own implied ~$0.05–0.08/mi on a
$25-30k vehicle, since $20k is now cheaper than the vehicle ARK itself assumes. The entire remaining
gap is scope: ARK carries almost nothing for teleoperation, customer support, field response, or
payment processing (~$0.045/mi on its own). Self-insurance narrows it a little — this file's
insurance line is already a loss-cost basis, not a marked-up premium — but a clean-record
self-insured loss cost is still ~$0.035–0.05/mi, not the ~$0.02 ARK implies; a fleet carrying
paying passengers still pays the claims. Morgan Stanley's ~$0.74/mi (incl. depreciation) lines up
with this file's **mid-scale** fully-loaded figure, i.e. MS is modelling an earlier / less-utilized
fleet than the 2032+ mature base here.

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
  (b) ARK's version *includes* D&A — compare it to this file's **fully-loaded** ~$0.42–0.47/mi
  (at the revised $20k capitalized cost), not the ex-D&A figure; (c) ARK assumes ~100k mi/yr,
  matching only this file's bull-mature case;
  (d) both Musk's and ARK's figures carry only a thin insurance/teleop/support allocation and no
  real payment-processing line. Treat $0.20/mi as a best-case 2030+ marketing target, not a
  planning number.

## Biggest uncertainties

1. **Insurance / claims** — swings ~$0.035 to $0.12+/mi on the realized crash rate and the tort
   environment. Tesla self-insures via its captive in 13 states (including every near-term robotaxi
   market — TX, FL, AZ, NV, CA), so the cost is loss cost + handling + tail reinsurance, not a
   marked-up third-party premium — but self-insurance also means a nuclear-verdict year lands
   straight on Tesla's P&L rather than an insurer's. Could be the largest single line or a minor one.
2. **Teleoperation ratio** — $0.025 to $0.13/mi across plausible operator:vehicle ratios.
3. **Utilization / annual miles — the dominant driver.** ~$0.50/mi at 40k mi/yr vs ~$0.32/mi at
   95k on opex alone, and it swings depreciation another ~$0.04 (95k) to ~$0.09 (40k) on top at the
   revised $20k capitalized cost (was ~$0.065 to ~$0.13 at $28-34k). Whether a mature Cybercab does
   55k or 95k mi/yr turns on demand density and service-area size, neither demonstrated yet (Waymo
   is at ~30–35k today).
4. **Vehicle life / capitalized cost** — at the revised $20k figure, depreciation ranges ~$0.03/mi
   (15% residual, 450k-mile life) to ~$0.09/mi (~5% residual, retired at ~4.5 yr / ~200k mi); the
   original $28-34k basis ranged ~$0.05-0.13/mi over the same life/residual spread — keep that
   wider range in mind if $20k turns out to be too aggressive a build-cost assumption. Turns on
   autonomy-hardware obsolescence cadence and whether packs are swapped or cars retired.
5. **Metro mix** — depot lease, insurance and wages roughly double from Phoenix to San Francisco.

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
- Waymo ~500k paid rides/week, ~18–20 trips/vehicle/day benchmark — https://www.thedriverlessdigest.com/p/waymo-hits-500000-weekly-rides-and
- Waymo coverage vs. ridership / per-vehicle utilization — https://businessmodelanalyst.com/waymo-coverage-vs-ridership-utilization/
- Tesla Insurance state list (13 states, incl. FL late 2025) & CA self-underwriting shift — https://www.notateslaapp.com/tesla-reference/913/tesla-insurance-a-look-at-its-cost-and-which-states-it-s-available-in/1000
