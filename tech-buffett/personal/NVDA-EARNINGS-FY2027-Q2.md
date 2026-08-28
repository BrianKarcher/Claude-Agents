# NVDA — Fiscal Q2 2027 Earnings Release Extract

**Fiscal period covered:** Q2 FY2027 (quarter ended July 26, 2026)
**Filing/publish date:** August 26, 2026 (reported after market close; stock reaction captured August 27, 2026)
**Source:** NVIDIA Newsroom press release, fetched directly ("NVIDIA Announces Financial Results for Second Quarter Fiscal 2027", https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027) — confirms all figures below. SEC EDGAR 8-K index (q2fy27pr.htm) direct fetch returned HTTP 403 and could not be read; the newsroom press release (same underlying release) was used instead. Pulled via WebSearch/WebFetch for this personal DCF request.

**UPDATE (post-initial-draft correction):** this extract originally carried an incorrect net income figure ($53,950M) and left the EPS/cash-flow/balance-sheet lines as unconfirmed data gaps. A direct fetch of the NVIDIA press release resolved all of them — see corrected tables below.

---

## Income Statement — GAAP ($M, except per-share)

| | Q2 FY2027 | Q2 FY2026 (prior year) |
|---|---|---|
| Revenue | 96,221 | ~46,700 (implied by +106% YoY) |
| YoY growth | +106% | — |
| QoQ growth | +18% (vs. Q1 FY2027's $81,600M) | — |
| Gross profit | 72,142 | — |
| Gross margin (GAAP) | 75.0% | 72.4% |
| Gross margin (non-GAAP) | 75.0% | — |
| Operating expenses | 8,408 | — (+55% YoY) |
| Operating income | 63,734 | — |
| Operating margin | 66.2% | — |
| Net income | 59,688 | 24,760 |
| Diluted EPS (GAAP) | $2.46 (confirmed) | $1.87 |
| Diluted EPS (non-GAAP) | $2.22 | — |
| Diluted weighted-avg shares | 24,285 | — |

**EPS reconciliation (RESOLVED):** GAAP diluted EPS of $2.46 ties out exactly against confirmed net income and share count ($59,688M / 24,285M = $2.458 ≈ $2.46). Non-GAAP EPS ($2.22) is LOWER than GAAP — the reverse of NVIDIA's usual pattern — consistent with GAAP net income being lifted by mark-to-market gains on NVIDIA's $42.8B marketable equity securities book (included in GAAP net income under ASU 2016-01, excluded from non-GAAP). The original extract's $53,950M net income figure was incorrect and is corrected here.

## Segment / Platform Revenue

Q1 FY2027 marked NVIDIA's shift from 5-segment reporting (Data Center, Gaming, Professional Visualization, Automotive, OEM & Other) to a 2-segment structure: **Data Center** and **Edge Computing** (gaming + professional visualization + automotive + robotics combined).

| Segment | Q2 FY2027 | % of Total | QoQ | YoY |
|---|---|---|---|---|
| Data Center | $89,000M | 92.5% | — | ~+117% |
| Edge Computing | $7,200M | 7.5% | +13% | +27% |
| **Total** | **$96,220M** | **100%** | +18% | +106% |

Customer-mix detail disclosed on the earnings call:
| Customer category | Q2 FY2027 Revenue | QoQ | YoY |
|---|---|---|---|
| Hyperscale customers | ~$49,000M | +13% | — |
| ACIE (AI Compute Infrastructure & Enterprise — NeoCloud, industrial, sovereign AI, enterprise) | ~$40,000M | +25% | +138% |

ACIE is now roughly half of total revenue and was described as growing at approximately 100% annualized.

## Cash Flow Statement ($M)

| | Q2 FY2027 | Q2 FY2026 (prior year) |
|---|---|---|
| Operating cash flow | 24,077 | — |
| Capital expenditures | (2,677) | — |
| Free cash flow | 21,400 | 13,500 |
| Depreciation & amortization | 1,127 | — |
| Stock-based compensation | 2,027 | — |

Note: FCF of $21.4B against confirmed net income of $59.7B implies an FCF/net-income conversion ratio of ~36% — well below NVIDIA's historical 90%+ norm (see NVDA-10K-FY2026.md for FY2026's 96,575/120,067 ≈ 80% annual conversion, itself already below the 90%+ figure referenced qualitatively in commentary). Attributed by the company/analysts to inventory build and supplier prepayments securing Blackwell/Rubin manufacturing and HBM memory supply.

## Balance Sheet Highlights ($M, as of July 26, 2026)

| | Q2 FY2027 (Jul 26, 2026) |
|---|---|
| Cash & cash equivalents | 22,443 |
| Marketable debt securities | 34,143 |
| Cash + cash equivalents + marketable debt securities | 56,586 |
| Marketable equity securities (strategic AI-ecosystem stakes) | 42,783 |
| Total debt (short + long-term) | 33,366 (CONFIRMED — up from $8,468M at FY2026 year-end; a real new bond issuance during H1 FY2027) |
| Net cash (cash+debt securities minus total debt) | 23,220 |
| Diluted weighted-avg shares outstanding | 24,285M (confirmed) |
| Total assets | 320,272 |

## Key Metrics Summary

| Metric | Q2 FY2027 |
|---|---|
| Revenue growth YoY | +106% |
| Revenue growth QoQ | +18% |
| Gross margin (GAAP/non-GAAP) | 75.0% / 75.0% |
| Operating margin | 66.2% |
| FCF (absolute) | $21.4B (conversion ~36% of net income — see note above) |
| SBC % of revenue | 2.1% (2,027 / 96,221) |

## Guidance Given (for Q3 FY2027)

- Revenue: **$108.0 billion ± 2%** (implies +12.3% QoQ at midpoint)
- Gross margin (GAAP and non-GAAP): **74.0% ± 50bps**
- Q4 FY2027 gross margin guided to **bottom at 71-72%**, explicitly attributed to rising memory (DRAM/HBM) costs
- A secondary source (BigGo Finance headline) referenced management guiding to approximately **70% revenue growth for FY2028** — treated in the DCF as closer to a supply-ceiling/Bull-case anchor than a Base-case assumption; not independently verified via a primary transcript quote.

## Qualitative Commentary (from earnings call coverage)

- **Supply vs. demand:** "supply chain is broadly constrained... supply sufficient to support approximately 70% growth, while demand exceeds that level."
- **Per-gigawatt monetization:** management framed revenue opportunity per gigawatt of deployed compute at ~$18B (Hopper) → ~$25B (Blackwell) → ~$40B (Vera Rubin).
- **China:** revenue share from China fell to a single-digit percentage of total revenue due to export controls; recent H200 export approvals cited as a potential (not yet realized at scale) re-entry path.
- **Stock reaction:** shares closed at $209.66 the prior session and rose to $227.98 (+8.74%) on/after the print; Deutsche Bank raised its price target to $220 around the same window.

## One-Time Items / Restatements

None identified for this specific quarter in this research pass.

## Data Gaps (explicit)

All previously-flagged gaps in this extract (operating cash flow, capex, SBC, total debt, diluted shares, GAAP EPS reconciliation) were resolved via a direct fetch of NVIDIA's press release and are now confirmed figures in the tables above.

- Direct SEC.gov 8-K fetch (q2fy27pr.htm) still returned HTTP 403; the NVIDIA Newsroom press release (same underlying release, different host) was fetched directly instead and used as the primary source for this update.
- Remaining gap: exact non-GAAP net income (only the $2.22 non-GAAP EPS figure was confirmed, not a non-GAAP net income dollar amount).
