# PLTR + peers (NVDA, SNOW) — valuation multiples and TTM fundamentals, as of Jul 31, 2026 close

Point-in-time market data. **Not quarterly actuals** — kept out of `../quarterly-financials.md` and `../other-metrics.md`. Goes stale daily; re-fetch before any re-record.

**Source:** stockanalysis.com — `/stocks/{pltr,nvda,snow}/statistics/` and `/stocks/{pltr,nvda,snow}/` overview pages. Site states its market-cap and fundamentals data come from S&P Global Market Intelligence.
**Fetched:** 2026-08-02 (pages show "At close: Jul 31, 2026, 4:00 PM EDT")
**Cross-checked against:**
1. **Internal consistency, all three tickers:** market cap ÷ TTM revenue reproduces the site's own P/S ratio — PLTR 295.01B/5.22B = 56.5 vs. stated 56.47 ✓; NVDA 4.86T/253.49B = 19.17 vs. stated 19.18 ✓; SNOW 101.65B/5.03B = 20.21 vs. stated 20.20 ✓.
2. PLTR's closing price ($123.06) and market cap ($295.01B) independently confirmed by Nasdaq and MarketBeat — see `PLTR-MARKETDATA-2026-07-31.md`.
3. PLTR's TTM revenue of $5.22B reconciles against the verified GAAP quarterly cache: Q2 2025 1,004.00 + Q3 2025 1,181.00 + Q4 2025 1,407.00 + Q1 2026 1,633.00 = **$5,225M** ✓. TTM gross profit $4.39B likewise: 810.76 + 973.79 + 1,191.00 + 1,417.00 = **$4,392.55M** ✓. This is a direct primary-source reconciliation of the aggregator's TTM figures.

## PLTR valuation multiples (as of Jul 31, 2026)
| Metric | Value |
|---|---|
| Price | $123.06 |
| Market cap | $295.01B |
| Enterprise value | $287.20B |
| **Trailing P/S** | **56.47x** |
| Forward P/S | 34.53x |
| **Trailing P/E** | **138.34x** |
| **Forward P/E** | **77.34x** |
| PEG | 1.50 |
| P/FCF | 109.74x |
| EV/EBITDA | 142.30x |
| Beta (5Y) | 1.56 |
| 50-day / 200-day MA | $130.72 / $152.89 |
| Short interest | 77.88M shares, 3.25% of shares out, 3.70% of float |
| Shares outstanding | 2.40B (Class A 2.30B); insiders 7.44%; float 2.10B |
| TTM revenue / gross profit / operating income / net income | $5.22B / $4.39B / $1.99B / $2.28B |
| TTM EPS | $0.89 |
| Employees | 4,429 |

## Peer comparison table (all three from the same source, same as-of date)
| Company | Market cap | Trailing P/S | TTM revenue | TTM revenue growth Y/Y | TTM gross profit | TTM gross margin (derived¹) |
|---|---|---|---|---|---|---|
| **Palantir (PLTR)** | $295.01B | **56.47x** | $5.22B | **+67.7%** | $4.39B | **84.1%** |
| NVIDIA (NVDA) | $4.86T | 19.18x | $253.49B | **+70.7%** | $187.95B | 74.1% |
| Snowflake (SNOW) | $101.65B | 20.20x | $5.03B | **+31.1%** | $3.38B | 67.2% |

¹ Gross margin = the same page's TTM gross profit ÷ TTM revenue. Arithmetic on two reported values, not a separately-quoted figure.

Closing prices Jul 31, 2026: PLTR $123.06, NVDA $200.75, SNOW $293.28.

## Notes — things a deck must not get wrong here
- **PLTR's trailing P/S is ~56x, not ~80x.** An earlier version of the deck stated "~80x trailing sales" in three places with no source; that is materially wrong at these prices.
- **NVIDIA is growing FASTER than Palantir on a TTM basis** (+70.7% vs. +67.7%). Any narrative that peers are "growing more slowly" is false on this data and must not be used. PLTR's *most recent quarter* grew +85% Y/Y, which is faster than its own TTM rate — if a slide compares growth, it must use the same basis (TTM vs. TTM, or latest-quarter vs. latest-quarter) for every company, and say which.
- **PLTR's 84.1% here is TTM GAAP gross margin.** It is not the same as the 86.8%/87% GAAP gross margin of the Q1 2026 quarter alone, and not the same as the 88% *adjusted* (non-GAAP, ex-SBC) gross margin from the investor deck. Three different numbers; label which one a slide shows.
- Snowflake is unprofitable (TTM operating income −$1.29B, net −$1.20B); its trailing P/E is n/a. Do not present a P/E comparison across these three.
- These are third-party computed multiples, not company-reported figures. Attribute the source and the as-of date on any slide that uses them.
