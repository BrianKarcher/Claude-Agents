# AMD — FY2008 through FY2025 (SEC XBRL company-concept API)

**Source:** SEC XBRL company-concept endpoints for CIK 0000002488 (Advanced Micro Devices, Inc.):
- https://data.sec.gov/api/xbrl/companyconcept/CIK0000002488/us-gaap/GrossProfit.json
- https://data.sec.gov/api/xbrl/companyconcept/CIK0000002488/us-gaap/OperatingIncomeLoss.json
- https://data.sec.gov/api/xbrl/companyconcept/CIK0000002488/us-gaap/SalesRevenueGoodsNet.json
- https://data.sec.gov/api/xbrl/companyconcept/CIK0000002488/us-gaap/SalesRevenueNet.json
- https://data.sec.gov/api/xbrl/companyconcept/CIK0000002488/us-gaap/RevenueFromContractWithCustomerExcludingAssessedTax.json

**Fetched:** 2026-08-03
**Filter applied:** `form` in (10-K, 10-K/A) and period length >= 300 days, i.e. annual figures as tagged in annual reports only.

**Cross-checked against:**
- **Primary cross-check (built in):** each 10-K presents three comparative fiscal years, so every fiscal year from FY2009 to FY2024 is independently tagged in **two or three separately filed, separately audited 10-Ks**. Every one of those repeated taggings agrees exactly, with the two documented exceptions below (FY2016 and FY2017, ASC 606 restatement).
- FY2008 and FY2009 additionally verified against the FY2008 and FY2009 10-K HTML directly — see `AMD-10K-FY2008.md`, `AMD-10K-FY2009.md`.
- FY2023–FY2025 additionally verified against the face of the FY2025 10-K income statement — see `AMD-10K-FY2025.md`.
- Line-item label mapping confirmed by rendering the "Consolidated Statements of Operations" R-pages of the FY2014, FY2016, FY2019 and FY2025 10-Ks: `us-gaap:GrossProfit` is the line captioned **"Gross margin"** (FY2018 and earlier) / **"Gross profit"** (FY2019+), and `us-gaap:OperatingIncomeLoss` is **"Operating income (loss)"** / **"Operating income"**.
- Independent non-SEC check: stockanalysis.com (FY2021–FY2025, exact) and companiesmarketcap.com (revenue, most years) — see `AMD-AGGREGATOR-FY1996-FY2025.md`.

## Figures ($ millions, GAAP) — as originally reported in each fiscal year's own 10-K

| FY | Period end | Revenue | Gross Profit | Operating Income | Reported in N filings |
|---|---|---|---|---|---|
| 2008 | 2008-12-27 | 5,808 | 2,320 | (1,955) | 1 (FY2010 10-K) + FY2008/FY2009 10-K HTML |
| 2009 | 2009-12-26 | 5,403 | 2,272 | 664 | 2 + FY2009 10-K HTML |
| 2010 | 2010-12-25 | 6,494 | 2,961 | 848 | 3 |
| 2011 | 2011-12-31 | 6,568 | 2,940 | 368 | 3 |
| 2012 | 2012-12-29 | 5,422 | 1,235 | (1,056) | 3 |
| 2013 | 2013-12-28 | 5,299 | 1,978 | 103 | 3 |
| 2014 | 2014-12-27 | 5,506 | 1,839 | (155) | 3 |
| 2015 | 2015-12-26 | 3,991 | 1,080 | (481) | 3 |
| 2016 | 2016-12-31 | 4,272 | 998 | (372) | 2 (see restatement note) |
| 2017 | 2017-12-30 | 5,329 | 1,823 | 204 | 1 (see restatement note) |
| 2018 | 2018-12-29 | 6,475 | 2,447 | 451 | 3 |
| 2019 | 2019-12-28 | 6,731 | 2,868 | 631 | 3 |
| 2020 | 2020-12-26 | 9,763 | 4,347 | 1,369 | 3 |
| 2021 | 2021-12-25 | 16,434 | 7,929 | 3,648 | 3 |
| 2022 | 2022-12-31 | 23,601 | 10,603 | 1,264 | 3 |
| 2023 | 2023-12-30 | 22,680 | 10,460 | 401 | 3 |
| 2024 | 2024-12-28 | 25,785 | 12,725 | 1,900 | 2 |
| 2025 | 2025-12-27 | 34,639 | 17,152 | 3,694 | 1 (most recent 10-K) |

Revenue tag by era: `SalesRevenueGoodsNet` / `SalesRevenueNet` for FY2008–FY2017; `RevenueFromContractWithCustomerExcludingAssessedTax` for FY2016 (restated) and FY2018+.

## ASC 606 restatement — FY2016 and FY2017 have two as-filed values

AMD adopted ASC 606 (revenue from contracts with customers) effective fiscal 2018 using the **full retrospective** method, restating FY2016 and FY2017. Both versions are genuine as-filed values.

| FY | Basis | Revenue | Gross Profit | Operating Income | Accession(s) reporting it |
|---|---|---|---|---|---|
| 2016 | As originally reported (pre-606) | 4,272 | 998 | (372) | 0000002488-17-000043 (FY2016 10-K), 0000002488-18-000042 (FY2017 10-K) |
| 2016 | ASC 606 restated | 4,319 | 1,003 | (373) | 0000002488-19-000011 (FY2018 10-K) |
| 2017 | As originally reported (pre-606) | 5,329 | 1,823 | 204 | 0000002488-18-000042 (FY2017 10-K) |
| 2017 | ASC 606 restated | 5,253 | 1,787 | 127 | 0000002488-19-000011 (FY2018 10-K), 0000002488-20-000008 (FY2019 10-K) |

The FY2017 operating-income difference is material — 204 vs. 127, a 38% swing. Any FY2017 figure on a slide must state which basis it is on.

FY2015 and earlier were **not** restated to ASC 606, so an all-606 series is not available before FY2016 regardless of which basis is chosen.

## Notes

- All values **GAAP as-reported**, in USD, converted from the API's units of dollars to $ millions.
- No annual value in the whole FY2008–FY2025 range disagrees between filings other than the two ASC 606 years above. That is a strong internal cross-check: 14 of the 18 years are corroborated by three independently filed 10-Ks.
- FY2008 is tagged in only one filing (the FY2010 10-K) because AMD's XBRL income-statement tagging begins there; it is corroborated instead by the FY2008 and FY2009 10-K HTML, which agree exactly.
- **Do not read FY2009's 664 operating income as an operational result** — it is created by a one-time +$1,242M Intel legal-settlement credit inside operating expenses. See `AMD-10K-FY2009.md`.
- Structural breaks in this series: GlobalFoundries manufacturing spun off March 2009; Xilinx acquired 2022-02-14 (drives the FY2022 revenue step-up and the intangible amortization that suppresses GAAP operating income in FY2022–FY2023); ZT Systems acquired 2025 with its manufacturing arm classified as discontinued operations in FY2025.
