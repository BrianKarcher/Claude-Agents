# PLTR — Other Quarterly Metrics Cache (segment revenue, customers, cash flow, non-GAAP)

Companion to `quarterly-financials.md` (which holds GAAP revenue / gross profit / operating income only).
**Read this file first before fetching anything.** Only fetch/verify a quarter-metric that is missing here or listed under "Known gaps."

Same discipline as `quarterly-financials.md`:
- Reported actuals only. **No guidance, no consensus estimates, no price targets** — those go in dated extract files and the deck, clearly labelled (see `extracts/PLTR-ANALYSTTARGETS-2026-08-02.md`).
- Point-in-time market data (price, market cap, institutional ownership) does **not** belong here either — see `extracts/PLTR-MARKETDATA-2026-07-31.md` and `extracts/PLTR-OWNERSHIP-2026-08-02.md`.
- Never overwrite a cited row. Never fill a blank cell by estimation, interpolation, or back-solving from a growth rate. A blank stays blank until a primary source is opened.
- `—` means **not verified** (not "zero", not "unavailable forever"). Every `—` that was actively checked is explained under "Known gaps."

---

## Table 1 — Segment revenue (US split, as reported by the company in $ millions, rounded to $1M by Palantir)

| Quarter | US revenue | US commercial | US comm. Y/Y | US government | US gov't Y/Y | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| Q1 2025 | 628 | 255 | +71% | 373 | +45% | extracts/PLTR-8K-Q1-2025.md | 2026-08-02 |
| Q2 2025 | 733 | 306 | +93% | 426 | +53% | extracts/PLTR-8K-Q2-2025.md | 2026-08-02 |
| Q3 2025 | — | — | — | — | — | not fetched | — |
| Q4 2025 | — | — | — | — | — | not fetched | — |
| **Q1 2026** | **1,282** | **595** | **+133%** | **687** | **+84%** | extracts/PLTR-8K-Q1-2026.md | 2026-08-02 |

Q1 2026 Q/Q: US +19%, US commercial +18%, US government +21%.
Internal check: 595 + 687 = 1,282 = the Q1 2026 10-Q's United States revenue of $1,282,066K.

**Worldwide segment split (10-Q Note 12, $ thousands) — a different cut, do not mix with the US split above:**

| Quarter | Government revenue | Commercial revenue | Source extract | Verified |
|---|---|---|---|---|
| Q1 2025 | 486,963 | 396,892 | extracts/PLTR-10Q-Q1-2026.md (comparative column) | 2026-08-02 |
| Q1 2026 | 858,410 | 774,173 | extracts/PLTR-10Q-Q1-2026.md | 2026-08-02 |

---

## Table 2 — Customer counts (trailing twelve months)

| TTM ended | Total customers | Total Y/Y | Commercial customers | Comm. Y/Y | US commercial customers | US comm. Y/Y | Source extract | Verified |
|---|---|---|---|---|---|---|---|---|
| Mar 31, 2025 | 769 | +39%¹ | 622 | — | 432 | — | extracts/PLTR-INVESTORDECK-Q1-2026.md; 769 also in extracts/PLTR-10Q-Q1-2026.md | 2026-08-02 |
| Jun 30, 2025 | 849 | +43%¹ | 692 | — | 485 | — | extracts/PLTR-INVESTORDECK-Q1-2026.md | 2026-08-02 |
| Sep 30, 2025 | 911 | — | 742 | — | 530 | — | extracts/PLTR-INVESTORDECK-Q1-2026.md | 2026-08-02 |
| Dec 31, 2025 | 954 | — | 780 | — | 571 | — | extracts/PLTR-INVESTORDECK-Q1-2026.md | 2026-08-02 |
| **Mar 31, 2026** | **1,007** | **+31%** | **832** | **+34%** | **615** | **+42%** | extracts/PLTR-INVESTORDECK-Q1-2026.md; 1,007 and 769 also in extracts/PLTR-10Q-Q1-2026.md | 2026-08-02 |

Q/Q growth as published: Jun-25 +10% / +11% / +12%; Sep-25 +7% / +7% / +9%; Dec-25 +5% / +5% / +8%; Mar-26 +6% / +7% / +8%.

