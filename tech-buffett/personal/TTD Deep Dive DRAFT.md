# The Trade Desk, Inc. (NASDAQ: TTD) — Deep Dive

**Date:** August 7, 2026 | **Price:** $13.81 (-22% today, day after Q2 2026 earnings) | **52-week range:** $12.83–$91.45 | **Market cap:** ~$6.49B | **Rating:** WATCH / ACCUMULATE ON WEAKNESS

**Thesis in one line:** A neutral, independent DSP for the open internet whose growth has cracked sharply (Q2 revenue +3% YoY, Q3 guided to decline ~12%) on a mix of real cyclical CPG/auto pressure and newly conceded execution shortfalls — but whose stock has fallen far enough (-85% from its peak) that even a bear-case continuation of the slump implies limited further downside from here.

This deep dive updates and supersedes, for read-through purposes, the April 16, 2026 deep dive (`DEEP-TTD-2026-04-16.txt`), using Q1/Q2 2026 actuals, current pricing, and the Q1/Q2 2026 earnings calls. Written to stand alone for a first-time reader.

---

## 1. Ad-Tech 101 — A Primer

Digital ad space is mostly sold **programmatically**: each time a webpage, app, or streaming show loads, the ad slot is auctioned in real time — **real-time bidding (RTB)** — with buy-side software deciding what to bid based on the viewer and the advertiser's goals, and sell-side software running the auction.

Every ad-tech platform sits inside a **two-sided network**: the **demand side** (advertisers and their agencies) and the **supply side** (publishers and platforms with inventory to sell — websites, apps, streaming, CTV). Neither side is valuable without the other, and this chicken-and-egg dynamic makes scale self-reinforcing: more advertiser budget attracts more publishers, more inventory attracts more advertisers.

**Core vocabulary:**
- **DSP (Demand-Side Platform)** — software advertisers/agencies use to bid on inventory across many publishers at once. TTD, Google DV360, and Amazon DSP are all DSPs.
- **SSP (Supply-Side Platform)** — the publisher-side counterpart, auctioning inventory to many DSPs at once (Magnite, PubMatic, Google's AdX).
- **Ad exchange** — the marketplace/auction mechanism connecting DSPs and SSPs.
- **Identity/data layer** — how a DSP recognizes who it's bidding on. As third-party cookies phase out, the industry has shifted to first-party data, clean rooms, and identity graphs. TTD's **UID2** is its open, non-proprietary identity standard.

**Where TTD sits:** a pure-play, independent DSP — demand-side only, no owned inventory, no search engine, no social feed, no retail marketplace. Everything it earns comes from helping advertisers buy inventory someone else owns. This is the foundation of its "we work exclusively for the buy side, no conflict of interest" positioning.

**Walled garden vs. open internet — the framework underlying this entire deep dive.** **Walled gardens** (Google Search/YouTube, Meta, Amazon O&O, TikTok) own the inventory, typically run the buying tool advertisers use to access it (DV360, Amazon DSP, Meta Ads Manager), and sometimes the exchange in between — vertically integrated across all three layers. An advertiser buying "Google ads" is largely buying inventory Google owns, priced and matched by Google's own systems, with limited outside auditability. The **open internet** is everything else — independent publishers, CTV apps outside the big platforms, audio, open-web display — fragmented supply that needs neutral intermediaries (DSPs like TTD, SSPs like Magnite/PubMatic) to connect to demand.

Why it matters: a vertically integrated walled garden has a structural incentive to favor its own inventory when it also decides the auction outcome ("self-preferencing") — the substance of the DOJ's antitrust case against Google's ad-tech stack. TTD, with no owned inventory, can credibly claim no such conflict. This "neutral fiduciary for the open internet" framing is TTD's central moat argument and recurs throughout this deep dive.

| Company | Owns inventory? | Runs a DSP? | Runs an exchange? | Position |
|---|---|---|---|---|
| Google | Yes — Search, YouTube | Yes — DV360 | Yes — AdX | Vertically integrated; control/data is the edge, self-preferencing is the antitrust exposure |
| Amazon | Yes — retail site, Prime Video | Yes — Amazon DSP | Partial | Same conflict-of-interest question, plus first-party shopper data no independent DSP can match |
| The Trade Desk | No | Yes — its only business | No | Demand-side only; wins on trust and independence, not supply control |

---

## 2. Unit Economics — What TTD Actually Sells

TTD runs a **toll-road model**: it doesn't own inventory, it charges a **platform fee** on advertiser spend flowing through its software. **Revenue = Gross Spend × Take Rate.** Management describes the take rate as having stayed in "a narrow band for 10 years," resisting price cuts in favor of a "not the cheapest, the best" positioning. At a take rate in the low-to-mid 20s% (consistent with FY2025's implied ~22-24%), Q2 2026's $715M of revenue implies roughly **$3.0-3.2B of gross spend for the quarter** — a low-teens-billions annualized run rate, and the more meaningful measure of TTD's footprint than revenue alone.

