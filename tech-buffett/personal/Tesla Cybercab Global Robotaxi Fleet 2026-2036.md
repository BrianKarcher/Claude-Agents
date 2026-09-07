# Tesla Cybercab — Global Robotaxi Fleet: Production, Removals & Net Fleet, 2026–2036

_Analysis date: 2026-09-07. Global scope (not just U.S.). Companion to, and topline complement of,
"Tesla Robotaxi Deployment Scenarios 2026-2036" (U.S.-metro, regulatory-paced, city-level detail —
keep using that file for near-term U.S. city/regulatory granularity) and
"Tesla Cybercab - Operating Cost per Mile (Scaled)" (unit economics, vehicle-life assumptions used
here)._

## Why this file exists

The prior deployment-scenarios file measured **U.S. active fleet only**, gated almost entirely by
regulatory/safety-case pace, and its single "Added that year" column conflated several different
things (production, deployment lag, replacement) into one number — which made it look like it was
ignoring Tesla's own stated manufacturing targets. It wasn't ignoring them, but it also never showed
its work against them.

This file fixes both problems: it's **global** (Cybercab is a purpose-built robotaxi with no
steering wheel — it has no meaningful market outside ride-hail fleet service, so essentially all
production is fleet-bound, unlike a normal consumer vehicle), and it separates **production**,
**retirement**, and **net fleet growth** into distinct columns so each number means one thing.

## Definitions

| Column | Meaning |
|---|---|
| **Produced** | Cybercabs manufactured and entering active global fleet service that year (all factories, all markets). Treated as ≈ total production since the vehicle has no material non-fleet use. |
| **Removed** | Cybercabs retired from active service that year (end of economic life). |
| **Net Add** | Produced − Removed. The actual year-over-year growth in the active global fleet. |
| **Cumulative Active Fleet** | Running total of Net Add — the size of the global in-service robotaxi fleet. |

**Not modeled as a separate line:** the staging/registration backlog visible today (hundreds of
Cybercabs staged at Giga Texas, ~45 registered/deployed as of Sept 2026). At the annual resolution
of this table that gap is noise — it matters for this quarter, not for a multi-year scenario — so
"Produced" here already nets out that lag rather than tracking it explicitly.

## Key assumptions

**Vehicle life (drives Removed):** per the companion cost file, economic life is ~4.5 years
(autonomy-hardware obsolescence) or a 350k-mile cap, whichever binds first. At base/bear
utilization (~55–75k mi/yr) the *time* cap binds first in all cases (350k ÷ 55–75k = 4.7–6.4 yrs,
both above 4.5); only in bull's high-utilization case (~95k mi/yr) does the mileage cap bind
slightly earlier (350k ÷ 95k ≈ 3.7 yrs). At annual resolution these round to the same number, so
this table uses a uniform **4-year retirement lag** across all three scenarios as an approximation —
Removed(year Y) = Produced(year Y−4). Real-world retirements would smooth into a distribution
around that point rather than land as a single-year step; treat this as a scenario-planning
simplification.

**Production ramp — anchored to and reconciled against Musk's stated targets:** Musk has stated a
long-term target of **~2M Cybercabs/yr** across factories, with a **~4M/yr stretch** floated as
aspirational/unconfirmed. Historically, Musk production targets have run 2–5 years ahead of
delivered reality (Model 3's "500k/yr" slipped ~2 years; Cybertruck volume has persistently
undershot its own targets). This file treats 2M/yr as the **Base-case ceiling**, reached in the
final year of the window (2036) rather than assumed from the start, and 4M/yr as the **Bull-case
ceiling**, requiring a second production line and simultaneous best-case regulatory/demand
conditions globally. **Bear never approaches either target** — Cybercab becomes a real but
sub-scale product, the way Cybertruck has relative to its own original volume ambitions.

**Global regulatory scope:** this is the single biggest reason cumulative fleet here runs well above
the old U.S.-only file. Assumptions:
- **U.S.**: same pace as the deployment-scenarios file (TX/FL first, AZ/NV next, slow/late coastal
  states).
- **China**: effectively **excluded in all three scenarios** — geopolitics, data-localization rules,
  and entrenched local players (Baidu Apollo Go, WeRide, Pony.ai, Didi) make Tesla-operated robotaxi
  service there implausible through 2036 even in the bull case.
