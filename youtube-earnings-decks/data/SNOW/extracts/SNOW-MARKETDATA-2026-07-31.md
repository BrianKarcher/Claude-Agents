# SNOW — market data as of market close Friday 2026-07-31 (aggregator, cross-checked)

**Source (primary of the two):** https://stockanalysis.com/stocks/snow/
Values displayed and timestamped on the page as **"July 31, 2026, 4:00 PM EDT"** (2026-08-02 is a Sunday; 2026-07-31 was the last trading day before this fetch).
**Fetched:** 2026-08-02
**Cross-checked against:** https://companiesmarketcap.com/snowflake/marketcap/ — states market cap **$101.65 Billion USD** and share price **$293.28** as of 2026-08-02 (reflecting the same 2026-07-31 close). Identical price and market cap from an independent aggregator.

## Figures

| Metric | Value | Source |
|---|---|---|
| Share price (close 2026-07-31) | $293.28 (−$4.82, −1.62% on the day) | stockanalysis.com; identical on companiesmarketcap.com |
| Market capitalization | $101.65B | both aggregators |
| Shares outstanding | 346.60M | stockanalysis.com |
| Revenue (TTM) as stated by aggregator | $5.03B | stockanalysis.com |

## Independent checks performed

1. **Market cap reconciles to price × shares:** 346.60M × $293.28 = **$101.65B**. Matches both aggregators' stated market cap.
2. **Shares outstanding reconciles exactly to an SEC primary source:** the cover page of Snowflake's Q1 FY2027 Form 10-Q (filed 2026-05-29) reports `dei:EntityCommonStockSharesOutstanding` = **346,600,000** as of 2026-05-15 (via https://data.sec.gov/api/xbrl/companyconcept/CIK0001640147/dei/EntityCommonStockSharesOutstanding.json) — the same 346.60M the aggregator shows.
3. **Aggregator TTM revenue reconciles to primary filings:** independently summing the four most recent reported quarters from SEC filings gives Q2 FY26 1,144,969 + Q3 FY26 1,212,909 + Q4 FY26 1,283,994 + Q1 FY27 1,390,951 = **$5,032,823K = $5.0328B**, matching stockanalysis.com's stated $5.03B. Also confirmed a second way: FY2026 total 4,683,946 − Q1 FY26 1,042,074 + Q1 FY27 1,390,951 = 5,032,823.

## Derived trailing P/S multiple

**P/S (TTM) = market cap / TTM revenue = $101.65B / $5.0328B = 20.20x**

- Numerator: 346.60M shares × $293.28 close on 2026-07-31.
- Denominator: sum of four reported quarters from SEC filings (see `SNOW-8K-Q1-FY2027.md`, `SNOW-8K-Q4-FY2026.md`, `SNOW-8K-Q3-FY2026.md`, `SNOW-8K-Q2-FY2026.md`), using **total** revenue, not product revenue.
- Round to **20.2x** for on-screen use.

## Notes

- The TTM denominator uses **total revenue** ($5.033B). If instead built on *product* revenue only, the denominator would be smaller and the multiple higher — Snowflake guides on product revenue, so it is easy to mix the two. Any P/S shown must state which revenue base it uses. This file's 20.20x is total-revenue-based, consistent with how NVDA's 19.18x is computed.
- Market cap and price are **point-in-time and go stale fast** — valid only as of the 2026-07-31 close; re-fetch for any later recording date. Per project policy these do not belong in `quarterly-financials.md` (actuals-only cache).
- Snowflake's share count has been **rising** (338.8M at Aug 2025 10-Q → 342.2M Nov 2025 → 345.7M Mar 2026 → 346.6M May 2026, per 10-Q/10-K cover pages), the opposite of NVDA's buyback-driven decline. Dilution matters if comparing market caps across dates.
- The 12-month analyst consensus price target of $298.23 shown on stockanalysis.com is a **forward estimate**, not an actual; label it as such if used and re-fetch rather than reusing this snapshot.