**Cost structure, Q2 2026 vs. Q2 2025:**

| Line item | Q2 2026 | % rev | Q2 2025 | % rev | YoY $ |
|---|---:|---:|---:|---:|---:|
| Platform operations | $184.3M | 25.8% | $151.0M | 21.8% | +22% |
| Sales & marketing | $174.4M | 24.4% | $161.1M | 23.2% | +8% |
| Tech & development | $140.7M | 19.7% | $134.3M | 19.3% | +5% |
| G&A | $114.0M | 15.9% | $130.9M | 18.9% | -13% |
| **Total opex** | **$613.5M** | **85.8%** | **$577.3M** | **83.2%** | **+6%** |
| **Op income** | **$101.6M** | **14.2%** | **$116.8M** | **16.8%** | **-13%** |

The line that matters most: **platform operations grew 22% while revenue grew 3%** — a real decoupling of TTD's largest controllable cost from growth. Management attributes it to migrating workloads from third-party cloud to owned data centers plus AI infrastructure spend, framed as near-term drag for better long-run unit costs — a bet not yet visible in the numbers. S&M and tech/dev both ticked up modestly as a share of revenue, the wrong direction for a scaling platform. G&A's improvement is a comparison artifact (Q2 2025 included a one-time $19M CEO option charge with no Q2 2026 equivalent), not real efficiency gain.

Net: operating margin fell from 16.8% to 14.2%, net margin from 13.0% to 9.0%, net income -29% YoY to $64.4M ($0.14 diluted EPS vs. $0.18).

**Adjusted EBITDA** was $241.3M (-11% YoY, 34% margin, -500bps YoY) — but notably *higher* than Q1 2026's 30% margin despite revenue growth decelerating further sequentially. Whether that's real cost discipline or one-time items (a useful-life change added $3.1M to net income) doing the work is unresolved.

**SBC as a real cost:** SBC was $109.6M (-15% YoY), improving to 15.3% of revenue from 18.6% — consistent with diluted share count falling 5.2% YoY (buybacks outpacing dilution). But netted against Q2's $136M reported FCF, **SBC-adjusted FCF was only ~$26M for the quarter** (~3-4% margin) — far thinner than FY2025's full-year estimated 16-17%. Whether Q2 is an outlier or a preview of a thinner new normal is an open question for the DCF.

**Why the business doesn't commoditize:** returning to Section 1's network framework — more spend trains Kokai's AI bidding on more outcome data, improving results, attracting more spend; more SSP integrations improve fill and pricing, attracting more spend; UID2 layers the same dynamic onto identity. A new entrant would need petabyte-scale bid data, integrations across ~100 major SSPs/data vendors, and years of agency trust — a catch-up only Google and Amazon are positioned to attempt, and even they'd be extending walled-garden platforms into the open internet rather than starting neutral.

---

## 3. Total Addressable Market — 10-Year View

The global digital ad market was ~$730B in 2025, heading toward ~$1.1T by 2030 (8-9% CAGR). Programmatic — ad space transacted via RTB — was ~$420B of that in 2025, heading toward ~$800B by 2030. Programmatic splits along the walled-garden/open-internet line: walled gardens capture ~65%; the **open internet** — TTD's actual TAM — is the remaining ~35%, or ~$150B in 2025 growing toward ~$280-320B by 2030. *(These macro figures are from April 2026 research and haven't been refreshed — directional at this scale, but worth spot-checking against current eMarketer/IAB data before use in a DCF.)*

**CTV** does most of the growth-rate work within that TAM: >40% of global ad spend by 2030, US CTV from ~$30B (2025) to ~$51B (2029), with 60-75% of US TV spend programmatic by 2030. CTV is already TTD's largest channel — "low 50s%" of Q2 2026 revenue, still growing double digits even as total growth stalled. Mobile was "high 20s%," display "low double-digit," audio ~7% but the fastest-growing channel for four straight quarters.