- **Europe / Middle East / other**: bear ≈ token pilots only; base sees meaningful EU + Gulf
  (UAE/Saudi) approval from ~2030; bull sees faster, broader international rollout (EU, Gulf, parts
  of APAC ex-China, Latin America) from ~2028.

This international layer is folded directly into the Produced/Net Add numbers below rather than
broken out by region — the point of this file is the global topline, not city-level detail (that's
what the companion U.S. file is for).

---

## Bear — Cybercab underdelivers, stays sub-scale (Cybertruck-like)

| Year | Produced | Removed | Net Add | Cumulative Active Fleet |
|------|---------:|--------:|--------:|-------------------------:|
| 2026 |     500 |       0 |     500 |                      500 |
| 2027 |   4,000 |       0 |   4,000 |                    4,500 |
| 2028 |  15,000 |       0 |  15,000 |                   19,500 |
| 2029 |  40,000 |       0 |  40,000 |                   59,500 |
| 2030 |  80,000 |     500 |  79,500 |                  139,000 |
| 2031 | 130,000 |   4,000 | 126,000 |                  265,000 |
| 2032 | 190,000 |  15,000 | 175,000 |                  440,000 |
| 2033 | 250,000 |  40,000 | 210,000 |                  650,000 |
| 2034 | 310,000 |  80,000 | 230,000 |                  880,000 |
| 2035 | 370,000 | 130,000 | 240,000 |                1,120,000 |
| 2036 | 430,000 | 190,000 | 240,000 |                1,360,000 |

2036 production (430k) = ~22% of Musk's 2M base target, ~11% of the 4M stretch. NHTSA-style
regulatory friction recurs, battery-pack/production constraints persist, and Tesla never gets
meaningfully past a handful of permissive markets — it stays boxed in, both at the factory and at
the regulator.

---

## Base — steady multi-year ramp, reaches Musk's stated 2M/yr target by 2036

| Year | Produced | Removed | Net Add | Cumulative Active Fleet |
|------|---------:|--------:|--------:|-------------------------:|
| 2026 |    1,500 |       0 |    1,500 |                    1,500 |
| 2027 |   12,000 |       0 |   12,000 |                   13,500 |
| 2028 |   45,000 |       0 |   45,000 |                   58,500 |
| 2029 |  110,000 |       0 |  110,000 |                  168,500 |
| 2030 |  220,000 |   1,500 |  218,500 |                  387,000 |
| 2031 |  400,000 |  12,000 |  388,000 |                  775,000 |
| 2032 |  650,000 |  45,000 |  605,000 |                1,380,000 |
| 2033 |  950,000 | 110,000 |  840,000 |                2,220,000 |
| 2034 | 1,300,000 | 220,000 | 1,080,000 |               3,300,000 |
| 2035 | 1,650,000 | 400,000 | 1,250,000 |               4,550,000 |
| 2036 | 2,000,000 | 650,000 | 1,350,000 |               5,900,000 |

Production reaches Musk's stated 2M/yr target exactly in 2036 — a decade after the 2024 "We, Robot"
unveil, roughly in line with how long his production targets typically take to land. **Net Add
(1.35M) is only 68% of Produced (2.0M) by 2036** — this is the mechanical answer to "why doesn't 2M
produced mean 2M new robotaxis a year": by the mid-2030s, replacing a fleet that's already in the
multi-million range eats a large and growing share of gross output.

---

## Bull — second line added, approaches Musk's 4M/yr stretch target

| Year | Produced | Removed | Net Add | Cumulative Active Fleet |
|------|---------:|--------:|--------:|-------------------------:|
| 2026 |    3,000 |       0 |    3,000 |                    3,000 |
| 2027 |   28,000 |       0 |   28,000 |                   31,000 |
| 2028 |  100,000 |       0 |  100,000 |                  131,000 |
| 2029 |  240,000 |       0 |  240,000 |                  371,000 |
| 2030 |  480,000 |   3,000 |  477,000 |                  848,000 |
| 2031 |  850,000 |  28,000 |  822,000 |                1,670,000 |
| 2032 | 1,350,000 | 100,000 | 1,250,000 |               2,920,000 |
| 2033 | 1,950,000 | 240,000 | 1,710,000 |               4,630,000 |
| 2034 | 2,600,000 | 480,000 | 2,120,000 |               6,750,000 |
| 2035 | 3,300,000 | 850,000 | 2,450,000 |               9,200,000 |
| 2036 | 4,000,000 | 1,350,000 | 2,650,000 |              11,850,000 |

