# TTD Deep Dive — Outline

Source material on hand: `TTD 2026-Q2 10-Q Extract.md`, `TTD 2026-Q2 Transcript Extract.md`, `research/filings/TTD-EARNINGS-FY2026-Q1.md`, `research/filings/TTD-TRANSCRIPT-FY2026-Q1.md`. Written as a first read — no assumed familiarity with prior TTD research.

---

## 0. Executive Summary
- What TTD is, in one line (open-internet programmatic ad-buying platform)
- Headline financial snapshot as of the most recent print: Q2 2026 revenue $715M (+3% YoY), Q3 guide implies a ~12% YoY *decline* — first guided revenue decline in company history
- Current market price and implied valuation (P/FCF, EV/EBITDA) — need current quote
- One-paragraph thesis-in-one-line: is this a structurally advantaged platform hitting a cyclical air pocket, or a business whose growth story has genuinely broken
- Rating framework placeholder (Watch / Accumulate / Pass) — pending DCF

## 1. Ad-Tech 101 — Primer
A first-time reader needs this before anything else in the deep dive will land. Keep it short and concrete.
- **Programmatic advertising in one paragraph:** ad impressions are bought and sold via automated real-time auctions (real-time bidding, "RTB") instead of humans negotiating insertion orders. Each time a webpage/app/CTV screen loads, an ad slot is auctioned off in milliseconds to the highest qualified bidder.
- **The two-sided network:**
  - *Demand side:* advertisers and their agencies, who want to buy audience attention
  - *Supply side:* publishers and platforms (websites, apps, streaming services), who have ad inventory to sell
  - The market only works if both sides are liquid — enough advertiser demand to make inventory valuable, enough quality inventory to make the platform worth advertisers' budget. This chicken-and-egg dynamic is why scale is a moat (more of one side attracts more of the other)
- **The core roles/acronyms:**
  - **DSP (Demand-Side Platform):** software advertisers/agencies use to bid on inventory across many publishers at once, using data and algorithms to decide what to bid and on whom. TTD, Google DV360, and Amazon DSP are all DSPs
  - **SSP (Supply-Side Platform):** the publisher-side counterpart — helps publishers auction their inventory to many DSPs at once (e.g., Magnite, PubMatic, Google's AdX)
  - **Ad exchange:** the marketplace/auction mechanism connecting DSPs and SSPs
  - **Identity/data layer:** how a DSP knows who it's bidding on — cookies historically, now first-party data, clean rooms, and identity graphs (TTD's UID2 is its open-alternative identity standard)
- **Where TTD sits:** TTD is a pure-play, independent DSP. It only operates on the demand side, representing advertisers/agencies as their buying agent — it does not own publisher inventory, a search engine, a marketplace, or a social platform. This is the basis of its "we only work for the buy side, we have no conflict of interest" positioning
- **Walled garden vs. open internet — the central distinction for this whole deep dive:**
  - *Walled gardens* (Google Search/YouTube, Meta, Amazon owned-and-operated, TikTok) own both the demand tooling *and* the supply (their own inventory), and often the exchange connecting them. An advertiser buying "Google ads" is buying inventory Google itself owns, priced and matched by Google's own systems, with limited external auditability
  - The *open internet* is every other umbrella of premium inventory — independent publishers, CTV apps outside the big platforms, audio, open web — that isn't owned by a single vertically integrated company. It needs independent, neutral intermediaries (DSPs like TTD, SSPs) to connect fragmented supply with demand
  - **Why this distinction matters competitively:** a walled garden has a structural incentive to favor its own owned-and-operated inventory when it's also the one deciding the auction outcome (self-preferencing) — this is the core of the DOJ's antitrust case against Google's ad stack. TTD, having no owned inventory to favor, can credibly claim to always pick the best placement for the advertiser's outcome. This "neutral fiduciary" positioning is TTD's central competitive/moat argument and shows up throughout Sections 4 and 5 below
- **How this maps onto TTD's competitors specifically:**
  - *Google:* walled garden (Search, YouTube) + also runs DV360 (a DSP, like TTD) + also runs AdX (an exchange) — vertically integrated across all three layers, which is both its advantage (control, data) and its antitrust exposure (self-preferencing)
  - *Amazon:* walled garden (retail site, Prime Video) + Amazon DSP — same structural conflict-of-interest question, plus first-party shopper data as a unique asset no independent DSP can replicate
  - *TTD:* demand-side only, no owned inventory — must win by being the best/most trusted buying tool for the open internet, not by controlling supply

