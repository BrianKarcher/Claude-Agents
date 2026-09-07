# Tesla Cybercab — Global Robotaxi Fleet Financials, 2026–2036

_Analysis date: 2026-09-07. Revised same day: vehicle depreciation rebuilt off a $20,000 capitalized
cost (was $28-34k) per the companion cost-per-mile file's updated Depreciation section — this
lowers the fully-loaded $/mi cost curve used below. Builds on "Tesla Cybercab Global Robotaxi Fleet
2026-2036" (fleet/production numbers) and "Tesla Cybercab - Operating Cost per Mile (Scaled)" (unit
economics). Global scope — supersedes the old U.S.-only "Revenue & fleet operating profit" section
in "Tesla Robotaxi Deployment Scenarios 2026-2036" for topline P&L purposes (that older file's
$/mile figures still reflect the original $28-34k depreciation basis and have NOT been updated —
don't mix its numbers with this file's)._

## Method

`Revenue = avg active fleet × miles/vehicle/yr × fare/mi`
`Fleet operating profit = Revenue − (miles × fully-loaded cost/mi)`

- **Avg active fleet** and **miles/vehicle/yr** — unchanged from the prior version of this file
  (sourced from the companion fleet file and the cost-per-mile file's utilization ramp).
- **Fare/mi** — unchanged (Tesla undercuts Waymo from the start, fares drift down over time).
- **Fully-loaded cost/mi** — **rebuilt this revision.** The opex portion (energy, maintenance,
  insurance, teleop, etc.) is unchanged; only the embedded vehicle-depreciation component was
  recalculated at the new $20k capitalized cost (depreciation now ~$0.04-0.09/mi vs. the original
  ~$0.065-0.13/mi — see the cost-per-mile file's Depreciation section). New cost = old cost − old
  depreciation + new depreciation, applied per scenario per year.
- **Excluded from "profit"** (unchanged scope): corporate autonomy R&D, charging/depot
  infrastructure capex and its D&A, fleet SG&A above local ops, income tax, catastrophe-year
  insurance tails, platform-licensing or owner-fleet revenue-share economics. Fleet-level EBIT-like
  figure, **not** a net-income contribution. Nominal dollars, no discounting.

---

## Bear

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |       250 |    25,000 |             0.01 | 0.81 | 2.34 |     −1.53 |          0.0 |             0.0 |               −0.0 |
| 2027 |     2,500 |    35,000 |             0.09 | 0.95 | 1.60 |     −0.66 |          0.1 |             0.1 |               −0.1 |
| 2028 |    12,000 |    38,000 |             0.46 | 0.99 | 1.10 |     −0.11 |          0.5 |             0.5 |               −0.1 |
| 2029 |    39,500 |    44,000 |             1.74 | 0.90 | 0.86 |     +0.04 |          1.6 |             1.5 |               +0.1 |
| 2030 |    99,250 |    48,000 |             4.76 | 0.81 | 0.76 |     +0.05 |          3.9 |             3.6 |               +0.2 |
| 2031 |   202,000 |    51,000 |            10.30 | 0.74 | 0.70 |     +0.04 |          7.6 |             7.2 |               +0.4 |
| 2032 |   352,500 |    53,000 |            18.68 | 0.68 | 0.67 |     +0.01 |         12.8 |            12.5 |               +0.3 |
| 2033 |   545,000 |    55,000 |            29.98 | 0.65 | 0.65 |      0.00 |         19.4 |            19.5 |               −0.1 |
| 2034 |   765,000 |    55,000 |            42.08 | 0.63 | 0.64 |     −0.01 |         26.5 |            26.9 |               −0.4 |
| 2035 | 1,000,000 |    55,000 |             55.0 | 0.61 | 0.63 |     −0.02 |         33.7 |            34.7 |               −1.0 |
| 2036 | 1,240,000 |    55,000 |             68.2 | 0.59 | 0.62 |     −0.03 |         40.5 |            42.3 |               −1.8 |
| **Cum. 2026–36** |  |  |  |  |  |  |     **~146** |        **~149** |            **~−2.4** |

The cheaper vehicle noticeably softens bear: it now shows a genuine breakeven-to-modestly-profitable
window from **2029 through 2032** (peak +$0.4B in 2031) before fare erosion catches up and it slides
back to a loss by 2033. That's a materially better shape than the prior ($28-34k-basis) version,
which never got meaningfully positive and finished at −$3.8B in 2036 (this revision: −$1.8B).
Cumulative profit over the full period is close to flat (~−$2.4B) rather than the prior ~−$9.5B —
bear is now "roughly break-even over the decade," not "a clear net loser."

---

## Base

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |       750 |    30,000 |             0.02 | 0.90 | 2.15 |     −1.25 |          0.0 |             0.0 |               −0.0 |
| 2027 |     7,500 |    42,000 |             0.32 | 1.05 | 1.40 |     −0.35 |          0.3 |             0.4 |               −0.1 |
| 2028 |    36,000 |    46,000 |             1.66 | 1.10 | 0.91 |     +0.19 |          1.8 |             1.5 |               +0.3 |
| 2029 |   113,500 |    55,000 |             6.24 | 1.00 | 0.66 |     +0.34 |          6.2 |             4.1 |               +2.1 |
| 2030 |   277,750 |    62,000 |            17.22 | 0.90 | 0.57 |     +0.33 |         15.5 |             9.8 |               +5.7 |
| 2031 |   581,000 |    68,000 |            39.51 | 0.82 | 0.51 |     +0.31 |         32.4 |            20.2 |              +12.2 |
| 2032 | 1,077,500 |    73,000 |            78.66 | 0.76 | 0.47 |     +0.29 |         59.8 |            37.0 |              +22.8 |
| 2033 | 1,800,000 |    75,000 |            135.0 | 0.72 | 0.45 |     +0.27 |         97.2 |            60.8 |              +36.4 |
| 2034 | 2,760,000 |    75,000 |            207.0 | 0.70 | 0.44 |     +0.26 |        144.9 |            91.1 |              +53.8 |
| 2035 | 3,925,000 |    75,000 |            294.4 | 0.68 | 0.43 |     +0.25 |        200.2 |           126.6 |              +73.6 |
| 2036 | 5,225,000 |    75,000 |            391.9 | 0.66 | 0.42 |     +0.24 |        258.6 |           164.6 |              +94.0 |
| **Cum. 2026–36** |  |  |  |  |  |  |     **~817** |        **~516** |            **~301** |

Breakeven still ~2028 (unchanged — the cost cut widens margin, it doesn't move the crossover, since
opex was already positive-crossing there). 2036 fleet profit rises to **+$94.0B** (was +$82.3B) —
about a 14% lift, entirely from the lower depreciation charge on the cheaper vehicle.

---

## Bull

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |     1,500 |    35,000 |             0.05 | 0.90 | 2.07 |     −1.17 |          0.0 |             0.1 |               −0.1 |
| 2027 |    17,000 |    48,000 |             0.82 | 1.05 | 1.33 |     −0.28 |          0.9 |             1.1 |               −0.2 |
| 2028 |    81,000 |    55,000 |             4.46 | 1.10 | 0.84 |     +0.26 |          4.9 |             3.7 |               +1.2 |
| 2029 |   251,000 |    65,000 |            16.32 | 1.00 | 0.59 |     +0.41 |         16.3 |             9.6 |               +6.7 |
| 2030 |   609,500 |    75,000 |            45.71 | 0.90 | 0.50 |     +0.40 |         41.1 |            22.9 |              +18.3 |
| 2031 | 1,259,000 |    83,000 |           104.50 | 0.82 | 0.44 |     +0.38 |         85.7 |            46.0 |              +39.7 |
| 2032 | 2,295,000 |    90,000 |           206.55 | 0.76 | 0.40 |     +0.36 |        157.0 |            82.6 |              +74.4 |
| 2033 | 3,775,000 |    95,000 |           358.63 | 0.72 | 0.38 |     +0.34 |        258.2 |           136.3 |             +121.9 |
| 2034 | 5,690,000 |    95,000 |           540.55 | 0.70 | 0.37 |     +0.33 |        378.4 |           200.0 |             +178.4 |
| 2035 | 7,975,000 |    95,000 |           757.63 | 0.68 | 0.36 |     +0.32 |        515.2 |           272.8 |             +242.4 |
| 2036 |10,525,000 |    95,000 |            999.9 | 0.66 | 0.35 |     +0.31 |        659.9 |           350.0 |             +309.9 |
| **Cum. 2026–36** |  |  |  |  |  |  |   **~2,118** |       **~1,125** |            **~993** |

Breakeven still ~2028. 2036 fleet profit rises to **+$309.9B** (was +$290.0B), a ~7% lift.

---

## Sanity checks — updated

- **Base 2036 fleet profit (~$94.0B)** and **Bull (~$309.9B)** are both higher than the prior
  ($28-34k-basis) version, purely from the cheaper vehicle's lower depreciation charge — the
  fleet-size, fare, and opex assumptions are all unchanged. The scale-of-the-business caveats from
  the prior version still apply in full: Base 2036 revenue (~$259B, unchanged — depreciation doesn't
  touch revenue) still exceeds the entire current global ride-hail industry's gross bookings.
- **Bear's improvement is the more interesting result.** A cheaper vehicle doesn't just pad an
  already-profitable scenario — it can flip a "modest structural loser" into "roughly breakeven,
  with a genuine multi-year profitable window." That's a useful, non-obvious takeaway: in a
  capital-intensive fleet business, unit cost discipline matters most exactly in the scenario where
  everything else (fares, demand, regulation) is going against you.
- **Fare sensitivity is unchanged** (it was never a function of depreciation): still ~$39B per
  $0.10/mi at base 2036 mileage, ~$100B per $0.10/mi at bull.

---

## Cross-check vs. the old U.S.-only revenue section

Not re-run this revision — that file still uses the original $28-34k depreciation basis. Comparing
it directly to this file now mixes two different cost bases; treat the comparison table from the
prior version of this file as describing the $28-34k world, not this one.

---

## Caveats

- **U.S.-calibrated $/mi applied globally** (unchanged caveat) — international cost variance still
  not modeled.
- **Fare path is a judgment call, globally applied uniformly** (unchanged).
- **Nominal dollars, no discounting to present value** (unchanged).
- **The $20k capitalized-cost assumption is new and below this project's original $28-34k estimate**
  for the vehicle — see the cost-per-mile file's Depreciation section for the reasoning. If that
  turns out to be too aggressive, every Fleet Profit figure in this revision should be read as an
  upper bound relative to the original ~$0.065-0.13/mi depreciation basis.
- **Bear's flat +cost-premium structure relative to base carries over unchanged** — same caveat as
  before about it being a simplification, now interacting with a lower depreciation base too.
- **Excluded costs (R&D, infra capex/D&A, corporate SG&A, tax) are real and large** — these remain
  fleet-operating-profit figures, not Tesla consolidated net income from robotaxi. The companion DCF
  file layers those in.

## Sources

- Fleet, production, and removal figures — companion file "Tesla Cybercab Global Robotaxi Fleet
  2026-2036".
- Utilization ramp and $/mi cost build, incl. the revised $20k depreciation schedule — companion
  file "Tesla Cybercab - Operating Cost per Mile (Scaled)".
- Base-case fare path and bear/bull opex adjustments — carried forward from "Tesla Robotaxi
  Deployment Scenarios 2026-2036" (Revenue & fleet operating profit section), with the depreciation
  component re-derived at $20k for this revision.
