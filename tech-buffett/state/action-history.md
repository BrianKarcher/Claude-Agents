# Action History

> Append-only. Never edit or delete prior entries. Every action, infusion, and dividend gets a timestamped entry here.
>
> Format for each entry:
>
> ## YYYY-MM-DD HH:MM ET — [ACTION TYPE] — [TICKER if applicable]
> - **Action:** Quick Scan | Initiation | Deep Dive | DCF | Buy | Sell | Rebalance | Infusion (bookkeeping) | Dividend (bookkeeping)
> - **Details:** ...
> - **Rationale:** ...
> - **Resulting state:** ...

---

## 2026-04-14 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 initial cash infusion recorded. No securities purchased.
- **Rationale:** User confirmed starting capital. Portfolio clock begins today.
- **Resulting state:** Cash $1,000.00 | Invested $0.00 | Total $1,000.00

---

## 2026-04-21 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. Second infusion.
- **Rationale:** Standing weekly deposit per portfolio rules.
- **Resulting state:** Cash $2,000.00 | Invested $0.00 | Total $2,000.00

---

## 2026-04-21 — Initiation — MSFT

- **Action:** Initiation of Coverage (Action 2)
- **Ticker:** MSFT (Microsoft Corporation, NASDAQ)
- **Details:** Full initiation of coverage report produced at `research/initiations/INIT-MSFT-2026-04-21.txt`. Covered: business description & Nadella transformation timeline, products & segments (Intelligent Cloud $100.4B / Productivity & Business Processes $77.8B / More Personal Computing $73.8B), customers & go-to-market (Fortune 500 near-100% penetration, EA/MCA contract structure), competitive landscape (Azure #2 at 23% vs AWS 32% vs GCP 11%; M365 ~85%+ enterprise share; Copilot at 11.5% AI assistant share declining from 18.8%), moat assessment (WIDE moat — switching costs, network effects, scale economics, intangible assets; vulnerability on Copilot monetization and OpenAI dependency), management (Nadella/Hood excellent; 10x market cap growth under Nadella), key risks (AI capex return uncertainty, OpenAI dependency, cloud growth deceleration, antitrust, macro, valuation compression), recent results (FY2025 rev $281.7B +15%, operating margin 45.6%, FCF $71.6B; Q1 FY2026 rev $77.7B +18%, Azure +40%; Q2 FY2026 rev $81.3B +17%), and valuation snapshot (TTM P/E ~26x, forward P/E ~22x, P/S ~11x, below 5-year avg forward P/E of 28-33x; analyst consensus target ~$580-600).
- **Rating:** ACCUMULATE. Best risk-adjusted large-cap compounder in tech, but the massive AI capex ramp ($65-80B/yr) and low Copilot penetration (3.3%) demand DCF confirmation before buying.
- **Rationale:** MSFT ranked #2 on the April 14 quick scan (8/10 score). It is the natural first large-cap holding for the portfolio given the allocation target of ~1/3 large cap. At ~22x forward earnings, it trades at the low end of its 5-year valuation range, offering a reasonable entry for a 10-year compounder thesis. Initiation completed to advance MSFT through the research pipeline (Init -> Deep Dive -> DCF -> Buy).
- **Resulting state:** Cash $2,000.00 unchanged. No trade. Deep Dive is the next eligible action for MSFT.

---

## 2026-04-17 — DCF — TTD

- **Action:** DCF (Action 4)
- **Ticker:** TTD (The Trade Desk, Inc., NASDAQ)
- **Details:** Full 10-year DCF model completed at `research/dcf/DCF-TTD-2026-04-17.txt`. Financial data pulled from SEC EDGAR (10-K FY2024, Q4/FY2025 earnings release Feb 25, 2026) via StockAnalysis.com aggregation. Model features: (a) SBC-adjusted FCF as the underwriting column ($491M SBC subtracted from $796M reported FCF = $305M FY2025 SBC-adj FCF), (b) Ventura set to $0 revenue in all scenarios, (c) take-rate compression sensitivity at -150bps (base) and -300bps (bear), (d) three scenarios with probability weights (Bear 25% / Base 55% / Bull 20%), (e) both perpetuity-growth and exit-multiple terminal value models averaged, (f) 12% and 14% hurdle rates, (g) 10-year explicit forecast 2026-2035 with declining share count (-2%/yr net of SBC).
- **Key results:**
  - Probability-weighted intrinsic value @ 12% hurdle: **$33.45/share** (32% margin of safety vs $22.76 market price)
  - Probability-weighted intrinsic value @ 14% hurdle: **$27.85/share** (18% margin of safety)
  - Bear-case floor: $10.62/share (53% downside risk)
  - Base-case value: $31.81/share (+40% upside)
  - Bull-case value: $66.50/share (+192% upside)
  - DCF >= $30 threshold from deep dive: **MET**
- **Rationale:** Action #4 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). TTD clears the $30 intrinsic threshold at the 12% hurdle rate. The asymmetry is favorable (base +40% vs bear -53%, probability-weighted toward the base). However, three of four buy conditions remain pending: Q1 2026 earnings (May 13), permanent CFO hire, and Amazon holdco-partner status. We do NOT proceed to a buy today.
- **Resulting state:** Rating upgraded from WATCH to **ACCUMULATE ON WEAKNESS**, pending May 13 Q1 2026 earnings confirmation. Cash $1,000.00 unchanged. No trade. Buy is gated on: (i) Q1 rev >= ~$645M (guide -500bps), (ii) permanent CFO by July 2026, (iii) no adverse Amazon holdco announcement. DCF valid for 60 days (expires June 16, 2026).

---

## 2026-04-16 — Deep Dive — TTD

- **Action:** Deep Dive
- **Ticker:** TTD (The Trade Desk, Inc., NASDAQ)
- **Details:** Long-form deep dive completed at `research/deep-dives/DEEP-TTD-2026-04-16.txt`. Sections: (0) Executive summary, (1) Unit economics & SBC reconciliation, (2) 10-year TAM (open-internet programmatic $150B -> $280-320B by 2030; CTV the growth engine), (3) Competitive dynamics (Amazon/DV360/TTD three-horse race; Amazon share erosion on CTV concentrated; structural asymmetry explained), (4) Bear-case teardown across all four user-specified pillars (CFO instability, Amazon DSP, Ventura OS, cyclical-vs-structural growth) with explicit weights and probabilistic decomposition of 17-point deceleration (~10-12pts transient, ~4-6pts structural), (5) Bull-case catalysts (political normalization, DOJ Google remedy, UID2 adoption, CTV secular, Kokai margin expansion), (6) Management & capital allocation (Green $148M personal buy March 2-4 2026 at $23-25 weighted avg.), (7) Optionality (UID2, Ventura ecosystem, international, DOJ windfall), (8) Five-year scenario table (Bear 25%/Base 55%/Bull 20% -> EV ~$63/share in 5 yrs, ~25% IRR), (9) Four-condition thesis-break checklist, (10) DCF marching orders (take-rate compression sensitivity, SBC-adjusted FCF, three-scenario probability weighting, 12% hurdle), (11) Preliminary view & buy pre-conditions.
- **Rationale:** Action #3 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). TTD remains #1 candidate by score (8/10). Deep dive stress-tested the four bear pillars the user specifically flagged: concluded CFO issue is culture-fit (25% weight, priced in), Amazon is the single most important variable (35% weight, partially priced in), Ventura is a sunk cost that self-corrected (10% weight, not critical), and deceleration is ~60% cyclical / ~40% structural vs market pricing closer to 100% structural. Base-case 5-year IRR of ~24% at current ~$21 warrants DCF next.
- **Resulting state:** Rating unchanged at WATCH / ACCUMULATE ON WEAKNESS. Cash $1,000.00 unchanged. No trade. DCF is the next eligible action for TTD; buy remains gated on DCF intrinsic >=$30/share AND Q1 2026 print (May 13) not missing by >500bps AND permanent CFO by July 2026 AND no adverse Amazon-primary-partner announcement at top-2 holdco.

---

## 2026-04-15 — Initiation — TTD

- **Action:** Initiation of Coverage
- **Ticker:** TTD (The Trade Desk, Inc., NASDAQ)
- **Details:** Full initiation of coverage report produced at `research/initiations/INIT-TTD-2026-04-15.docx`. Covered business description & history (founded 2009, Nasdaq IPO 2016, buy-side-only DSP), products & segments (Kokai AI platform, UID2, CTV/Ventura OS, Retail Media), customers & go-to-market (agency holding companies, >95% retention), competitive landscape & moat (20% DSP share, independence trust moat, data network effects, UID2 infrastructure, vs. Google DV360 ~40% and Amazon DSP), management (Jeff Green founder/CEO; CFO instability yellow flag — two CFO changes in ~30 months, Tahnil Davis interim CFO), key risks (growth deceleration, Amazon DSP, walled garden re-acceleration, Publicis tension, Ventura OS execution, macro sensitivity), recent financial results (FY2025 revenue $2.896B +18% YoY; Q4 2025 revenue $847M +14%; FY2025 FCF $796M; Q1 2026 guidance ≥$678M +10%), and valuation snapshot (P/FCF ~12x, EV/EBITDA ~13x, forward P/E ~10x, P/S ~3.4x — trough-level multiples; analyst avg. target ~$46.63 vs. ~$21 market price).
- **Rationale:** TTD ranked #1 on the April 14 quick scan (8/10 score). Trough-level valuation on a structurally advantaged, founder-led, net-cash business warrants thorough coverage. No buy initiated pending CFO resolution and Q1 2026 growth floor confirmation.
- **Resulting state:** Rating: WATCH / ACCUMULATE ON WEAKNESS. Cash $1,000.00 unchanged. No trade executed.

---

## 2026-04-14 — Quick Scan

- **Action:** Quick Scan
- **Details:** Researched 22 tech/disruptor candidates across large, mid, and small cap buckets using live market data (prices as of April 14, 2026). Scored each on revenue growth, FCF margin, valuation, moat, and risk. Full raw notes saved to `research/scans/scan-2026-04-14.md`.
- **Rationale:** First scan to populate the candidate list and identify the highest-conviction opportunities for further initiation reports.
- **Resulting state:** `state/candidates.md` replaced with 22-candidate ranked list. Top 3: TTD (#1, 8/10), MSFT (#2, 8/10), NVDA (#3, 7/10).
