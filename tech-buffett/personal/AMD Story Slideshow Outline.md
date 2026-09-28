# AMD — "The Story" Slideshow Outline (YouTube)

Narrative walk-through: history → bull case → bear case → role in AI → base case → the numbers → DCF → valuation.

Source material (all in `personal/`): `DCF-AMD-2026-09-02.txt` ("TAM-reached" model), `DCF-AMD-2026-07-09.txt` (generic-growth model, for the before/after), `AMD-EARNINGS-2026-Q2.md`, `AMD-ADVANCING-AI-2026.md`, `AMD 2025 10-K.txt`, `AMD 2026-Q1 10-Q.txt`, `AMD 2026-Q1 Transcript.txt`. Build slides from the bracketed data points — don't re-derive them. Every dollar figure below traces to those files; the pre-2020 history beats are general-knowledge context and should be sanity-checked before recording.

Price/valuation anchor throughout: **$459.45** (Sept 2, 2026 intraday), ~**$762B** market cap, ~**15x** FY2026E revenue.

---

## PART 1 — THE STORY

### Slide 1 — Title
- **AMD: From Near-Bankruptcy to the AI Arena**
- Subtitle: A 55-year-old chip company got a second life — how much of the AI future is already in the price?
- "As of Sept 2, 2026 · $459.45 · ~$762B market cap"

### Slide 2 — The Setup: What AMD Actually Is
- Fabless semiconductor company — designs chips, TSMC builds them
- Four reporting segments (FY2025 revenue $34,639M):
  - **Data Center** $16,635M — EPYC server CPUs + Instinct AI GPUs
  - **Client** $10,640M — Ryzen PC processors
  - **Gaming** $3,910M — Radeon + game-console chips
  - **Embedded** $3,454M — Xilinx FPGAs / adaptive SoCs
- One line to remember: *Data Center is now the whole thesis; everything else is ballast.*

### Slide 3 — The Near-Death Era (context, ~2014–2015)
- Stock traded near ~$2; balance sheet stretched, losing share to Intel on CPUs and NVIDIA on GPUs
- Lisa Su takes over as CEO (Oct 2014) with a simple plan: bet everything on a from-scratch high-performance CPU core
- The bet was existential — there was no "plan B" year

### Slide 4 — The Turnaround Engine: "Zen"
- 2017: the "Zen" architecture ships as Ryzen (PC) and EPYC (server)
- Year after year of share gains against an Intel stuck on its manufacturing problems
- Result over the following years: consumer credibility back, then a genuine server-CPU franchise

### Slide 5 — Buying the Second Act
- Xilinx acquisition (closed early 2022, ~$49B stock deal) → the Embedded segment + FPGA/adaptive compute
- Pensando (2022) → data-center networking / DPUs
- Downside baked in for years: ~**$2.3B/yr** of acquisition-intangible amortization sitting inside GAAP COGS/opex — a drag that mechanically *runs off* over the next decade

### Slide 6 — Where the Story Stands Today (Q2 2026)
- Revenue **$11,536M, +50% YoY** — a record quarter
- GAAP gross margin **54%**, GAAP operating margin **17.3%** (was just **7.4%** company-wide in FY2024)
- GAAP EPS **$1.38** / non-GAAP EPS **$1.66**
- Free cash flow **$1,558M** (op cash flow $2,366M − capex $808M)
- Net **cash** ~**$9,885M** ($13,111M cash & ST investments vs $3,226M debt) — zero balance-sheet risk
- The turnaround is *done*. The next chapter is the AI arena.

---

## PART 2 — THE BULL CASE

### Slide 7 — Bull Case in One Slide
- AMD is now a *credible #2* in AI accelerators, with a non-AI base that cushions the fall and a net-cash balance sheet
- Three pillars:
  1. The Data Center inflection is **already reported**, not promised
  2. **~14 GW** of multi-year customer commitments give revenue visibility that didn't exist 12 months ago
  3. A second, independent growth vector — EPYC server CPUs — is still compounding

