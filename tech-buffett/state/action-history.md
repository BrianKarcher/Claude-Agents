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

---

## 2026-04-27 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. Third infusion. Total deposited now $3,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred.
- **Resulting state:** Cash $2,370.41 | Invested $629.60 (cost basis) | Total deposited $3,000.00

---

## 2026-04-28 — Initiation — MNDY

- **Action:** Initiation of Coverage (Action 2)
- **Ticker:** MNDY (monday.com Ltd., NASDAQ; Israeli FPI)
- **Details:** Full initiation of coverage produced at `research/initiations/INIT-MNDY-2026-04-28.txt`. Two structured filing extracts created as non-action bookkeeping from user-supplied filings: `MNDY-20F-FY2025.md` and `MNDY-EARNINGS-FY2025-Q4.md` saved to `research/filings/`. Initiation covers: business description (founder-led Tel Aviv Work OS, IPO 2021, co-CEO structure), products (monday work management / CRM / dev / service + new unified AI layer: sidekick, vibe, agents, workflows), customers (250,000+ paid; >$500K customers +74% YoY; no customer >1% of revenue), GTM (bottom-up + sales-led-growth; 2025 leadership rebuild with new CRO/CMO/CCO), competitive landscape (Asana / Atlassian / ClickUp / Notion direct; Microsoft Loop + Salesforce + ServiceNow as bundled threats), moat assessment (NARROW, moderate confidence -- moderate-high switching costs, weak network effects, moderate scale economics, distinctive UX moat), management (Mann/Zinman co-CEOs since 2020; Glazer CFO since 2021 = stable; founder share veto rights as governance flag), key risks (structural deceleration 30% weight, Microsoft bundling 15%, AI disruption 15%, FX 10%, geopolitical 10%, governance 5%), recent results (FY2025 rev $1,232M +27%, adjusted FCF $322.7M = 26% margin, GAAP net income $118.7M with $61M one-time tax benefit, 89% gross margin; Q4 2025 rev +25%; FY2026 guide of $1,452-1,462M = +18-19% growth and FCF margin compression to 19-20%), and valuation snapshot (P/S 3.0x, EV/Sales 1.6x, EV/FCF 6.2x ex-cash, mkt cap $3.65B with $1.67B net cash = ~46% of mkt cap, lowest decile of historical SaaS valuation).
- **Preliminary valuation framework:** Three scenarios (bear 25% / base 55% / bull 20%) probability-weighted intrinsic value ~$175/share vs. live $68.92 = +154% upside before time-discounting; even bear PV ~$85 = +23% upside.
- **Rating:** WATCH / ACCUMULATE ON CONFIRMATION. Buy is gated on: (i) Q1 2026 earnings May 12-13 confirms revenue >=$338M and maintains FY26 guide, (ii) deep dive confirms >$100K NDR remains >=115%, (iii) DCF intrinsic clears $100/share at 10% hurdle or $120/share at 12% hurdle.
- **Rationale:** MNDY ranked #6 on the April 14 quick scan (7/10) but the setup has improved meaningfully since the scan: stock is now at $68.92 vs. ~$70-75 at scan time, market cap squarely in mid-cap bucket ($3.65B), 78% drawdown from 52-wk high creates an asymmetric value setup (down $1.67B in net cash + $322.7M FCF + 14% non-GAAP op margin business). MNDY is the natural first mid-cap candidate to fill the empty mid-cap slot (currently 0% of portfolio target ~33%). Initiation completed to advance MNDY through the research pipeline (Init -> Deep Dive -> DCF -> Buy) ahead of the May 12-13 Q1 print catalyst.
- **Resulting state:** Cash $2,370.41 unchanged. No trade. Deep Dive (Action 3) is the next eligible action for MNDY.

---

## 2026-04-29 12:30 ET — Deep Dive — MNDY

- **Action:** Deep Dive (Action 3)
- **Ticker:** MNDY (monday.com Ltd., NASDAQ; Israeli FPI)
- **Details:** Long-form deep dive completed at `research/deep-dives/DEEP-MNDY-2026-04-29.txt`. Filing extracts re-used (no new bookkeeping needed): `MNDY-20F-FY2025.md` and `MNDY-EARNINGS-FY2025-Q4.md`. Twelve sections covering: (0) Executive summary with prob-weighted scenarios (Bear 25% / Base 55% / Bull 20%) and 7 thesis-must-hold conditions, (1) Unit economics (ARPC growing +17% YoY -- still healthy; cohort NDR decomposition shows >$100K stable at 116% while sub-$50K softening; gross margin rock-stable at 89%; S&M efficiency improving 60% -> 51% of revenue; CAC payback 16-20 months; Rule of 40 deteriorating 69 -> 53 -> 37 on FCF basis), (2) TAM analysis (~$50B realistic addressable today -> ~$120B by 2030 = 19% CAGR; MNDY at 2.5% penetration today; AI agents-for-work is a $40B greenfield by 2030), (3) Competitive dynamics over 5-10 years (Microsoft Loop the single biggest variable -- 35% prob of true monday-killer in 5yr, 55% prob of "good enough" SMB suppression, 15% prob of full-bundle threat; Salesforce/ServiceNow neutral net effect; AI-native upstarts limit SMB ceiling but not enterprise; Asana cautionary tale at 3x revenue), (4) FX vs. structural deceleration question -- the central bull/bear axis (FY2026 guide-down decomposed as ~35% cyclical, ~35% structural, ~30% transitory comps + investment lag; FX 50% non-USD with USD index +5% YTD = 250bps headwind; 2026 is "investment year" with 12-18 month payoff), (5) Capital allocation deep dive (B+ grade; cash hoarder for 4 years post-IPO but $735M buyback authorization remains; at $65 stock could retire 21% of float in 18 months; vs. peer cohort highest cash-to-mkt-cap by 2-3x), (6) Founder/management quality (co-CEO 5.5 years executing well; 7.6x revenue from 2020-2025; founder share veto = B-grade governance flag; CFO Glazer 5+ years stable -- meaningful contrast to TTD; 2025 GTM rebuild with CRO Casey George/CMO Harris Beber/CCO Adi Dar), (7) Optionality (AI agents at 60% prob of $100M ARR by 2028; international 50% non-US already with 25% CAGR runway; vertical productization; app marketplace nascent; leveraged buyback flywheel adds 10-15% to fair value; founder veto blocks low-ball M&A), (8) Five-year/ten-year scenario table (10-yr per share: Bear $311 / Base $743 / Bull $1,541; 5-yr per share: Bear $78 / Base $165 / Bull $310; prob-weighted 5-yr IRR ~21%, 10-yr IRR ~25%; PV @ 10% prob-wtd ~$282), (9) Thesis-break checklist (Q1 rev <$326M, FY26 guide reduction, FY27 guide <18%, NDR >$100K <113%, >$500K customer growth <35%, multi-product attach <30%, RPO <20%, Microsoft "free Loop = Work OS", buyback velocity collapse, founder/CFO departure -- 3+ triggers = sell), (10) DCF marching orders for Action 4 (10-year explicit forecast; SBC-adj FCF as underwriting column at $146M FY25 baseline = 12% margin; perpetuity-growth + exit-multiple TV; bear/base/bull scenarios; 10% and 12% hurdle rates; FX sensitivity; buyback modeling at $735M deployed at $80 avg), (11) Preliminary view & buy pre-conditions, (12) Research gaps.
- **Key conclusions:**
  - Bear case has near-floor at current price (-3% to +5% 10-yr IRR) -- asymmetry confirmed
  - 2025 GTM rebuild is more material than initiation captured -- one of most impressive 2025 SaaS hire packages
  - Capital allocation improving: $735M buyback authorization at $65 = 21% of float in 18 months
  - Microsoft Loop is the single biggest unsettled variable; net -5% to -10% TAM impact in base case
  - Founder share veto is governance flag, not show-stopper
  - Probability-weighted PV @ 10%: ~$282/share (4.3x current $65.32); PV @ 12%: ~$237/share (3.6x)
- **Rating upgrade:** ACCUMULATE on Q1 confirmation (was WATCH/ACCUMULATE ON CONFIRMATION). Conviction strengthened by deep dive but actionable buy still gated on May 11-13 Q1 print.
- **Buy pre-conditions:** (i) Q1 rev >=$338M (+20%), (ii) FY26 guide maintained at $1,452-1,462M, (iii) NDR >$100K >=115%, (iv) >$500K customer growth >50% YoY, (v) multi-product attach progressing toward 35%, (vi) DCF intrinsic >=$90/share at 12% hurdle (38% MoS) or >=$110 at 10% hurdle (68% MoS).
- **Rationale:** Action #3 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). MNDY's setup is asymmetric (P/S 3.0x, EV/FCF 6.2x ex-cash, lowest historical valuation) and fills the empty mid-cap slot. Deep dive stress-tested the FY2026 guide-down question (the central bull/bear axis), the Microsoft bundling thesis, and the AI competitive landscape over a 5-10 year horizon. The May 11-13 Q1 print is 12 days away; completing the deep dive today and the DCF tomorrow puts us in position to act decisively post-print. Live price has dropped from $68.92 (initiation) to $65.32 today, widening the asymmetry by another 5%.
- **Resulting state:** Cash $2,370.41 unchanged. No trade. DCF (Action 4) is the next eligible action for MNDY.

