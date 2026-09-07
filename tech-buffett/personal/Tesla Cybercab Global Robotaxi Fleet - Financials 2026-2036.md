# Tesla Cybercab — Global Robotaxi Fleet Financials, 2026–2036

_Analysis date: 2026-09-07. Builds directly on "Tesla Cybercab Global Robotaxi Fleet 2026-2036"
(fleet/production numbers) and "Tesla Cybercab - Operating Cost per Mile (Scaled)" (unit
economics). Global scope — supersedes the old U.S.-only "Revenue & fleet operating profit" section
in "Tesla Robotaxi Deployment Scenarios 2026-2036" for topline P&L purposes; that file's section
remains useful as the U.S.-only reference point this one is cross-checked against below._

## Method

`Revenue = avg active fleet × miles/vehicle/yr × fare/mi`
`Fleet operating profit = Revenue − (miles × fully-loaded cost/mi)`

- **Avg active fleet** = average of prior- and current-year-end Cumulative Active Fleet from the
  companion fleet file (vehicles added mid-year don't earn a full year's miles).
- **Miles/vehicle/yr** = the utilization ramp from the cost-per-mile file, extended per scenario
  (bear mature ~55k, base mature ~75k, bull mature ~95k mi/yr).
- **Fare/mi** and **fully-loaded cost/mi** = the same base-case unit-economics curve as the old
  U.S.-only file (Tesla undercuts Waymo from the start, fares drift down over time as competition
  and scale both bite), with the same bear/bull adjustments applied (bear: fares ~10% lower, cost
  ~$0.20/mi higher; bull: fares ~same as base, cost ~$0.08/mi lower). **This file does not re-derive
  $/mi economics for international markets** — it applies the U.S.-calibrated curve globally, which
  is a real simplification (see Caveats).
- **Excluded from "profit"** (same scope as the old file): corporate autonomy R&D, charging/depot
  infrastructure capex and its D&A, fleet SG&A above local ops, income tax, catastrophe-year
  insurance tails, platform-licensing or owner-fleet revenue-share economics. This is a fleet-level
  EBIT-like figure, **not** a net-income contribution. All figures nominal (no discounting).

---

## Bear

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |       250 |    25,000 |             0.01 | 0.81 | 2.40 |     −1.59 |          0.0 |             0.0 |               −0.0 |
| 2027 |     2,500 |    35,000 |             0.09 | 0.95 | 1.65 |     −0.71 |          0.1 |             0.1 |               −0.1 |
| 2028 |    12,000 |    38,000 |             0.46 | 0.99 | 1.15 |     −0.16 |          0.5 |             0.5 |               −0.1 |
| 2029 |    39,500 |    44,000 |             1.74 | 0.90 | 0.90 |      0.00 |          1.6 |             1.6 |                0.0 |
| 2030 |    99,250 |    48,000 |             4.76 | 0.81 | 0.80 |     +0.01 |          3.9 |             3.8 |                0.0 |
| 2031 |   202,000 |    51,000 |            10.30 | 0.74 | 0.74 |      0.00 |          7.6 |             7.6 |                0.0 |
| 2032 |   352,500 |    53,000 |            18.68 | 0.68 | 0.70 |     −0.02 |         12.8 |            13.1 |               −0.3 |
| 2033 |   545,000 |    55,000 |            29.98 | 0.65 | 0.68 |     −0.03 |         19.4 |            20.4 |               −1.0 |
| 2034 |   765,000 |    55,000 |            42.08 | 0.63 | 0.67 |     −0.04 |         26.5 |            28.2 |               −1.7 |
| 2035 | 1,000,000 |    55,000 |             55.0 | 0.61 | 0.66 |     −0.05 |         33.7 |            36.3 |               −2.6 |
| 2036 | 1,240,000 |    55,000 |             68.2 | 0.59 | 0.65 |     −0.06 |         40.5 |            44.3 |               −3.8 |
| **Cum. 2026–36** |  |  |  |  |  |  |     **~146** |        **~156** |            **~−9.5** |

Bear doesn't just "hover at breakeven" the way the old U.S.-only file described it — at global scale,
competitive fare pressure (from Waymo, Baidu/local players abroad, human ride-hail undercutting on
price) erodes fare faster than a sub-scale, friction-laden operation can cut costs. It breaks even
briefly around 2029–2031, then **slides into a structurally loss-making business** as the decade
progresses. Never durably profitable — worse than "flat," genuinely negative by the 2030s.

---

