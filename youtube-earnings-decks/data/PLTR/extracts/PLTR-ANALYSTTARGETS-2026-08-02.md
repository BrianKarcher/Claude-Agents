# PLTR — analyst price targets, fetched 2026-08-02 (ahead of the Aug 3, 2026 Q2 2026 call)

Forward-looking third-party estimates. **Not actuals.** Kept out of the quarterly cache tables per project policy. Price targets go stale fast — re-fetch before every recording; do not reuse this file after a subsequent ratings action.

**Fetched:** 2026-08-02
**Sources opened directly:**
- `https://stockanalysis.com/stocks/pltr/forecast/` (consensus and "Latest Forecasts" table; page states the poll is of analysts per S&P Global)
- `https://stockanalysis.com/analysts/mariana-perez-mora/` (BofA analyst's dated ratings history)
- `https://stockanalysis.com/analysts/brent-thill/` (Jefferies analyst's dated ratings history)
- `https://www.marketbeat.com/stocks/NASDAQ/PLTR/price-target/` (full dated ratings table, 30+ rows)
- `https://www.benzinga.com/quote/PLTR/analyst-ratings` (full dated ratings table, 100 rows)
- `https://finbold.com/wall-street-analyst-updates-palantir-stock-price-target-3/` and the Yahoo Finance syndication of "Palantir Stock Soars — Gets Massive $200 Price Target Ahead of Critical Earnings" (news confirmation of the Oppenheimer note)

Reference price for upside math: $123.06 (Jul 31, 2026 close — see `PLTR-MARKETDATA-2026-07-31.md`).

## The three firms requested

### 1. Oppenheimer — **VERIFIED**
| Field | Value |
|---|---|
| Firm | Oppenheimer |
| Rating | Outperform (reaffirmed) |
| **Price target** | **$200** |
| Date of the note | **July 27, 2026** |
| Implied upside vs. $123.06 | +62.5% |

Corroboration (four independent sources agree on firm + $200 + Jul 27, 2026 + Outperform/Buy):
- stockanalysis.com "Latest Forecasts": Oppenheimer, Buy, Reiterates, $200, Jul 27, 2026.
- MarketBeat: 7/27/2026, Oppenheimer, Reiterated Rating, Outperform (target cell blank on MarketBeat).
- Benzinga: 04/30/2026, Oppenheimer, Initiates, → $200, Outperform — i.e. the $200 target was **set at initiation on Apr 30, 2026** and reaffirmed on Jul 27, 2026.
- News (finbold; Yahoo syndication): "Oppenheimer reaffirmed its Outperform rating and maintained a $200 price target ahead of the company's second-quarter earnings report," dated Monday, July 27, 2026.

**Unresolved detail — do not name the analyst on a slide.** stockanalysis attributes the note to **Martin Yang**; MarketBeat attributes it to **Param Singh**; Benzinga names no analyst. Two aggregators conflict, so the analyst name is not verified. Cite the firm only.

### 2. Bank of America Securities — **CURRENT TARGET NOT VERIFIABLE**
| Field | Value |
|---|---|
| Most recent rating action | **Buy, maintained, July 28, 2026** (analyst Mariana Perez Mora) — *rating only, no price target published* |
| Most recent **published price target** | **$255**, raised from $215, "Maintains Buy" — dated **November 4, 2025** |

- stockanalysis.com's analyst page for Mariana Perez Mora lists her Jul 28, 2026 PLTR action explicitly with **Price Target: "n/a"**. Her other July 2026 notes on that page (TDY, BAH, KBR, OSIS, AMTM) all carry targets, so the "n/a" is a genuine absence, not a page-parsing failure.
- Benzinga: "The high is $255 issued by B of A Securities on November 4, 2025." Its ratings table shows B of A Securities rows at 11/04/2025 ($215 → $255, Maintains Buy), 09/23/2025 ($180 → $215), 08/05/2025 ($150 → $180), 02/04/2025 ($90 → $125). Nothing after 11/04/2025.
- MarketBeat independently shows the same 11/4/2025 row: Bank of America, Mariana Perez, Boost Target, Buy, $215 ➝ $255.

**Conclusion:** BofA has a *current* Buy rating (Jul 28, 2026) but its last *published* price target is nine months old. If the deck cites $255, it must be labelled "**BofA Securities, $255, set Nov 4, 2025**" — presenting it as a current pre-earnings target would be misleading. Do not attach the Jul 28, 2026 date to the $255 figure; those are two different events.

### 3. Jefferies — **UNVERIFIABLE, DO NOT USE**
No current, reliably-attributed Jefferies price target for PLTR could be found. The sources conflict irreconcilably:
- **Benzinga**: last Jefferies row is **02/04/2025 — Maintains Underperform, $28 → $60**. Benzinga's own summary text says "The low is $60 issued by Jefferies on February 4, 2025."
- **MarketBeat**: last Jefferies row is **1/22/2026 — "Set Target" $208.00**, with *no rating* attached and no analyst named.
- **stockanalysis.com**: Brent Thill (Jefferies) analyst page lists his ratings through Jul 31, 2026 and contains **no PLTR row** at all in the visible history.
- MarketBeat's own "analysts covering PLTR in the past 90 days" list (Argus, Benchmark, BNP Paribas Exane, BTIG, Cantor Fitzgerald, Citigroup, DA Davidson, Oppenheimer, Phillip Securities, President Capital, Rosenblatt, RBC, UBS, Wedbush, Weiss, Wolfe, Zacks) **does not include Jefferies**.

A $60 Underperform and a $208 target 11 months apart, with the firm absent from current-coverage lists, cannot be resolved into a defensible current figure. **No Jefferies target is being recorded. Do not substitute a plausible-sounding number, and do not infer that the consensus low of $70 belongs to Jefferies** — no source attributes it.

## Consensus and other firm-attributed targets (context only, all forward-looking estimates)

stockanalysis.com / S&P Global poll, as of Jul 31–Aug 2, 2026:
| Metric | Value |
|---|---|
| Analysts polled | 32 |
| Consensus rating | Buy (19 Strong Buy, 1 Buy, 10 Hold, 1 Sell, 1 Strong Sell as of Jul '26) |
| Average price target | $182.20 (+48.06%) |
| Median | $200 |
| Low / High | $70 / $255 |

Benzinga's separate consensus: $176.75 across 29 analysts. MarketBeat's separate consensus (per search-surfaced summary, not relied upon): different again. Consensus figures are **not interchangeable across vendors** — pick one and attribute it.

Most recent dated, firm-attributed actions (from stockanalysis + MarketBeat + Benzinga, where at least two agree):
| Date | Firm | Action | Target |
|---|---|---|---|
| Jul 31, 2026 | RBC Capital (Rishi Jaluria) | Reiterates Underperform/Sell | $90 |
| Jul 30, 2026 | Rosenblatt Securities (John McPeake) | Maintains Buy | $225 |
| Jul 28, 2026 | BofA Securities (Mariana Perez Mora) | Maintains Buy | no target published |
| Jul 27, 2026 | Oppenheimer | Reiterates Outperform | $200 |
| Jul 24, 2026 | Citigroup (Tyler Radke) | Maintains Buy, lowers target | $225 → $200 |
| Jul 17, 2026 | DA Davidson (Gil Luria) | Maintains Buy | $175 |

## Notes
- Everything in this file is a **forward-looking third-party estimate**, never an actual. Any deck use must be visually and textually flagged (an "(E)"/"estimate"/"price target" label, distinct styling) per the project's never-fabricate policy.
- TipRanks was attempted for a fourth cross-check and returned HTTP 403 to both WebFetch and curl; fintel.io also 403s.
- Vendor "upside %" columns are computed as of each note's own date, not against the current price — recompute against $123.06 if an upside figure is shown.