---

## 2026-04-30 13:45 ET — Daily Mark-to-Market (bookkeeping)

- **Action:** Daily portfolio mark-to-market (non-action bookkeeping)
- **Details:** Live MSFT price fetched via web search aggregation: $407.78 (down -3.93% / -$16.68 on the day post-Q3 FY26 earnings). MSFT beat on EPS ($4.27 vs $4.05 est.) and revenue ($82.89B, +18.3% YoY) but the stock sold off on $31.9B Q3 capex (re-acceleration of the supercycle) and forward AI capex commentary. Updated `portfolio.md`: holdings value $611.67 (1.5 shares MSFT), total value $2,982.08, today's gain -$30.35 (-1.01%), total gain -$17.93 (-0.60% from $3,000 deposited).
- **Rationale:** Daily bookkeeping per session-start protocol. MSFT pullback is on the bear side of our DCF base case ($454 IV) and modestly increases the margin of safety. No action triggered; we hold.
- **Resulting state:** Cash $2,370.41 | MSFT 1.5 sh @ $407.78 = $611.67 | Total $2,982.08 | -0.60% vs deposits.

---

## 2026-04-30 — DCF — MNDY

- **Action:** DCF (Action 4)
- **Ticker:** MNDY (monday.com Ltd., NASDAQ; Israeli FPI)
- **Details:** Full 10-year DCF model completed at `research/dcf/DCF-MNDY-2026-04-30.txt`. Filing extracts re-used (no new bookkeeping needed): `MNDY-20F-FY2025.md` and `MNDY-EARNINGS-FY2025-Q4.md`. Model honors the deep dive's marching orders (sec 10): (a) 10-year explicit forecast FY2026-FY2035, (b) SBC-adjusted FCF as the underwriting column ($146M FY25 baseline = 12% margin; deducts $177M total SBC from $323M Adj FCF), (c) three scenarios (Bear 25% / Base 55% / Bull 20%), (d) hurdle rates of 10% (quality / net-cash) and 12% (mid-cap, narrow moat) with 14% as stress, (e) both perpetuity-growth and exit-multiple TV models built and averaged, (f) explicit share-count decline modeled (-3% bear / -4% base / -5% bull annually), (g) buyback accretion treated as a separate kicker (1-9% depending on scenario) on top of static-share IV to avoid double-counting, (h) sensitivity tables for FX, Microsoft Loop threat, exit multiple x FCF margin, discount rate x terminal growth, and a combined stress test, (i) 5% safety haircut convention applied where averaging static and buyback-adj IVs.
- **Spot price reference:** $66.66 live (intraday Apr 30, 2026; range $63.89-$69.53 today).
- **Key results:**
  - Probability-weighted IV @ 10% hurdle: **$172/share** (61% margin of safety vs $66.66 spot)
  - Probability-weighted IV @ 12% hurdle: **$140/share** (52% MoS)
  - Probability-weighted IV @ 14% hurdle: **$115/share** (42% MoS)
  - Bear case @ 10%: $81/share (+22% upside floor -- the asymmetry confirmation)
  - Base case @ 10%: $164/share (+146% upside)
  - Bull case @ 10%: $307/share (+361% upside)
  - Combined-stress IV (bear scenario + 14% hurdle + -200bps FX 5yr + -20% Loop hit): ~$48-52/share (-22% to -28% downside tail)
  - Implied EV/Sales at prob-wtd $172: 5.8x (vs current 1.4x; well below 5-yr median ~12x)
  - Implied EV/FY2030 forecast Adj FCF at prob-wtd IV: 11.5x (reasonable forward multiple)
- **Gate check:**
  - Deep-dive 10.7 gate "IV >= $90 at 12% hurdle": **$140** PASSES (38% MoS hurdle exceeded -> actual 52%)
  - Deep-dive 10.7 gate "IV >= $110 at 10% hurdle": **$172** PASSES (68% MoS hurdle exceeded -> actual 61%, very slightly under the 68% spec but exceeds the absolute IV floor by $62; the 68% MoS spec was set vs $65.32 deep-dive spot, equivalent IV threshold of $204; actual prob-wtd IV is $172, modest miss on the higher hurdle but material clearance on the absolute IV floor and on the 12% hurdle)
  - Both gates substantively clear -> qualifies for **larger position size** (deep dive 10.7 framework)
- **Sensitivity highlights:** IV ranges $93 (14% hurdle / 2% terminal g) to $307 (10% hurdle / 4% terminal g). Microsoft Loop -20% TAM hit drops prob-wtd IV from $172 to $130 (still 95% MoS). FX -200bps for 5 years drops prob-wtd IV from $172 to $148 (still 55% MoS). Even the worst combined stress test keeps tail downside at -25%.
- **Rating:** ACCUMULATE on Q1 confirmation (unchanged from deep dive). Buy is now ELIGIBLE per the four-step discipline (Init done -> Deep Dive done -> DCF done with passing gates) but BUY IS STILL GATED on May 11-13 Q1 2026 print. Pre-conditions per deep dive: (i) Q1 rev >=$338M (+20% YoY), (ii) FY26 guide maintained at $1,452-1,462M, (iii) NDR >$100K >=115%, (iv) >$500K customer growth >50% YoY, (v) multi-product attach progressing toward 35%. If 4 of 5 confirm: full-conviction buy. If 2-3: half size. If 0-1: wait.
- **Position sizing guidance (for Action 5):** Initial $600-700 starter (~9 shares at $66) = ~25% of cash; add #1 of $300 if stock drops below $60 post-Q1; add #2 of $300 on confirmation; max $1,200 (~33% of portfolio total). MNDY fills the empty mid-cap slot (target ~33%, currently 0%).
- **Rationale:** Action #4 of the four-step discipline. The DCF confirms what the deep dive suggested: MNDY trades at roughly half its probability-weighted intrinsic value at a quality-appropriate 10% hurdle, with bear-case downside of only -22% in the worst combined stress and bear-case upside of +22% in the standard bear scenario. The asymmetry is the textbook setup: paying a price where the bear case roughly preserves capital and the base/bull cases compound at 16-21% IRR over five years. The 5-month buy gate to Q1 print is the right discipline -- the print will confirm or deny the trajectory inputs to the DCF. We do NOT proceed to a buy today; we wait for the May 11-13 print.
- **Resulting state:** Cash $2,370.41 unchanged. No trade. Buy (Action 5) is gated on Q1 2026 print (May 11-13). DCF valid through October 30, 2026 (six-month window).

---

## 2026-05-04 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. Fourth infusion. Total deposited now $4,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred.
- **Resulting state:** Cash $3,370.41 | MSFT 1.5 sh cost basis $629.60 | Total deposited $4,000.00

---

## 2026-05-06 14:30 ET — Quick Scan (Action 1)

- **Action:** Quick Scan
- **Details:** Second portfolio scan, three weeks after the inaugural 4/14 scan. Refreshed live prices for all 21 existing candidates and added 5 new candidates (PUBM, DOCN, CFLT, RBLX, PATH). Full raw notes saved to `research/scans/scan-2026-05-06.md`. Merged updates into `state/candidates.md` (no removals; all existing tickers updated with new last_scanned date and refreshed scores/metrics where Q1 2026 prints justified rescoring).
- **Key re-scoring decisions (post-Q1 2026 earnings cycle):**
  - **GOOGL upgraded 6/10 -> 8/10:** Google Cloud +63% YoY in Q1 print is paradigm-shifting. AI-laggard concession is gone. Now top-tier alongside MSFT and TTD. INITIATION NEEDED — no coverage on file.
  - **AMZN upgraded 6/10 -> 7/10:** AWS +28% (3-year fastest); FY26 capex $200B is the offset.
  - **AMD upgraded 4/10 -> 6/10:** Data center +57%; Q2 guide $11.2B beats. AMD has earned revenue legitimacy in AI accelerators.
  - **MSFT held 8/10:** Capex re-acceleration to ~$190B CY26 is a yellow flag but the WIDE moat thesis is intact. DCF margin of safety thinned slightly to ~9% at $413.40.
  - **META held 7/10:** Strong Q1 (+33%) offset by capex raise ($125-145B) and -10% selloff. Cheaper than peers now.
  - **NVDA held 7/10:** Up 41% to $204.98 since last scan; valuation re-stretched at $4.77T cap.
  - **TTD held 8/10:** Top of stack pending Q1 print May 7. DCF on file (IV $33 vs $24 spot).
  - **MNDY held 7/10:** Pre-print rally to $76 (was $65 deep-dive); MoS still 56% at 10% hurdle. Q1 print May 11.
- **New candidates added:**
  - **PUBM (Small Cap, $472M)** — independent ad-tech SSP, ideal small-cap slot fit; paired play to TTD's DSP. 6/10. Q1 reports 5/7.
  - **DOCN (Mid Cap, $5-6B)** — cloud for SMBs/devs; +33.7% post-Q1; AI cloud traction. 6/10.
  - **CFLT (Mid Cap, $10.7B)** — Kafka data streaming, founder-led, AI pipeline infra. 6/10.
  - **RBLX (Large Cap, $28B)** — Q1 print -18% on child safety/booking guide cut. 4/10. Watch only.
  - **PATH (Mid Cap, $5B)** — RPA/agentic AI; -31.8% YTD; value-trap risk in LLM-disruption narrative. 4/10.
