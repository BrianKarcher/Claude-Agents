# PLTR — Q1 2026 Business Update (official investor presentation, 37 pages)

**Source:** https://investors.palantir.com/files/Palantir%20-%20Q1%202026%20Business%20Update.pdf
(Palantir Investor Relations; the supplemental investor presentation referenced in the Q1 2026 earnings release. Not filed on EDGAR.)
**Fetched:** 2026-08-02 (downloaded PDF, text extracted with `pdftotext -layout`)
**Cross-checked against:**
1. Form 10-Q Q1 2026 (`PLTR-10Q-Q1-2026.md`) — total customer counts 1,007 / 769 match exactly; adjusted gross margin 88% matches the 10-Q MD&A's "88% when excluding stock-based compensation"; adjusted gross profit $1,434,691 = GAAP gross profit $1,416,785 + SBC in cost of revenue $17,906 ✓.
2. Q1 2026 8-K press release (`PLTR-8K-Q1-2026.md`) — segment revenue, adjusted operating income/margin, adjusted FCF, adjusted EPS all identical.
3. Internal consistency: the appendix's Y/Y revenue-growth series (p.30) reconciles against every quarter in `../quarterly-financials.md` — Q2 2024 +27%, Q3 2024 +30%, Q4 2024 +36%, Q1 2025 +39%, Q2 2025 +48%, Q3 2025 +63%, Q4 2025 +70%, Q1 2026 +85%, all matching the cached GAAP revenue series to the rounded percent.

## Figures

### Customer counts (TTM), p.23 and p.24 — the only source for the commercial-only cuts
| TTM ended | Total customer count | Commercial customer count | US commercial customer count |
|---|---|---|---|
| Mar 31, 2025 | 769 | 622 | 432 |
| Jun 30, 2025 | 849 (+10% Q/Q) | 692 (+11% Q/Q) | 485 (+12% Q/Q) |
| Sep 30, 2025 | 911 (+7% Q/Q) | 742 (+7% Q/Q) | 530 (+9% Q/Q) |
| Dec 31, 2025 | 954 (+5% Q/Q) | 780 (+5% Q/Q) | 571 (+8% Q/Q) |
| **Mar 31, 2026** | **1,007 (+6% Q/Q)** | **832 (+7% Q/Q)** | **615 (+8% Q/Q)** |
| **Y/Y growth (Mar-26 vs Mar-25)** | **+31%** | **+34%** | **+42%** |

Arithmetic check on the stated Y/Y figures: 1,007/769 = +30.9% ✓; 832/622 = +33.8% ✓; 615/432 = +42.4% ✓.

### Adjusted gross profit / adjusted gross margin, p.32 (appendix reconciliation)
| Metric ($ thousands) | Q1 2026 |
|---|---|
| Gross profit (GAAP) | 1,416,785 |
| Add: stock-based compensation | 17,906 |
| **Adjusted gross profit** | **1,434,691** |
| **Adjusted gross margin** | **88%** (exact: 87.88%) |

Only Q1 2026 is shown in this reconciliation table — the deck does not give a prior-year adjusted gross margin here, but the 10-Q MD&A states Q1 2025 was **82%** excluding SBC.

### Rule of 40 components, p.30 (appendix) — adjusted operating margin series
| Quarter | Y/Y revenue growth | Adjusted operating margin | Rule of 40 |
|---|---|---|---|
| Q2 2024 | 27% | 37% | 64% |
| Q3 2024 | 30% | 38% | 68% |
| Q4 2024 | 36% | 45% | 81% |
| Q1 2025 | 39% | 44% | 83% |
| Q2 2025 | 48% | 46% | 94% |
| Q3 2025 | 63% | 51% | 114% |
| Q4 2025 | 70% | 57% | 127% |
| **Q1 2026** | **85%** | **60%** | **145%** |

### Cash flow, p.26 and p.31
Cash from operations $899,165 (55% margin) vs. $310,263 (35%) in Q1 2025; adjusted free cash flow $924,630 (57%) vs. $370,377 (42%). Ended Q1 2026 with **$8.0B** in cash, cash equivalents and US Treasury securities, and no debt.

### Other stated metrics
- Q1 2026 headline slide (p.4) repeats: US revenue +104% Y/Y to $1.28B; US commercial +133% Y/Y / +18% Q/Q to $595M; US government +84% Y/Y / +21% Q/Q to $687M; adjusted FCF $925M (57% margin); adjusted operating income $984M (60% margin); adjusted EPS $0.33, GAAP EPS $0.34.
- **Net dollar retention was 150% in Q1 2026** (p. "Billings/RPO" slide).
- Rule of 40 peer chart (p.3) is sourced by Palantir to "S&P Capital IQ, information as of May 3, 2026," top 100 companies by market cap.

## Notes
- **Adjusted gross margin (88%) is a non-GAAP measure that appears ONLY in this investor presentation**, not in the 8-K press release. The GAAP gross margin for the same quarter is 87% (86.78% exact). Label which one a slide is showing.
- Customer counts are **trailing-twelve-month** counts, not point-in-time. A slide should say "TTM."
- The three customer-count series are nested and easy to conflate: total (1,007) ⊃ commercial (832) ⊃ US commercial (615). The most commonly mis-cited figure is 1,007 as a "commercial customer" count — it is not.
- The PDF's text layer drops some ligatures/capitals (e.g. "opera ng", "djusted"); figures were read from the numeric columns, which extract cleanly, and every headline value was cross-checked against the 8-K or 10-Q above.
- Rule-of-40 and adjusted-operating-margin percentages are Palantir's own rounded values; recomputing from the underlying $ figures gives 60.2% (Q1 2026), 44.2% (Q1 2025), 46.3% (Q2 2025) — consistent.
