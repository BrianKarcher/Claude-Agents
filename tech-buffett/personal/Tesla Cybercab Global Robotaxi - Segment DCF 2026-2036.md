================================================================================
TESLA CYBERCAB — GLOBAL ROBOTAXI SEGMENT DCF
Standalone segment valuation, NOT a Tesla per-share price target
Date: September 7, 2026 (revised three times same day: (1) vehicle capex
$30k -> $20k, (2) depreciation schedule in the cost-per-mile file rebuilt
off the same $20k basis, fixing the D&A/capex mismatch flagged in revision
1, (3) discount rates lowered — Base 13.0%->10.0%, Bull 11.0%->9.0%,
Bear 15.5%->13.0%)
Sources: "Tesla Cybercab Global Robotaxi Fleet 2026-2036" (fleet/production),
         "Tesla Cybercab Global Robotaxi Fleet - Financials 2026-2036"
         (fleet operating profit, now on the $20k depreciation basis), "Tesla
         Cybercab - Operating Cost per Mile (Scaled)" (unit economics,
         vehicle life, $20k depreciation schedule). DCF conventions (unlevered
         FCF = NOPAT + D&A - Capex, 15% flat tax) follow the same house
         methodology as this folder's other DCFs (DCF-AMD-2026-09-02.txt
         etc.), adapted for a segment rather than a whole public company.
================================================================================

WHAT THIS FILE IS (READ FIRST)
-------------------------------
This is a DCF on the Cybercab robotaxi business AS IF IT WERE A STANDALONE
COMPANY — an enterprise value, not a per-share price target. Combining this
with the rest of Tesla into a sum-of-parts TSLA price target is a separate
exercise this file does not attempt.

