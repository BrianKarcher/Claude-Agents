# AMD — aggregator cross-check (independent, non-SEC)

**Fetched:** 2026-08-03

Used **only as a cross-check** on the SEC-filing figures in `AMD-XBRL-FY2008-FY2025.md`, `AMD-10K-FY2007.md`, `AMD-10K-FY2008.md`, `AMD-10K-FY2009.md` and `AMD-10K-FY2025.md`. No cache row is sourced from an aggregator.

## Source 1 — stockanalysis.com (revenue, gross profit, operating income)

**Source:** https://stockanalysis.com/stocks/amd/financials/
**Coverage returned:** FY2021–FY2025 only (free tier shows five years; a `range=20Y` request still returned five).

| FY | Revenue | Gross Profit | Operating Income | Matches SEC? |
|---|---|---|---|---|
| 2021 | 16,434 | 7,929 | 3,648 | exact |
| 2022 | 23,601 | 10,603 | 1,264 | exact |
| 2023 | 22,680 | 10,460 | 401 | exact |
| 2024 | 25,785 | 12,725 | 1,900 | exact |
| 2025 | 34,639 | 17,152 | 3,694 | exact |

All 15 values match the filings exactly.

## Source 2 — companiesmarketcap.com (revenue only)

**Source:** https://companiesmarketcap.com/amd/revenue/
**Coverage returned:** 1996–2025 plus a 2026 TTM figure. Values given to 3 significant figures.

| FY | Aggregator | SEC as-reported | SEC restated/recast | Verdict |
|---|---|---|---|---|
| 2006 | 5.64 B | 5,649 | 5,627 | matches as-reported |
| 2007 | 5.93 B | 6,013 | 5,858 | **matches neither — disregard** |
| 2008 | 5.87 B | 5,808 | — | **does not match — disregard** |
| 2009 | 5.40 B | 5,403 | — | matches |
| 2010 | 6.49 B | 6,494 | — | matches |
| 2011 | 6.56 B | 6,568 | — | matches |
| 2012 | 5.42 B | 5,422 | — | matches |
| 2013 | 5.29 B | 5,299 | — | matches |
| 2014 | 5.50 B | 5,506 | — | matches |
| 2015 | 3.99 B | 3,991 | — | matches |
| 2016 | 4.27 B | 4,272 | 4,319 | matches as-reported |
| 2017 | 5.39 B | 5,329 | 5,253 | **matches neither — disregard** |
| 2018 | 6.47 B | 6,475 | — | matches |
| 2019 | 6.73 B | 6,731 | — | matches |
| 2020 | 9.76 B | 9,763 | — | matches |
| 2021 | 16.43 B | 16,434 | — | matches |
| 2022 | 23.60 B | 23,601 | — | matches |
| 2023 | 22.68 B | 22,680 | — | matches |
| 2024 | 25.78 B | 25,785 | — | matches |
| 2025 | 34.63 B | 34,639 | — | matches |

## Notes

- **companiesmarketcap.com is wrong on FY2007, FY2008 and FY2017** — its values match neither the as-originally-reported nor the restated/recast SEC figures. This is exactly the class of aggregator error the project's cross-check rule exists to catch. Do not use that site as a source for AMD; the SEC filings govern. Its other 17 years agree, so it remains usable as a directional sanity check only.
- macrotrends.net was attempted (https://www.macrotrends.net/stocks/charts/AMD/amd/gross-profit) and returned HTTP 402; wisesheets.io returned HTTP 404. Neither contributed to verification.
- Neither aggregator supplied gross profit or operating income before FY2021, so the pre-2021 gross-profit and operating-income cross-checks rest entirely on the SEC filings — which is the stronger basis anyway: each of those years is tagged identically in two or three independently filed 10-Ks, and FY2006–FY2009 additionally foot against their own filings' quarterly tables and expense lines.
