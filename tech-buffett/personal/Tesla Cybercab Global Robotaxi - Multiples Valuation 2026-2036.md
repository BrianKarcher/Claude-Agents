================================================================================
TESLA CYBERCAB — GLOBAL ROBOTAXI SEGMENT: MULTIPLES-ONLY VALUATION
A comps-based alternative to the DCF, not a replacement for its findings
Date: September 7, 2026
Sources: "Tesla Cybercab Global Robotaxi Fleet - Financials 2026-2036"
         (Revenue, Fleet Operating Profit), "Tesla Cybercab Global Robotaxi -
         Segment DCF 2026-2036" (Segment EBIT, D&A add-back, R&D/SG&A
         allocations — reused here to build Segment EBITDA). Public-company
         comp multiples pulled live via web search Sept 7, 2026 (Uber, Lyft,
         Sixt) — see Sources section for links.
================================================================================

WHY THIS FILE EXISTS
----------------------
The DCF file's own numbers make the case against relying on it alone: base
case free cash flow is negative for six straight years (2026-2031, roughly
-$12.7B cumulative) before turning positive, which means most of that DCF's
value comes from the terminal value, not the explicit cash flows — the
early-years burn is real information about funding risk, but it tells you
almost nothing about what the business is actually worth once built. A pure
multiples approach sidesteps this entirely: it doesn't need a single dollar
of the 2026-2031 cash flow forecast. It just asks "if the market values
comparable businesses at N times revenue or EBITDA, what would THIS business
be worth once it looks like [2030 / 2033 / 2036's projected financials]?"
That's a genuinely different question from the DCF's, not just a different
way of answering the same one — and the two methods disagreeing tells you
something real (see Section 5).

THE HEADLINE FINDING, BEFORE THE NUMBERS
-------------------------------------------
Multiples valuation does NOT produce more conservative numbers than the DCF
— for base and bull, it produces LARGER ones, often by 3-5x. That's not a
bug in this file; it's a structural feature of applying a growth-company
multiple to a still-fast-growing reference year. A DCF's terminal value
explicitly assumes growth decelerates to ~3%/yr forever; a multiple borrowed
from today's market instead implicitly assumes the business keeps growing
roughly the way comparable growth companies do — which, if the reference
year is still growing 30-150%/yr (true at every year tested here), is a much
more optimistic assumption than the DCF's terminal growth rate. **Which
method is "right" depends entirely on whether you believe growth really
craters to GDP-like rates right at your reference year, or keeps compounding
past it** — and that's a judgment call, not something either method proves.


================================================================================
SECTION 1 — COMPARABLE COMPANY MULTIPLES (pulled live, Sept 7, 2026)
================================================================================

| Company | EV/Revenue | EV/EBITDA | Notes |
|---|--:|--:|---|
| **Uber** | ~2.7x | ~20-22x | Asset-light marketplace; takes a ~20-25% commission on gross bookings — Uber's "Revenue" is that commission, NOT the full fare. Implied EBITDA margin ~13%. |
| **Lyft** | ~1.2x | ~35-41x (LTM, noisy) / ~7-12x (2026E, Wolfe Research) | Smaller, thinner-margin Uber peer; LTM EV/EBITDA is inflated by a low current-year EBITDA base — the forward estimate is more representative. |
| **Sixt** (fleet-owning mobility/rental) | n/a (not sourced) | ~5.3x | Asset-heavy comp: owns its fleet, like Cybercab does and Uber/Lyft don't. Much lower multiple than the asset-light platforms. |
| **Hertz / Avis** | n/a | n/a (distressed) | Asset-heavy, over-levered, persistently loss-making — negative stockholders' equity at Avis. The cautionary comp for what "owns a depreciating fleet, doesn't make money" looks like to the market. |

**The critical adjustment before using any of this:** Cybercab's projected
"Revenue" in the companion financials file is the **entire fare** — Tesla
operates the fleet directly, so there's no driver payout to net out. That
makes it economically equivalent to Uber's **gross bookings**, not Uber's
reported revenue (the commission on those bookings). Applying Uber's 2.7x
EV/Revenue directly to Cybercab's fare-based "Revenue" would be comparing a
100%-of-fare number to a ~20%-of-fare multiple — a fivefold overstatement
baked in before any judgment is even applied. This file uses **EV/EBITDA as
the primary method** for exactly this reason: EBITDA nets out the
driver-payout-equivalent cost regardless of how "Revenue" is defined, so it
doesn't inherit this mismatch. EV/Revenue is shown only as a **derived
cross-check** (see Section 3), not as an independent second method.


================================================================================
SECTION 2 — SEGMENT EBITDA (from the DCF file's Segment EBIT + D&A add-back)
================================================================================

Segment EBITDA = Segment EBIT (Fleet Op. Profit − R&D − SG&A) + Vehicle D&A
add-back, at three reference years.

| | 2030 | 2033 | 2036 |
|---|--:|--:|--:|
| **Bear** Revenue ($B) | 3.9 | 19.4 | 40.5 |
| **Bear** EBITDA ($B) | -1.89 | -1.25 | -1.00 |
| **Base** Revenue ($B) | 15.5 | 97.2 | 258.6 |
| **Base** EBITDA ($B) | 3.33 | 38.75 | 108.84 |
| **Base** EBITDA margin | 21% | 40% | 42% |
| **Bull** Revenue ($B) | 41.1 | 258.2 | 659.9 |
| **Bull** EBITDA ($B) | 15.47 | 130.25 | 344.33 |
| **Bull** EBITDA margin | 38% | 50% | 52% |

**Bear's EBITDA is negative at all three reference years** — it never
crosses into positive EBITDA territory (peak is -$0.90B around 2035; see the
DCF file). EV/EBITDA is mathematically undefined/meaningless here; Section 4
handles bear separately.

Base and bull EBITDA margins (21-52%) run well above Uber's implied ~13%
margin — the structural reason is the same driver-payout point from
Section 1: Tesla keeps the whole fare, Uber keeps a commission, so of course
the segment's margin on its own (much larger) revenue base looks richer.
This is not this file overstating margins; it's a real structural
consequence of the vertically-integrated fleet-operator model versus a
marketplace model, and it's exactly why the EV/EBITDA multiple chosen below
is set BELOW Uber's despite the higher margin (see Section 3 rationale).


================================================================================
SECTION 3 — CHOSEN MULTIPLES & VALUATION (BASE AND BULL)
================================================================================

EV/EBITDA multiples chosen, declining over time as growth decelerates
(base revenue growth: ~150%/yr in 2030 -> ~83%/yr around 2033 -> ~39%/yr by
2036; bull stays faster throughout):

           2030    2033    2036    Rationale
  BASE      14x     12x     10x    Below Uber's ~21x throughout — discount
                                    for real fleet-ownership/residual-value
                                    risk, regulatory/safety-case risk Uber's
                                    asset-light model doesn't carry, and
                                    because this is a decade-out FORECAST
                                    margin, not Uber's already-realized one.
  BULL      18x     15x     13x    Smaller discount to Uber — bull assumes
                                    best-in-class execution and a de-risked
                                    regulatory environment, closer to (but
                                    still below) Uber's multiple.

BASE VALUATION (EV/EBITDA method)
  2030: $3.33B x 14 =  $46.6B
  2033: $38.75B x 12 = $465.0B
  2036: $108.84B x 10 = $1,088.4B

BULL VALUATION (EV/EBITDA method)
  2030: $15.47B x 18 =  $278.5B
  2033: $130.25B x 15 = $1,953.8B
  2036: $344.33B x 13 = $4,476.3B

DERIVED EV/REVENUE CROSS-CHECK (= EV ÷ Revenue, for comparison to Uber's
2.7x / Lyft's 1.2x — remembering these are on a fare-equivalent, not
take-rate, revenue base, so a HIGHER multiple than Uber's is defensible
despite the "asset-heavy discount" logic above, precisely because 100% of
this revenue can become profit at maturity, vs. only Uber's commission
slice):

           2030    2033    2036
  BASE     3.0x    4.8x    4.2x
  BULL     6.8x    7.6x    6.8x

These implied revenue multiples exceed Uber's 2.7x, which is the expected
and correct result once you account for the gross-bookings-vs-take-rate
distinction (Section 1) — a red flag would be if these came out BELOW 2.7x,
which would suggest the EBITDA multiple was too rich for the margin implied.
They don't, so the two views are at least internally consistent.

PRESENT VALUE (discounted back to 2026 at the DCF file's own WACC — revised
2026-09-07 to 10.0% base, 9.0% bull — purely so these numbers are comparable
to the DCF's enterprise values; this is NOT part of a "pure" multiples
method, which by design doesn't discount anything):

           Reference year   Future EV    PV to 2026    Per TSLA Share*
  BASE          2030          $46.6B        $31.8B          $8.98
  BASE          2033         $465.0B       $238.6B         $67.40
  BASE          2036       $1,088.4B       $419.6B        $118.53
  BULL          2030         $278.5B       $197.3B         $55.73
  BULL          2033       $1,953.8B     $1,068.6B        $301.86
  BULL          2036       $4,476.3B     $1,890.6B        $534.07

*Per-share = PV ÷ Tesla's Q2 2026 diluted weighted-average share count
(~3.54B shares, per Tesla's 10-Q). Same caveat as the DCF file: this is the
robotaxi segment's value added to a TSLA share, not a price target — it
excludes the rest of Tesla and doesn't net corporate cash/debt. For
calibration, TSLA closed around $352.89 on Sept 6, 2026.


================================================================================
SECTION 4 — BEAR: WHY MULTIPLES DON'T REALLY WORK HERE
================================================================================

Bear's EBITDA is negative at every reference year (-$1.89B in 2030 down to
-$1.00B in 2036 — it doesn't cross zero, just gets slightly less negative).
There is no meaningful EV/EBITDA multiple to apply to a negative number.
The honest options are:

1. **Defer to the DCF's answer.** The DCF file already found bear's
   enterprise value is NEGATIVE (~-$22.3B) under a wind-down assumption —
   i.e., a rational owner stops funding this scenario. A multiples approach
   can't improve on that; it can only fail to produce a number at all.
2. **Apply a distressed-comp revenue floor**, in the spirit of Hertz/Avis
   trading near or below their asset value while structurally loss-making.
   At a rough 0.3-0.5x revenue floor (own judgment, not comp-sourced — no
   clean Hertz/Avis multiple exists to cite, see Section 1):
     2030: $3.9B x 0.4 = $1.6B
     2033: $19.4B x 0.4 = $7.8B
     2036: $40.5B x 0.4 = $16.2B
   PV to 2026 at 13.0% (revised 2026-09-07, was 15.5%): ~$1.0B / $3.3B /
   $4.8B respectively — **per TSLA share (÷3.54B): ~$0.28 / $0.93 / $1.36.**
   Trivial next to base/bull, which is the point: bear isn't a smaller
   version of the other scenarios, it's a scenario where this segment barely
   registers on a TSLA share at all.

Treat option 2 as a rough floor on liquidation-ish value, not a real
valuation — it exists so bear has SOME number in the summary table, not
because it's methodologically sound. Option 1 (defer to the DCF's negative
EV) is the more honest read of what bear actually means.


================================================================================
SECTION 5 — WHY THIS DIVERGES SO MUCH FROM THE DCF, AND WHAT TO DO ABOUT IT
================================================================================

(Both files' discount rates were lowered 2026-09-07: DCF Base 13.0%->10.0%,
Bull 11.0%->9.0%, Bear 15.5%->13.0%; the multiples file's PV figures below
use the same revised rates.)

           DCF Enterprise Value    Multiples EV (PV, 2036 reference)   DCF $/sh   Multiples $/sh (2036)
  BEAR          ~-$25.4B                 ~$4.8B (distressed floor only)   -$7.18          $1.36
  BASE          ~$342.0B                 ~$419.6B  (1.2x the DCF)         $96.61        $118.53
  BULL        ~$1,982.2B               ~$1,890.6B  (1.0x the DCF, 2036)  $559.94        $534.07
                                       ~$1,068.6B   (0.5x the DCF, 2033)                 $301.86
                                         ~$197.3B   (0.1x the DCF, 2030)                  $55.73

(Per-share = EV ÷ 3.54B diluted TSLA shares, same basis as the DCF file.)

Two things stand out:

**1. The reference-year choice swings the multiples answer by 9-13x on its
own** (base: $31.8B at 2030 vs. $419.6B at 2036; bull: $197.3B vs.
$1,890.6B). This is the multiples method's version of the DCF's WACC/TGR
sensitivity — and arguably a BIGGER lever, because it's not a continuous
dial, it's "which year do you believe the market would actually be looking
at." There's no principled way to pick one reference year over another
without also taking a view on when (or whether) the market starts pricing
this business as a mature, de-risked platform vs. a still-scaling growth
story.

**2. At the 2036 reference year, multiples and DCF land within ~1.0-1.2x of
each other for base and bull** — closer agreement than the reference-year
sensitivity above might suggest, and a reasonable cross-check that neither
method is wildly miscalibrated against the other once you anchor both to
the same terminal year. The DCF's terminal value (Section 3 of that file)
is itself built partly from a 16x/20x exit multiple — so the two files were
never fully independent to begin with; this file mainly replaces the DCF's
single exit-multiple assumption with a comp-sourced, cited one, and shows
what happens if you apply it at earlier reference years too.

**Bottom line for using this file:** don't average the DCF and multiples
numbers together and call it a synthesized estimate — that would hide the
real disagreement (which is about how fast growth decelerates, not a
modeling error) behind a false precision. Use the DCF for the "can Tesla
actually fund and reach this scale" question (its explicit FCF path is the
right tool for that), and use this file for the "what would a market
willing to pay growth-company multiples value it at once it gets there"
question — and treat the size of the gap between them, not either number
alone, as the real signal about how much of this valuation is optionality
on continued growth beyond whatever year you pick.


================================================================================
DISCLOSURES & LIMITATIONS
================================================================================
- Comp multiples (Uber, Lyft, Sixt) were pulled live via web search on
  September 7, 2026 from secondary aggregators (GuruFocus, stockanalysis.com,
  multiples.vc, Wolfe Research), not directly from primary filings for this
  file — treat as directionally right, not decimal-precise. LTM figures for
  Lyft in particular are noisy (EBITDA base is small and volatile).
- No pure-play public robotaxi comp exists (Waymo, Zoox are not public) —
  every comp used here is an imperfect analogue (asset-light marketplace,
  asset-heavy rental, or take-rate-vs-fare mismatch), which is exactly why
  Section 1's driver-payout adjustment matters so much.
- EV/EBITDA multiples chosen for the segment (10-18x) are this file's own
  judgment calls, informed by but not directly copied from the comps —
  there is no formula that converts "Uber trades at 21x" into "Cybercab
  base case should trade at 10-14x"; that gap is a reasoned discount for
  fleet-ownership, residual-value, and regulatory risk, not a derived number.
- Reference years (2030/2033/2036) were chosen for spacing/comparability to
  the DCF file, not because they're the "correct" points at which a market
  would actually re-rate this business — Section 5 makes the case that this
  choice matters more than almost anything else in this file.
- Personal, standalone research file, outside the tech-buffett Init -> Deep
  Dive -> DCF pipeline. Does NOT qualify Tesla (or this segment) for
  portfolio purchase under CLAUDE.md / the agent ruleset. Not investment
  advice.

## Sources
- [Uber EV-to-EBITDA — GuruFocus](https://www.gurufocus.com/term/enterprise-value-to-ebitda/UBER)
- [Uber Technologies (UBER) Statistics & Valuation — stockanalysis.com](https://stockanalysis.com/stocks/uber/statistics/)
- [Uber — Public Comps and Valuation Multiples — multiples.vc](https://multiples.vc/public-comps/uber-valuation-multiples)
- [LYFT EV-to-EBITDA — GuruFocus](https://www.gurufocus.com/term/enterprise-value-to-ebitda/LYFT)
- [Lyft — Public Comps and Valuation Multiples — multiples.vc](https://multiples.vc/public-comps/lyft-valuation-multiples)
- [UBER, LYFT Deep Dive: Updated AV Market Model and Share Shifts — Wolfe Research](https://www.wolferesearch.com/wp-content/uploads/2026/03/Uber-Lyft-Deep-Dive-Updated-AV-Market-Model-and-Share-Shifts.pdf)
- [Sixt — Public Comps and Valuation Multiples — multiples.vc](https://multiples.vc/public-comps/sixt-valuation-multiples)
- [Avis Plummets 12%, Hertz Drops 5% — Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/avis-plummets-12-hertz-drops-133221920.html)
================================================================================