**Retail media** — ad inventory sold against retailers' first-party data — is the fastest-growing ad category globally (~20% CAGR). TTD's pitch to retailers who don't want to route budgets through a competitor (Amazon) is a direct extension of its neutral-intermediary positioning; partner retailers now cover >80% of US retail sales.

**Penetration:** ~$12-13B of TTD gross spend against a ~$150B open-internet TAM is roughly **8% penetration** — even flat, a TAM growing to ~$280-320B by 2030 is a mechanical tailwind independent of competitive share. The real question this hands off to Competitive Dynamics: does TTD capture its fair share of that growth, or does Amazon DSP take a disproportionate share at TTD's expense?

---

## 4. Competitive Dynamics

**The three-horse race:** the last hard share snapshot (February 2025 — stale, flagged for refresh) put the DSP market at roughly Google DV360 ~47%, Amazon DSP ~20%, TTD ~19%, everyone else ~14%. Amazon's ad revenue grew 23% YoY in Q4 2025 vs. TTD's 14% — if that gap persisted through 2026, Amazon has kept taking 1-2 points of combined share per year, mostly from TTD rather than Google, since TTD and Amazon compete more directly for open-internet-plus-CTV budgets. This remains the single most consequential competitive fact in this deep dive.

**Amazon's real advantages:** first-party data on 200M+ Prime members; owned CTV inventory (Prime Video) increasingly bundled with exclusive live-sports rights; the primary Netflix ad-tier DSP relationship (12 markets, effective Q4 2025) — a genuine loss for non-Amazon DSPs; secondary Spotify (fall 2025) and Yahoo DSP (March 2026) deals; cross-subsidy from AWS/Retail letting it run the DSP as a loss leader.

**Amazon's real disadvantages:** a trust deficit with agencies (buying through a retail competitor); thin reach into genuine open-internet inventory outside its own properties; no log-level transparency comparable to TTD's; an opaque take rate; a closed identity ecosystem versus UID2's open standard.

**Google DV360** is under a live legal threat — the DOJ's ad-tech antitrust case produced 2024-2025 liability findings, with remedy proceedings ongoing through 2026. A forced AdX/DV360 divestiture would be a real tailwind for TTD (more open-internet inventory in a genuinely competitive auction); behavioral remedies would matter less. A "Google buyer direct program" for simple, low-priced Programmatic-Guaranteed-style deals was referenced by an analyst on the Q2 call — a new wrinkle not covered in the April research, worth investigating further.

**Meta/TikTok** are budget competitors, not DSP competitors — walled gardens on the sell side that pull spend away in weak macro periods (simpler attribution, arguably worse long-run ROAS), directly relevant to Section 5's CPG/auto story.

**Management's own framing (Q2 call, Dan Salmon exchange):** Jeff Green made three arguments worth recording directly. "An auction with only one bidder isn't an auction" — a handful of scaled players is evidence of a durable market, not a warning sign. On take-rate comparisons: bundled with underlying media cost, TTD's 8% fee nets an advertiser $1.08 per dollar of media, while a competitor's 4% fee on inventory that costs it nothing to fill might net $1.04 for worse-performing media — walled gardens are structurally incentivized to fill their own inventory first because it's nearly free to them (a restatement of Section 1's self-preferencing point, now framed as a reason to discount their headline pricing). And: AI-driven decisioning doesn't disrupt the DSP model — "it is AI" — and TTD's independence becomes more valuable, not less, as competitors lean harder into owned-and-operated inventory.

**Fresh evidence since April:** a major pharma brand was won back from Amazon DSP in Q1 2026 (JBP targeting +114% spend growth) — a concrete instance of share moving toward TTD. Management also now contrasts its >80% US-retail-sales coverage against Amazon's own reported <15% share of US retail spend. Neither point overturns the share-loss trend implied by the Feb 2025 snapshot, but both cut against a simple "Amazon is inevitably winning" narrative.

**Net assessment:** the most defensible 5-year read is a splintering of the DSP market by use case — Amazon likely keeps winning disproportionate retail-connected/O&O-adjacent CTV share; TTD likely retains dominant open-internet, agency-workflow, and identity-layer share; DV360 serves Google-stack-anchored buyers. In that world TTD can still compound at a respectable double-digit rate — just not its historical 25-30%. The open question carried into Section 5: is Amazon's share capture large enough to explain most of the current deceleration, or is it genuinely the cyclical CPG/auto story management describes?

