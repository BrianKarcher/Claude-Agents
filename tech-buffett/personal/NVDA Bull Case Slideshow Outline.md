# NVDA Bull Case — Slideshow Outline

Source material: `DCF-NVDA-2026-08-27.txt`, `NVDA-EARNINGS-FY2027-Q2.md`, `NVDA-EARNINGS-FY2027-Q1.md`, `NVDA-10K-FY2026.md`, `NVDA GTC 2026 Summary.md` (all in this folder). This is an outline for a personal deck — content per slide, not full prose. Build slides directly from the bracketed data points; don't re-derive them.

---

### Slide 1 — Title
- NVIDIA (NVDA): The Bull Case
- Subtitle: AI infrastructure's dominant platform, priced for growth but not for its own guidance
- Date / "as of Aug 27, 2026" price ($227.98) and market cap (~$5.54T)

### Slide 2 — Thesis in One Slide
- One-sentence thesis: NVIDIA doesn't just supply the AI buildout, it effectively *is* the AI buildout — and the market is pricing continued execution, not the acceleration management itself is guiding to.
- 3 supporting pillars (expand each in later sections):
  1. Growth is supply-constrained, not demand-constrained
  2. Moat is widening, not narrowing (CUDA + full-stack + agentic inference + robotics)
  3. Valuation: Bull case DCF ($843/share) still sits below where current price would require flawless-forever execution — i.e., there's room between "priced for perfection" and "priced for the Bull case"

### Slide 3 — What NVIDIA Actually Sells Today
- Two-segment structure (as of Q1 FY2027): **Data Center** (~92.5% of revenue) and **Edge Computing** (gaming, pro-viz, automotive, robotics)
- Q2 FY2027 snapshot: $96.2B revenue, +106% YoY, +18% QoQ, beat guide by ~5.7%
- Customer mix: hyperscalers ~$49B, ACIE (enterprise/NeoCloud/sovereign AI) ~$40B and growing ~100% annualized — genuine diversification signal, not just "the Big 4 hyperscalers"

### Slide 4 — The Core Bull Argument: Supply, Not Demand, Is the Constraint
- Direct management quote (Q2 FY2027 call): "supply chain is broadly constrained... supply sufficient to support approximately 70% growth, while demand exceeds that level"
- Why this matters for a bull case: near-term results are gated by TSMC/HBM packaging capacity, not by convincing anyone to buy — a fundamentally different (and more favorable) risk profile than typical demand-driven hardware cycles
- Q3 FY2027 guide: $108.0B ±2% (+12.3% QoQ) — guidance itself implies acceleration, not deceleration, off an already enormous base

### Slide 5 — The Monetization Ladder
- Management's own framing: revenue per gigawatt of deployed AI compute
  - Hopper: ~$18B/GW
  - Blackwell: ~$25B/GW
  - Vera Rubin: ~$40B/GW
- Bull case doesn't require unit growth alone — each platform generation extracts more $ per unit of power/compute deployed
- Tie to GTC 2026: Vera Rubin (H2 2026) claims ~10x perf/watt over Blackwell and ~10x lower inference token cost — the mechanism behind the ladder stepping up