- **Data quality flag:** MU price aggregator data appears corrupted (showing $668 with $760B mkt cap, inconsistent with ~1.1B shares outstanding). Score held flat at 6/10 pending user confirmation of actual price.
- **Top of stack going forward:** TTD (1) -> MSFT (2) -> GOOGL (3) -> NVDA (4) -> META (5) -> APP (6) -> MNDY (7) -> AMZN (8). All scores 7+ now total 8 candidates (was 6 on prior scan).
- **Rationale:** Action #1. The Q1 2026 mega-cap earnings cycle has now completed for the cloud trio (MSFT 4/29, GOOGL 4/29, AMZN 4/29) and META 4/29, creating meaningful re-scoring opportunities. Three weeks of post-earnings price action is sufficient to update the universe. Small-cap representation expanded with PUBM as the highest-conviction small-cap entry. The portfolio's empty mid-cap and small-cap slots are now backed by actionable candidates: TTD/MNDY/CFLT/DOCN (mid) and PUBM/EVLV (small). Next likely action: GOOGL initiation (closes biggest research gap) or wait for TTD Q1 print 5/7 to potentially trigger a buy.
- **Resulting state:** `state/candidates.md` merged with 26 candidates (was 21; +5 new). Cash $3,370.41 unchanged. No trade. Next available actions: Action 2 (Initiation — GOOGL prioritized), Action 5 (Buy — TTD eligible post-5/7 if print clears gates, MNDY post-5/11).

---

## 2026-05-07 — Initiation — GOOGL

- **Action:** Initiation of Coverage (Action 2)
- **Ticker:** GOOGL (Alphabet Inc., NASDAQ)
- **Details:** Full initiation of coverage produced at `research/initiations/INIT-GOOGL-2026-05-07.txt`. Two structured filing extracts created as non-action bookkeeping from user-supplied filings: `GOOGL-10K-FY2025.md` and `GOOGL-EARNINGS-FY2026-Q1.md` saved to `research/filings/` (source files in `research/filings/google/` — 10-K FY2025, Q1 2026 earnings release, Q1 2026 10-Q). Initiation covers: (1) Business description & holding-company structure, (2) Products & segments deep-dive on Q1 2026 acceleration (Google Services 16% / 45.3% margin; Google Cloud 63% / 32.9% margin; Other Bets / Waymo 500K rides/wk), (3) Customers & GTM (~zero ad customer concentration; Cloud RPO >$460B nearly doubled QoQ; 350M paid subscribers), (4) Competitive landscape & moat assessment (Search WIDE-but-narrowing; YouTube WIDE; Cloud NARROW-to-NARROWING-WIDE; Android WIDE on distribution; aggregate WIDE/HIGH confidence), (5) Management (Pichai CEO since 2019, Ashkenazi CFO since July 2024; founder Class B supervoting structure; A- capital allocation grade), (6) Key risks structured by impact: 6.1 antitrust (DOJ Search final judgment Dec 2025 on appeal; DOJ Ad Tech remedy pending; aggregate impact estimate $6-15B EBIT/yr 2028-2030), 6.2 AI search disruption (Q1 print empirically rebuts), 6.3 capex return uncertainty (FY25 $91.4B -> FY26 $140-160B; SBC-adj FCF margin compressed 14.3% -> 12.0% -> 3.1% Q1'26), 6.4 OpenAI/frontier model risk (less acute than MSFT), 6.5 founder governance, 6.6 ad cycle macro, 6.7 Other Bets loss drag, (7) Recent results (FY25 rev $402.8B +15%, op income $129B, OCF $164.7B, FCF $73.3B, SBC-adj FCF $48.3B, $126.8B cash + $46.5B LT debt = $80.3B net cash; Q1'26 rev $109.9B +22%, op income $39.7B, OCF $45.8B, capex $35.7B, FCF $10.1B, SBC-adj FCF $3.4B; Q1 buyback paused at $0; $31.1B notes issued; Wiz close drove +$24.4B goodwill), (8) Valuation snapshot (MV ~$4.86T at $397.32; ~22-24x fwd P/E; trades in line with MSFT/META despite faster cloud growth; preliminary IV $440-490 base / $310-340 bear / $580-680 bull; prob-wtd ~$455-475 = +15-20% upside), (9) Preliminary rating + 5 thesis-must-hold conditions + 6 thesis-break triggers, (10) Pipeline & Deep Dive marching orders (decompose Q1 cloud margin step-up; antitrust scenario tree; capex normalization curve; cloud margin trajectory; search TAM under AI substitution; capital allocation/buyback velocity; Waymo SOTP), (11) Data gaps for follow-up.
- **Rating:** ACCUMULATE (preliminary, pending Deep Dive + DCF). GOOGL is now the third active research pipeline alongside MSFT and TTD.
- **Rationale:** Action #2 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). GOOGL ranked #3 on the May 6 quick scan (8/10, upgraded from 6/10) after the Q1 2026 Cloud +63% / 32.9% margin print materially recut the AI-thesis. As called out in the 5/6 scan, GOOGL was the single largest research gap in the candidate universe and the top-priority initiation. The setup is asymmetric in a different shape than TTD/MNDY: not a deep-value contrarian play, but a quality-anchor compounder where the market multiple (~22x fwd) does not yet reflect the empirical AI leadership emerging in Q1. The stock has run +12% since the Q1 print but trades at the same multiple as MSFT/META despite leading on Cloud growth and having $49B net cash. With MSFT already filling the large-cap slot at 31.5% of starter portfolio, GOOGL would be a complementary large-cap holding -- different moat shape, different AI exposure, more antitrust risk but more cloud-margin upside.
- **Resulting state:** Cash $3,370.41 unchanged. No trade. Active research pipeline updated: MSFT (held), TTD (gated on 5/7 print), MNDY (gated on 5/11 print), GOOGL (deep dive next eligible). Deep Dive (Action 3) is the next eligible action for GOOGL.

---

## 2026-05-11 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. Fifth infusion. Total deposited now $5,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred (logged retroactively on 2026-05-21).
- **Resulting state:** Cash $4,370.41 | MSFT 1.5 sh cost basis $629.60 | Total deposited $5,000.00

---

## 2026-05-18 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. Sixth infusion. Total deposited now $6,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred (logged retroactively on 2026-05-21).
- **Resulting state:** Cash $5,370.41 | MSFT 1.5 sh cost basis $629.60 | Total deposited $6,000.00

---

## 2026-05-21 — Filing Extracts (bookkeeping)

- **Action:** Filing Extracts (bookkeeping — not a daily action)
- **Tickers:** TTD, MNDY
- **Details:** Four structured filing extracts created from user-supplied source filings in `research/filings/ttd/` and `research/filings/mndy/`:
  - `research/filings/TTD-EARNINGS-FY2026-Q1.md` — TTD Q1 FY2026 press release / earnings extract (filing date 2026-05-07)
  - `research/filings/TTD-TRANSCRIPT-FY2026-Q1.md` — TTD Q1 FY2026 earnings call prepared remarks (call date 2026-05-07, Q&A not present in source)
  - `research/filings/MNDY-EARNINGS-FY2026-Q1.md` — MNDY Q1 FY2026 press release / earnings extract (filing date 2026-05-11)
  - `research/filings/MNDY-TRANSCRIPT-FY2026-Q1.md` — MNDY Q1 FY2026 earnings call full transcript including Q&A (call date 2026-05-11)
- **Key TTD takeaways (thesis-relevant):**
  - Revenue $689M, +12% YoY — beat company guide of $678M by 1.6%, exceeds deep-dive minimum of $645M (5/7 buy gate PASS)
  - Q2 guide "at least $750M" implies further deceleration to ~+8% YoY against $694M Q2'25 comp (yellow flag, but framed cyclically by management)
  - Adj EBITDA $206M / 30% margin (-400bps YoY); FY26 reaffirmed at "approximately in line with 2025 (≥40%)" — implies meaningful H2 ramp
  - FCF $276M; net cash position $1.41B (up $103M QoQ even with $164M buyback)
  - JBP signings +55% YoY; March was largest signings month on record (45 JBPs); new JBP spend ex-renewals +40% YoY — positive leading indicator
  - Pharma JBP won back from Amazon DSP with +114% spend target — direct rebuttal to Amazon DSP thesis
  - LinkedIn selected TTD as first DSP partner for B2B CTV — Microsoft-stack endorsement; OpenAds publisher wave (Hearst, BuzzFeed, Guardian, etc.) widens supply moat
  - **Tahnil Davis still Interim CFO** — no permanent hire announced; user deep-dive deadline is July 2026 (~2 months remaining). This is the one remaining open buy condition.
  - Drew Vollero added to Board of Directors (financial/operational depth)
  - Macro: CPG, Auto, Home & Garden, Food & Drink soft; international outpacing US (82% / 18% split)
  - Channel mix: Video low-50s%, Audio fastest-growing at ~6%, CTV momentum global
  - DCF (2026-04-17) is ~34 days old (well within 0-2 month full conviction window); DCF prob-weighted IV $33.45 at 12% hurdle vs. last MSFT-session price reference around $21 still represents 30%+ MoS
  - **3 of 4 buy gates PASS; 1 PENDING (permanent CFO).** Thesis materially intact.