### Slide 8 — Pillar 1: The Inflection Is in the Numbers
- Data Center Q2 2026 revenue **$6,718M, +107% YoY** — 58.2% of the company
- Data Center segment operating income **+$2,103M** (31.3% margin) — swung from a **−$155M loss** a year earlier
- Company GAAP operating margin: **7.4% (FY24) → 17.3% (Q2'26)**
- Q3 2026 guide: **~$13.0B ±$0.3B, +41% YoY**, non-GAAP gross margin ~56% — the ramp is visibly accelerating into H2

### Slide 9 — Pillar 2: Committed Capacity
- Multi-gigawatt, multi-generation commitments cited at Advancing AI 2026:
  - **Meta** — up to 6 GW of Instinct GPUs
  - **OpenAI** — up to 6 GW
  - **Anthropic** — up to 2 GW of "Helios" rack-scale systems
  - **Oracle** — 50,000-GPU supercluster
  - **~14 GW total** of committed AI compute
- MI450 / Helios rack-scale platform ramping **H2 2026** — the product these commitments hang on

### Slide 10 — Pillar 3: EPYC Is a Second Engine
- Server-CPU share still compounding against Intel
- Management raised the **server CPU TAM to ~$200–220B by 2030** (from ~$60B a year earlier)
- A real (if hard-to-size) slice of that CPU demand is itself AI-driven — head/host nodes, inference orchestration, agentic workloads ("AI-attached EPYC")

### Slide 11 — What the Bull Case Pays Off To
- DCF Bull case: 2030E revenue **$250B**, 2036E revenue **$567B** (larger than NVIDIA's FY2026 revenue)
- GAAP operating margin scales toward **~31%** as acquisition amortization runs off and mix shifts to Data Center
- Intrinsic value **~$824/share** → **+79% upside** from $459 (price is 0.56x the bull case)
- Translation: this is a genuine *"AMD becomes a top-3 global company"* scenario

---

## PART 3 — THE BEAR CASE

### Slide 12 — Bear Case in One Slide
- Even if the AI money shows up, AMD may not *keep* much of it
- The real competition for AMD's share isn't only NVIDIA — it's its own biggest customers' in-house chips
- And at $459, the stock is priced for a good outcome already

### Slide 13 — Bear Point 1: The Custom-Silicon Squeeze
- AMD's largest potential customers — Google, Amazon, Microsoft, Meta, OpenAI — are all building their own accelerators (TPU, Trainium, MAIA, MTIA, an OpenAI in-house part)
- The merchant "everything that isn't NVIDIA" bucket AMD competes for may be structurally *smaller* than the headline TAM implies
- Bear case: Instinct share stalls at **~3.3%** of the accelerator pool (vs ~5.5% base / ~8.8% bull) as ROCm never reaches CUDA parity

### Slide 14 — Bear Point 2: The Dilution Overhang
- Per public reporting, AMD issued warrants to **both** Meta (Feb 2026) and OpenAI (Oct 2025) — up to **~160M shares each**, ~$0.01 strike, vesting on the customers' own purchase milestones + AMD's stock price
- Combined **~320M shares ≈ 16% potential dilution**, not in the 1,659M share count
- Effect on the DCF if both vest in full: Base **~$306 → ~$257**, Bull **~$824 → ~$691**, probability-weighted **~$371 → ~$312**
- It also hands two major customers pricing leverage over AMD

### Slide 15 — Bear Point 3: Near-Term Margin & Cyclical Drags
- MI450/Helios flagged as **below corporate-average gross margin** during the H2 2026 ramp
- Memory/HBM cost inflation — management flagged H2 2026 client/gaming demand risk specifically from rising DRAM/HBM prices
- Client + Gaming (~33% of FY2026E revenue) are cyclical PC/console businesses — Gaming was **−31% YoY** in Q2 2026
- China: Q1 2026 data-center AI revenue *fell* sequentially on "the China transition"; FY2025 carried ~$440M of MI308 export-control charges

### Slide 16 — Bear Point 4: Valuation Leaves No Room
- At $459 (~$762B, ~15x FY2026E revenue) the stock trades at **~1.5x** the DCF base case and **~1.24x** the probability-weighted value
- Bear case intrinsic value: **~$90/share** (−80%)
- A stock priced near a bullish fair value reacts violently to any data point that isn't bullish

---

## PART 4 — AMD'S ROLE IN AI

### Slide 17 — Where AMD Sits in the AI Stack
- **Not** a pure-play AI-accelerator company — an *AI-levered* company
- In the "TAM-reached" 2030 base case, **~30–40% of revenue is still NOT AI-accelerator**: server CPU (part traditional), PC CPUs, consoles, embedded/FPGA
- That non-AI base both cushions the downside and dilutes the upside vs a pure-play like NVIDIA

### Slide 18 — The Pitch: Rack-Scale, Not Just a Chip
- Helios = GPU (Instinct MI450) + CPU (EPYC) + networking (Pensando), co-engineered down to named customer deployments
- Positioned as the credible *second source* to NVIDIA's Rubin-generation rack systems — hyperscalers want a viable #2
- More points of failure than a standalone chip launch, but also a much bigger prize per win

### Slide 19 — The TAM AMD Is Aiming At (Lisa Su, Advancing AI 2026)
| Market | A year ago | New 2030 call | Implied growth |
|---|---|---|---|
| Data-center AI **accelerator** TAM | ~$500B by 2028 | **~$1.4T by 2030** | >45% CAGR |
| **Server CPU** TAM | ~$60B | **~$200–220B by 2030** | >50% CAGR |
| Combined HPC + AI compute | — | **~$2T by 2030** | ~40% CAGR |
- Not disclosed at the event: no revenue targets, no market-share goal, no gross-margin target, no dated EPS target

### Slide 20 — The Honest Caveat on That TAM
- A **$1.4T** accelerator TAM in 2030 is ~3.5–4x the entire 2026 AI-silicon market run-rate
- Requires AI-infrastructure capex to compound at **~45%/yr for four more years with no digestion pause** — no hardware cycle in history has done that
- The DCF *adopts* this as a stated premise; it does **not** endorse it. Strip 30% off the TAM and the base case falls toward ~$200/share.
- **This assumption does most of the work in every number that follows.**

---

## PART 5 — THE BASE CASE

### Slide 21 — Base Case: The Central Story
- The $1.4T TAM largely appears, but AMD holds only **~5.5%** accelerator share (~$77B in 2030) — NVIDIA's CUDA moat + hyperscaler custom silicon absorb the rest
- EPYC reaches ~41.5% of a *haircut* $165B server-CPU TAM (~$68.5B)
- Helios execution is real but bumpier than guided; client/gaming grow modestly off a memory-cost-pressured 2026
- GAAP operating margin plateaus at **25%**

### Slide 22 — Base Case: The Growth Path
- FY2026E revenue **$49,500M** (+42.9% YoY) — bottom-up: H1 actual $21,789M + Q3 guide ~$13.0B + Q4 estimate ~$14.7B
- 2030E revenue **$170B** · 2036E revenue **$356B** — roughly **7.2x** FY2026E inside a decade
- Even this "central" case assumes an extraordinary outcome — and still lands **~33% below** today's price

---

## PART 6 — THE NUMBERS

### Slide 23 — Q2 2026 Scorecard
| Metric | GAAP | Non-GAAP |
|---|---|---|
| Revenue | $11,536M (+50% YoY) | — |
| Gross margin | 54% | 56% |
| Operating income | $1,990M (17.3%) | $3,094M (26.8%) |
| Net income | $2,297M | $2,760M |
| Diluted EPS | $1.38 | $1.66 |
- Operating cash flow $2,366M · Capex $808M · **FCF $1,558M**
- Cash + ST investments $13,111M · Total debt $3,226M · **Net cash ~$9,885M**
- Diluted shares 1,659M (excludes the ~320M Meta + OpenAI warrant shares)

### Slide 24 — Segment Picture: FY2025 → Q2 2026
| Segment | FY2025 rev | Q2'26 rev | Q2'26 mix | YoY |
|---|---|---|---|---|
| Data Center | $16,635M | $6,718M | 58.2% | **+107%** |
| Client | $10,640M | $3,062M | 26.5% | +23% |
| Gaming | $3,910M | $779M | 6.8% | −31% |
| Embedded | $3,454M | $977M | 8.5% | +19% |
| **Total** | **$34,639M** | **$11,536M** | | **+50%** |
- Data Center segment operating margin ~31.3% — swung from a **−$155M loss** in Q2'25

### Slide 25 — The 2030 Fork: It's All About Accelerator Share
(Accelerator TAM fixed at **$1,400B**; AMD's *share* is the variable)
| | BEAR | BASE | BULL |
|---|---|---|---|
| AMD Instinct share of $1.4T | 3.3% | 5.5% | 8.8% |
| Instinct revenue 2030 | $46B | $77B | $123B |
| EPYC revenue 2030 | $46B | $68.5B | $97B |
| **Total revenue 2030E** | **$112B** | **$170B** | **$250B** |
| **Total revenue 2036E** | **$197B** | **$356B** | **$567B** |
- 3.3% vs 8.8% share is a **~$77B revenue swing in 2030 alone** — bigger than AMD's entire Data Center segment today

---

## PART 7 — THE DCF

### Slide 26 — How the Model Is Built
- 10-year explicit forecast (2027E–2036E) off the bottom-up FY2026E anchor ($49.5B)
- Discounts **SBC-adjusted FCF** = NOPAT + D&A − CapEx − stock-based comp; NOPAT at a 15% tax rate
- Adds **net cash** of $9,885M to enterprise value
- Each scenario carries its *own* WACC / terminal growth / exit multiple — a decade of flawless execution implies lower residual risk
- Fabless model = capex tops out near ~2% of revenue even in the bull case (a structural FCF advantage — but AMD does *not* capture the datacenter-construction economics its customers do)

### Slide 27 — The Three Scenarios
| Scenario | WACC | TGR | Exit | 2036E revenue | 2036E SBC-adj FCF | **IV / share** |
|---|---|---|---|---|---|---|
| **Bull** | 10.0% | 3.5% | 26x | $567,000M | $124,729M | **$823.86** |
| **Base** | 11.5% | 3.0% | 20x | $356,000M | $60,682M | **$306.22** |
| **Bear** | 13.5% | 2.0% | 14x | $197,000M | $23,209M | **$90.19** |
- Probability-weighted (25% bull / 45% base / 30% bear): **$370.82**
- Simple average of the three: **$406.76**

### Slide 28 — Base-Case DCF Bridge
- PV of explicit 2027–2036 FCFs: **$170,001M**
- + PV of terminal value (avg of perpetuity-growth and 20x exit): **$328,139M**
- = Enterprise value **$498,140M** + net cash $9,885M = **Equity value $508,025M**
- ÷ 1,659M shares = **$306.22 / share**
- For scale: that ~$508B implied equity value is ~**34% below** AMD's ~$762B market cap today

### Slide 29 — Sensitivity: The Base Case Can't Reach $459
- Base-case IV across a full WACC × terminal-growth grid (20x exit): **every cell** sits below the $459 price
- Most generous corner — 9.5% WACC / 4.0% TGR — is **$407.93**, still ~11% under the market
- To justify $459 you need **bull-case operating assumptions**, not just a friendlier discount rate

---

## PART 8 — VALUATION & TAKEAWAY

### Slide 30 — Where $459 Sits
| Reference | Value | vs. $459.45 |
|---|---|---|
| Bull case | $823.86 | **+79%** |
| Simple average | $406.76 | −11% |
| Probability-weighted | $370.82 | −19% |
| Base case | $306.22 | **−33%** |
| Bear case | $90.19 | −80% |
| Fully diluted for warrants | Base ~$257 / Bull ~$691 / prob-wtd ~$312 | — |
- The market is paying today for: the $1.4T TAM to *substantially* materialize **AND** AMD to hold mid-single-digit accelerator share **AND** margins to reach the mid-20s

### Slide 31 — The Before/After (why the model moved)
- **July 9, 2026 model** (generic top-down growth): Base **$167** / Bull **$357** / prob-wtd **$181** — price then $517
- **Sept 2, 2026 model** (adopts Lisa Su's $1.4T TAM + strong Q2): Base **$306** / Bull **$824** / prob-wtd **$371** — price $459
- ~80% of the ~2x lift is the **TAM assumption swap**, ~20% is two quarters of real results — *not* a changed view of the business
- Same conclusion both times: good business, price not offering a margin of safety — the gap is just narrower now, and the bull case finally clears the price

### Slide 32 — Bull vs. Bear, Side by Side
| The bull says | The bear says |
|---|---|
| Inflection already reported: DC +107%, segment margin 31% | Custom ASICs, not NVIDIA, cap AMD's share at ~3% |
| ~14 GW committed across Meta/OpenAI/Anthropic/Oracle | ~320M warrant shares = ~16% dilution to those same customers |
| EPYC a second engine; CPU TAM raised to $200B+ | MI450 ramp is margin-dilutive; client/gaming cyclical + HBM cost |
| Bull DCF ~$824 (+79%) | Base ~$306 (−33%), priced at 1.5x fair value |

### Slide 33 — Bottom Line
- Business quality: **MODERATE-HIGH** — the turnaround is real and the AI inflection is in the reported numbers
- Valuation at $459: **LOW conviction** — you're paying fair value for a great outcome and hoping for a spectacular one
- Gets genuinely interesting on this framework in the **low-$300s** (base-case value); high-conviction only in the **low-$200s** (where even a haircut TAM works)
- What would change the call: a pullback toward ~$300, **or** 2–3 quarters of clean Helios execution that justifies a sub-10% bull discount rate and shifts weight from bear to base

### Slide 34 — Disclosures
- Personal research, not investment advice. Standalone analysis outside the tech-buffett Init → Deep Dive → DCF pipeline; does **not** qualify AMD for the portfolio.
- The valuation is **conditional** on Lisa Su's Advancing AI 2026 TAM figures being reached — figures this analysis does not independently endorse.
- Instinct-vs-EPYC and "AI-attached vs traditional" splits are analyst allocations, not company disclosure.
- Q2 2026 financials and TAM figures pulled from AMD IR / newsroom / secondary financial news; FY2026E is a bottom-up estimate, not a company or consensus figure.
- Meta + OpenAI warrant terms not verified against primary filings.

---

**Note:** All financials and DCF outputs come straight from the files listed at the top — no new figures were invented for this outline. Slides 3–5 (pre-2020 history) are general-knowledge framing; verify specific dates/dollar amounts before recording. The deck intentionally keeps the bear case and the TAM caveat (Slides 12–16, 20) prominent — a one-sided story is less credible and less useful.