### Slide 6 — Silicon Roadmap: Multi-Generation Visibility
- Three-generation roadmap previewed at GTC 2026: Vera Rubin (2026) → Rubin Ultra w/ Kyber (2027) → Feynman (2028)
- $1 trillion in cumulative Blackwell + Vera Rubin orders through 2027 (management's own figure, GTC 2026)
- Why bulls care: multi-year revenue visibility most semiconductor companies never get, reducing (not eliminating) the "one bad quarter" tail risk

### Slide 7 — Moat Extension #1: Groq / Agentic Inference
- ~$20B asset-purchase acquisition of Groq (closed Dec 2025); Groq 3 LPU unveiled at GTC 2026
- LPX rack (256 LPUs) designed to sit beside Vera Rubin rack-scale systems — targets low-latency, large-context agentic inference workloads
- Bull read: pre-empts the "NVIDIA only wins training, loses inference to specialized/custom silicon" bear argument by buying the leading inference-specialist architecture outright

### Slide 8 — Moat Extension #2: Software / Agentic AI Stack
- NVIDIA Agent Toolkit (NemoClaw runtime, AI-Q blueprint, Nemotron open models), OpenShell security runtime
- Dynamo 1.0 inference software — claimed up to 7x inference performance improvement on Blackwell in NVIDIA benchmarks
- CUDA-X libraries exposed as callable "skills" for AI agents — extends the CUDA lock-in from raw compute into the agent-orchestration layer itself

### Slide 9 — Moat Extension #3: Physical AI & Robotics (the optionality nobody's modeling)
- Cosmos 3 (world foundation model), Isaac GR00T N1.6 (vision-language-action model for humanoids)
- FANUC + ABB (~1/3 of global industrial robot production) integrating Isaac
- Uber autonomous-vehicle partnership launching in LA
- Bull framing: this is a call option not in the base DCF — if physical AI scales even modestly, it's incremental upside on top of the Data Center thesis, not a substitute for it

### Slide 10 — Enterprise Diversification Beyond Hyperscalers
- GTC 2026 partner roster: Cadence, Dassault Systèmes, PTC, Siemens, Synopsys (EDA/design tools) bringing Omniverse/CUDA-X into FANUC, HD Hyundai, Honda, JLR, Mercedes-Benz, Samsung, SK hynix, TSMC, PepsiCo workflows
- Ties directly to the ACIE revenue line (~half of total revenue now, +138% YoY) — the "4 hyperscalers" concentration bear case is measurably less true than a year ago

### Slide 11 — Financial Profile: Still a Software-Like Margin Structure at Hardware Scale
- Q2 FY2027: 75.0% gross margin, 66.2% operating margin, $96.2B quarterly revenue
- FY2026 capex was just $6.0B on $215.9B revenue (2.8%) — structurally capital-light vs. the hyperscaler customers buying its chips
- Net cash position: $23.2B (post the H1 FY2027 debt increase — see caveats slide) plus a separately-held $42.8B of strategic AI-ecosystem equity stakes (not even in the DCF's equity bridge)

### Slide 12 — DCF Bull Case: Assumptions
- 10-year explicit forecast, FY2028E–FY2037E, off a bottom-up FY2027E anchor ($405.8B, built from 2 actual quarters + 1 guided quarter + 1 estimated quarter)
- Bull case revenue growth: 65% (FY28E) decelerating to 9% (FY37E) — note this *approaches but does not exceed* management's own ~70% supply-ceiling framing
- Bull case operating margin: 62% (FY28E) → 57% (FY37E) — still assumes real memory-cost and competitive pressure, just less than Base/Bear
- WACC 9.0% / TGR 3.5% / exit multiple 28x SBC-adjusted FCF
- WACC rationale: reflects a world where the AI buildout proves structurally durable and NVIDIA's ACIE diversification de-risks the business toward an MSFT-like (10% WACC) risk profile

### Slide 13 — DCF Bull Case: Output
- FY2037E revenue: ~$3.3T | FY2037E SBC-adjusted FCF: ~$1.52T
- Intrinsic value per share: **~$843**
- vs. current price $227.98 → implied upside +270% (price is 0.27x Bull-case IV)
- Compare to Base case ($330/share, +45% upside) and Bear case ($83/share, -64%) for context — Bull is the top of a wide but not unbounded range

### Slide 14 — Sensitivity: Even Conservative Corners Clear the Current Price
- WACC × TGR grid (Base case, 22x exit held constant): current $227.98 price sits **below every cell**, from the most conservative corner (12.5% WACC / 2.0% TGR → $265/share) to the most generous (8.5% WACC / 4.0% TGR → $450/share)
- Exit-multiple sensitivity (10.5% WACC / 3.0% TGR): ranges $283–$365/share across 14x–28x
- Framing for the slide: the bull case isn't "you have to believe extreme numbers" — the *base* case alone already implies meaningful upside; the bull case is what happens if execution tracks management's own stated ceiling

### Slide 15 — Why the Market Might Still Be Underpricing This
- Beat-and-raise pattern: beat Q2 guide by ~5.7%, guided Q3 to *accelerate* QoQ (+12.3%) off an already enormous base
- "Sell-the-news" stock behavior at GTC 2026 (rallied ~4% intraday, closed +1.65%) suggests the market treats even major structural announcements skeptically — a possible source of persistent mispricing if the announcements prove out
- Historical pattern: NVDA has now beaten its own guide multiple consecutive quarters — probability-weighting in the DCF (30% Bull / 50% Base / 20% Bear) reflects this track record more than AMD's comparable model does (25/45/30)

### Slide 16 — Known Bear Points, and the Bull Rebuttal
(One slide, two columns — anticipate the pushback rather than ignore it)
- "It's already too big to keep compounding" → per-GW monetization ladder (Slide 5) means growth doesn't require proportional unit growth
- "Hyperscaler concentration" → ACIE now ~half of revenue, +138% YoY (Slide 10)
- "Competitors are catching up" → Groq acquisition + CUDA-X agent lock-in (Slides 7–8); AMD's own Bull case tops out an order of magnitude below NVDA's Base case
- "New $33B debt load is a red flag" → small effect on DCF (~$1/share) but a real data point to watch — see next slide

### Slide 17 — Honest Caveats (keep even in a bull deck)
- FCF conversion fell to ~36% in Q2 FY2027 (inventory build + supplier prepayments for Blackwell/Rubin) — a real near-term cash dynamic, not yet a red flag but worth tracking
- Total debt jumped from $8.5B to $33.4B in H1 FY2027 — new, unexplained-in-detail leverage
- Gross margin guided down from 75.0% (Q2) toward a 71–72% floor (Q4 FY2027) on memory/HBM cost inflation — industry-wide, but real
- Terminal-value risk: Bull case implies FY2037E revenue of ~$3.3T — a "law of large numbers" bet that dominates every other assumption in the model

### Slide 18 — Catalysts / What to Watch Next
- Vera Rubin data center availability (H2 2026) — first real read on the 10x perf/watt and monetization-ladder claims
- FCF conversion recovery toward historical 90%+ norms (signals inventory build was tactical, not demand-driven)
- Continued ACIE growth at scale (proof concentration risk is structurally declining, not just this quarter)
- Any update on use of proceeds from the new $33.4B in debt
- Next GTC (regional events through the year) and Q3 FY2027 earnings (next print)

### Slide 19 — Summary / Takeaway
- Base case already implies ~31% margin of safety at current price; Bull case ($843) implies the stock could more than triple if NVIDIA merely executes to its own stated ceiling
- This is a highly asymmetric, high-quality growth bet — not a classic "cheap on today's numbers" value case
- Conviction: business quality — HIGH. Valuation call — MODERATE (terminal-value sensitivity is large; see caveats)

### Slide 20 — Appendix / Backup
- Full scenario table (Bull/Base/Bear WACC, TGR, exit multiple, IV/share)
- Full sensitivity grids (Section 6 of the DCF)
- Source list / disclosures (per the DCF's Disclosures section — personal research only, not investment advice, not a tech-buffett portfolio qualifier)

---

**Note:** This outline is built entirely from the Bull-case assumptions and figures already in `DCF-NVDA-2026-08-27.txt` and `NVDA GTC 2026 Summary.md` — no new figures were invented for this outline. It intentionally includes Slides 16–17 (bear pushback + caveats) because a one-sided bull deck is less useful and less credible than one that shows its work against the counterargument.