¹ Total-customer Y/Y for TTM ended Mar 31, 2025 (+39%) and Jun 30, 2025 (+43%) come from the respective quarters' press releases, which state the percentage without an absolute count.

**The three series are nested: total (1,007) contains commercial (832) contains US commercial (615).** The most commonly mis-cited figure is 1,007 as a "commercial customer count" — it is not; it includes government agencies (each separately-contracting sub-agency counted separately per the 10-Q definition). An AI search summary encountered on 2026-08-02 made exactly this error.

---

## Table 3 — Cash flow and free cash flow ($ thousands)

| Quarter | Net cash from operating activities | Capex (purchases of P&E) | CFO − capex (derived²) | Adjusted FCF (company non-GAAP) | Adj. FCF margin | Source extract | Verified |
|---|---|---|---|---|---|---|---|
| Q2 2024 | 144,187 | (2,879) | 141,308 | 148,660 | 22% | extracts/PLTR-8K-Q2-2025.md (comparative column) | 2026-08-02 |
| Q1 2025 | 310,263 | (6,184) | 304,079 | 370,377 | 42% | extracts/PLTR-8K-Q1-2025.md; extracts/PLTR-8K-Q1-2026.md (comparative) | 2026-08-02 |
| Q2 2025 | 539,251 | (7,634) | 531,617 | 568,769 | 57% | extracts/PLTR-8K-Q2-2025.md | 2026-08-02 |
| Q3 2025 | — | — | — | — | — | not fetched | — |
| Q4 2025 | — | — | — | — | — | not fetched | — |
| **Q1 2026** | **899,165** | **(7,401)** | **891,764** | **924,630** | **57%** | extracts/PLTR-8K-Q1-2026.md; extracts/PLTR-10Q-Q1-2026.md | 2026-08-02 |

² **"CFO − capex" is arithmetic on two reported line items, not a company-published metric.** Palantir does not report a plain free cash flow. Its "adjusted free cash flow" additionally adds back cash paid for employer payroll taxes related to SBC (Q1 2026: +32,866; Q1 2025: +66,298; Q2 2025: +37,152), which is why it is the larger number. If a slide says "free cash flow," it must say which of the two it means. Do not present adjusted FCF as GAAP or as "free cash flow" unqualified.

---

## Table 4 — Non-GAAP (adjusted) margins and EPS

All figures in this table are **non-GAAP**, as defined and published by Palantir (excluding stock-based compensation and related employer payroll taxes; adjusted EPS also excludes income tax effects/adjustments at an assumed 23.0% long-term effective rate). GAAP comparatives are shown alongside so the two can never be confused.

| Quarter | Adj. gross margin | Adj. operating margin | Adj. income from ops ($K) | **Adj. EPS diluted** | GAAP EPS diluted | GAAP op. margin | Source extract | Verified |
|---|---|---|---|---|---|---|---|---|
| Q2 2024 | — | 37% | 253,567 | — | — | 16%³ | extracts/PLTR-8K-Q2-2025.md; extracts/PLTR-INVESTORDECK-Q1-2026.md (p.30) | 2026-08-02 |
| Q3 2024 | — | 38% | — | — | — | — | extracts/PLTR-INVESTORDECK-Q1-2026.md (p.30) | 2026-08-02 |
| Q4 2024 | — | 45% | — | — | — | — | extracts/PLTR-INVESTORDECK-Q1-2026.md (p.30) | 2026-08-02 |
| Q1 2025 | 82% | 44% | 390,710 | **$0.13** | $0.08 | 20% | extracts/PLTR-8K-Q1-2025.md; 82% from extracts/PLTR-10Q-Q1-2026.md MD&A | 2026-08-02 |
| Q2 2025 | — | 46% | 464,385 | **$0.16** | $0.13 | 27% | extracts/PLTR-8K-Q2-2025.md | 2026-08-02 |
| Q3 2025 | — | 51% | — | — | — | — | extracts/PLTR-INVESTORDECK-Q1-2026.md (p.30) | 2026-08-02 |
| Q4 2025 | — | 57% | — | — | — | — | extracts/PLTR-INVESTORDECK-Q1-2026.md (p.30) | 2026-08-02 |
| **Q1 2026** | **88%** | **60%** | **983,545** | **$0.33** | **$0.34** | **46%** | extracts/PLTR-8K-Q1-2026.md; 88% from extracts/PLTR-INVESTORDECK-Q1-2026.md (p.32) | 2026-08-02 |