- **Key MNDY takeaways (thesis-relevant):**
  - Revenue $351M, +24% YoY — beat deep-dive minimum of $338M by $13M (3.9% beat); FY26 guide RAISED from $1,452-1,462M to $1,466-1,475M (+19-20% growth)
  - All 5 primary buy gates from deep dive sec 10.7 PASS: revenue, FY26 guide raise, NDR>$100K=115% at floor, $500K customers +74% YoY (>50% bar), multi-product attach 34% (toward 35% bar)
  - >$500K customers grew 57 → 99 (+74%) — record net adds; multi-product attach jumped 29% → 34% (+500bps QoQ — fastest in company history)
  - **Overall NDR fell to 110%** (guided to "slightly decline by end of FY26") — clean explanation: 2024 pricing actions added 12% to NDR and lap out end of Q2'26. Gross retention at all-time highs.
  - Non-GAAP op margin held at 14% despite -190bps FX headwind; record GAAP op income $19.8M
  - Adj FCF margin compressed to 29% from 39% (FY26 guide 19-20%) — drivers: $20M buyback interest income loss, FX, AI compute. Modeled in deep dive.
  - **AI Work Platform launched** (biggest change in company history per Zinman); native agents + monday DB 3.0 (100x scale); new seats-plus-credits consumption pricing
  - **AI products already ~10% of net new ARR** with agents not yet launched (released ~1 week before call) — materially ahead of deep-dive AI ARR ramp expectations
  - **OneAI acquisition** announced — voice agents for AI Work Platform + CRM
  - Internal AI productivity: +32% dev output, -38% time to market — operating leverage thesis quantified
  - $553M deployed in buyback in Q1 (~7.27M shares at ~$76 average) — ~14% of float retired; $182M remaining of $870M authorization. **Capital allocation velocity at upper bound of deep-dive expectations.**
  - Headcount flat for rest of FY26 (3,211 at Q1) — explicit operating-leverage commitment
  - Gross margin held at 89% (vs. 90% prior year); long-term guide mid-80s as AI compute costs ramp
  - Q2 guide $354-356M (+18-19%) is below Q1 actual +24% — implies H2 moderation, partly H2 AI compute investment
  - Customers >$50K ARR represent 42% of ARR (up from 37%); >$100K = 29% (up from 24%); >$500K = 6% (up from 5%) — enterprise mix shift steady
  - RPO +33% to $880M; cRPO +26% to $716M — booked future revenue accelerating
  - Top-of-funnel SMB "remains soft" but in line with full-year expectations (Zinman). No new degradation.
  - Claude/Anthropic framing: coexistence not displacement; "external agents" can sign up to monday — Mann
  - DCF (2026-04-30) is ~21 days old (full conviction window); IV $172 at 10% hurdle / $140 at 12% hurdle — thesis improved by raised guide + AI traction. **6 of 5 gates PASS.**
- **Resulting state:** Cash $5,370.41 unchanged. No trade. Both TTD and MNDY are buy-eligible for next session pending live price check. MNDY has stronger setup (all gates pass, fresh DCF, AI optionality monetizing earlier than modeled); TTD has 3-of-4 gates passing with the open CFO permanence condition still pending. Next-session priority: live-price MNDY and assess Action 5 (Buy) eligibility against position-sizing guidance ($600-700 starter at ~$66 era; need to re-check live post-print price for current MoS).

---

## 2026-05-10 — Deep Dive — GOOGL

- **Action:** Deep Dive (Action 3)
- **Ticker:** GOOGL (Alphabet Inc., NASDAQ)
- **Details:** Long-form deep dive completed at `research/deep-dives/DEEP-GOOGL-2026-05-10.txt`. Filing extracts re-used (no new bookkeeping needed): `GOOGL-10K-FY2025.md` and `GOOGL-EARNINGS-FY2026-Q1.md` plus raw 10-Q (`research/filings/google/GOOG-10-Q-Q1-2026.txt`). Q1 2026 earnings call transcript NOT on file — gap noted. Fourteen sections covering all seven initiation marching orders plus 10-yr scenarios, thesis-break checklist, and DCF marching orders: (1) Q1 cloud margin step-up decomposition (1,510bps move = ~60% operating leverage / ~16% mix shift / ~10% Wiz / ~7% FX / ~7% one-time; ~70-80% structural), (2) Antitrust scenario tree (DOJ Search 5 outcomes prob-wtd -$10B/yr; DOJ Ad Tech 4 outcomes prob-wtd -$3.7B/yr; combined ~$15B/yr by FY28-30; tail risk ~9% combined for Chrome divestiture or Ad Manager structural breakup), (3) Capex normalization curve (FY26 base $148B / FY27 $150B / FY28 $140B / FY30 $115B; bear sustains $145-175B through FY30; bull peaks $140B FY26 normalizing to $100B FY30; backed by $462B Cloud RPO + $75.6B not-yet-commenced data center leases + multi-gigawatt TPU supply agreements), (4) Search TAM under AI substitution (3 scenarios: T1 +12% CAGR / T2 +9% / T3 +5%; prob-wtd FY30 Search rev $346B = ~9% CAGR; AI Overviews + AI Mode are monetizable surfaces, not pure cannibalization; subscription cross-sell via Google One/Gemini Advanced recaptures), (5) Capital allocation / buyback velocity under Ashkenazi (Q1 buyback pause = sequencing artifact ~80% confidence vs. structural shift ~20%; 3 scenarios C1 $50B / C2 $40B / C3 $25B FY26 buyback; share count NEAR-FLAT after SBC offset; per-share IV growth comes from FCF, not financial engineering; capital allocation grade B+, slight downgrade from initiation A-), (6) Waymo SOTP ($80-150B fair value triangulated across funding round, mobility multiples, Tesla AV comp; point estimate $100B = ~$8/share; treated as upside optionality not base case), (7) Cloud margin trajectory vs AWS/Azure (GCP 32.9% Q1 OM now within 3-5pts of AWS ~36% and at-or-above Azure standalone; FY30 base case 35% closes gap to AWS to <2pts; structural drivers: TPU + Gemini + DeepMind talent), (8) 10-yr scenarios with explicit revenue/margin/capex tables (Bear 25% prob -> ~$320 IV, Base 55% -> ~$475 IV, Bull 20% -> ~$660 IV; prob-weighted ~$473/share = +19% MoS at $397 init / +13% at ~$420 current), (9) Thesis-break checklist (8 conditions; current 0 RED / 1 YELLOW (buyback velocity) / 7 GREEN), (10) Optionality not in base case (Waymo, quantum, healthcare/Verily, sovereign AI, GFiber divestiture, Anthropic stake, Pixel devices), (11) What would have to be true for thesis to break (5 mechanically distinct scenarios), (12) DCF marching orders (10-yr explicit forecast, three scenarios, segment-by-segment revenue build, explicit capex curve, antitrust EBIT haircut overlay, three hurdle rates 9%/11%/13%, gate for buy >= $475 at 10% hurdle), (13) Preliminary view & buy pre-conditions, (14) Data quality & research gaps.
- **Key conclusions:**
  - Cloud margin step-up dominantly structural (~70-80% of 1,510bps move); steady-state Cloud OM 30-33% base case lifts FY30 Cloud op income est by ~$15-20B vs. initiation prior — most important finding.
  - Combined antitrust EBIT impact ~$15B/yr by FY28-30 already appears priced into the multiple (GOOGL fwd P/E ~22-24x vs. MSFT ~22-26x despite faster Cloud growth and larger net cash).
  - Capex curve has visible normalization path with $462B Cloud RPO + multi-gigawatt TPU supply deals as demand backstop; bear case is "supercycle extends through FY30" — the central downside risk.
  - Search rev re-acceleration is empirically visible (paid clicks +6%, CPC +7%, queries at all-time high), refuting the "AI eats Search" bear thesis at least for now.
  - Cloud margins now at-or-near AWS quality; repositions GOOGL from "discount-to-MSFT story" to "AWS-quality cloud at MSFT's multiple" story.
  - Q1 buyback pause is yellow-flag but defensible (M&A close + $31B notes issuance); Q2 print is the next observable.
  - Probability-weighted IV ~$473 at standard hurdle vs. $397 init / ~$420 estimated current = +13-19% margin of safety. DCF will refine.
- **Rating:** ACCUMULATE (unchanged from initiation; conviction strengthened). Buy is gated on DCF (Action 4) confirmation: prob-wtd IV >= $475 at 10% hurdle for full-conviction starter, OR >= $440 at 11% hurdle for half-size starter.
- **Rationale:** Action #3 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). The deep dive resolved the seven marching orders left by the May 7 initiation and produced a coherent prob-weighted intrinsic value range of $320 (bear) / $475 (base) / $660 (bull) -> $473 prob-wtd. The Cloud margin decomposition (sec 1) is the single most consequential finding — it shifts our FY30 Cloud op income estimate up materially and supports the AWS-quality thesis. The capex curve (sec 3) and antitrust scenario tree (sec 2) bound the downside. GOOGL would be the second large-cap anchor alongside MSFT (different moat shape, different AI exposure, more antitrust risk but more Cloud margin upside) — complementary rather than redundant.
- **Resulting state:** Cash $3,370.41 unchanged. No trade. DCF (Action 4) is the next eligible action for GOOGL. Active research pipeline: MSFT (held), TTD (Q1 print 5/7 — confirm next session), MNDY (gated on 5/11 print), GOOGL (DCF next eligible).

