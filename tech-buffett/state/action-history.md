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

## 2026-04-22 — Deep Dive — MSFT

- **Action:** Deep Dive (Action 3)
- **Ticker:** MSFT (Microsoft Corporation, NASDAQ)
- **Details:** Long-form deep dive completed at `research/deep-dives/DEEP-MSFT-2026-04-22.txt`. Three structured filing extracts created as non-action bookkeeping from user-supplied filings: `MSFT-10K-FY2025.md`, `MSFT-10Q-FY2026-Q1.md`, `MSFT-10Q-FY2026-Q2.md` saved to `research/filings/`. Deep dive covers: (0) Executive summary, (1) Unit economics and financial architecture (revenue mix shift to 77% services, segment margins, H1 FY2026 run rates, SBC analysis at 4.2% of rev, FCF bridge showing compression from 30.2% to ~20% margin due to capex supercycle), (2) The capex question ($100-120B FY2026 capex -- 70% productive / 30% over-investment risk, with demand signals from $625B RPO and Azure 39-40% growth providing evidence), (3) TAM analysis (base case: $490B revenue by FY2030, 12% CAGR; Azure to $154B+ on cloud TAM reaching $700B), (4) Competitive dynamics over 10 years (Azure vs AWS vs GCP stable oligopoly; M365 moat widening; OpenAI partnership fraying -- 20% probability of material AI advantage erosion from OpenAI defection + AWS Frontier deal), (5) Capital allocation history (A- grade M&A under Nadella; $42.5B returned in FY2025; elite management), (6) Moat assessment (WIDE with HIGH confidence -- switching costs, network effects, scale economics, intangibles), (7) Scenario analysis (Bull 25%: $644 / Base 50%: $500 / Bear 25%: $330 -> probability-weighted ~$494, ~23% upside from ~$400), (8) Thesis-break checklist (AI capex destroying value, OpenAI becoming competitor, Copilot failure, antitrust, Nadella departure), (9) Optionality (agentic AI, healthcare, sovereign cloud, OpenAI equity stake ~$80-100B+), (10) Preliminary valuation (24-25x forward P/E vs 5yr avg 28-33x), (11) DCF marching orders (10% discount rate, three scenarios, explicit capex curve, SBC-adjusted FCF).
- **Rationale:** Action #3 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). MSFT ranked #2 on the April 14 scan (8/10) and is the natural first large-cap holding. The deep dive confirms: (a) MSFT is the highest-quality business in the candidate universe with a WIDE moat, (b) the AI capex supercycle is the key risk variable for the DCF, (c) at 24-25x forward earnings the stock is at the low end of its 5-year valuation range, (d) probability-weighted 3-year expected value of ~$494 implies ~23% upside (moderate but adequate for a quality anchor position). Copilot adoption lag (3.3% penetration, users prefer ChatGPT 76% vs Copilot 18%) and OpenAI friction (AWS Frontier deal, lawsuit threats) are the primary thesis risks. Rating remains ACCUMULATE.
- **Resulting state:** Cash $2,000.00 unchanged. No trade. DCF is the next eligible action for MSFT.

---

## 2026-04-23 — DCF — MSFT

- **Action:** DCF (Action 4)
- **Ticker:** MSFT (Microsoft Corporation, NASDAQ)
- **Details:** Full 10-year DCF model completed at `research/dcf/DCF-MSFT-2026-04-23.txt`. Financial data sourced from SEC filings (10-K FY2025, 10-Q FY2026 Q1, 10-Q FY2026 Q2) previously extracted to `research/filings/`. Model features: (a) SBC-adjusted FCF as the underwriting column (SBC at 4.0% of revenue deducted from FCF), (b) three scenarios with probability weights (Bull 25% / Base 50% / Bear 25%), (c) explicit capex curve declining from $100B FY2026 supercycle peak to $55-70B by FY2032-36 depending on scenario, (d) both perpetuity-growth (3.0% terminal g) and exit-multiple (18-25x SBC-adj FCF) terminal value models averaged, (e) 10% discount rate reflecting MSFT's quality (AA+ balance sheet, $49B net cash, 70%+ recurring revenue, WIDE moat), (f) 10-year explicit forecast FY2027-FY2036, (g) 18% effective tax rate, (h) shares flat at 7,430M (buybacks offset SBC dilution).
- **Key results:**
  - Bull case IV: **$624/share** (+50% upside from $417)
  - Base case IV: **$454/share** (+9% upside)
  - Bear case IV: **$276/share** (-34% downside)
  - Probability-weighted intrinsic value @ 10% hurdle: **$452/share**
  - Margin of safety at $416.51: **7.9%**
  - At 12% hurdle rate: prob-weighted IV drops to ~$336 (stock overvalued)
  - Capex stress test (sustained $95B through FY2029): IV drops to ~$400 (stock fairly valued to slightly overvalued)
  - Terminal value = 63-69% of enterprise value across scenarios
  - Revenue CAGR: Bull 12.8%, Base 10.5%, Bear 7.0% over 10 years
  - FY2036 SBC-adj FCF: Bull $416B, Base $314B, Bear $198B