---

## 5. The Growth Deceleration — Bear Case Teardown

**Quarter-by-quarter:**

| Period | Revenue growth YoY | Note |
|---|---:|---|
| FY2023 | +23% | |
| FY2024 | +26% | Boosted by election-year political spend |
| Q1 2025 | +25% | |
| Q2 2025 | +19% | |
| Q3 2025 | +18% | |
| Q4 2025 | +14% reported, ~+19% ex-political | |
| FY2025 | +18% | |
| **Q1 2026** | **+11.8%** ($688.9M vs. $678M guide) | Beat guide +1.6% |
| **Q2 2026** | **+3%** ($715.1M vs. "at least $750M" guide) | **Missed guide ~5%** |
| **Q3 2026 guide** | **~-12%** ("at least $650M") | First-ever guided revenue decline |

Deceleration has run for six straight quarters, so this isn't a one-quarter anomaly. More important: **Q1 beat its own guide; Q2 missed its own guide** by nearly 5% — a materially worse signal than smooth deceleration. A company that decelerates but keeps hitting its own numbers has visibility into its business; a company that guides down and then misses the down-guide has a forecasting model that broke in one quarter. This should carry the most weight in any read of management credibility this quarter.

**Management's framing:** Green opened the call with unusually direct self-criticism — *"Our revenue growth is below our expectations and below the standard we hold ourselves to."* Relative to this team's historical pattern of sweeping, optimistic claims, that's a real break in tone and should be read as a genuine severity signal.

**Two causes cited:** (1) macro pressure concentrated in CPG and auto (~25% of the business), tied to tariffs, oil prices, and a "consumer wealth bifurcation" pushing pressured advertisers toward cheaper, lower-decisioning media over TTD's higher-fee model — corroborated by cited P&G and GM commentary; (2) **self-acknowledged execution shortfalls**, unelaborated beyond justifying the leadership wave in Section 6 — a genuinely new admission versus the April research's largely-external framing of the deceleration.

**What management wouldn't do:** pressed directly (Jason Helfstein, Oppenheimer) to quantify the macro/execution/other split, Green declined, saying the pressure is concentrated in "a handful" of large customers without a number attached. A mild yellow flag — Wall Street clearly wanted a number and didn't get one, on a call where the CEO had just volunteered unusual candor about execution.

**Reduced visibility:** new CFO Nate Olmstead (~1 month into the seat) explicitly flagged reduced forward visibility and said the Q3 guide assumes no macro improvement. No full-year outlook, no updated margin framework ("stay tuned"). Combined with the Q2 miss, management has effectively told the market its own forecasting has degraded — which should directly discount confidence in the Q3 guide and any near-term DCF inputs built on it.

**Is this actually Amazon, undescribed?** CPG and auto — the two categories management names — are also the categories most exposed to Amazon's retail-data advantage and O&O bundling (Section 4). A CPG brand cutting budget *and* shifting more of what remains to Amazon looks identical in TTD's numbers to "a large customer under pressure." Management's refusal to quantify the split makes this ambiguity unresolvable from the call alone — the single most important open question feeding the DCF.

**Litigation overhang:** the securities class action (C.D. Cal., purchases 11/15/23-8/8/25) had its motion to dismiss **denied** 3/17/2026, with trial set for **May 16, 2028** — a worse outcome than dismissal, though not itself evidence of merit. The Nevada reincorporation litigation saw the Delaware Supreme Court affirm against plaintiffs on the books-and-records matter (6/26/2026), but fiduciary-duty claims remain pending. Related derivative actions are stayed; a data-privacy case is in discovery through September 2027. None of these look individually thesis-breaking, but a 2028 trial date means this overhang spans the entire holding period this deep dive evaluates.

**Rough attribution** of the drop from FY2024's 26% growth to the Q3 guide's ~-12%: political-spend lapping (real, one-time, mostly done); CPG/auto macro (plausible, partially corroborated externally, not independently verified against actual ad-budget data); newly conceded execution shortfalls (unquantified); Amazon share loss (not named directly, structurally plausible, probably entangled with the macro story rather than separable from it).