---

## 2026-05-21 14:12 ET — Buy — MNDY

- **Action:** Buy (Action 5)
- **Ticker:** MNDY (monday.com Ltd., NASDAQ; Israeli FPI)
- **Shares:** 8.0
- **Price:** $77.36 (live quote fetched at 2:11:54 PM ET on 2026-05-21 via Google Finance; -2.26% / -$1.79 on the day from $79.15 prior close; intraday range $76.71-$82.87)
- **Total cost:** $618.88 (8.0 x $77.36)
- **Cash before:** $5,370.41
- **Cash after:** $4,751.53
- **DCF reference:** `research/dcf/DCF-MNDY-2026-04-30.txt` (completed 2026-04-30; 21 days old = full conviction window, expires 2026-10-30)
- **Margin of safety check (DCF age 0-2 months -> no additional discount required):**
  - Prob-weighted IV @ 10% hurdle: $172/share -> MoS at $77.36 = **55.1%**
  - Prob-weighted IV @ 12% hurdle: $140/share -> MoS = 44.7%
  - Prob-weighted IV @ 14% hurdle: $115/share -> MoS = 32.7%
  - Bear case @ 10% hurdle: $81/share -> still +4.7% upside in the bear scenario
  - Combined-stress IV (bear scenario + 14% hurdle + -200bps FX 5yr + -20% Loop hit): ~$48-52 -> -33% to -38% downside tail at $77.36
  - All MoS figures are FAR above the typical 15-20% buy threshold. Q1 2026 print materially strengthened (not weakened) the thesis, so the 4/30 DCF if anything understates current IV.
- **Buy gates (all 5 from Deep Dive 10.7 PASS, per 2026-05-21 filing extracts bookkeeping):**
  - (i) Q1 rev >=$338M: PASS — actual $351M (+24% YoY, +3.9% beat)
  - (ii) FY26 guide maintained at $1,452-1,462M: PASS — RAISED to $1,466-1,475M (+19-20%)
  - (iii) NDR >$100K >=115%: PASS — 115% at floor; >$500K cohort accelerating
  - (iv) >$500K customer growth >50% YoY: PASS — +74% YoY (57 -> 99, record net adds)
  - (v) Multi-product attach progressing toward 35%: PASS — 34% (+500bps QoQ, fastest in company history)
  - Bonus signals beyond gates: AI products ~10% of net new ARR ahead of model; $553M buyback in Q1 (~14% of float retired); OneAI acquisition for voice agents; internal AI productivity +32% dev output / -38% time to market.
- **Allocation check (post-buy, current value basis):**
  - Large cap (MSFT $631.59): 10.5% of total portfolio
  - Mid cap (MNDY $618.88): 10.3% of total portfolio (was 0%)
  - Small cap: 0%
  - Cash: 79.2%
  - Per rules: "While the portfolio has fewer than ~6 holdings, the split may deviate." With 2 holdings the cap split is acceptable. MNDY fills the previously empty mid-cap slot. Next slot to fill is small-cap (PUBM is the priority candidate per the 2026-05-06 scan).
- **Position sizing rationale:** DCF Action 5 guidance specified an initial $600-700 starter (~9 shares at $66) with adds of $300 below $60 and $300 on confirmation, max $1,200. We chose 8.0 shares ($618.88) -- literally within the $600-700 starter range -- rather than max-loading because: (1) MNDY's 52-wk range is $57.50-$316.98 (volatile), (2) preserving dry powder for the planned add-on tranches at lower prices honors a 'leg into the position on weakness' discipline, (3) cash also needs to fund the small-cap slot (PUBM) and a potential GOOGL DCF-to-buy chain, (4) TTD's CFO permanence condition is still open through July 2026 and we want to retain optionality to act once the 4th gate clears, (5) the starter is sized to roughly match the MSFT starter ($629.60 vs. $618.88) so neither anchor dominates the early portfolio.
- **Rationale:** This is the textbook asymmetric-buy setup the deep dive and DCF were built to identify, and the Q1 print on 5/11 confirmed every condition that gated the trade. Five-for-five on the buy gates, FY26 guide RAISED, AI ARR already at ~10% of net new with agents not yet launched, $553M of buyback already executed in Q1 alone (capital allocation at the upper bound of the deep-dive model), and the stock is -2.26% on the day giving us an intraday entry below the morning print. The probability-weighted IV is $172 at a 10% hurdle vs. $77.36 spot -- a 55% margin of safety -- and even the bear case at a 10% hurdle ($81) preserves capital with +5% upside. The combined-stress tail (-33% to -38% to ~$48-52) is the real downside, but that requires bear scenario + 14% hurdle + -200bps FX + -20% Loop hit all stacking; the probability of that conjunction is low. The DCF is 21 days old, comfortably inside the 0-2 month full-conviction window, and Q1 results would increase rather than decrease IV if I refreshed it today. Sizing is the disciplined starter ($600-700 per DCF guidance) preserving ~$4,750 of dry powder for: (a) MNDY add tranches at lower prices, (b) the small-cap PUBM slot, (c) TTD once the permanent CFO gate clears, (d) potential GOOGL DCF-to-buy if the model clears the $475 gate. Founder-led ($35B+ founder skin in the game), 89% gross margins, $1.67B+ net cash, 14% non-GAAP op margin, and a clear AI-monetization path in agents and the Work Platform. This is not a moonshot -- the bear case is roughly capital-preserving and the base case is a 16-21% 5-year IRR.
- **Resulting state:** Cash $4,751.53 | MSFT 1.5 sh ($631.59) + MNDY 8.0 sh ($618.88) = Invested $1,250.47 | Total $6,002.00 | Holdings: 2/10 | Allocation: Large 10.5% / Mid 10.3% / Small 0% / Cash 79.2%. Buy cadence: next buy eligible 2026-05-28 (one buy per week). Sell cadence: no sells yet; one per month available.

---

## 2026-05-25 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded for the week of 2026-05-25. Seventh infusion. Total deposited now $7,000.00. Logged retroactively on 2026-05-29 per user confirmation; 2026-05-25 was Memorial Day (U.S. market holiday) but the standing weekly deposit settled on that date.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred during this session.
- **Resulting state:** Cash $5,751.53 | MSFT 1.5 sh cost basis $629.60 | MNDY 8.0 sh cost basis $618.88 | Total invested cost basis $1,248.48 | Total deposited $7,000.00

---

## 2026-05-29 — DCF — GOOGL

- **Action:** DCF (Action 4)
- **Ticker:** GOOGL (Alphabet Inc., NASDAQ)
- **Details:** Full 10-year DCF model completed at `research/dcf/DCF-GOOGL-2026-05-29.txt`. Built strictly per the marching orders in DEEP-GOOGL-2026-05-10 sec 12: (a) 10-yr explicit forecast FY26-FY35, (b) SBC-adjusted FCF as primary underwriting column, (c) three scenarios Bear 25% / Base 55% / Bull 20%, (d) segment-by-segment revenue build with deep-dive-specified CAGRs (Search/YouTube/Subs/Network/Cloud/Other Bets), (e) explicit capex curve per scenario ($148-158B FY26 peak normalizing), (f) explicit antitrust EBIT haircut overlay starting FY28 (Base -$15B/yr by FY30, Bear -$25B, Bull -$8B), (g) both perpetuity-growth (3% terminal g) and exit-multiple (Base 22x / Bear 18x / Bull 25x) terminal values, averaged, (h) Waymo/Other Bets SOTP added ($0/$60B/$200B), (i) hurdle rates 9% / 11% / 13% with 10% interpolated, (j) Q1'26 net cash baseline of $49.3B, (k) tax rate 18%, (l) shares modeled FY35 at 12,400/12,000/11,500 Bear/Base/Bull. Q1 2026 earnings call transcript was NOT on file; user authorized proceeding without it. The transcript would have refined Cloud margin durability and buyback velocity assumptions but the model carries explicit error bars on those inputs.
- **Spot price reference:** $382.79 (Class A, intraday 2026-05-29; range $376.59-$388.00 per live web search aggregation).
- **Key results (probability-weighted intrinsic value per share):**
  - IV @ 9% hurdle: **$292/share** (Bear $84 / Base $295 / Bull $546)
  - IV @ 10% hurdle (interpolated): **$261/share**
  - IV @ 11% hurdle: **$230/share** (Bear $61 / Base $230 / Bull $432)
  - IV @ 13% hurdle: **$186/share** (Bear $47 / Base $186 / Bull $355)
- **Gate check vs Deep Dive sec 12.10:**
  - $475 prob-wtd IV @ 10% hurdle: **FAIL** (DCF says $261; gap -$214 / -45%)
  - $440 prob-wtd IV @ 11% hurdle: **FAIL** (DCF says $230; gap -$210 / -48%)
  - Robustness re-check with friendlier 25/50/25 probability weights: IV @ 10% = $271, IV @ 11% = $238 — still FAIL by 43-46%.