## Base

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |       750 |    30,000 |             0.02 | 0.90 | 2.20 |     −1.30 |          0.0 |             0.0 |               −0.0 |
| 2027 |     7,500 |    42,000 |             0.32 | 1.05 | 1.45 |     −0.40 |          0.3 |             0.5 |               −0.1 |
| 2028 |    36,000 |    46,000 |             1.66 | 1.10 | 0.95 |     +0.15 |          1.8 |             1.6 |               +0.2 |
| 2029 |   113,500 |    55,000 |             6.24 | 1.00 | 0.70 |     +0.30 |          6.2 |             4.4 |               +1.9 |
| 2030 |   277,750 |    62,000 |            17.22 | 0.90 | 0.60 |     +0.30 |         15.5 |            10.3 |               +5.2 |
| 2031 |   581,000 |    68,000 |            39.51 | 0.82 | 0.54 |     +0.28 |         32.4 |            21.3 |              +11.1 |
| 2032 | 1,077,500 |    73,000 |            78.66 | 0.76 | 0.50 |     +0.26 |         59.8 |            39.3 |              +20.5 |
| 2033 | 1,800,000 |    75,000 |            135.0 | 0.72 | 0.48 |     +0.24 |         97.2 |            64.8 |              +32.4 |
| 2034 | 2,760,000 |    75,000 |            207.0 | 0.70 | 0.47 |     +0.23 |        144.9 |            97.3 |              +47.6 |
| 2035 | 3,925,000 |    75,000 |            294.4 | 0.68 | 0.46 |     +0.22 |        200.2 |           135.4 |              +64.8 |
| 2036 | 5,225,000 |    75,000 |            391.9 | 0.66 | 0.45 |     +0.21 |        258.6 |           176.3 |              +82.3 |
| **Cum. 2026–36** |  |  |  |  |  |  |     **~817** |        **~551** |            **~266** |

Breakeven ~2028, same as the old U.S.-only file. But the global scale by the outer years is
dramatically larger — see the sanity checks below before treating the 2036 numbers as a "modest
base case."

---

## Bull

| Year | Avg Fleet | Mi/Veh/Yr | Total Miles (B) | Fare | Cost | Profit/mi | Revenue ($B) | Fleet Cost ($B) | Fleet Profit ($B) |
|------|----------:|----------:|-----------------:|-----:|-----:|----------:|-------------:|----------------:|-------------------:|
| 2026 |     1,500 |    35,000 |             0.05 | 0.90 | 2.12 |     −1.22 |          0.0 |             0.1 |               −0.1 |
| 2027 |    17,000 |    48,000 |             0.82 | 1.05 | 1.37 |     −0.32 |          0.9 |             1.1 |               −0.3 |
| 2028 |    81,000 |    55,000 |             4.46 | 1.10 | 0.87 |     +0.23 |          4.9 |             3.9 |               +1.0 |
| 2029 |   251,000 |    65,000 |            16.32 | 1.00 | 0.62 |     +0.38 |         16.3 |            10.1 |               +6.2 |
| 2030 |   609,500 |    75,000 |            45.71 | 0.90 | 0.52 |     +0.38 |         41.1 |            23.8 |              +17.4 |
| 2031 | 1,259,000 |    83,000 |           104.50 | 0.82 | 0.46 |     +0.36 |         85.7 |            48.1 |              +37.6 |
| 2032 | 2,295,000 |    90,000 |           206.55 | 0.76 | 0.42 |     +0.34 |        157.0 |            86.8 |              +70.2 |
| 2033 | 3,775,000 |    95,000 |           358.63 | 0.72 | 0.40 |     +0.32 |        258.2 |           143.5 |             +114.8 |
| 2034 | 5,690,000 |    95,000 |           540.55 | 0.70 | 0.39 |     +0.31 |        378.4 |           210.8 |             +167.6 |
| 2035 | 7,975,000 |    95,000 |           757.63 | 0.68 | 0.38 |     +0.30 |        515.2 |           287.9 |             +227.3 |
| 2036 |10,525,000 |    95,000 |            999.9 | 0.66 | 0.37 |     +0.29 |        659.9 |           370.0 |             +290.0 |
| **Cum. 2026–36** |  |  |  |  |  |  |   **~2,118** |       **~1,186** |            **~932** |

Bull crosses **~1 trillion miles/yr** by 2036. Breakeven ~2028, same as base.

---

## Sanity checks — these numbers are large enough to interrogate before using them