The honest read: the macro piece is better corroborated than it was in April, but overall confidence should be *lower* than in April — Q2 missed guidance rather than merely decelerating, management conceded a new execution component, and visibility has explicitly degraded. Cyclical-vs-structural is still the right frame, but the Q3 print is now needed to confirm a floor before underwriting a cyclical-recovery thesis at size.

---

## 6. Leadership & Organizational Reset

**Jeff Green (CEO/co-founder)** has run TTD for its entire ~17-year life, compounding revenue at a ~34% CAGR since a 10-year-old IPO. The company carries a dual-class structure (Class B, 10 votes/share) — a real control-concentration risk most shareholders have accepted given the track record. His communication style has historically trended toward sweeping claims (CTV "fundamentally transformed," a now-deprioritized Ventura CTV-OS once framed as "revolutionary") that argue for discounting forward rhetoric and weighting filings more heavily. Cutting the other way: in March 2026 he personally bought **$148M of TTD stock** (~6M shares at $23-25 avg, via what public reporting describes as an estate-planning vehicle) — a scale that reads as genuine conviction, not routine 10b5-1 activity. At today's $13.81, that purchase sits roughly **40-45% underwater**, which meaningfully tempers the signal: Green made a large, costly bet on a price level the stock has since fallen well below.

**The CFO seat** has cycled unusually fast for a company this size:

| CFO | Tenure | Notes |
|---|---|---|
| Laura Schenkein | ~Jun 2023 – mid-2025 | Orderly, announced transition |
| Alex Kayyal | Aug 2025 – Jan 24, 2026 (~5 mo.) | Ex-Lightspeed VC; **terminated**, announced on a Sunday; kept his board seat through 2026 — reads more like a culture-fit dispute than a for-cause dismissal |
| Tahnil Davis (interim) | Jan – mid-2026 | 11-year veteran, Chief Accounting Officer; deep book knowledge through the transition |
| **Nate Olmstead (permanent)** | **Mid-2026 –** | Ex-Penguin Solutions/Logitech/HPE; signed the Q2 10-Q; ~1 month into the seat at the Q2 call |

TTD reaffirmed 2025 results and guidance at the time of Kayyal's termination — evidence against an accounting-integrity explanation, not conclusive. Net effect: the CFO-instability risk from April is **resolved** narrowly (a permanent CFO is in place), replaced by a smaller one — the newest financial leader is guiding through the worst quarter in company history with no tenure and no track record here. Whether Olmstead stabilizes the business or is himself learning it mid-crisis isn't yet knowable.

**The leadership wave:** Vivek Kundra (COO); Kristi Argyilan (Chief Commercial Officer, ex-Uber ads, retail-media network builder, focused on data partnerships feeding Audience Unlimited/measurement); Ron Lamprecht (Chief Business Development Officer, pulled from a broader-than-advertising role at **Amazon** — notable given Section 4); Sarah Gavin (CMO); Vinny Rinaldi (VP Client Strategy & Growth, ex-Hershey's, a self-described critic of "cheap reach" buying — a pointed hire given Section 5's finding on advertisers rotating to cheaper media). Green called this "hundreds" of hires beyond the five names above ("I'm nervous about leaving somebody out") — a much larger overhaul than the headline titles suggest, and one that reads either as decisive corrective action or evidence of deeper prior gaps. The next 2-3 quarters of execution, not this quarter's hiring announcements, will distinguish the two.

**Board changes:** Drew Vollero was newly added (disclosed on the Q1 call); Green also referenced unnamed further board additions on the Q2 call — a gap to close via proxy/8-K. Worth reading against the litigation backdrop above: a 2028 securities-trial date and unresolved fiduciary-duty claims are exactly the kind of overhang where governance-credibility refreshes carry independent value.

**Capital allocation:** net cash grew to $1.485B (from $1.303B at YE25) despite continued buybacks — organic cash generation still outpacing capital return. No debt; a $750M undrawn revolver ($745M available). $78M repurchased in Q2 ($241M over H1); board added $350M of authorization in February 2026, $269M remaining at quarter-end. Diluted share count down 5.2% YoY. Minimal M&A history (nothing notable since Adbrain, 2017) — a conservative, founder-aligned posture.

**Grading this quarter's communication:** opening with unhedged self-criticism, naming specific struggling categories, and providing granular counter-metrics (JBP, top-100, channel/geo detail) reads as more transparent than this team's historical pattern — a genuine, modest positive. Cutting against it: the refusal to quantify the macro/execution split, and a brand-new CFO with no independent standing to fill that gap. Net: more candid than usual, but the candor stops short of the number investors most wanted.