- **Capex curve (base case):** FY26 $100B (31% of rev) -> FY28 $95B (22%) -> FY30 $75B (14%) -> FY32 $65B (10%) -> FY36 $60B (7%). This is the critical assumption -- if capex stays elevated 2-3 years longer than modeled, the stock is fairly valued to slightly overvalued today.
- **Sensitivity highlights:** IV ranges from $336 (12% WACC) to $535 (9% WACC). Base-case exit multiple sensitivity: $397 at 18x to $498 at 25x. Terminal growth sensitivity: $387 at 2.0% to $548 at 4.0%.
- **Rationale:** Action #4 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). The DCF confirms MSFT is reasonably valued but not cheap. The 7.9% margin of safety is thin -- below our typical 15-20% threshold for conviction buys. However, this is the highest-quality business in the candidate universe with a WIDE moat, and the 10% discount rate is appropriate for that quality. Two viable paths: (A) buy a small starter position now to establish the large-cap anchor, or (B) wait for a pullback to $380-400 or post-Q3 earnings clarity (April 29). Q3 earnings are 6 days away, adding event risk to an immediate purchase.
- **Rating:** ACCUMULATE (unchanged). MSFT clears DCF purchase eligibility. Buy is now legal pending market hours and cash availability.
- **Resulting state:** Cash $2,000.00 unchanged. No trade. Buy (Action 5) is now eligible for MSFT. DCF valid through June 22, 2026.

---

## 2026-04-24 13:10 ET — Buy — MSFT

- **Action:** Buy (Action 5)
- **Ticker:** MSFT (Microsoft Corporation, NASDAQ)
- **Shares:** 1.5
- **Price:** $419.73 (live quote fetched at 1:10 PM ET, April 24, 2026, via Google Finance)
- **Total cost:** $629.60 (1.5 x $419.73)
- **Cash before:** $2,000.00
- **Cash after:** $1,370.41
- **DCF reference:** `research/dcf/DCF-MSFT-2026-04-23.txt` (completed April 23, 2026; expires June 22, 2026)
- **Allocation check:**
  - Large cap: $629.60 / $2,000.01 = 31.5% (target ~33%) -- on target
  - Mid cap: $0 / $2,000.01 = 0% (target ~33%) -- acceptable deviation with only 1 holding; will fill with mid-cap next
  - Small cap: $0 / $2,000.01 = 0% (target ~33%) -- acceptable deviation with only 1 holding; will fill with small-cap next
  - Per rules: "While the portfolio has fewer than ~6 holdings, the split may deviate; the target tightens as the portfolio fills out."
- **Rationale:** MSFT is the portfolio's first purchase -- a large-cap anchor position in the highest-quality business in our candidate universe. The April 23 DCF produced a probability-weighted intrinsic value of $452/share at a 10% discount rate, implying 7.9% margin of safety at today's $419.73 price. While the margin of safety is thin by classic Buffett standards, the position is deliberately sized as a small starter (31.5% of portfolio, $630 of $2,000) for three reasons: (1) MSFT has a WIDE moat with HIGH confidence -- switching costs across the enterprise stack, network effects in M365/LinkedIn/GitHub, scale economics in Azure, and intangible assets in brand/IP -- making a lower margin of safety acceptable for a quality anchor; (2) at 24-25x forward P/E, the stock trades at the low end of its 5-year valuation range (avg 28-33x), which the DCF confirms as reasonable; (3) Q3 FY2026 earnings on April 29 present a near-term catalyst -- Azure growth of 39-40% and $625B in remaining performance obligations signal demand is robust despite the $100B capex supercycle. The starter size preserves $1,370 in cash for mid-cap and small-cap positions to build toward the 1/3-1/3-1/3 allocation target. If Q3 earnings disappoint and the stock pulls back to $380-400, the DCF base case ($454) would offer a 12-16% margin of safety, warranting a potential add. This is not a moonshot -- it is a 10-15% compounder for a decade, anchored by durable competitive advantages and a management team (Nadella/Hood) that has compounded market cap 10x since 2014.
- **Resulting state:** Cash $1,370.41 | Invested $629.60 (1 holding: MSFT 1.5 shares) | Total $2,000.01 | Holdings: 1/10

---

## 2026-04-14 — Quick Scan

- **Action:** Quick Scan
- **Details:** Researched 22 tech/disruptor candidates across large, mid, and small cap buckets using live market data (prices as of April 14, 2026). Scored each on revenue growth, FCF margin, valuation, moat, and risk. Full raw notes saved to `research/scans/scan-2026-04-14.md`.
- **Rationale:** First scan to populate the candidate list and identify the highest-conviction opportunities for further initiation reports.
- **Resulting state:** `state/candidates.md` replaced with 22-candidate ranked list. Top 3: TTD (#1, 8/10), MSFT (#2, 8/10), NVDA (#3, 7/10).