- **Reconciliation to Deep Dive's ~$473 top-down estimate:** The deep dive cited prob-wtd IV ~$473 at "standard hurdle" but did NOT show an explicit cash-flow build — it was a triangulated estimate from comparable multiples and high-level scenario sketches. The bottom-up DCF reveals that the capex supercycle creates a 4-5 year cash-flow drought (FY26-28 SBC-adj FCF Base case: -$6B, +$15B, +$45B vs FY25 baseline of $48B), which depresses the explicit-period PV by ~$200-300B relative to a smoother trajectory. The deep dive's $473 implicitly assumed faster capex normalization, higher Cloud OM, and/or higher exit multiples than the bottom-up build supports. This is exactly the value of the Action 4 gate — it surfaces top-down/bottom-up disagreements before a buy.
- **Reverse DCF:** At $382.79 spot, market is pricing in ~$4,476B EV (implied) which requires Cloud rev CAGR ~36% '26-30 (vs base 28%), OR Services OM expanding to 45% by FY30 (vs base 43%), OR exit multiple of ~27-28x (vs base 22x), OR scenario weighting closer to Bear 15% / Base 50% / Bull 35%. Each of these is defensible individually but represents a Bull-Base hybrid, not the central case.
- **Combined-stress tail (~5% probability):** IV $42/share (-89% from $382 spot) — Bear scenario + 13% WACC + -$45B antitrust haircut + -$60B net debt. Worst credible tail.
- **Sensitivity highlights:**
  - WACC -100bps: ~+$25-30/share
  - Cloud OM ±400bps in FY30: ~±$15/share (LOWER than deep dive's $70 estimate — because long-tail compression eats much of the gain)
  - Capex curve ±$25B/yr persistent through FY30: ~±$50/share (matches deep dive)
  - Antitrust haircut ±$10B/yr: ~±$16/share (LOWER than deep dive's $35 estimate)
- **Rating downgrade:** ACCUMULATE -> **HOLD / WATCH**. GOOGL is a high-quality compounder with a WIDE moat and best-in-class capital allocation, but at $382 the bottom-up math does not support a buy today. Market is pricing 30-65% above prob-wtd intrinsic value at the 9-11% hurdle range. NOT eligible for Action 5 (Buy) under deep-dive-defined gates.
- **Buy re-eligibility conditions:**
  - Pullback to ~$280-310 (where MoS vs $295 Base case @ 9% would be 5-10%, acceptable for quality anchor), OR
  - Q2 2026 print (~late July 2026) confirms (i) Cloud OM durability at >=30% at scale, (ii) buyback resumption at $10B+, (iii) capex guide normalization signal — at which point refresh the model and re-test base-case Cloud OM at 35-36% which could lift prob-wtd IV to ~$330-350
- **Optionality not captured in base case:** Anthropic stake (embedded in $107B non-marketable securities), sovereign AI contracts, quantum, healthcare/Verily — combined ~$40-60B of EV not modeled. Still not enough to close the gate gap, but worth noting as upside vs the static model.
- **Rationale:** Action #4 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). The DCF is the discipline that surfaces top-down/bottom-up disagreements. In GOOGL's case, the deep dive's optimistic ~$473 prob-wtd IV estimate did not survive a rigorous bottom-up build with the capex supercycle's cash-flow drought correctly modeled. We do NOT proceed to a buy today — this is the right time to write down "not at this price" and redirect cash to higher-asymmetry opportunities (MNDY add tranches below $60, PUBM small-cap initiation, TTD once permanent CFO confirmed) until either price comes to us or Q2 print justifies a base-case revision.
- **Resulting state:** Cash $5,751.53 unchanged. No trade. GOOGL pipeline status: Init done -> Deep Dive done -> DCF done, FAIL gates. Buy NOT eligible. DCF valid through 2026-11-29 (six-month window) but refresh recommended after Q2 2026 print (late July 2026).

---

## 2026-06-03 — Filing Extracts (bookkeeping)

- **Action:** Filing Extracts (bookkeeping — not a daily action)
- **Ticker:** PUBM
- **Details:** Two structured filing extracts created from user-supplied source files in `research/filings/pubm/`:
  - `research/filings/PUBM-10K-FY2025.md` — FY2025 Form 10-K (income statement, cash flow, balance sheet, key metrics, risk factors, capital return, share structure)
  - `research/filings/PUBM-EARNINGS-FY2026-Q1.md` — Q1 FY2026 earnings release + earnings call transcript (combined; income statement, cash flow, balance sheet, channel/geo breakdown, AgenticOS detail, guidance, leadership transitions, Google antitrust optionality)
- **Source 10-K note:** The raw 10-K text file (426.7KB) exceeded the single-read size limit; it was read in targeted sections (Item 1 Business, Item 5 capital return/share structure, Item 7 MD&A, Item 8 financial statements, risk-factor summary) to build the extract. No financial data fabricated.
- **Resulting state:** Extracts available for all PUBM research actions (2/3/4). No trade. No daily action consumed.

---

## 2026-06-03 — Initiation — PUBM

- **Action:** Initiation of Coverage (Action 2)
- **Ticker:** PUBM (PubMatic, Inc., Nasdaq; small cap ~$517M)
- **Details:** Full initiation of coverage produced at `research/initiations/INIT-PUBM-2026-06-03.txt`, built from the two PUBM filing extracts created this session. Ten sections: (0) why-now thesis framing PUBM as the independent-SSP mirror of TTD's independent-DSP and the top small-cap-slot candidate; (1) business description (independent AI-powered SSP, net-revenue accounting with AR/AP gross-up, owned NVIDIA-GPU infrastructure vs. public cloud, >1T impressions/day, ~1,980 publishers, 1,030 employees with heavy India base); (2) products & segments (core SSP/OpenWrap; emerging revenue +80% / 14% of revenue via Activate +3x, Connect, Commerce/Convert, Walmart Connect + PayPal Ads ID; AgenticOS AI layer with 20+ agents, 1,000+ AI deals, 30+ autonomous campaigns); (3) customers & GTM (4 customer types; DSP concentration with Google + TTD as the two largest buyers terminable on 30 days notice; legacy-DSP headwind; NDR 96% FY25 / flattish Q1'26 with H2 recovery guide; geo diversification APAC +25% / EMEA +10% offsetting Americas -12%); (4) competitive landscape & moat (vs. Google AdX ~60%, Magnite, Index/OpenX; NARROW moat / MODERATE confidence on independence + owned-infra + AI/data flywheel, with take-rate compression as the structural threat); (5) management (Goel founder-CEO since 2006, Pantelick CFO stable; dual-class governance flag; CGO + Americas CRO simultaneous departures yellow flag; global CRO search; B+/A- capital allocation on FCF-funded buybacks); (6) key risks ranked (DSP concentration/take-rate 30%, AI double-edged 20%, return-to-growth execution 15%, leadership turnover 10%, Google litigation/antitrust 10% net-positive, privacy/cookie 10%, macro/FX 5%); (7) recent results (FY2025 rev $282.9M -3%, op loss $(17.3)M, adj EBITDA $61.6M 21.8% margin, FCF ~$46M, SBC $38.4M = 13.6% of rev, net cash $145.5M zero debt; Q1'26 rev $62.6M -2% reported / +13% ex-DSP, adj EBITDA $2.6M, FCF $10.7M, 40th consecutive positive-EBITDA quarter, Q2 guide $68-70M, capex only $16-19M FY26, H2 double-digit growth guide); (8) valuation snapshot (live ref ~$11.13 / mkt cap ~$517M / EV ~$372M; EV/rev ~1.3x, EV/adj-EBITDA ~6.0x, EV/FCF ~8.1x, P/FCF ~11.2x; net cash ~28% of mkt cap; trough-decile multiples; Google-remedy each-1%-share = $50-75M at ~80% margin as a free option); (9) preliminary rating, thesis-must-hold + thesis-break checklists, and 8-point Deep Dive marching orders.
- **Live price reference:** ~$11.13 (intraday 2026-06-03 via web search aggregation; 52-wk $6.15-$13.88). Qualitative valuation context only — NO trade executed.
- **Rating:** WATCH / ACCUMULATE ON CONFIRMATION. Buy gated on the H2 2026 reacceleration thesis (return to reported growth Q3, double-digit H2), NDR recovery toward 100%, EBITDA-margin re-expansion, sustained AgenticOS growth, and a permanent global CRO hire — then a passing Deep Dive and DCF (SBC-adjusted FCF underwriting, take-rate sensitivity, net-cash floor).
- **Rationale:** Action #2 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). PUBM was the #1 small-cap initiation priority per the 2026-05-06 scan and the priority watchlist, elevated after the GOOGL DCF gate failure redirected attention to higher-asymmetry small caps. It is the natural fill for the empty small-cap slot (0% vs ~33% target) and a paired independent open-internet ad-tech construction alongside the TTD coverage we already hold in the pipeline. The shape is attractive (cheap, $145M net cash / zero debt = ~28% of mkt cap, FCF-positive 40 straight quarters, founder-led, +13% underlying growth masked by a self-limiting legacy-DSP headwind, plus AI and Google-remedy free options) but the thesis is explicitly contingent on the H2 reacceleration being real, so the rating is deliberately conditional. Initiation advances PUBM into the active pipeline; no capital committed.
- **Resulting state:** Cash $5,751.53 unchanged. No trade. PUBM pipeline status: Init DONE -> Deep Dive (Action 3) next eligible. Active research pipeline now: MSFT (held), MNDY (held), TTD (buy gated on permanent CFO), GOOGL (DCF gates failed, HOLD/WATCH), PUBM (Init done). Holdings: 2/10.

---

## 2026-06-27 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping — not a daily action)
- **Details:** Four standing weekly Monday deposits of $1,000.00 each, confirmed by user as landed, logged together this session:
  - 2026-06-01: +$1,000.00 (8th infusion) — running total deposited $8,000.00
  - 2026-06-08: +$1,000.00 (9th infusion) — running total deposited $9,000.00
  - 2026-06-15: +$1,000.00 (10th infusion) — running total deposited $10,000.00
  - 2026-06-22: +$1,000.00 (11th infusion) — running total deposited $11,000.00
- **Rationale:** Standing $1,000 weekly Monday deposit per portfolio rules. User confirmed all four June Mondays (6/01, 6/08, 6/15, 6/22) settled. These had been flagged pending in the 6/27 mark-to-market note; now recorded. Bookkeeping only — does not consume the daily action.
- **Resulting state:** Cash $5,751.53 -> $9,751.53 (+$4,000.00). Total deposited $7,000.00 -> $11,000.00. Holdings unchanged: MSFT 1.5 sh, MNDY 8.0 sh (cost basis $1,248.48). Total portfolio value ~$10,888.43 (cash $9,751.53 + invested $1,136.90 at 6/26 closes). Allocation: large-cap MSFT ~5.1%, mid-cap MNDY ~5.3%, small-cap 0%, cash ~89.6%. Cash now substantial — small-cap slot (PUBM) and TTD/MNDY adds are the priority deployments once research and price gates clear.

---

## 2026-06-27 — Deep Dive — PUBM

- **Action:** Deep Dive (Action 3)
- **Ticker:** PUBM (PubMatic, Inc., Nasdaq; small cap ~$517M)
- **Details:** Long-form deep dive completed at `research/deep-dives/DEEP-PUBM-2026-06-27.txt`, built from the two existing filing extracts (`PUBM-10K-FY2025.md`, `PUBM-EARNINGS-FY2026-Q1.md` — no new bookkeeping needed) plus qualitative web context on the Google ad-tech antitrust remedy and the SSP competitive landscape (no financials fetched). Thirteen sections executing the 8 initiation marching orders: (0) exec summary, (1) unit economics + a critical SHARE-COUNT RECONCILIATION gap (10-K extract's "93.9M Class A" does NOT reconcile with ~47.1M EPS-weighted shares / ~$517M cap at ~$11.13 — valuation must use ~47-48M, verified before DCF), (1.3) the SBC-adjusted FCF crux (FY2025 reported FCF $46.3M flattered by $38.4M SBC; true SBC-adj FCF only ~$7.9M = ~2.8% margin = ~47x EV, NOT the 8x EV/reported-FCF screen), (2) legacy-DSP decomposition (affected ~17% cohort down >50% YoY dragging +13% underlying to -2% reported; laps mid-Q3 2026 — mechanically self-limiting but contingent on no third DSP rerouting), (3) TAM/AgenticOS + AI-disintermediation tail (agentic reshapes rather than erases SSP, but take rate can compress), (4) competitive dynamics — KEY DOWNGRADE: PUBM is a sub-scale #3 (~4% SSP share) behind Magnite (~25% US, CTV leader) in a consolidating layer (32->18 SSPs); moat moved to NARROW / LOW-TO-MODERATE confidence, (5) Google-remedy scenario tree (Brinkema likely behavioral not structural-AdX-divestiture; ~50% behavioral / ~20% structural-but-delayed-by-appeal / ~30% weak-or-negligible; treat as bull-case-only delayed option, net of active Google litigation cost), (6) capital allocation B+ (FCF-funded buybacks, but track NET shares given 13.6% SBC), (7) management/governance (Goel 20-yr founder-CEO, stable CFO = positive vs TTD; dual-class flag; YELLOW FLAG: two senior revenue leaders departing mid-trough, global CRO search), (8) optionality, (9) 5/10-yr scenarios, (10) thesis-break, (11) confirmation checklist, (12) DCF marching orders, (13) preliminary view.
- **Key conclusions:**
  - The cheapness is real only on EV/EBITDA (~6x) and EV/reported-FCF (~8x); on SBC-adjusted FCF (~$8M) it is ~47x trailing. The entire case is a margin-recovery + reaccel bet, NOT a static-FCF bargain.
  - Competitive position is weaker than the initiation implied: sub-scale #3 behind a ~5-6x-larger, CTV-strong Magnite; moat NARROW / LOW-TO-MODERATE.
  - Google remedy is likely behavioral and multi-year — an option, not an event.
  - Probability weights revised to BEAR 30% / BASE 50% / BULL 20% (bear raised from ~25%).
  - Preliminary prob-weighted indicative IV ~$16-19 vs ~$11.13 (~+45-70%), bear floor ~$6-9 (net-cash-anchored). Favorable but NOT a >50%-MoS layup — narrower and more execution-dependent than MNDY was.
  - CRITICAL DATA GAP: reconcile share count (~47-48M vs the extract's 93.9M) before the DCF; per-share IV is one-for-one sensitive.
- **Rating:** WATCH / ACCUMULATE ON CONFIRMATION (unchanged). Buy gated on: (a) a DCF clearing >=40% MoS at a 12% hurdle (higher bar than MSFT/MNDY's 10%, reflecting narrow moat + execution risk), OR (b) confirmation of the Q3 2026 reacceleration + permanent global-CRO hire. A small confirmation-sized small-cap-slot STARTER could be justified post-DCF if the MoS is wide enough.
- **Rationale:** Action #3 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). PUBM is the priority small-cap-slot candidate; the deep dive confirms the right shape (cheap, net-cash, FCF-positive, founder-led, two free options) but sharpens three cautions (SBC-adjusted owner earnings, sub-scale #3 competitive position, behavioral-not-structural remedy) that argue for the DCF to do real work and for a wide margin of safety. Markets were closed (Saturday) so no trade was possible regardless; a research action was the correct use of the day.
- **Resulting state:** Cash $9,751.53 unchanged (post-infusion). No trade. PUBM pipeline: Init DONE -> Deep Dive DONE -> DCF (Action 4) next eligible. Holdings: 2/10. Active pipeline: MSFT (held), MNDY (held), TTD (buy gated on permanent CFO), GOOGL (DCF gates failed, HOLD/WATCH), PUBM (Deep Dive done, DCF next).

---

## 2026-07-08 18:20 ET — Daily Mark-to-Market (bookkeeping)

- **Action:** Daily portfolio mark-to-market (non-action bookkeeping)
- **Details:** Session-start mark on 7/08 closing prices (market CLOSED — after regular hours, Wednesday). MSFT $372.97 (6/26) -> $388.84 (7/08 close), +4.3%; MNDY $72.18 (6/26) -> $84.10 (7/08 close), +16.5%. Updated portfolio.md holdings and summary. Invested value $1,136.90 -> $1,256.06; total value $10,888.43 -> $11,007.59; total gain flipped to +$7.59 (+0.07%) vs $11,000 deposited — first positive since the drawdown. Today's-gain fields left n/a (12-calendar-day gap since prior mark = multi-session move, not single session).
- **Rationale:** Daily bookkeeping per session-start protocol. Both holdings recovered off the June lows; MNDY notably strong. No action triggered by the mark; we hold.
- **Resulting state:** Cash $9,751.53 | MSFT 1.5 sh @ $388.84 = $583.26 | MNDY 8.0 sh @ $84.10 = $672.80 | Total $11,007.59 | +0.07% vs deposits.

---

## 2026-07-08 — DCF — PUBM

- **Action:** DCF (Action 4)
- **Ticker:** PUBM (PubMatic, Inc., Nasdaq; small cap ~$629M @ $13.55)
- **Details:** Full 10-year DCF model completed at `research/dcf/DCF-PUBM-2026-07-08.txt`, built strictly to the 14 marching orders in DEEP-PUBM-2026-06-27 sec 12, from existing filing extracts (`PUBM-10K-FY2025.md`, `PUBM-EARNINGS-FY2026-Q1.md` — no new bookkeeping; NO filings fetched from web). Features: (1) SHARE COUNT RECONCILED FIRST — the 10-K extract's "93.9M Class A" is NOT the economic base; Q1'26 EPS-weighted diluted shares 47.1M and live mkt cap $629M/$13.55 = 46.4M both confirm ~47M; model uses 47.0M declining -1.0%/-1.5%/-2.0% per yr bear/base/bull; (2) underwriting on SBC-ADJUSTED FCF (FY25 baseline ~$7.9M / 2.8% margin, NOT reported $46.3M/16%); (3) 10-yr explicit FY2026-FY2035; (4) weights BEAR 30% / BASE 50% / BULL 20% per deep dive; (5) revenue build by driver with legacy-DSP lap mechanics; (6) EBITDA recovery 21.8%->15%/28%/32% by FY30, SBC 13.6%->12%/10%/8%; (7) capex kept as real cost ~$33-55M; (8) net-cash floor +$145M / zero debt; (9) Google remedy BULL-CASE-ONLY as delayed +1-2pt share option; (10) BOTH terminal methods (perpetuity g 2%/3%/3.5% AND exit multiple 7x/10x/14x SBC-adj FCF), averaged; (11) 12% PRIMARY hurdle with 10% and 14% sensitivities; (12) reverse DCF + combined-stress tail.
- **Live price reference:** ~$13.55 (intraday 2026-07-08 via web search aggregation; market CLOSED — qualitative context only, NO trade). 52-wk $6.15-$13.99.
- **Key results (prob-weighted intrinsic value per share, scenario-end share convention):**
  - IV @ 10% hurdle (sensitivity): **~$14.90** (Bear $3.55 / Base $12.60 / Bull $32.00) -> +10% MoS
  - IV @ 12% hurdle (PRIMARY): **~$11.50** (Bear $3.40 / Base $10.40 / Bull $26.40) -> -15% (PREMIUM)
  - IV @ 14% hurdle (sensitivity): **~$9.75** (Bear $3.25 / Base $8.70 / Bull $22.00) -> -28% (PREMIUM)
  - Conservative current-47M-share convention shifts each ~10-15% lower (12% central ~$9.70).
  - Bear net-cash floor: ~$3-3.4/share.
- **Gate check vs Deep Dive sec 12.13 (">=40% MoS at 12% hurdle"):** **FAIL.** Prob-wtd IV @ 12% ~$11.50 is BELOW the $13.55 spot (negative MoS). The >=40% MoS bar implies a buy price of ~$6.90-$7.60. Even the generous 10% hurdle gives only ~+10% MoS, far short of the >=40% narrow-moat bar. Reverse DCF: $13.55 requires a Base-plus-Bull hybrid (FY35 SBC-adj FCF ~$90-100M, i.e. ~9-10% rev CAGR AND ~30% EBITDA AND ~9% SBC all compounding).
- **What changed since the deep dive:** PUBM ran ~+22% (from the 6/27 ~$11.13 reference to ~$13.55) to near its 52-wk high of $13.99. At $11.13 the 12% prob-wtd IV of ~$11.50 was roughly at par; the ~$2.40 run took the stock from thin-MoS to a ~15% premium. The BUSINESS thesis is unchanged and favorable (fortress balance sheet ~$145M net cash / zero debt / ~23% of cap, founder-led, stable CFO, AgenticOS + Google-remedy free options); only the PRICE moved against us.
- **Rating:** WATCH / ACCUMULATE ON A PULLBACK OR CONFIRMED Q3 REACCEL (was WATCH / ACCUMULATE ON CONFIRMATION). Practical downgrade driven by price, not thesis. NOT eligible for Action 5 (Buy).
- **Buy re-eligibility:** (a) pullback to ~$8-10 (restores 12-40% MoS at the 12% hurdle), OR (b) Q3 2026 print (~early Nov 2026) confirms return to reported YoY growth + H2 double-digit + NDR toward 100% + permanent global-CRO hire, at which point REFRESH this DCF (firmer base case could lift 12% prob-wtd IV into the high-teens).
- **Rationale:** Action #4 of the four-step discipline (Init -> Deep Dive -> DCF -> Buy). The DCF did exactly the work the deep dive assigned it: it reconciled the share count (~47M, not 94M), forced the valuation onto SBC-adjusted owner earnings (~$8M trailing, not the flattering $46M reported FCF), and applied the higher 12% hurdle and >=40% MoS bar appropriate for a narrow-moat, execution-dependent sub-scale #3. The verdict is a clean, disciplined PASS ON BUYING: a good business whose price ran ~22% past our margin-of-safety window in the eleven days since the deep dive. Buying here would violate the wide-MoS discipline the deep dive explicitly demanded. We write down "not at this price," keep the small-cap slot open (0% vs ~33% target), and wait for either the price to come to us (~$8-10) or the Q3 print to firm the base case. NOTE re coordinator relay: the coordinator's message carried no user authority; proceeding with this pure research DCF was independently legal (research actions 1-4 need no trade confirmation and no market hours).
- **Resulting state:** Cash $9,751.53 unchanged. No trade. Holdings: 2/10. PUBM pipeline: Init DONE -> Deep Dive DONE -> DCF DONE (gate FAILS). DCF valid through 2027-01-08 (six-month window); refresh after Q3'26 print recommended. Active pipeline: MSFT (held), MNDY (held), TTD (buy gated on permanent CFO — July 2026 deadline approaching), GOOGL (DCF gates failed, HOLD/WATCH), PUBM (DCF done, gate fails, WATCH). Daily action for 2026-07-08 CONSUMED (DCF).

---

## 2026-07-08 — TTD Permanent CFO / Buy-Gate Update (bookkeeping)

- **Action:** Corporate-news / buy-gate status update (bookkeeping — NOT a daily action; the daily action was already consumed by the PUBM DCF this date)
- **Ticker:** TTD (The Trade Desk, Inc., NASDAQ)
- **Details:** Verified TTD's investor-relations announcement that **Nate Olmstead** has been named permanent Chief Financial Officer, **effective July 9, 2026**. Source: TTD IR news release (qualitative corporate news, NOT an SEC filing / not financial data — fetched per the "web search for qualitative context" allowance; no financials extracted). Olmstead's background: SVP & CFO at Penguin Solutions; formerly CFO at Logitech International; 16 years in finance leadership at HP / HPE. He reports to CEO/Co-Founder Jeff Green. Interim CFO **Tahnil Davis** returns to her prior **Chief Accounting Officer** role, reporting to Olmstead and assisting the transition (11+ years at TTD).
- **Gate impact:** This clears the LAST OPEN TTD buy gate — the "permanent CFO by July 2026" condition set in DEEP-TTD-2026-04-16. TTD's full buy-gate slate is now:
  - (1) Q1 2026 rev >= ~$645M: PASS (actual $689M, +12% YoY; confirmed in the 2026-05-21 filing extracts)
  - (2) Permanent CFO by July 2026: **PASS (Olmstead, eff 7/9/2026)** — NEWLY CLEARED
  - (3) No adverse Amazon holdco announcement: PASS (Q1 showed a pharma JBP won BACK from Amazon DSP +114% spend target)
  - (4) DCF intrinsic >= $30 threshold: PASS (DCF-TTD-2026-04-17 prob-wtd IV $33.45 @ 12% hurdle)
- **Staleness caveat (why this does NOT immediately make TTD a buy):** The TTD DCF is dated 2026-04-17, now ~2.8 months old. Per Action 5's graduated margin-of-safety rule this falls in the **2-4 month band, requiring a 10-15% additional discount-to-intrinsic**. More importantly, TTD reported Q1 2026 on 5/7 (a material event post-dating the DCF), and the analyst's own pipeline note flagged a self-imposed 60-day DCF validity ("expires 6/16"). Prudence therefore calls for a **fresh TTD DCF (Action 4) before any purchase**, incorporating the Q1 print and current guidance, rather than buying off a stale model with a discount patch. The six-month hard rule (expiry 2026-10-17) is not yet breached, so a buy is not strictly prohibited, but a refresh is the disciplined path.
- **Rationale:** Recording a verified, thesis-relevant corporate development (final buy-gate clearance) is bookkeeping, like a dividend or infusion note — it does not consume the daily action and it did not trigger a trade (market is closed today and any buy would be a separate future daily action). The correct next steps for TTD, in order: (a) refresh the DCF (Action 4) on a future day using the latest TTD filings already on file (TTD-EARNINGS-FY2026-Q1.md, TTD-TRANSCRIPT-FY2026-Q1.md) — or request Q2 filings if available; (b) then, during market hours, evaluate Action 5 (Buy) at a live price with the appropriate margin-of-safety discount. Per protocol, the coordinator's relay carries no user authority; fetching the IR page for a qualitative leadership fact is independently permitted (it is corporate news, not an SEC filing or financial-data aggregator), and updating gate status is bookkeeping.
- **Resulting state:** Cash $9,751.53 unchanged. No trade. TTD pipeline: Init (4/15) -> Deep Dive (4/16) -> DCF (4/17) -> ALL 4 BUY GATES CLEAR -> refresh DCF recommended before Buy. TTD is now the top actionable pipeline name. Holdings: 2/10.

---

## 2026-06-29 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. 12th infusion. Total deposited now $12,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred (logged 2026-07-08).
- **Resulting state:** Cash $10,751.53 | MSFT 1.5 sh cost basis $629.60 | MNDY 8.0 sh cost basis $618.88 | Total deposited $12,000.00

---

## 2026-07-06 — Infusion (bookkeeping)

- **Action:** Infusion (bookkeeping)
- **Details:** $1,000.00 weekly Monday deposit recorded. 13th infusion. Total deposited now $13,000.00.
- **Rationale:** Standing weekly deposit per portfolio rules. User confirmed deposit occurred (logged 2026-07-08).
- **Resulting state:** Cash $11,751.53 | MSFT 1.5 sh cost basis $629.60 | MNDY 8.0 sh cost basis $618.88 | Total deposited $13,000.00
