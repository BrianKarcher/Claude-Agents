# PLTR — institutional ownership snapshot, fetched 2026-08-02

Point-in-time snapshot; **not a quarterly actual**. Kept out of the quarterly cache tables.

**Fetched:** 2026-08-02
**Underlying data period:** 13F filings for the quarter ended **March 31, 2026** (Q2 2026 13Fs, as of Jun 30, 2026, are not due until Aug 14, 2026 and were not yet reflected).

## THE HEADLINE FINDING: the three named sources disagree materially. There is no single verified "institutional ownership %" for PLTR.

| Source (opened directly) | Reported figure | Stated/implied basis |
|---|---|---|
| **Nasdaq** — `https://api.nasdaq.com/api/company/PLTR/institutional-holdings?limit=15&type=TOTAL` (the data behind nasdaq.com/market-activity/stocks/pltr/institutional-holdings) | **70.20%** | 1,611,804,577 institutional shares held by 3,306 institutions, ÷ "Total Shares Outstanding 2,296 million" — i.e. the **Class A count only**. Total holdings value $198,349 million. Latest 13F period in the data: 3/31/2026. |
| **stockanalysis.com** — `https://stockanalysis.com/stocks/pltr/statistics/` | **57.91%** | Denominator is total shares outstanding (2.40B, all classes). Same page: Owned by Insiders 7.44%, Float 2.10B. Page snapshot dated Jul 31, 2026 close. |
| **MarketBeat** — `https://www.marketbeat.com/stocks/NASDAQ/PLTR/institutional-ownership/` | **45.65%** | Labelled "Current Institutional Ownership Percentage," derived from 13F filings. Same page: 2,390 institutional buyers / 1,510 sellers over the last 12 months; $39.41B inflows vs. $12.59B outflows. Page states "last updated on 8/2/2026." |

Spread: **45.65% to 70.20%** — a 25-point range on the same nominal metric.

### Why they differ (as far as can be determined from the pages themselves)
- **Different denominators.** Nasdaq divides by Class A shares (2,296M); stockanalysis divides by all classes (2,397M). Applying Nasdaq's 1,611.8M institutional shares to the all-class denominator gives 67.2%, not 57.91% — so denominator choice alone does not reconcile them.
- **Different numerators.** The three vendors evidently apply different rules for which 13F filers, share classes, and stale filings to include. None of the pages publishes its exact inclusion rule.
- MarketBeat's figure is the most conservative; Nasdaq's the most aggressive.

### Largest holders (Nasdaq, from 13F data; most recent row dates 12/31/2025–3/31/2026)
- Vanguard Group Inc — 215,444,098 shares, market value $26,512,551 thousand, +1,557,828 shares (+0.728%), report date 12/31/2025.
- MarketBeat's FAQ, separately, names the largest holders by value over the previous two years as Vanguard ($38.30B), State Street ($18.20B), Geode Capital Management ($9.60B), Morgan Stanley ($5.19B), Norges Bank.

### Nasdaq active-position summary (13F period 3/31/2026)
| Category | Holders | Shares |
|---|---|---|
| Increased positions | 1,611 | 323,304,189 |
| Decreased positions | 1,438 | 75,898,148 |
| Held positions | 257 | 1,212,602,240 |
| **Total institutional** | **3,306** | **1,611,804,577** |

## Notes / how to use this
- **Do not put a bare "institutional ownership: X%" stat on a slide.** Any figure used must name the source and the as-of basis, e.g. "70.2% of Class A shares (Nasdaq, 13F data as of Mar 31, 2026)" or "45.65% (MarketBeat, 13F filings, as of Aug 2, 2026)". Presenting one number unattributed implies a precision that does not exist.
- If the deck's existing unsourced claim happens to fall inside 45.65–70.20%, that is **not** verification — match it to a specific source or replace it.
- fintel.io was attempted as a fourth source and returned HTTP 403; no fourth data point was obtained.
- Palantir does not report institutional ownership in its own filings, so there is no primary source for this metric — every figure here is a third-party 13F aggregation.