## 2. Unit Economics — What TTD Actually Sells
- The "toll road" model: platform fee on gross advertiser spend, not owned media inventory
- Revenue = gross spend x take rate; back into implied gross spend from reported revenue
- Take rate stability: management describes it as in a "narrow band for 10 years" (per Q2 call) — test this claim
- Contribution margin / operating leverage at the account level
- Cost structure walk: platform operations (now ~26% of revenue, up from ~22% — flag the cloud-to-owned-datacenter transition as a driver), sales & marketing, tech & development, G&A
- Adjusted EBITDA bridge and margin trend (34% in Q2 2026, down ~500bps YoY but up sequentially from Q1's 30%)
- SBC as a real economic cost — build a reported-FCF vs FCF-less-SBC framework; note SBC as % of revenue is actually improving YoY (15.3% vs 18.6%)
- Why the business doesn't commoditize easily (network effects: bid data -> AI decisioning -> outcomes -> more advertisers; publisher integrations; UID2 identity layer)

## 3. Total Addressable Market — 10-Year View
- Global digital ad market size and growth trajectory
- Programmatic share of that market
- Open-internet (non-walled-garden) share — TTD's actual hunting ground, since Google/Meta/TikTok/Amazon O&O capture the majority of programmatic
- CTV as the specific growth engine within open-internet; TTD's CTV mix (~50%+ of revenue per channel mix data)
- Retail media as a fast-growing adjacent category and TTD's position as neutral intermediary
- TTD's estimated penetration of its addressable TAM — is there still runway independent of the current growth wobble

## 4. Competitive Dynamics
- The three-horse race: Google DV360, Amazon DSP, The Trade Desk — market share snapshot
- Amazon DSP's structural advantages (first-party retail data, Prime Video/Netflix/Spotify inventory, cross-subsidy from AWS/Retail) vs structural disadvantages (agency trust deficit competing with brands, walled architecture, lack of log-level transparency, opaque take rate)
- Google DV360 and the DOJ ad-tech antitrust remedy process — potential tailwind if forced divestiture occurs
- Meta/TikTok as budget competitors rather than direct DSP competitors
- Net assessment: where does TTD retain durable share vs where is it structurally exposed

## 5. The Growth Deceleration — Bear Case Teardown
This is the core section given where the stock's narrative currently sits.
- **The data:** revenue growth trajectory quarter by quarter through Q2 2026, culminating in the Q3 guide implying a ~12% YoY decline
- **Management's own framing:** "below our expectations and below the standard we hold ourselves to" — explicit self-criticism, unusual for this management team
- **Two causes management cites:**
  1. Macro pressure concentrated in CPG and Auto (~25% of business combined) — tariffs, oil prices, bifurcated consumer
  2. Self-acknowledged execution shortfalls — being addressed via a wave of new senior leadership hires
- **What management would NOT do when pressed:** quantify the macro-vs-execution split directly (Helfstein exchange on the Q2 call) — treat this non-answer as a signal to weigh
- **Reduced visibility:** CFO explicitly flagged reduced forward visibility vs recent history; no full-year outlook or updated margin framework given ("stay tuned")
- **Competitive erosion angle:** how much of the "handful of large CPG/Auto accounts" story could be Amazon DSP share loss described without naming it — test against any available share data
- **Litigation overhang:** securities class action (motion to dismiss denied 3/17/26, trial set May 2028) and Nevada reincorporation litigation — multi-year distraction risk, not fatal but real
- Assign rough weights/probabilities to each contributing factor, similar to a structural-vs-cyclical decomposition

## 6. Leadership & Organizational Reset
- CEO/Founder Jeff Green — track record, communication style, dual-class share structure
- CFO: Nate Olmstead, permanent as of this filing (signed the Q2 10-Q), ~1 month into the seat during a guided-down quarter — assess as a fresh-start positive vs a risk of leading through the worst print in company history with no tenure
- New leadership wave: COO Vivek Kundra, Chief Commercial Officer Kristi Argyilan (ex-Uber advertising, veteran retail-media builder), Chief Business Development Officer Ron Lamprecht (ex-Amazon, held a broader-than-advertising role there), CMO Sarah Gavin, VP Client Strategy & Growth Vinny Rinaldi (ex-Hershey's, vocal critic of "cheap reach" media buying) — assess whether this reads as a credible infusion of large-company operating discipline or a signal of deeper organizational dysfunction; note Green's own framing on the Q2 call ("I'm nervous about leaving somebody out") signals this is a large, still-growing wave, not just these six names
- Board changes: Drew Vollero newly appointed to the Board of Directors (disclosed on the Q1 2026 call); Green references additional unnamed "amazing industry leaders" added to the board on the Q2 call — confirm identities via proxy/8-K before writing the full deep dive, and assess whether board refresh is aimed at governance credibility ahead of the pending securities class action / Nevada reincorporation litigation (Section 4)
- Capital allocation track record: buyback pace ($78M in Q2, $269M authorization remaining after a $350M Feb 2026 addition), diluted share count down 5.2% YoY, net cash position $1.485B and growing despite repurchases, no debt
- Grade management on the honesty/transparency of this quarter's communication specifically

## 7. Bull Case / What's Still Working
- Joint Business Plans (JBPs): 217 clients, +38% YoY, revenue growing 6x faster than company average — assess whether this is genuinely incremental or an accretive mix shift masking a shrinking base
- Top-100 accounts: majority still growing double digits
- Sub-top-500 advertisers: +50% YoY YTD — "green shoots" narrative
- International: EMEA/APAC ~+30% YTD, China >100% YTD (still only ~17% of total revenue — assess how much this can realistically offset US deceleration at current scale)
- Retail media: partner retailers now >80% of US retail sales, renewed Walmart partnership
- Product roadmap: measurement framework (alpha), Audience Unlimited (open beta), Zuma UX upgrade, Enterprise Kokai — assess as genuine differentiation or standard roadmap noise
- Balance sheet optionality: $1.485B net cash, no debt, room to accelerate buybacks at a depressed price
- Long-horizon catalysts: Google antitrust remedy, UID2 as identity standard, CTV secular growth through 2030

## 8. Scenarios — 5-Year Price Path
- Build bear/base/bull table: 2026-2030 revenue CAGR, exit-year FCF margin, exit multiple, implied equity value, implied 5-year IRR at current price
- Explicitly anchor the bear case on Q3 guide extending into Q4/2027 (i.e., the decline is not a one-quarter air pocket)
- Explicitly anchor the base case on cyclical CPG/Auto normalization plus successful leadership ramp restoring high-single/low-double-digit growth by 2027-2028
- Bull case anchored on a genuine reacceleration story (JBP mix shift, international scaling, Google antitrust tailwind)

## 9. What Would Have to Be True for the Thesis to Break (or Hold)
- Define explicit, falsifiable triggers for the next 2-4 quarters: e.g., Q3 actual vs the ~-12% guide, whether a full-year or FY27 framework is given, net revenue retention trend, any holding-company (WPP/Omnicom) DSP preferred-partner announcement favoring Amazon, further leadership departures
- Define what "thesis holds" looks like: Q3 print in line with or better than guide, Q4 stabilization/reacceleration signal, leadership team executing visibly on the three priorities Green named (Zuma/Kokai shipping, measurement/Audience Unlimited ramp, new leaders ramped)

## 10. Valuation & Next Steps
- Current price vs FCF, EV/EBITDA, and reported vs FCF-less-SBC multiples
- Whether a DCF is warranted now or should wait for the Q3 print (given management's own admission of reduced visibility)
- Decision framing: Watch / Accumulate on weakness / Pass, and what would move it either direction

---

**Data gaps to fill before writing the full deep dive:**
- Current TTD share price (not yet pulled)
- Net revenue retention rate for Q2 (not disclosed in the extracts on hand — check full 10-Q/press release)
- Full Q1 2026 figures for the growth-trajectory table in Section 4 (filings exist in `research/filings/` but haven't been extracted into the same format as the Q2 files)
- Whether Ventura OS was mentioned at all on the Q2 call (not referenced in the transcript extract — confirm via full transcript)
- Current DV360/Amazon DSP market share figures (last known snapshot is from Feb 2025 per prior research — needs refreshing)
- Full slate of board additions beyond Drew Vollero — Green references more on the Q2 call without naming them; check the latest proxy statement or 8-Ks for names/backgrounds