- **Base 2036 revenue (~$259B)** is on the order of 2–3× Tesla's entire current total company
  revenue (all segments combined) — from a single product line that barely exists commercially
  today. That's not disqualifying (this is a 2036 projection for a business most people don't
  believe will get this big), but it means "Base" here is really "a genuinely bullish outcome that
  isn't the most-aggressive scenario," not "the modest, likely case."
- **Global ride-hail industry today** (Uber, Didi, Lyft, Grab, Bolt, Ola combined) does gross
  bookings on the order of $150–250B/yr. **Base 2036 revenue alone would exceed that entire current
  industry**; **Bull 2036 revenue (~$660B) would be roughly 3–4× it.** For this to be revenue rather
  than a fantasy, either (a) cheap driverless fares expand the total ride-hail + car-ownership-
  replacement market well beyond its current size (the thesis this whole model assumes), or (b)
  Tesla captures share other operators would otherwise have kept. Both are plausible directionally;
  neither is close to demonstrated yet.
- **Fare sensitivity dominates at this scale.** At 2036 base mileage (~392B mi), every **$0.10/mi**
  of fare = **~$39B** of revenue and profit (cost is fare-independent). At bull mileage (~1,000B mi),
  it's **~$100B** per $0.10/mi. The single most judgment-laden input in this whole file (the fare
  path) swings the outer-year numbers by tens to a hundred billion dollars either way.
- **This still doesn't mean base is "wrong."** The fleet numbers underneath it were the ones you
  already sanity-checked and found more plausible than the prior U.S.-only version. This section
  exists so the resulting dollar figures get the same scrutiny the fleet figures did — big fleet
  numbers were always going to produce big dollar numbers once you multiply by fare.

---

## Cross-check vs. the old U.S.-only revenue section

| | Bear 2036 Rev | Bear 2036 Profit | Base 2036 Rev | Base 2036 Profit | Bull 2036 Rev | Bull 2036 Profit |
|---|---:|---:|---:|---:|---:|---:|
| Old file (U.S.-only) | $9.9B | ~$0.0B | $68.1B | $21.7B | $229B | $85.9B |
| This file (global) | $40.5B | −$3.8B | $258.6B | $82.3B | $659.9B | $290.0B |
| Ratio | ~4.1× | n/a | ~3.8× | ~3.8× | ~2.9× | ~3.4× |

Base and Bull scale up roughly in line with the underlying fleet ratio (global fleet ≈ 3.8–4.1×
the old U.S.-only fleet by 2036), which is the expected, consistent result. **Bear does not scale
the same way — it turns net loss-making globally where the old file showed it flat.** That's a real
methodology difference (this file's bear cost premium is a flat +$0.20/mi rather than tapering), not
a fleet-scope artifact — worth knowing if you compare the two files directly.

---

## Caveats

- **U.S.-calibrated $/mi applied globally.** Insurance, labor, and depot costs vary a lot by
  country (the cost-per-mile file itself notes depot/insurance/wages "roughly double from Phoenix to
  San Francisco" — international variance is likely wider still, e.g. Gulf-state labor cost vs.
  Western Europe regulatory/insurance cost). No regional $/mi breakout exists yet; this is the
  single biggest simplification in this file.
- **Fare path is a judgment call, globally applied uniformly** — same caveat the old file carried,
  now amplified by scale (see sensitivity above).
- **Nominal dollars, no discounting to present value** — a 2036 dollar here is not risk-adjusted or
  time-valued; don't feed these directly into a DCF without doing that step separately.
- **Bear's flat +$0.20/mi cost premium is a simplification** — a real bear world would likely see
  the premium narrow somewhat as *some* scale is achieved even in a weak scenario, or widen further
  if regulatory friction actively raises compliance/insurance costs. Treat the bear loss trajectory
  as directionally right, not a precise number.
- **Excluded costs (R&D, infra capex/D&A, corporate SG&A, tax) are real and large** — these are
  fleet-operating-profit figures, not anything close to Tesla consolidated net income from robotaxi.
  Don't quote these as "Tesla will earn $X in profit" without that distinction.

## Sources

- Fleet, production, and removal figures — companion file "Tesla Cybercab Global Robotaxi Fleet
  2026-2036".
- Utilization ramp and $/mi cost build — companion file "Tesla Cybercab - Operating Cost per Mile
  (Scaled)".
- Base-case fare path and bear/bull $/mi adjustments — carried forward from "Tesla Robotaxi
  Deployment Scenarios 2026-2036" (Revenue & fleet operating profit section).
