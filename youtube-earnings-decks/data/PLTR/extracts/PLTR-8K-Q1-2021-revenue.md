# PLTR — Q1 2021 (partial — revenue only) — SUPERSEDED

> **SUPERSEDED 2026-08-02 by `PLTR-8K-Q1-2021.md`.** Do not use this file. The full quarter has since
> been verified from the actual primary source (8-K Exhibit 99.1 filed 2021-05-11), which reports
> revenue $341,234K, gross profit $267,123K, and loss from operations $(114,014)K. The revenue figure
> below was correct but imprecise; the gaps below are now closed. Kept only for provenance history.

**Original source (weak):** search-surfaced confirmation of Palantir's Q1 2021 earnings release (quarter ended March 31, 2021, reported May 11, 2021); figure corroborated by multiple independent references (CNBC coverage, Palantir's own press release headline) to "$341 million" revenue for the quarter, beating a ~$332.2M consensus estimate.
**Fetched:** 2026-08-02
**Period:** Three months ended March 31, 2021

## Figures

| Metric | Value | Status |
|---|---|---|
| Total revenue | $341M | Superseded — exact figure is $341,234K per the 8-K. |
| Gross profit | — | Gap closed — $267,123K per the 8-K. See `PLTR-8K-Q1-2021.md`. |
| Operating income | — | Gap closed — $(114,014)K per the 8-K. See `PLTR-8K-Q1-2021.md`. |

## Notes

- Historical note on why this extract was weak: the session that wrote it hit HTTP 403 on SEC.gov via
  the WebFetch tool and stopped there. SEC.gov's fair-access policy requires a descriptive
  User-Agent; `curl -A "<app>/<version> (<email>)"` returns HTTP 200 for both the submissions JSON at
  `data.sec.gov` and document URLs under `www.sec.gov/Archives/`. A 403 from one fetch tool is not
  evidence that a filing is inaccessible.