Production reaches Musk's full 4M/yr stretch target by 2036 — requiring a second high-volume line,
near-flawless execution, and simultaneous best-case global regulatory conditions (all three at once,
historically rare for Tesla). Cumulative active fleet of ~11.85M by 2036 is a **"robotaxi
meaningfully displaces both ride-hail and some private car ownership"** world.

**Honesty check:** the old U.S.-only file deliberately kept its bull case (4.6M cumulative by 2036,
US-only) *below* the "10M+" figures Musk has floated, calling that restraint out as a feature. This
new global bull case, once you take his 4M/yr *production* target at face value and let it flow
through to fleet, lands at ~11.85M globally — squarely in the territory the old file was avoiding.
That's not an error; it's what happens when you stop discounting the production number and start
asking "what if it's actually true and it all becomes fleet." Read Bull here as **"Musk's stated
targets realized in full,"** not as a most-likely outcome — Base is the more grounded central case.

---

## Reconciliation vs. Musk's stated targets

| Scenario | 2036 Produced | % of 2M base target | % of 4M stretch target |
|---|---:|---:|---:|
| Bear | 430,000 | 22% | 11% |
| Base | 2,000,000 | 100% | 50% |
| Bull | 4,000,000 | 200% | 100% |

## Cross-check vs. the U.S.-only deployment file

Old file's cumulative **U.S.** active fleet by 2036: Bear 320,000 / Base 1,430,000 / Bull 4,600,000.
This file's **global** cumulative by 2036: Bear 1,360,000 / Base 5,900,000 / Bull 11,850,000.

Base and Bull here run well above the old U.S.-only numbers for two independent reasons that
compound: (1) global scope adds international fleet the old file didn't count at all, and (2) this
file paces production toward Musk's stated targets instead of implicitly assuming Tesla caps out at
a "single production system's practical ceiling" well below what Musk has actually said — which is
the specific gap that prompted this rebuild. Bear stays closer to the old file's shape because in a
bear world neither manufacturing scale nor international expansion happens anyway.

---

## What this doesn't tell you

This file is a **fleet-count and production model**, not a revenue/profit model — pair it with the
old deployment file's "Revenue & fleet operating profit" section and the cost-per-mile file for
$/mile and P&L. Fare, utilization, and cost-per-mile assumptions from those files still apply; they
weren't re-derived here. A global fleet this large also implies fare and utilization figures may
need revisiting at scale (a lot more competitive/regulatory variance across markets than a
U.S.-only model has to account for) — treat that as an open item, not something this file resolved.

## Caveats

- The 4-year uniform retirement lag is a simplification (real retirements spread across a range of
  years around that point); it understates near-term Removed slightly and could shift the first
  retirement-driven inflection by a year or two either direction.
- International rollout pace (ex-China) is judgment, not evidenced — there's no current Tesla
  robotaxi operation outside the U.S. to calibrate against, unlike the U.S. file which has real
  city-by-city data points.
- Bear/Base/Bull here are Musk-target-anchored on the production side; if Musk's 2M/4M figures
  themselves turn out to be wrong by a wide margin (raised or lowered), this whole table's ceiling
  moves with them — it inherits that single-source risk more than the old file did.

## Sources

- Musk's 2M/yr long-term target and 4M/yr stretch figure — as referenced in user/analyst discussion
  of Tesla's Cybercab production ambitions (2026).
- Vehicle life, mileage cap, and utilization assumptions — companion file "Tesla Cybercab - Operating
  Cost per Mile (Scaled)".
- U.S. fleet pace, current state (hundreds staged / ~45 deployed, NHTSA probe, battery-pack capacity
  citation) — companion file "Tesla Robotaxi Deployment Scenarios 2026-2036" and its sources.
