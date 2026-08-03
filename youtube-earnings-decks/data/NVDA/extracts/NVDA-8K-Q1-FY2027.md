# NVDA — Q1 FY2027 (three months ended April 26, 2026) — 8-K Exhibit 99.1 earnings press release

**Source:** https://www.sec.gov/Archives/edgar/data/1045810/000104581026000051/q1fy27pr.htm
(Exhibit 99.1 to the Form 8-K filed 2026-05-20, accession 0001045810-26-000051 — "NVIDIA Announces Financial Results for First Quarter Fiscal 2027", includes CONDENSED CONSOLIDATED STATEMENTS OF INCOME, unaudited)
**Fetched:** 2026-08-02
**Cross-checked against:**
1. Internal consistency of the release itself: revenue 81,615 − cost of revenue 20,458 = gross profit 61,157; 61,157 / 81,615 = 74.93%, matching the release's stated GAAP gross margin of 74.9%. Operating income 61,157 − 7,621 = 53,536, matching the stated figure.
2. Prior-year comparable column (Q1 FY2026, quarter ended April 27, 2025) revenue $44,062M is the same value used as the Y/Y base for the stated "up 85%": 81,615 / 44,062 − 1 = 85.23%.
3. TTM revenue derived from this release plus `NVDA-8K-Q3-FY2026.md` and `NVDA-10K-FY2026.md` ($253,491M) independently matches stockanalysis.com's stated Revenue (ttm) of $253.49B — see `NVDA-MARKETDATA-2026-07-31.md`.

## Figures ($ millions unless noted) — GAAP

| Metric | Q1 FY2027 (Apr 26, 2026) | Prior-year comparable Q1 FY2026 (Apr 27, 2025) |
|---|---|---|
| Revenue | 81,615 | 44,062 |
| Cost of revenue | 20,458 | 17,394 |
| Gross profit | 61,157 | 26,668 |
| Gross margin (stated) | 74.9% | 60.5% |
| Research and development | 6,321 | 3,989 |
| Sales, general and administrative | 1,300 | 1,041 |
| Total operating expenses | 7,621 | 5,030 |
| Operating income | 53,536 | 21,638 |
| Net income | 58,321 | 18,775 |
| Diluted EPS | $2.39 | $0.76 |
| Diluted weighted-average shares (millions) | 24,391 | 24,611 |

Sequential quarter, from the release's own Q1 FY27 Summary table: **Q4 FY2026 revenue $68,127M**, Q4 FY2026 GAAP gross margin 75.0%, Q4 FY2026 GAAP operating income $44,299M, Q4 FY2026 GAAP net income $42,960M.

Derived (exact arithmetic, not estimates):
- YoY revenue growth = 81,615 / 44,062 − 1 = **+85.23%** (release states "up 85%")
- GAAP gross margin = 61,157 / 81,615 = **74.93%** (release states 74.9%)

## Notes

- All figures above are **GAAP**. The release also presents non-GAAP figures that must not be substituted: non-GAAP gross margin 75.0%, non-GAAP operating income $53,783M, non-GAAP net income $45,548M, non-GAAP diluted EPS $1.87. For a peer-comps gross-margin row, use the **GAAP 74.9%**.
- **Non-GAAP definition change:** the release states that beginning in Q1 FY2027, NVIDIA's non-GAAP measures **no longer exclude stock-based compensation expense**, and that historical non-GAAP information has been restated to include SBC. This makes NVDA's non-GAAP figures non-comparable to pre-FY2027 non-GAAP figures. GAAP figures are unaffected.
- GAAP net income of $58,321M is inflated by a **$15,936M non-cash gain from equity securities** (in "Other income (expense), net" of $15,929M); GAAP net income exceeds non-GAAP net income this quarter for that reason. Do not use net income as a proxy for operating performance in this quarter without flagging that gain.
- **Segment reporting change:** NVIDIA states it is transitioning to a new reporting framework with two market platforms (Data Center and Edge Computing, with Data Center split into Hyperscale and ACIE). Data Center Q1 FY27 revenue was a record $75.2B (up 92% YoY); Edge Computing was $6.4B (up 29% YoY). Older Compute/Networking or Graphics segment splits are not comparable to these.
- **Forward-looking (do NOT put in the cache table, label clearly if used in a deck):** Q2 FY2027 outlook of revenue $91.0B ±2%, GAAP gross margin 74.9% ±50bp, GAAP operating expenses ~$8.5B — company guidance issued 2026-05-20, and NVIDIA notes it assumes no Data Center compute revenue from China.
- Fiscal calendar: NVIDIA's FY2027 Q1 ended April 26, 2026. This is a **different fiscal calendar than Palantir's** (PLTR uses calendar quarters). Any PLTR/NVDA comp table must label periods by each company's own most-recently-reported quarter, not pretend they are the same period.
- Fetch method: SEC.gov returns 403 to WebFetch; `curl` with an explicit descriptive User-Agent returns 200. Directory listings work via `.../index.json`, not the HTML index.