---

## 7. Bull Case — What's Still Working

**JBPs:** 217 clients, +38% YoY, JBP revenue growing ~6x faster than company average. Read this as a mix-shift metric, not pure incrementality — if JBP revenue is growing 6x faster than the average, the non-JBP base is mechanically growing far slower than the 3% headline, plausibly flat or shrinking. A shift toward deeper enterprise relationships may be a higher-quality base, but it's evidence the weakness sits concentrated in the non-JBP remainder, not that the whole business is fine.

**Top-100 / sub-500 "green shoots":** majority of top-100 accounts still growing double digits; advertisers outside the top 500 growing >50% YoY YTD. "Majority of top-100" implicitly concedes a minority isn't — plausibly the same handful of large accounts driving the shortfall. The sub-500 growth is real but off a small base, a small absolute-dollar offset to weakness at the top. Both read as evidence the *pattern* of weakness is concentrated, not that a floor is near.

**International:** EMEA/APAC each ~+30% YTD, China >100% YTD, >50% CTV growth YoY in both — still only ~17% of revenue (US ~83%). The arithmetic: even 30-40% growth on 17% of revenue can't offset an 83%-of-revenue US business decelerating toward flat for several more years at current relative scale. A genuine long-term positive, not a near-term offset.

**Retail media:** partner retailers now cover >80% of US retail sales vs. Amazon's own reported <15% of US retail spend — a genuine, differentiated asset. Open question: coverage isn't monetization, and what share of *current revenue* retail media actually represents isn't disclosed in the materials reviewed — a gap worth closing before weighting this point further.

**Product roadmap:** a measurement framework (alpha, fixing broken last-click/last-view attribution), Audience Unlimited (subscription-style third-party data, "what Spotify did to music," moving to open beta), and "Zuma" (a usability/UX upgrade). Case studies: a General Mills/Nature Valley UK campaign (retail data + Koa AI) drove 5x sales uplift, 92% lower CPM, 2x ROAS over four months; an Audience Unlimited beta cut a global advertiser's cost-per-unique-household and data CPM >25% each. These are cherry-picked wins, not evidence about the median client outcome — but the strategic logic is sound and directly responsive to the bear case (better measurement counters the cheap-reach rotation, Audience Unlimited addresses data-access friction, Zuma addresses Kokai's adoption friction). Whether they move the growth number is a 2027 execution question.

**Balance sheet optionality:** $1.485B net cash, no debt, $269M remaining buyback authorization, share count down 5.2% YoY. At today's $13.81 — a genuinely depressed multiple — continued buybacks are mechanically more accretive than at a higher price, a real positive independent of any narrative resolving favorably.

**Long-horizon catalysts, not underwritten in any base case:** a Google ad-tech antitrust remedy (AdX/DV360 divestiture would be a structural tailwind; no new timing information found in the Q1/Q2 materials reviewed, a gap to close); UID2 as the default open-internet identity standard (a Visa-like infrastructure outcome, still speculative); CTV's secular TAM growth through 2030 (Section 3), independent of TTD's competitive outcome.

**Net read:** no single bull point offsets the scale of Section 5's guidance miss or the Q3 guided decline. Together they support a narrower claim — the core of the business (largest accounts as a whole, structured enterprise relationships, international, product roadmap) isn't obviously broken, and weakness is plausibly concentrated rather than pervasive. That's meaningfully weaker than "the deceleration is temporary and reversal is imminent" — the gap between those two claims is what the Q3 print (Section 9) needs to resolve.

---

## 8. Scenarios — 5-Year Price Path

TTD trades at **$13.81** as of August 7, 2026 — the session immediately following Q2 earnings, down ~22% on the day, near its 52-week low ($12.83-$91.45 range, ~$6.49B market cap, down ~85% from peak). A stock that falls 22% in a day on a quarter that missed guidance by ~5% is pricing in more than this quarter's shortfall — it's pricing in a meaningfully worse multi-year trajectory than management is describing. That gap, between what the price now assumes and what Sections 5-7 actually support, is what this table tests.

