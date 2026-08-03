# PLTR — market data snapshot, close of Friday July 31, 2026

Point-in-time snapshot; **not a quarterly actual**. Deliberately kept out of `../quarterly-financials.md` and `../other-metrics.md`. Goes stale immediately — re-fetch rather than reuse if the deck's "as of" date changes.

**Context:** last trading session before Palantir's Q2 2026 earnings call on Monday, August 3, 2026 (after market close).

**Primary source (price):** Nasdaq official historical quote API for PLTR —
`https://api.nasdaq.com/api/quote/PLTR/historical?assetclass=stocks&fromdate=2026-07-27&todate=2026-08-01`
**Primary source (market cap):** https://stockanalysis.com/stocks/pltr/market-cap/ (page states "Data Source: S&P Global Market Intelligence", "Last updated: Jul 31, 2026")
**Fetched:** 2026-08-02
**Cross-checked against:**
1. stockanalysis.com quote header: "123.06 +0.80 (0.65%) At close: **Jul 31, 2026, 4:00 PM EDT**" — matches Nasdaq's close exactly.
2. marketbeat.com/stocks/NASDAQ/PLTR/institutional-ownership/ quote header: "$123.06 +0.80 (+0.65%) Closing price **07/31/2026 04:00 PM Eastern**" — third independent confirmation.
3. Internal consistency: $295.01B market cap ÷ $123.06 = 2,397.3 million shares, which matches the 2,397,311,977 total shares (Class A+B+F) on the Q1 2026 10-Q cover page as of April 27, 2026 (see `PLTR-10Q-Q1-2026.md`). The market cap is therefore consistent with an all-share-class basis.

## Figures

| Metric | Value | As of |
|---|---|---|
| **Closing price** | **$123.06** | Fri Jul 31, 2026, 4:00 PM EDT |
| Prior close (Thu Jul 30, 2026) | $122.26 | — |
| Day change | +$0.80 (+0.65%) | Jul 31, 2026 |
| Day open / high / low | $122.29 / $123.39 / $119.62 | Jul 31, 2026 |
| Volume | 29,085,070 | Jul 31, 2026 |
| After-hours (last) | $122.76 (−0.30, −0.24%) at 7:59 PM EDT | Jul 31, 2026 |
| **Market capitalization** | **$295.01 billion** | Jul 31, 2026 (S&P Global Market Intelligence via stockanalysis.com) |
| Enterprise value | $287.20 billion | Jul 31, 2026 |
| Market-cap 1-year change | −21.18% | Jul 31, 2026 |
| Market-cap rank | #47 globally | Jul 31, 2026 |
| Prior year-end market cap (Dec 31, 2025) | $423.66 billion | Dec 31, 2025 |
| 52-week range | $106.37 – $207.52 | as of Jul 31, 2026 (Nasdaq) |
| 52-week price change | −22.41% | as of Jul 31, 2026 (stockanalysis) |
| Confirmed next earnings date | Mon Aug 3, 2026, after market close | per Nasdaq and stockanalysis |

### Recent daily closes (Nasdaq historical), for context/charting
| Date | Close | Volume |
|---|---|---|
| Jul 27, 2026 | $131.53 | 36,708,200 |
| Jul 28, 2026 | $123.53 | 43,597,310 |
| Jul 29, 2026 | $123.00 | 27,207,860 |
| Jul 30, 2026 | $122.26 | 27,801,630 |
| **Jul 31, 2026** | **$123.06** | 29,085,070 |

## Notes
- **Nasdaq's `/api/quote/PLTR/info` endpoint mislabels the date.** It returns `lastSalePrice $123.06` with `lastTradeTimestamp "Jul 30, 2026"`. That timestamp is wrong/lagging: the same payload reports `netChange +0.80`, and $122.26 (the Jul 30 close per the historical table) + $0.80 = $123.06. The **historical** endpoint, plus stockanalysis and MarketBeat, all place $123.06 at the **Jul 31, 2026** close. Use the historical endpoint, not the info endpoint, for dated closes.
- Market cap is a **third-party computed** figure (price × shares outstanding, S&P Global methodology), not a company-reported number. If a slide states it, attribute it. It is consistent with the all-class share count, not the Class A count alone (Class A alone would give ~$282.6B).
- Do not carry these values forward to a later "as of" date — the whole point of this file is that it is dated.