**Revision 2 note (fixes revision 1's flagged inconsistency):** revision 1
cut vehicle capex to $20k/unit but kept depreciating those vehicles on a
schedule built for a $28-34k vehicle, overstating the non-cash D&A add-back.
That's now fixed — the cost-per-mile file's Depreciation section was rebuilt
at $20k, which also lowered the fully-loaded $/mi cost figures the financials
file uses, which RAISES Fleet Operating Profit. The two effects mostly
offset in free cash flow (see "Why the FCF barely moved" below) but Fleet
Operating Profit, Segment EBIT, and enterprise value are all now higher than
revision 1's numbers, and internally consistent for the first time.

WHY THE FCF BARELY MOVED, EVEN THOUGH FLEET OPERATING PROFIT DID
------------------------------------------------------------------
Lowering the depreciation schedule shifts a fixed dollar amount from the
"fleet cost" line into the "D&A add-back" line — it's the same non-cash
charge, just correctly sized instead of overstated. In a DCF, if that dollar
amount isn't taxed (EBIT still negative), it nets to exactly zero in FCF:
EBIT rises by the same amount D&A add-back falls, and the two changes
cancel. Where EBIT is already POSITIVE (base 2030+, bull 2029+), the higher
taxable income costs a little real tax — so FCF ends up VERY SLIGHTLY LOWER
than revision 1's (mistaken) version in those years, and the base case's
FCF-positive milestone slips from 2031 back to 2032. Fleet Operating Profit,
Segment EBIT, and NOPAT are all meaningfully higher; free cash flow is
almost unchanged. This is a useful general lesson: fixing a D&A/capex
mismatch mostly reallocates reported profit, it doesn't create or destroy
cash.

THE HEADLINE FINDING, BEFORE THE NUMBERS
-----------------------------------------
Free cash flow turns positive in **2032 in the base case** (2031 in
revision 1's inconsistent version; 2033 at the original $30k-capex/$28-34k-
depreciation basis). Cumulative cash burn 2026-2031 (base case) is roughly
**-$12.7B** — essentially the same funding requirement as revision 1, just
one year later to clear. Bear's cumulative FCF (-$57.9B) and bull's
(+$577.0B) are both within ~1% of revision 1's figures. **The $20k unit-cost
change still does almost all the work; fixing the depreciation basis behind
it is mostly a bookkeeping correction, not a new cash-flow driver.**


================================================================================
SECTION 1 — ASSUMPTIONS (UPDATED THIS REVISION IN BOLD)
================================================================================

VEHICLE CAPEX: $20,000/unit produced (unchanged from revision 1), applied to
GROSS Produced units.

INFRASTRUCTURE CAPEX: $4,000 per NET-ADD vehicle (unchanged).

**VEHICLE D&A (added back to NOPAT as non-cash) — REBUILT THIS REVISION:**
Total Miles x depreciation-$/mile, now using the cost-per-mile file's
$20k-capitalized-cost depreciation schedule (previously $28-34k-based,
which is what created the inconsistency flagged in revision 1). New
depreciation-$/mi by scenario/phase (~2/3 of the old figures, since
depreciation scales linearly with capitalized cost):
                    Early    Mid      Mature    Lean/Bull-mature
  Base ($/mi)        0.09     0.07     0.05           n/a
  Bear ($/mi)        ~0.10-0.13 (interpolated, lower utilization)  0.067 mature
  Bull ($/mi)        ~0.07-0.09 (interpolated, higher utilization) 0.043 mature

R&D ALLOCATION (unchanged):
                 2026  2027  2028  2029  2030  2031  2032  2033  2034  2035  2036
  Bear ($B)       1.0   1.2   1.4   1.6   1.8   2.0   2.1   2.2   2.3   2.4   2.5
  Base ($B)       1.2   1.5   1.8   2.1   2.4   2.7   3.0   3.2   3.4   3.6   3.8
  Bull ($B)       1.5   2.0   2.5   3.0   3.5   4.0   4.3   4.6   4.8   5.0   5.2

SG&A ALLOCATION (unchanged):
                 2026  2027  2028  2029  2030  2031  2032  2033  2034  2035  2036
  Bear ($B)       0.3   0.4   0.5   0.6   0.7   0.8   0.9   1.0   1.1   1.2   1.3
  Base ($B)       0.4   0.5   0.7   0.9   1.1   1.3   1.5   1.7   1.9   2.1   2.3
  Bull ($B)       0.5   0.7   1.0   1.3   1.6   1.9   2.2   2.5   2.8   3.1   3.4

TAX RATE: 15% flat (unchanged), applied only to positive segment pre-tax
income.

DISCOUNT RATES / TERMINAL ASSUMPTIONS (revised 2026-09-07, third revision):
  BASE: 10.0% WACC (was 13.0%), 3.0% TGR, 16x exit multiple
  BULL: 9.0% WACC (was 11.0%), 3.5% TGR, 20x exit multiple
  BEAR: 13.0% WACC (was 15.5%), terminal value = $0


================================================================================
SECTION 2 — SEGMENT FCF BUILD ($20k vehicle capex, $20k-basis depreciation)
================================================================================

BASE
                        2026    2027    2028    2029    2030    2031    2032    2033    2034    2035    2036
Fleet Op. Profit ($B)  -0.03   -0.11   +0.32   +2.12   +5.68  +12.25  +22.81  +36.45  +53.82  +73.60  +94.05
Less R&D                1.20    1.50    1.80    2.10    2.40    2.70    3.00    3.20    3.40    3.60    3.80
Less SG&A                0.40    0.50    0.70    0.90    1.10    1.30    1.50    1.70    1.90    2.10    2.30
Segment EBIT ($B)      -1.63   -2.11   -2.19   -0.88   +2.18   +8.25  +18.31  +31.55  +48.52  +67.90  +87.95
Tax (15%, floor $0)     0.00    0.00    0.00    0.00    0.33    1.24    2.75    4.73    7.28   10.19   13.19
NOPAT ($B)             -1.63   -2.11   -2.19   -0.88   +1.86   +7.01  +15.56  +26.82  +41.24  +57.72  +74.76
+ Vehicle D&A (new)      0.00    0.03    0.14    0.46    1.15    2.37    4.48    7.20   11.03   15.69   20.89
- Vehicle capex ($20k)   0.03    0.24    0.90    2.20    4.40    8.00   13.00   19.00   26.00   33.00   40.00
- Infra capex            0.01    0.05    0.18    0.44    0.87    1.55    2.42    3.36    4.32    5.00    5.40
FREE CASH FLOW ($B)    -1.66   -2.37   -3.13   -3.06   -2.27   -0.17   +4.62  +11.66  +21.95  +35.41  +50.25

Turns FCF-positive in **2032** (revision 1: 2031 — the one-year slip is the
small tax leakage from correctly taxing the higher EBIT). Cumulative FCF
2026-2031 (before turning positive): ~-$12.7B. Cumulative FCF 2026-2036:
~+$111.2B.

BULL
                        2026    2027    2028    2029    2030    2031    2032    2033    2034    2035    2036
Fleet Op. Profit ($B)  -0.06   -0.23   +1.16   +6.69  +18.28  +39.71  +74.36 +121.93 +178.39 +242.44 +309.93
Less R&D                1.50    2.00    2.50    3.00    3.50    4.00    4.30    4.60    4.80    5.00    5.20
Less SG&A                0.50    0.70    1.00    1.30    1.60    1.90    2.20    2.50    2.80    3.10    3.40
Segment EBIT ($B)      -2.06   -2.93   -2.34   +2.39  +13.18  +33.81  +67.86 +114.83 +170.79 +234.34 +301.33
Tax (15%, floor $0)     0.00    0.00    0.00    0.36    1.98    5.07   10.18   17.22   25.62   35.15   45.20
NOPAT ($B)             -2.06   -2.93   -2.34   +2.03  +11.21  +28.74  +57.68  +97.61 +145.17 +199.19 +256.13
+ Vehicle D&A (new)      0.00    0.06    0.30    0.93    2.29    4.91    9.29   15.42   23.24   32.58   43.00
- Vehicle capex ($20k)   0.06    0.56    2.00    4.80    9.60   17.00   27.00   39.00   52.00   66.00   80.00
- Infra capex            0.01    0.11    0.40    0.96    1.91    3.29    5.00    6.84    8.48    9.80   10.60
FREE CASH FLOW ($B)    -2.13   -3.54   -4.44   -2.80   +1.99  +13.36  +34.97  +67.19 +107.93 +155.97 +208.53

Turns FCF-positive in **2030**, same as revision 1. Cumulative FCF 2026-2029
(before turning positive): ~-$12.9B. Cumulative FCF 2026-2036: ~+$577.0B.

BEAR
                        2026    2027    2028    2029    2030    2031    2032    2033    2034    2035    2036
Fleet Op. Profit ($B)  -0.02   -0.06   -0.05   +0.07   +0.24   +0.39   +0.26   -0.06   -0.42   -0.99   -1.77
Less R&D                1.00    1.20    1.40    1.60    1.80    2.00    2.10    2.20    2.30    2.40    2.50
Less SG&A                0.30    0.40    0.50    0.60    0.70    0.80    0.90    1.00    1.10    1.20    1.30
Segment EBIT ($B)      -1.32   -1.66   -1.95   -2.13   -2.26   -2.41   -2.74   -3.26   -3.82   -4.59   -5.57
Tax                     0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00    0.00
NOPAT ($B)             -1.32   -1.66   -1.95   -2.13   -2.26   -2.41   -2.74   -3.26   -3.82   -4.59   -5.57
+ Vehicle D&A (new)      0.00    0.01    0.04    0.14    0.37    0.74    1.29    2.01    2.82    3.69    4.57
- Vehicle capex ($20k)   0.01    0.08    0.30    0.80    1.60    2.60    3.80    5.00    6.20    7.40    8.60
- Infra capex            0.00    0.02    0.06    0.16    0.32    0.50    0.70    0.84    0.92    0.96    0.96
FREE CASH FLOW ($B)    -1.33   -1.75   -2.27   -2.95   -3.81   -4.77   -5.95   -7.09   -8.12   -9.26  -10.56

Never turns positive, same qualitative shape as revision 1 (bear's EBIT is
never positive, so there's no tax leakage — this scenario is essentially
unchanged by the depreciation fix, as the "why the FCF barely moved"
argument predicts). Cumulative FCF 2026-2036: ~-$57.9B.


================================================================================
SECTION 3 — DCF & TERMINAL VALUE
================================================================================

Explicit period 2027-2036 (10 years, discounted); 2026 is the anchor year.
**Discount rates lowered this revision** (Base 13.0%->10.0%, Bull
11.0%->9.0%, Bear 15.5%->13.0%) — TGR and exit multiples unchanged.

BASE (10.0% WACC, 3.0% TGR, 16x exit multiple)
  Sum of PV of explicit FCFs (2027-2036):                       $44.5B  (was $33.9B at 13.0% WACC)
  Terminal-year (2036) FCF:                                     $50.2B  (unchanged — WACC doesn't affect the FCF build)
  TV (perpetuity, g=3.0%): 50.25 x 1.03 / (0.10-0.03) =        $739.3B  -> PV $285.0B
  TV (exit multiple, 16x): 50.25 x 16 =                        $804.0B  -> PV $309.9B
  Average PV of TV:                                                     $297.5B
  ENTERPRISE VALUE (Base):                                       ~$342.0B  (was ~$228.5B)

BULL (9.0% WACC, 3.5% TGR, 20x exit multiple)
  Sum of PV of explicit FCFs (2027-2036):                       $272.6B  (was $232.7B at 11.0% WACC)
  Terminal-year (2036) FCF:                                     $208.5B  (unchanged)
  TV (perpetuity, g=3.5%): 208.53 x 1.035 / (0.09-0.035) =    $3,924.2B  -> PV $1,657.6B
  TV (exit multiple, 20x): 208.53 x 20 =                      $4,170.6B  -> PV $1,761.6B
  Average PV of TV:                                                    $1,709.6B
  ENTERPRISE VALUE (Bull):                                       ~$1,982.2B  (was ~$1,473.9B)

BEAR (13.0% WACC, terminal value = $0)
  Sum of PV of explicit FCFs (2027-2036):                       -$25.4B  (was -$22.3B at 15.5% WACC)
  Terminal value:                                                    $0
  ENTERPRISE VALUE (Bear):                                        ~-$25.4B  (was ~-$22.3B)

Base and Bull rise substantially (+50% and +34% respectively) on the lower
discount rate — the DCF's outer-year FCFs are enormous, so shaving 2-3
points off WACC has an outsized effect on their present value. **Bear gets
MORE negative, not less**, despite also having a lower WACC — with a $0
terminal value and no positive FCF ever, discounting less heavily just means
the (persistently negative) explicit-period cash flows count for more, not
less. This is a useful reminder that "lower discount rate = higher value"
only holds when the underlying cash flows are eventually positive.


================================================================================
SECTION 4 — SENSITIVITY (BASE CASE)
================================================================================

TABLE A: ENTERPRISE VALUE ($B) — WACC x TERMINAL GROWTH RATE (perpetuity
method only, for comparability across cells)

WACC \ TGR    2.0%      3.0%      4.0%
8.5%         $399.9    $467.3    $564.8
10.0%        $291.5    $329.6    $380.3   <- base case (perpetuity-only)
11.5%        $220.5    $243.9    $273.5

TABLE B: ENTERPRISE VALUE ($B) — EXIT MULTIPLE (10.0% WACC)
  10x  $238.2
  12x  $277.0
  14x  $315.7
  16x  $354.5   <- exit-multiple-only version of the base case
  18x  $393.2
  20x  $431.9

Every cell is meaningfully higher than the prior (13.0% WACC) version — as
expected, since this grid is the most WACC-sensitive part of the whole file
by construction.


================================================================================
SECTION 5 — SCENARIO SUMMARY
================================================================================

Scenario   WACC    TGR    Exit   Cum. FCF 2026-36   2036 FCF   Enterprise Value   Per TSLA Share*
BULL       9.0%   3.5%    20x         +$577.0B       $208.5B     ~$1,982.2B        ~$559.94
BASE      10.0%   3.0%    16x         +$111.2B        $50.2B       ~$342.0B         ~$96.61
BEAR      13.0%    n/a    n/a          -$57.9B       -$10.6B        ~-$25.4B         ~-$7.18

Probability-weighted (20% Bull / 45% Base / 35% Bear, unchanged weights):
  0.20 x 1,982.2 + 0.45 x 342.0 + 0.35 x (-25.4) = ~$541.5B  -> **~$152.97/share**

Simple average of the three scenarios: ~$766.3B -> **~$216.47/share**

*Per-share figures divide the segment's enterprise value by Tesla's Q2 2026
diluted weighted-average share count of ~3.54B shares (source: Tesla 10-Q,
via GuruFocus/AlphaQuery). **This is the robotaxi segment's value ADDED to a
TSLA share, not a TSLA price target** — it excludes Tesla's auto, energy,
and services businesses entirely, and doesn't net any corporate cash or debt
(this is a segment EV, not a consolidated equity bridge). To get anywhere
near an actual TSLA fair value you'd add this to an independent valuation of
the rest of Tesla. For calibration only: TSLA closed around **$352.89** on
Sept 6, 2026 — so Base alone (~$96.61) would be roughly 27% of the current
share price, and Bull alone (~$559.94) exceeds the entire current share
price by itself. Share count is held flat at 3.54B (no SBC dilution modeled
over the decade) — a real simplification given Tesla's history of ongoing
equity compensation issuance.


================================================================================
SECTION 6 — WHAT THIS DOESN'T TELL YOU / OPEN ITEMS
================================================================================

- **The D&A/capex mismatch flagged in revision 1 is resolved.** No further
  action needed there unless the $20k unit-cost assumption itself changes
  again, in which case both the capex line here AND the depreciation
  schedule in the cost-per-mile file need to move together, as they now do.
- **No TSLA per-share translation** (unchanged) — segment enterprise value
  only.
- **Funding reality check, updated:** base needs ~$12.7B of cumulative
  funding before turning cash-generative (vs. ~$12.4B in revision 1's
  inconsistent version — the difference is the one-year-later crossover);
  bull ~$12.9B (unchanged); bear ~$57.9B over the decade with no turnaround
  (unchanged).
- **R&D/SG&A allocations, infra capex, and the $20k unit-cost figure remain
  judgment calls**, not sourced from any Tesla disclosure. $20k sits below
  this project's original $28-34k cost-per-mile estimate for the vehicle —
  still worth treating as a "meaningfully cheaper than currently estimated"
  case rather than a refinement, per the cost-per-mile file's own note.

================================================================================
DISCLOSURES & LIMITATIONS
================================================================================
- CONDITIONAL VALUATION built entirely on the fleet and financials files in
  this folder, which are themselves scenario-planning exercises, not
  forecasts. Every uncertainty flagged in those files flows through here and
  is compounded by this file's own assumptions (R&D/SG&A allocation, unit
  capex, discount rates).
- Personal, standalone research file, outside the tech-buffett Init -> Deep
  Dive -> DCF pipeline. Does NOT qualify Tesla (or this segment) for
  portfolio purchase under CLAUDE.md / the agent ruleset. Not investment
  advice.
================================================================================