**Methodology:** Q1 ($688.9M) + Q2 ($715.1M) + a Q3 guide-consistent ~$650M + an assumed Q4 in the $680-700M range implies **~$2.7B of FY2026 revenue** — modestly below FY2025's ~$2.9B, TTD's first-ever full-year decline. Share count is assumed to keep falling modestly in the base/bull cases and hold flat in the bear case (capital preserved for balance-sheet defense). *This is an illustrative model, not the full DCF still owed (Section 10).*

|  | **BEAR** (25%) | **BASE** (55%) | **BULL** (20%) |
|---|---:|---:|---:|
| Anchor | Q3's ~-12% is not a trough — persists through 2027 before stabilizing at low-single-digit growth | CPG/auto normalizes, the leadership wave executes, growth recovers to high-single/low-double digits by 2027-28 | Genuine reacceleration: JBP mix matures, international scales, Google antitrust remedy delivers a tailwind |
| 2026-2030 rev. CAGR | ~4% | ~10% | ~17% |
| 2030 revenue | ~$3.2B | ~$3.95B | ~$5.1B |
| 2030 FCF margin (SBC-adj.) | ~20% | ~27% | ~33% |
| 2030 FCF | ~$630M | ~$1.07B | ~$1.67B |
| Exit FCF multiple | 11x | 19x | 24x |
| 2030 equity value | ~$6.9B | ~$20.3B | ~$40.1B |
| Per share | **~$15** | **~$45** | **~$91** |
| 5-yr IRR (vs. $13.81) | **~2%** | **~27%** | **~46%** |

**Probability-weighted:** 0.25×$15 + 0.55×$45 + 0.20×$91 = **~$47** in five years — an expected 5-year IRR of roughly **28%**.

**Reading it:** even the bear scenario — Q3's decline extending through 2027 — implies only modest further downside from here. That's a direct function of how far the stock has already fallen; a ~16x P/E and an 85%-off-peak market cap already price in much of the bad news. This doesn't mean there's no downside risk (a bear case extending past 2027, a further Q3 guide-down, or a genuine structural break with Amazon could all still be worse than modeled), but the asymmetry at $13.81 is meaningfully better than the April research found at ~$21, purely on price. The unusually wide gap between the bear (~$15) and base (~$45) outcomes reflects how much this setup hinges on Section 5's central unresolved question: cyclical, or the leading edge of structural Amazon share loss?

---

## 9. What Would Have to Be True (or Hold)

**Scoring the April research's own checklist first**, since three-plus months and two earnings reports have passed:

*Six break conditions:*

| # | Condition | Status |
|---|---|---|
| 1 | WPP/Omnicom names Amazon DSP primary | Not confirmed either way — data gap |
| 2 | Net revenue retention <90% | Not disclosed in Q1/Q2 materials — recurring data gap |
| 3 | Q1 revenue meaningfully below guide, or FY26 implies <8% growth | Q1 **beat** guide (+1.6%); **Q2 missed** its own guide by ~5% one quarter later — the letter didn't fire on schedule, the spirit fired in Q2 |
| 4 | Material restatement | No evidence |
| 5 | Permanent CFO search extends past Sept 2026 | **Did not fire** — Olmstead in place well ahead of deadline |
| 6 | Take rate compresses >300bps in a quarter | Not confirmed — margin compression looks cost-driven, not take-rate-driven |

Net: 0 of 6 technically fired, but #3 fired in substance late, and two remain open data gaps rather than confirmed negatives.

*Four "thesis definitely holds" conditions — the more revealing scorecard:*

