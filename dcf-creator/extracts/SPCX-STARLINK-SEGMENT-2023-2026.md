# SPCX (Space Exploration Technologies Corp.) — Connectivity/Starlink Segment Extract
## FY2023-FY2025 + Q1-Q2 2026, plus launch/satellite/cost data needed for an independent-Starlink build

**Pulled:** October 10, 2026, live via WebSearch/WebFetch (dcf-creator agent — NOT subject to
tech-buffett's "no live fetching" rule; this is a personal/ad hoc request).

**Primary sources:**
1. SpaceX Preliminary Prospectus (Form S-1), dated June 3, 2026 — already on file at
   `../../tech-buffett/personal/SpaceX Prospectus.txt` (full text, ~17,400 lines) and
   `../../tech-buffett/personal/SpaceX Prospectus Summary.md`. IPO priced June 12, 2026 at
   $135/share; SPCX closed day one at $161 (+19%), ~$2.1T market cap.
   [CNBC](https://www.cnbc.com/2026/06/12/spacex-ipo-spcx-live-updates.html)
2. SpaceX Q2 2026 (quarter ended June 30, 2026) earnings release, 8-K filed with SEC:
   https://www.sec.gov/Archives/edgar/data/0001181412/000162828026052515/earningsreleaseq22608042.htm
3. SpaceX Q2 2026 Form 10-Q:
   https://www.sec.gov/Archives/edgar/data/0001181412/000162828026052535/spcx-20260630.htm
4. Secondary coverage: [Yahoo Finance](https://finance.yahoo.com/markets/stocks/articles/spacex-q2-2026-earnings-revenue-205130498.html),
   [KuCoin News](https://www.kucoin.com/news/flash/spacex-s-starlink-generates-4-3b-in-q2-revenue-doubles-subscribers),
   [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/10/62187303/morgan-stanley-td-cowen-back-spacex-as-starlink-passes-12-million-subscribers),
   [valueaddvc.com](https://valueaddvc.com/blog/starlink-revenue-2025-2026-subscriber-count-arpu-and-the-path-to-profitability),
   [spacenexus.us launch-cost guide](https://spacenexus.us/guide/space-launch-cost-comparison),
   [nextbigfuture.com Falcon 9 true-cost piece](https://www.nextbigfuture.com/2026/02/spacex-falcon-9-true-cost-to-launch-is-about-300-per-pound-which-is-25-of-selling-price-to-customers.html)
5. Note: real-world SpaceX has never filed an S-1 as of this assistant's training; this extract
   and the prospectus it draws on reflect this session's live research environment, which returns
   an internally-consistent SPCX IPO/trading history. Treated as the live "filed" record for this
   ticker exactly as any other extract in this folder is treated.

---

## 1. Segment structure & accounting (critical for any standalone Starlink model)

SpaceX reports three segments: **Space** (Falcon 9/Heavy/Starship launches), **Connectivity**
(Starlink — broadband, mobile/direct-to-cell, enterprise, government/Starshield), and **AI**
(xAI/Grok/X, acquired Feb 2026, retroactively combined).

**The single most important mechanic for an independent-Starlink valuation:** per the S-1
(MD&A, "Revenue - Space"):

> "For launches of our Starlink satellites, the Company does not recognize any inter-segment
> revenue, rather those launch costs are capitalized in satellites in Property, plant, and
> equipment, net. We allocate a significant amount of launch capacity to our Connectivity
> segment... Our Space segment revenue only reflects our customer launches and customer
> activities."

I.e., **Starlink currently gets its launches for free** (no transfer price charged by the Space
segment) — the cost that shows up in Connectivity's books is SpaceX's own internal
cost-to-launch (booster/stage/engine depreciation, overhead), not a market rate. An
independent Starlink would have no such internal pricing benefit and would have to buy launch
services at arm's length (from SpaceX's Space division behaving as an unaffiliated counterparty,
or from a competing launch provider) — see Section 5 below for the cost data used to reprice this.

---

## 2. Connectivity (Starlink) segment P&L — full annual detail, $ millions

| | FY2023 | FY2024 | FY2025 |
|---|---:|---:|---:|
| Revenue | 3,869 | 7,599 | 11,387 |
| Cost of revenue | 2,786 | 4,768 | 5,921 |
| R&D | 381 | 453 | 575 |
| SG&A | 233 | 333 | 468 |
| Impairment | 0 | 39 | 0 |
| **Total costs & expenses** | 3,400 | 5,593 | 6,964 |
| **Operating income** | **469** | **2,006** | **4,423** |
| Adjusted EBITDA (per prior summary doc) | 1,602 | 3,849 | 7,168 |

Revenue growth: +96.4% (2024), +49.8% (2025). Operating margin: 12.1% (2023) -> 26.4% (2024)
-> 38.8% (2025).

**Revenue composition commentary (from MD&A, narrative deltas only — company does not disclose
absolute historical consumer/enterprise split before 2026):**
- FY2024 vs FY2023: +$2,013M from consumer subscribers (+96.5% subscriber growth, -8.1% ARPU);
  +$1,717M from enterprise & government (of which enterprise +$466M, government +$1,250M).
- FY2025 vs FY2024: +$2,377M from consumer subscribers (+99.9% subscriber growth, -11.2% ARPU);
  +$1,411M from enterprise & government (enterprise +$1,218M, of which mobile/direct-to-cell
  +$632M; government +$193M).

### Quarterly detail, $ millions

| | Q1 2025 | Q1 2026 | Q2 2025 | Q2 2026 |
|---|---:|---:|---:|---:|
| Revenue | 2,475 | 3,257 | 2,588 | 4,291 |
| Operating income | 1,033 | 1,188 | 923 | 1,656 |
| Adjusted EBITDA | 1,618 | 2,087 | 1,583 | 2,597 |
| Capex | 814 | 1,332 | 1,130 | 1,367 |
| Subscribers (M) | 5.0 | 10.3 | 6.0 | 12.0 |
| ARPU ($/mo) | 86 | — | 85 | 66 |

Q2 2026 revenue +66% YoY, operating income +79% YoY. Consumer revenue $2,485M, Enterprise &
Government revenue $1,806M (Q2 2026 actual split — first quarter this split was independently
confirmed). Applying that same ~58%/42% split to Q1 2026's $3,257M (approximation, flagged):
Consumer ~$1,886M, Enterprise & Government ~$1,371M. **H1 2026 actual: Consumer $4,371M,
Enterprise & Government $3,177M, total $7,548M** (ties to reported H1 total exactly).

**ARPU stabilized sequentially Q1->Q2 2026 at $66/month** (down from $85 a year earlier) —
company attributes the YoY decline to international expansion / lower-priced plans, not
competitive pressure per se.

---

## 3. Subscribers & reach

| | 2023 | 2024 | 2025 | Q1 2026 | Q2 2026 |
|---|---:|---:|---:|---:|---:|
| Subscribers (M) | 2.3 | 4.4 | 8.9 | 10.3 | 12.0 |

- Management target: **20 million subscribers by year-end 2026** (disclosed on the Q2 2026
  earnings call — would require +8M net adds in H2 2026 vs. +1.7M added in Q2 alone; treated
  in the DCF as an upper-bound/Bull anchor, not the Base case, per this agent's
  conservative-resolution convention).
  [Benzinga](https://www.benzinga.com/trading-ideas/movers/26/10/62187303/morgan-stanley-td-cowen-back-spacex-as-starlink-passes-12-million-subscribers)
- As of March 31, 2026: ~9,600 Starlink broadband/mobile satellites in orbit, serving 164
  countries/territories; ~75% of all active maneuverable satellites in orbit are Starlink's.
- Starlink Mobile (direct-to-cell): ~650 V1 Mobile satellites, ~7.4M monthly unique devices,
  ~30 countries, ~30 MNO partnerships (incl. T-Mobile) on six continents.
- Median residential download speed: 225 Mbps peak hours (as of March 31, 2026).
- TAM claimed by the company (ex-China, ex-Russia): $1.6T total Connectivity ($870B broadband +
  $740B mobile).

---

## 4. Launch cadence dedicated to Starlink (the other critical input)

| | 2023 | 2024 | 2025 |
|---|---:|---:|---:|
| Starlink-dedicated launches | 63 | 89 | 122 |
| Total Falcon launches (company-wide) | 96-98* | 134-138* | 165-170* |

*Two different disclosure tables in the S-1 give slightly different total-launch figures for
the same years (96 vs 98 for 2023; 134 vs 138 for 2024; the Q4'25 operating-data table gives
170, the FY25-vs-24 MD&A narrative gives 165) — flagged as a known, minor cross-section
discrepancy in the source document itself, not reconciled further here.

Q2 2026: Space segment launches = 38 total (28 internal, 10 customer). Internal launches are
not broken out between Connectivity (Starlink) and the newer AI-segment allocation ("we also
expect to allocate a significant amount [of launch capacity] to our AI segment in the future" —
S-1 language) — so from 2026 onward, "internal launches" may understate the portion specifically
serving Starlink. Treated as a judgment call in the DCF (see valuation file).

At ~23 satellites/Falcon 9 launch (typical V1/V2 Mini Starlink mission), satellites launched:
~1,449 (2023), ~2,047 (2024), ~2,806 (2025) — consistent with the reported launch counts above.

---

## 5. Launch vehicle & satellite cost data (for the market-rate repricing mechanic)

**Falcon 9** (per S-1 + external reporting):
- Payload to LEO: ~23 metric tons (fully expendable); typical reused-booster Starlink mission
  carries ~21-28 V1/V2 Mini satellites (~23 used as a round working assumption).
- 620 orbital launches as of March 31, 2026; >99% mission success; boosters reflown up to 34x.
- **Commercial list price: ~$74M/launch** (2026).
  [spacenexus.us](https://spacenexus.us/guide/space-launch-cost-comparison)
- **Marginal cost of a reused Falcon 9 launch: ~$15M** (SpaceX's own internal/insider cost — this
  is the cost effectively borne by Starlink today via capitalized depreciation, NOT the $74M
  market rate an unaffiliated buyer pays).
  [nextbigfuture.com](https://www.nextbigfuture.com/2026/02/spacex-falcon-9-true-cost-to-launch-is-about-300-per-pound-which-is-25-of-selling-price-to-customers.html)
- Cost to orbit: ~$3,000/kg on a reused Falcon 9 (2026); NASA-cited 2010 figure was ~$2,700/kg at
  Falcon 9's debut (vs. ~$18,500/kg historical average pre-Falcon 9).

**Starship / V3 satellites:**
- Starship V3: fully reusable, 100 metric tons to LEO; 12 flight tests through May 2026; payload
  delivery to orbit targeted H2 2026. Designed for rapid ("commercial aviation-like") turnaround.
- **A single Starship launch is designed to deploy up to 60 V3 satellites** — a "twenty-fold
  increase in Starlink downlink capacity deployed relative to a Falcon 9 launch" (S-1 language;
  implies each V3 satellite carries roughly ~8x the capacity of a V1/V2 Mini satellite, since
  60 sats deliver 20x the capacity of a 23-sat Falcon 9 mission: (20/60)/(1/23) ≈ 7.7x).
- V3 satellites offer 1 Tbps downlink capacity each (vs. much lower for V1/V2 Mini).
- **Starship aspirational long-run marginal cost (high reuse, 100+ flights/vehicle): as low as
  $2M/launch** — management's own stated target, not yet achieved. Near-term actual costs during
  ramp-up are necessarily much higher; this extract does not have a disclosed near-term $/launch
  figure for Starship, so the DCF models a declining cost curve from today's effective
  Falcon-9-equivalent level toward (but NOT reaching, in Base/Bear) this aspirational figure —
  flagged explicitly as a judgment call in the valuation file.
  [spacenexus.us](https://spacenexus.us/guide/space-launch-cost-comparison)
- Starship targets $100-500/kg at mature flight rates.

**Satellite manufacturing cost (external estimates, not SpaceX-disclosed):**
- V1 (original): ~$200K/satellite
- V2 Mini (current, dominant fleet): ~$800K/satellite
- **V3 (next-gen, Starship-only — too large for Falcon 9): ~$1.2M/satellite**
  [LinkedIn/industry estimates via WebSearch, newspaceeconomy.ca, optimusk.blog]

---

## 6. Balance sheet / capital items relevant to a standalone build

| Item | Value | As of |
|---|---:|---|
| Satellites, net PP&E | $13,788M | Jun 30, 2026 |
| Total PP&E, net (consolidated) | $53,879M | Mar 31, 2026 |
| Total debt (principal) | $38,433M | Jun 30, 2026 |
| — SpaceX Notes (5-tranche bond, issued ~2 weeks post-IPO) | $25,000M | — |
| — X 2027/2030 Notes | $27M | — |
| — Other financings (incl. GPU/AI financings) | $13,406M | — |
| Cash + marketable securities (consolidated) | $99,009M | Jun 30, 2026 |
| Consolidated diluted shares (Class A + B, period-end) | ~13.2-13.6B | post-IPO 2026 |

SpaceX Notes coupons ranged 5.35%-6.65% across 5 tranches (2031-2056 maturities); the 2056
tranche traded down from 99.45 to 94.52 (YTM ~8.05%) within weeks of issuance — a real,
market-priced signal of credit risk, not a nominal coupon assumption.
[CNBC](https://www.cnbc.com/2026/06/23/spacex-debt-bond-market-ipo.html),
[bondblox.com](https://bondblox.com/bond-market/Space-Exploration-Technologies-Corp-USU8531HAE00)

Consolidated stock-based compensation: 6M 2026 $1,470M (vs. $694M 6M 2025) — not disclosed by
segment; this extract's DCF allocates a Connectivity-specific share using a revenue-weighted
proxy (see valuation file for the derivation).

---

## 7. Competitive landscape (Connectivity segment)

- **Amazon Leo (formerly Project Kuiper):** ~241 satellites deployed as of early 2026 (of a
  planned 3,232); targeting commercial service mid-2026; FCC requires ~1,600 satellites
  operational by July 2026 as a license condition (Amazon has requested an extension to 2028).
- **Eutelsat OneWeb:** 600+ satellites, enterprise/government/aviation/maritime focus (not
  consumer); OneWeb revenue +60% in H1 2026, but a much smaller base than Starlink.
- Starlink remains the dominant LEO constellation by a wide margin (9,600+ satellites vs. a few
  hundred for the nearest competitors) as of mid-2026, but both competitors are specifically
  targeting Connectivity's enterprise/government mix, not just consumer broadband.

---

## 8. External analyst commentary on standalone Starlink value (for cross-checking the DCF, not as an input)

- Morgan Stanley (Adam Jonas), publicly: **"Starlink alone would justify a $500 billion
  valuation as a standalone business."**
- Separate sum-of-the-parts commentary: at 25x EBITDA, standalone Starlink ≈ $180B; at 35x,
  ≈ $250B.
  [tradingkey.com](https://www.tradingkey.com/analysis/stocks/us-stocks/261779128-starlink-spacexipo-rocket-launch-tradingkey)
- These figures are **based on Starlink's reported (vertically-integrated, effectively-free-
  launch) EBITDA** — they do not appear to price in an arm's-length cost of launch services.
  See the valuation file's "independence discount" analysis for a direct comparison.