³ Q2 2024 GAAP operating margin computed from the cached GAAP figures: 105,339 / 678,134 = 15.5%, i.e. 16%.

**Q1 2026 GAAP diluted EPS ($0.34) is HIGHER than adjusted diluted EPS ($0.33).** This is not a typo: the non-GAAP tax adjustment (−$243,624K) exceeds the SBC add-backs. Any slide comparing "EPS beat" figures must not silently swap one for the other.

**Adjusted gross margin is disclosed only in the quarterly investor presentation**, not in the 8-K press release — which is why only two quarters above are filled in. GAAP gross margin for Q1 2026 was 87% (86.78% exact); Q1 2025 was 80%.

**Rule of 40 (Palantir's own definition: Y/Y revenue growth + adjusted operating margin), from the Q1 2026 deck appendix p.30:** Q2 2024 64%, Q3 2024 68%, Q4 2024 81%, Q1 2025 83%, Q2 2025 94%, Q3 2025 114%, Q4 2025 127%, Q1 2026 145%. The Y/Y revenue-growth half of every one of those eight quarters reconciles against the GAAP revenue series in `quarterly-financials.md`.

**Net dollar retention:** 150% in Q1 2026 (extracts/PLTR-INVESTORDECK-Q1-2026.md). Earlier quarters not verified.

---

## Known gaps

Recorded explicitly so a future session knows what was *checked and unavailable* vs. *never checked*. **None of these may be filled by estimation, interpolation, or back-solving.**

1. **Q3 2025 and Q4 2025 — segment revenue, cash flow, adjusted EPS: NEVER CHECKED.** The Q3 2025 (8-K filed 2025-11-03, accession 0001321655-25-000130) and Q4/FY2025 (8-K filed 2026-02-02, accession 0001321655-26-000004) earnings releases exist on EDGAR and were not opened in this session — only their adjusted operating margins and Y/Y growth were captured, from the Q1 2026 deck appendix. If a deck needs these quarters, fetch those two exhibits.
2. **Adjusted gross margin for all quarters except Q1 2026 (and Q1 2025 via the 10-Q's 82%): NOT AVAILABLE from the sources opened.** It is not in the 8-K press releases; it appears only in each quarter's own investor presentation. Fetch the relevant quarter's Business Update PDF from `investors.palantir.com/files/` if needed.
3. **Adjusted EPS for Q2 2024, Q3 2024, Q4 2024, Q3 2025, Q4 2025: NEVER CHECKED.** Available in each quarter's press-release reconciliation table; not fetched here.
4. **Commercial / US-commercial customer counts before TTM ended Mar 31, 2025: NOT COVERED** by the Q1 2026 deck, whose charts start at Mar 31, 2025. Earlier quarters would need earlier Business Update PDFs.
5. **Exact-thousands US commercial / US government revenue: NOT DISCLOSED.** Palantir publishes the US split only to the nearest $1 million (press release and investor deck). The 10-Q's exact-thousands segment note is the *worldwide* commercial/government cut, which is a different measure. Do not present $595M / $687M with more precision than $1M, and do not derive an "exact" US split from the worldwide segment note.
6. **Q2 2026 and later: not yet reported** as of 2026-08-02 — the Q2 2026 call is 2026-08-03. Guidance issued 2026-05-04 for Q2/FY2026 is recorded in `extracts/PLTR-8K-Q1-2026.md` under a clearly-marked forward-looking heading and must never be promoted into this table.

## Reconciliation notes

- Fetching the Q1 2025, Q2 2025, and Q1 2026 primary press releases this session also **validated previously aggregator-sourced rows** in `quarterly-financials.md` for Q2 2024, Q1 2025, Q2 2025, and Q1 2026 (revenue / gross profit / operating income all match the filings to the rounding). No corrections were needed.
- SEC.gov returns HTTP 403 to the WebFetch tool but serves `curl` with a descriptive User-Agent header. `https://data.sec.gov/submissions/CIK0001321655.json` and each accession's `index.json` are the fastest route to the right exhibit filename.