| # | Condition | Status |
|---|---|---|
| 1 | Q1 revenue beats $700M | **Missed** — $688.9M (beat the company's own $678M guide, not this stricter bar) |
| 2 | Credible permanent CFO by July 2026 | **Met, narrowly** |
| 3 | Q2 growth above Q1 growth (reacceleration) | **Clearly failed** — 11.8% → 3% |
| 4 | Amazon share gains plateau | Not confirmed |

Condition 3 failed outright. This deep dive cannot claim the April base case was vindicated — the April research was more optimistic about the pace of stabilization than what actually happened, even though Section 8 shows the stock's current price already prices in a lot of that disappointment.

**Forward triggers from here:**

*Breaks further if:* Q3 actual comes in below the ~$650M floor (a second consecutive miss); YoY decline worsens into Q4 rather than stabilizing; a top-2 holding company (WPP, Omnicom) names Amazon DSP primary; Olmstead or any Section 6 leadership hire departs within 2-3 quarters (a far worse signal than the original CFO churn, given how recently they joined); management continues withholding a forward framework past Q3.

*Holds if:* Q3 meets or beats the ~$650M floor; the YoY decline narrows into Q4 (even "-12%" toward "-6% to -8%" would matter); a preliminary FY2027 framework appears by Q3/Q4; disclosed NRR holds ≥95% (still the single most useful undisclosed metric, and a priority to chase down); no further departures, plus at least one concrete proof point from the new leadership wave.

**Net framing:** given Section 8's finding that price already discounts a lot of bad news, the practical stance isn't "wait for perfect confirmation" but: **the Q3 2026 print, expected within 1-2 months, is the single highest-value piece of information this deep dive can wait for** — it directly tests the bear-vs-base split in Section 8.

---

## 10. Valuation & Next Steps

**Snapshot (Aug 7, 2026):** price $13.81 (-22% today); market cap ~$6.49B; net cash $1.485B → **EV ≈ $5.0B**; trailing P/E ~16.25x.

**Run-rate multiples:** a clean TTM figure isn't assembled (Q3/Q4 2025 Adjusted EBITDA and SBC weren't pulled into this format — a gap to close). Annualizing H1 2026, the only clean base on hand:

| Metric | H1 2026 | Annualized | EV / metric |
|---|---:|---:|---:|
| Free cash flow | $412.0M | ~$824M | ~6.1x |
| FCF less SBC | ~$193.5M | ~$387M | ~12.9x |
| Adjusted EBITDA | $447.4M | ~$895M | ~5.6x |

Treat these as an upper bound on cheapness, not a settled answer — H1 blends a strong Q1 with a weak, guide-missing Q2, and doubling it ignores Q3's guided decline. A more honest full-year figure sits closer to Section 8's ~$630M bear-case FCF if Q3-Q4 land near guide. Even so, the finding survives: **the current entry multiple sits well below the 11x exit multiple this deep dive assigned to the bear scenario** — the numeric version of Section 8's asymmetry argument.

**DCF timing:** Section 9 already flagged Q3 as the highest-value pending information, and management itself has flagged reduced visibility. Anchoring a precise DCF today means anchoring on a guide management has admitted carries more uncertainty than usual, and that already missed once. Better sequencing: build the DCF's structure now using Section 8's scenario framework, but don't finalize a single-point intrinsic value or act on a buy until Q3 lands; then re-run the probability weights — a beat shifts mass toward base/bull, a second miss shifts it toward (and possibly worsens) the bear case.

**Decision:** not "confirmed, buy aggressively," not "broken, walk away." **WATCH / ACCUMULATE ON WEAKNESS** — the same label as the April research, but re-derived: not because the operating story has been vindicated (Section 9 shows it largely hasn't), but because the price has fallen far enough that risk/reward has improved without needing operating confirmation. Bear-case downside is limited (~2% 5-yr IRR even if the decline runs through 2027); base/bull upside is substantial if Section 9's triggers resolve favorably; but the thesis-hold checklist wasn't cleared, visibility is explicitly degraded, and the team steering through this is newly installed — none of which supports sizing up aggressively before Q3. A small starter position ahead of Q3 is a defensible way to express the asymmetry without needing to correctly call cyclical-vs-structural in advance; full sizing should wait for at least one "thesis holds" trigger, most importantly a Q3 print that meets or beats its own guide.

**For this portfolio specifically:** TTD isn't currently held. The portfolio's own rules require a DCF completed within six months with a graduated margin-of-safety before any buy — Section 8's scenario table would need to become an actual DCF (per the sequencing above) before it satisfies that gate.

**Data gaps to close before this is a finished document:**
- Net revenue retention for Q2 2026
- Full identity of board additions beyond Drew Vollero
- Whether Ventura OS came up at all on the Q2 call
- Refreshed DV360/Amazon DSP market share (last hard snapshot: Feb 2025)
- Retail media's actual share of current TTD revenue, not just retailer-coverage %
- Q3/Q4 2025 Adjusted EBITDA and SBC, for a true TTM multiple
- Current status of the DOJ Google ad-tech antitrust remedy timeline

---

**Sources:** TTD Q1/Q2 2026 10-Q and press releases, Q1/Q2 2026 earnings call transcripts, `DEEP-TTD-2026-04-16.txt` and `DCF-TTD-2026-04-17.txt` (April 2026 research), stockanalysis.com (price data, Aug 7, 2026). No position held in TTD at time of writing.
