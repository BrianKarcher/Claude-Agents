# PLTR — Quarterly Financials Cache (GAAP, $ millions)

Read this file first before fetching anything for PLTR. Only fetch/verify a quarter that's missing or listed as a gap below.

**Companion cache:** segment (US commercial / US government) revenue, customer counts, cash flow / free cash flow, and non-GAAP margins & adjusted EPS live in `other-metrics.md` — check there too before fetching. Point-in-time market data (price, market cap, institutional ownership) and analyst price targets are not cached in either table; they live as dated files in `extracts/` (`PLTR-MARKETDATA-*.md`, `PLTR-OWNERSHIP-*.md`, `PLTR-ANALYSTTARGETS-*.md`) and must be re-fetched fresh.

| Quarter | Revenue | Gross Profit | Operating Income | Source extract | Verified |
|---|---|---|---|---|---|
| Q1 2021 | 341.23 | 267.12 | -114.01 | extracts/PLTR-8K-Q1-2021.md | 2026-08-02 |
| Q2 2021 | 375.64 | 284.72 | -146.15 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q3 2021 | 392.15 | 305.34 | -91.94 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q4 2021 | 432.87 | 345.30 | -58.94 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q1 2022 | 446.36 | 351.95 | -39.44 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q2 2022 | 473.01 | 370.79 | -41.75 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q3 2022 | 477.88 | 370.27 | -62.19 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q4 2022 | 508.62 | 404.31 | -17.83 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q1 2023 | 525.19 | 417.54 | 4.12 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q2 2023 | 533.32 | 426.42 | 10.07 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q3 2023 | 558.16 | 450.24 | 39.98 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q4 2023 | 608.35 | 499.71 | 65.79 | extracts/PLTR-8K-Q4-2023.md | 2026-08-02 |
| Q1 2024 | 634.34 | 518.08 | 80.88 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q2 2024 | 678.13 | 549.57 | 105.34 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q3 2024 | 725.52 | 578.88 | 113.14 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q4 2024 | 827.52 | 652.99 | 11.04 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q1 2025 | 883.86 | 710.89 | 176.05 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q2 2025 | 1,004.00 | 810.76 | 269.32 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q3 2025 | 1,181.00 | 973.79 | 393.26 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q4 2025 | 1,407.00 | 1,191.00 | 575.39 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |
| Q1 2026 | 1,633.00 | 1,417.00 | 754.00 | extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md | 2026-08-02 |

## Known gaps

- ~~**Q1 2021 gross profit and operating income**~~: **CLOSED 2026-08-02.** Verified from the primary source — 8-K Exhibit 99.1 earnings press release filed 2021-05-11, cross-checked against the Q1 2021 10-Q and the Q1 2022 press release's prior-year column. See `extracts/PLTR-8K-Q1-2021.md`. Revenue also refined from 341.0 to the exact 341.23 reported. Q1 2021 is now safe to use in charts requiring all three metrics. (Note: SEC.gov 403s the WebFetch tool but serves `curl` with an explicit User-Agent — that's how this was retrieved.)
- **Q2 2026 and later**: not yet reported as of this cache's last update (2026-08-02) — the Q2 2026 earnings call is scheduled for 2026-08-03. Do not add a row until it's actually reported; guidance/estimates for Q2 2026 belong in the deck only, clearly labeled, never in this actuals-only cache.

## Reconciliation notes

- All figures are **GAAP**, not Palantir's "Adjusted" (non-GAAP) metrics used elsewhere in some decks. See `extracts/PLTR-AGGREGATOR-Q2-2021-Q1-2026.md` for the full cross-check methodology (FY2024 and FY2025 quarterly sums reconcile against independently reported annual totals).
- **2026-08-02 upgrade of confidence on four aggregator-sourced rows.** While gathering data for `other-metrics.md`, the Q1 2025, Q2 2025 and Q1 2026 earnings press releases were opened directly. They confirm the aggregator rows for Q2 2024 (678,134 / 549,572 / 105,339), Q1 2025 (883,855 / 710,885 / 176,048), Q2 2025 (1,003,697 / 810,763 / 269,317) and Q1 2026 (1,632,583 / 1,416,785 / 753,998) — all match to the rounding shown above. No corrections needed; these four rows are now primary-source-verified. Extracts: `extracts/PLTR-8K-Q1-2025.md`, `extracts/PLTR-8K-Q2-2025.md`, `extracts/PLTR-8K-Q1-2026.md`, `extracts/PLTR-10Q-Q1-2026.md`.
