# NVDA — market data as of market close Friday 2026-07-31 (aggregator, cross-checked)

**Source (primary of the two):** https://stockanalysis.com/stocks/nvda/
Values displayed and timestamped on the page as **"Jul 31, 2026, 4:00 PM EDT"** (2026-08-02 is a Sunday; 2026-07-31 was the last trading day before this fetch).
**Fetched:** 2026-08-02
**Cross-checked against:** https://companiesmarketcap.com/nvidia/marketcap/ — states market cap **$4.862 Trillion USD** and share price **$200.75** as of 2026-08-02 (reflecting the same 2026-07-31 close). Identical price and market cap from an independent aggregator.

## Figures

| Metric | Value | Source |
|---|---|---|
| Share price (close 2026-07-31) | $200.75 | stockanalysis.com; identical on companiesmarketcap.com |
| Market capitalization | $4.86T (companiesmarketcap: $4.862T) | both aggregators |
| Shares outstanding | 24.22B | stockanalysis.com |
| Revenue (TTM) as stated by aggregator | $253.49B | stockanalysis.com |

## Independent checks performed

1. **Market cap reconciles to price × shares:** 24.22B × $200.75 = **$4,862.2B = $4.862T**. Matches both aggregators' stated market cap.
2. **Shares outstanding reconciles to an SEC primary source:** the cover page of NVIDIA's Q1 FY2027 Form 10-Q (filed 2026-05-20) reports `dei:EntityCommonStockSharesOutstanding` = **24,200,000,000** as of 2026-05-15 (via https://data.sec.gov/api/xbrl/companyconcept/CIK0001045810/dei/EntityCommonStockSharesOutstanding.json). NVIDIA rounds this cover figure to the nearest 100 million, so 24.2B (SEC, mid-May) vs 24.22B (aggregator, end-July) is consistent.
3. **Aggregator TTM revenue reconciles to primary filings:** independently summing the four most recent reported quarters from SEC filings gives Q2 FY26 46,743 + Q3 FY26 57,006 + Q4 FY26 68,127 + Q1 FY27 81,615 = **$253,491M = $253.491B**, matching stockanalysis.com's stated $253.49B exactly. The aggregator's other figures are therefore not being taken on faith.

## Derived trailing P/S multiple

**P/S (TTM) = market cap / TTM revenue = $4,862.2B / $253.491B = 19.18x**

- Numerator: 24.22B shares × $200.75 close on 2026-07-31.
- Denominator: sum of four reported quarters from SEC filings (see `NVDA-8K-Q1-FY2027.md`, `NVDA-8K-Q3-FY2026.md`, `NVDA-10K-FY2026.md`), not an aggregator estimate.
- Round to **19.2x** for on-screen use.

## Notes

- Market cap and price are **point-in-time and go stale fast** — this figure is only valid as "as of the 2026-07-31 close" and must be re-fetched, not reused, for any later recording date. Per project policy these do not belong in `quarterly-financials.md` (actuals-only cache); they live here as a dated snapshot.
- A trailing P/S built on TTM revenue is **backward-looking by construction**. NVIDIA guided Q2 FY2027 revenue to $91.0B; a forward P/S would be materially lower. Do not blend the two, and label whichever is shown.
- NVIDIA repurchased ~$19.3B of stock in Q1 FY2027 alone, so share count is falling quarter over quarter; prefer the most recent aggregator share count over an older 10-Q cover figure when computing market cap, and note the date.
- The 12-month analyst consensus price target of $302.83 shown on stockanalysis.com is a **forward estimate**, not an actual. If used in a deck it must be labeled as consensus estimate, and it should be re-fetched fresh rather than reused from this file.
