# SNOW — Quarterly Financials Cache (GAAP, $ thousands)

Read this file first before fetching anything for SNOW. Only fetch/verify a quarter that's missing or listed as a gap below.

**Fiscal calendar warning:** Snowflake's fiscal year ends **January 31**. FY2027 Q1 ended **2026-04-30**. Not aligned to PLTR's calendar quarters or NVDA's late-January fiscal year. Always label periods with Snowflake's own fiscal quarter name plus the period end date.

**Revenue definition warning:** Snowflake reports **total revenue** and, separately, **product revenue** (~96% of total; the remainder is professional services and other). It guides on *product* revenue. Both are recorded below — never mix them in a growth rate or a multiple.

| Quarter | Period ended | Revenue (total) | Product revenue | Gross Profit (total) | GAAP gross margin (total) | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|---|---|---|
| Q2 FY2026 | 2025-07-31 | 1,144,969 | not captured | 773,154 | 67.5% | not captured | extracts/SNOW-8K-Q2-FY2026.md | 2026-08-02 |
| Q3 FY2026 | 2025-10-31 | 1,212,909 | not captured | 822,036 | 67.8% | not captured | extracts/SNOW-8K-Q3-FY2026.md | 2026-08-02 |
| Q4 FY2026 | 2026-01-31 | 1,283,994 | 1,226,631 | 857,663 | 66.8% | (318,159) | extracts/SNOW-8K-Q4-FY2026.md | 2026-08-02 |
| Q1 FY2027 | 2026-04-30 | 1,390,951 | 1,334,329 | 926,451 | 66.6% | (326,154) | extracts/SNOW-8K-Q1-FY2027.md | 2026-08-02 |

Prior-year comparables captured from the releases' own prior-year columns (usable, primary-sourced):

| Quarter | Period ended | Revenue (total) | Product revenue | Gross Profit (total) | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| Q1 FY2026 | 2025-04-30 | 1,042,074 | 996,813 | 693,288 | (447,257) | extracts/SNOW-8K-Q1-FY2027.md | 2026-08-02 |
| Q2 FY2025 | 2024-07-31 | 868,823 | not captured | 580,745 | not captured | extracts/SNOW-8K-Q2-FY2026.md | 2026-08-02 |
| Q3 FY2025 | 2024-10-31 | 942,094 | not captured | 621,200 | not captured | extracts/SNOW-8K-Q3-FY2026.md | 2026-08-02 |
| Q4 FY2025 | 2025-01-31 | 986,770 | 943,303 | 653,586 | (386,678) | extracts/SNOW-8K-Q4-FY2026.md | 2026-08-02 |

Annual, for reconciliation:

| Fiscal year | Period ended | Revenue (total) | Product revenue | Gross Profit | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| FY2026 | 2026-01-31 | 4,683,946 | 4,472,317 | 3,146,141 | (1,435,165) | extracts/SNOW-8K-Q4-FY2026.md | 2026-08-02 |
| FY2025 | 2025-01-31 | 3,626,396 | 3,462,422 | 2,411,723 | (1,456,010) | extracts/SNOW-8K-Q4-FY2026.md | 2026-08-02 |

## Derived figures (exact arithmetic from the rows above — no estimation)

- **Most recent reported quarter: Q1 FY2027** (ended 2026-04-30, reported 2026-05-27).
- **Q1 FY2027 total-revenue YoY growth** = 1,390,951 / 1,042,074 − 1 = **+33.5%** (Snowflake states 33%).
- **Q1 FY2027 product-revenue YoY growth** = 1,334,329 / 996,813 − 1 = **+33.9%** (Snowflake states 34%).
- **Q1 FY2027 GAAP total gross margin** = 926,451 / 1,390,951 = **66.6%** (release rounds to 67%).
- **Q1 FY2027 GAAP product gross margin** = 947,455 / 1,334,329 = **71.0%** — a *different* metric; label it explicitly if used.
- **TTM total revenue through Q1 FY2027** = 1,144,969 + 1,212,909 + 1,283,994 + 1,390,951 = **5,032,823** ($5.0328B). Confirmed two independent ways: (a) FY2026 4,683,946 − Q1 FY2026 1,042,074 + Q1 FY2027 1,390,951 = 5,032,823; (b) matches stockanalysis.com's stated Revenue (ttm) of $5.03B.
- Four quarters of FY2026 sum to the reported annual total: 1,042,074 + 1,144,969 + 1,212,909 + 1,283,994 = 4,683,946 ✓

## Known gaps

- **Q2 FY2026 and Q3 FY2026 product revenue and operating income:** deliberately not captured — those quarters were opened only for the total-revenue line needed in the TTM build. Gross profit *was* captured for them. Re-open the source URLs in the corresponding extracts if a deck needs product revenue or operating loss for those quarters; do not derive them.
- **Q2 FY2025 and Q3 FY2025 product revenue and operating income:** same — prior-year columns were captured for revenue and gross profit only.
- **All quarters before Q2 FY2025:** never checked. Not a dead end, just not needed for the peer-comps table this cache was created for.
- **Q2 FY2027 and later:** not yet reported as of 2026-08-02. Snowflake guided Q2 FY2027 product revenue to $1,415–1,420M and FY2027 product revenue to $5,840M — **non-GAAP guidance, not actuals**, and on the *product* revenue base. Per project policy that does not belong in this table.

## Reconciliation notes

- All figures are **GAAP**. Snowflake is **GAAP operating-loss-making in every period recorded here**, including Q1 FY2027 (−$326.2M, a −23.4% operating margin) and all of FY2026 (−$1,435.2M). Its non-GAAP operating income is positive (Q1 FY2027: +$165.8M, 11.9% margin) because it excludes stock-based compensation and related items. Presenting the non-GAAP figure without labeling it would materially misstate profitability — this is the single most important caveat for any SNOW slide.
- Gross-margin percentages in the main table are computed as total gross profit / total revenue from the rows shown; the release itself rounds to whole percents (67%).
- Non-financial Q1 FY2027 metrics available in `extracts/SNOW-8K-Q1-FY2027.md` (net revenue retention 126%, 779 customers >$1M TTM product revenue, RPO $9.21B) — all primary-sourced and usable.
- Market cap, share price, and P/S multiples are **not** stored here (point-in-time, goes stale). See `extracts/SNOW-MARKETDATA-2026-07-31.md` for a dated snapshot and the P/S arithmetic.
- Snowflake's share count is **rising** (dilution), unlike NVDA's buyback-driven decline: 338.8M (Aug 2025) → 342.2M (Nov 2025) → 345.7M (Mar 2026) → 346.6M (May 2026) per 10-Q/10-K cover pages.
