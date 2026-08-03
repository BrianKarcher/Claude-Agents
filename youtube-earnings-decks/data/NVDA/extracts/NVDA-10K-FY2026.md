# NVDA — FY2026 (fiscal year ended January 25, 2026) — Form 10-K, annual revenue only

**Source:** https://data.sec.gov/api/xbrl/companyconcept/CIK0001045810/us-gaap/Revenues.json
Single fact retrieved: `us-gaap:Revenues`, period 2025-01-27 → 2026-01-25, value **215,938,000,000**, form **10-K**, fy 2026, fp FY, filed **2026-02-25** (accession 0001045810-26-000021, primary document `nvda-20260125.htm`).
This is the XBRL-tagged value from NVIDIA's own FY2026 Form 10-K as filed with the SEC — i.e. a primary source, retrieved via SEC's structured-data API rather than by parsing the 10-K HTML.
**Fetched:** 2026-08-02
**Purpose:** cross-check the quarterly revenue chain used to build TTM revenue through Q1 FY2027.
**Cross-checked against:** quarterly sum from primary releases — Q1 FY26 44,062 + Q2 FY26 46,743 + Q3 FY26 57,006 + Q4 FY26 68,127 = **215,938**. Exact match, no rounding residual.

## Figures ($ millions) — GAAP

| Metric | FY2026 (ended 2026-01-25) |
|---|---|
| Revenue | 215,938 |

## Notes

- Only the annual revenue fact was pulled. No margin, operating income, or balance-sheet data from the 10-K is recorded here; do not infer any.
- Note that the earlier `us-gaap:RevenueFromContractWithCustomerExcludingAssessedTax` concept has no facts for NVDA after FY2022 — NVIDIA tags top-line revenue as `us-gaap:Revenues`. A future session querying the wrong concept will get an empty result and should not read that as "data unavailable."
- Q4 FY2026 revenue ($68,127M) is itself sourced from the Q1 FY2027 press release's sequential-quarter column (`NVDA-8K-Q1-FY2027.md`), and is independently confirmed by 215,938 − 147,811 = 68,127.
