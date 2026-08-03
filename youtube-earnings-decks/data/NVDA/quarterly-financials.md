# NVDA — Quarterly Financials Cache (GAAP, $ millions)

Read this file first before fetching anything for NVDA. Only fetch/verify a quarter that's missing or listed as a gap below.

**Fiscal calendar warning:** NVIDIA's fiscal year ends in late January. FY2027 Q1 ended **2026-04-26**. NVDA quarters are *not* calendar quarters and are *not* aligned to PLTR's calendar quarters or SNOW's Jan-31 fiscal year. Always label periods with NVIDIA's own fiscal quarter name plus the period end date.

| Quarter | Period ended | Revenue | Gross Profit | Gross Margin | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| Q2 FY2026 | 2025-07-27 | 46,743 | not captured | 72.4% | not captured | extracts/NVDA-8K-Q3-FY2026.md | 2026-08-02 |
| Q3 FY2026 | 2025-10-26 | 57,006 | not captured | 73.4% | not captured | extracts/NVDA-8K-Q3-FY2026.md | 2026-08-02 |
| Q4 FY2026 | 2026-01-25 | 68,127 | 51,093 | 75.0% | 44,299 | extracts/NVDA-8K-Q1-FY2027.md | 2026-08-02 |
| Q1 FY2027 | 2026-04-26 | 81,615 | 61,157 | 74.9% | 53,536 | extracts/NVDA-8K-Q1-FY2027.md | 2026-08-02 |

Prior-year comparable captured from the Q1 FY2027 release's own prior-year column (usable, primary-sourced):

| Quarter | Period ended | Revenue | Gross Profit | Gross Margin | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| Q1 FY2026 | 2025-04-27 | 44,062 | 26,668 | 60.5% | 21,638 | extracts/NVDA-8K-Q1-FY2027.md | 2026-08-02 |

Annual, for reconciliation:

| Fiscal year | Period ended | Revenue | Source extract | Verified |
|---|---|---|---|---|
| FY2026 | 2026-01-25 | 215,938 | extracts/NVDA-10K-FY2026.md | 2026-08-02 |

## Derived figures (exact arithmetic from the rows above — no estimation)

- **Most recent reported quarter: Q1 FY2027** (ended 2026-04-26, reported 2026-05-20).
- **Q1 FY2027 YoY revenue growth** = 81,615 / 44,062 − 1 = **+85.2%** (NVIDIA states "up 85%").
- **Q1 FY2027 GAAP gross margin** = 61,157 / 81,615 = **74.9%**.
- **TTM revenue through Q1 FY2027** = 46,743 + 57,006 + 68,127 + 81,615 = **253,491** ($253.491B). Confirmed two independent ways: (a) FY2026 215,938 − Q1 FY2026 44,062 + Q1 FY2027 81,615 = 253,491; (b) matches stockanalysis.com's stated Revenue (ttm) of $253.49B.

## Known gaps

- **Q2 FY2026 and Q3 FY2026 gross profit and operating income (dollars):** deliberately not captured. Those quarters were fetched only for the revenue needed in the TTM build. The stated GAAP gross *margin* percentages are recorded, but the dollar gross profit and operating income were not read off the statements — **do not compute them from the margin percentage**, re-open `extracts/NVDA-8K-Q3-FY2026.md`'s source URL instead.
- **All quarters before Q1 FY2026:** never checked. Not a dead end — simply not needed for the peer-comps table this cache was created for. Fetch from the corresponding 8-K earnings releases if a chart needs a longer history.
- **Q2 FY2027 and later:** not yet reported as of 2026-08-02. NVIDIA guided Q2 FY2027 revenue to $91.0B ±2% (issued 2026-05-20) — that is **guidance, not an actual**, and per project policy it does not belong in this table. Do not add a row until reported.

## Reconciliation notes

- All figures are **GAAP**. NVIDIA also reports non-GAAP measures (Q1 FY2027 non-GAAP gross margin 75.0%, non-GAAP operating income $53,783M, non-GAAP net income $45,548M, non-GAAP diluted EPS $1.87). Do not substitute them.
- **Non-GAAP definition change from Q1 FY2027 onward:** NVIDIA's non-GAAP measures no longer exclude stock-based compensation, and historical non-GAAP figures were restated to include SBC. Non-GAAP series that straddle this change are not comparable. GAAP series are unaffected — another reason to keep this cache GAAP-only.
- Q1 FY2027 GAAP net income ($58,321M) exceeds non-GAAP net income because of a **$15.9B non-cash gain on equity securities**. Net income is not recorded in this table; if a future deck adds it, that gain must be flagged.
- Market cap, share price, and P/S multiples are **not** stored here (point-in-time, goes stale). See `extracts/NVDA-MARKETDATA-2026-07-31.md` for a dated snapshot and the P/S arithmetic.
