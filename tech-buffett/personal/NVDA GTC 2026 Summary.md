# NVIDIA GTC 2026 — Summary

**Event:** GTC San Jose 2026 (NVIDIA's flagship developer conference)
**Date:** March 16, 2026 (Jensen Huang two-hour keynote, SAP Center, San Jose)
**Note on scope:** As of this summary (Aug 27, 2026), GTC San Jose in March is the most recent *flagship* GTC. NVIDIA also runs smaller regional GTC events (Paris, DC, etc.) throughout the year — this summary covers the March flagship event only, since that's what "latest GTC 2026" refers to in company/press usage.

---

## Big Picture

Huang's core thesis: AI has moved from being a *feature* to being an *industrial production system* — tokens are the output of "AI factories," and the entire compute/software/enterprise stack needs to be redesigned around that framing. The keynote spanned the full stack: silicon roadmap, physical AI/robotics, agentic AI software, and enterprise partnerships.

## Business Outlook

- Huang raised NVIDIA's cumulative order outlook for Blackwell + Vera Rubin to **~$1 trillion through 2027** (up from a prior ~$500B figure).
- Stock reaction was a "sell-the-news" pattern: NVDA rallied as much as ~4% intraday during the keynote (touching ~$188) before paring gains to close up **+1.65% at $183.22**.

## Silicon / Hardware Roadmap

- **Vera Rubin platform** (data center availability confirmed for H2 2026):
  - Rubin GPU: dual-die design, 336B transistors, 288GB HBM4 memory at 22 TB/s bandwidth, ~50 petaflops FP4 inference per chip.
  - Vera CPU: 88 custom Olympus ARM cores.
  - NVLink 6 interconnect plus supporting networking silicon.
  - Claimed ~10x performance-per-watt improvement over Grace Blackwell; ~10x reduction in inference token cost vs. Blackwell.
  - System is described as ~1.3 million components at rack scale.
- **Roadmap beyond Rubin:** Rubin Ultra with Kyber (2027), then Feynman (2028) — a three-generation preview.
- **Groq 3 LPU:** NVIDIA's first chip stemming from its ~$20B asset-purchase acquisition of Groq (completed December 2025). The Groq 3 LPX rack holds 256 LPUs, optimized for low-latency, large-context agentic inference workloads, designed to sit alongside Vera Rubin rack-scale systems.
- **Space infrastructure:** previewed early plans/module ("Space-1") toward future data centers in orbit — long-horizon, not a near-term product.

## Physical AI & Robotics

- **Cosmos 3** foundation model: billed as the first "world foundation model" unifying synthetic world generation, vision reasoning, and action simulation — aimed at accelerating generalized robot intelligence for complex/unstructured environments.
- **Isaac GR00T N1.6**: vision-language-action model giving humanoid robots the ability to perceive, reason, and act in unstructured environments.
- **Physical AI Data Factory Blueprint:** an open reference architecture for gathering/shaping/assessing real-world and simulated training data. Early partners named: FieldAI, Hexagon Robotics, Linker Vision, Milestone Systems, Skild AI, Uber, Teradyne Robotics.
- **Autonomous vehicles:** new Uber partnership to launch autonomous vehicles in Los Angeles on NVIDIA's stack.
- **Industrial robotics:** FANUC and ABB — together roughly a third of global industrial robot production — will integrate NVIDIA's Isaac AI platform into their robots.

## Agentic AI / Software

- **NVIDIA Agent Toolkit** — three components:
  - **NemoClaw**: secure runtime for autonomous agents ("claws").
  - **AI-Q**: open agent blueprint for enterprise deep research.
  - **Nemotron** family of open models.
- **NVIDIA OpenShell**: open-source runtime enforcing policy-based security/network/privacy guardrails for autonomous agents.
- **NVIDIA Dynamo 1.0**: open-source software for generative/agentic inference at scale; paired with Blackwell, NVIDIA claims up to **7x** inference performance improvement in internal benchmarks.
- **CUDA-X libraries** (cuDF, cuOpt, AI-Q, NeMo, PhysicsNeMo, CUDA-Q) now exposed to AI agents as callable domain-specific "skills."

## Enterprise Partnerships

- Software/design partners: **Cadence, Dassault Systèmes, PTC, Siemens, Synopsys** — bringing CUDA-X, Omniverse, and GPU-accelerated industrial tools into design/engineering/manufacturing workflows.
- Named enterprise customers/integrators: **FANUC, HD Hyundai, Honda, JLR, KION, Mercedes-Benz, MediaTek, PepsiCo, Samsung, SK hynix, TSMC.**

## Read Across for the NVDA Thesis (relevant to the Aug 27, 2026 DCF in this same folder)

- The **$1T order outlook through 2027** and the Vera Rubin per-GPU specs are consistent with — and partly the basis for — the "supply-constrained, not demand-constrained" framing NVIDIA repeated on the Q2 FY2027 earnings call five months later (see `DCF-NVDA-2026-08-27.txt`).
- **Groq acquisition** (LPU line) and the **Agent Toolkit / Dynamo** software push are NVIDIA's answer to the "hyperscaler custom silicon + inference-specific competition" risk flagged in the DCF's risk section — an attempt to extend the moat from training into agentic inference specifically, where competitors like Groq (as a standalone) and custom ASICs had been gaining attention.
- **Physical AI / robotics** (Cosmos 3, Isaac GR00T, Uber AV deal, FANUC/ABB) is a distinct, still-early optionality vector not modeled at all in the DCF's Data Center-driven forecast — worth watching as a potential future segment if it scales, but not yet material to revenue.
- The **sell-the-news stock pattern** (rally then fade on the same day) is a recurring behavior for NVDA around major catalysts and is consistent with the DCF's Section 8 observation that the stock reacts violently to single data points in both directions.

---

## Sources

- [CNBC — Nvidia GTC 2026: CEO Jensen Huang keynote Blackwell Vera Rubin](https://www.cnbc.com/2026/03/16/nvidia-gtc-2026-ceo-jensen-huang-keynote-blackwell-vera-rubin.html)
- [NVIDIA Newsroom — CEO Jensen Huang and Global Technology Leaders to Showcase Age of AI at GTC 2026](https://nvidianews.nvidia.com/news/nvidia-ceo-jensen-huang-and-global-technology-leaders-to-showcase-age-of-ai-at-gtc-2026)
- [Data Center Knowledge — GTC 2026: Nvidia Unveils Vera Rubin AI Platform, Eyes $1T by 2027](https://www.datacenterknowledge.com/data-center-chips/gtc-2026-nvidia-unveils-vera-rubin-ai-platform-eyes-1t-by-2027)
- [AI2Work — Everything Nvidia Just Announced at GTC 2026](https://ai2.work/blog/everything-nvidia-just-announced-at-gtc-2026-vera-rubin-agentic-ai-and-a-1-trill)
- [FirstPassLab — NVIDIA GTC 2026: Vera Rubin, Gigawatt AI Deals, Networking Engineer Guide](https://firstpasslab.com/blog/2026-03-16-nvidia-gtc-2026-vera-rubin-networking-engineer-guide/)
- [Automate.org — NVIDIA GTC 2026 Doubles Down on Physical AI, Humanoids](https://www.automate.org/ai/industry-insights/nvidia-declares-big-bang-of-physical-ai-at-gtc-2026)
- [Robotics 24/7 — NVIDIA GTC 2026: NVIDIA, global robotics leaders look to take physical AI to the real world](https://www.robotics247.com/article/nvidia-gtc-2026-nvidia-global-robotics-leaders-look-to-take-physical-ai-to-the-real-world)
- [The AI Insider — 10 Robotics Highlights From Nvidia GTC 2026](https://theaiinsider.tech/2026/03/21/10-robotics-highlights-from-nvidia-gtc-2026/)
- [Futurum Group — At GTC 2026, NVIDIA Stakes Its Claim on Autonomous Agent Infrastructure](https://futurumgroup.com/insights/at-gtc-2026-nvidia-stakes-its-claim-on-autonomous-agent-infrastructure/)
- [NVIDIA Newsroom — NVIDIA Ignites the Next Industrial Revolution in Knowledge Work With Open Agent Development Platform](https://nvidianews.nvidia.com/news/ai-agents)
- [NVIDIA Newsroom — Enterprise Software Leaders Build AI Agents With NVIDIA](https://nvidianews.nvidia.com/news/enterprise-software-leaders-build-ai-agents-with-nvidia)
- [Gradient Flow — NVIDIA's Next Moves: A Practitioner's Guide to GTC 2026](https://gradientflow.com/nvidia-gtc-2026/)
- [Yahoo Finance — Stock Market Today, March 16: Nvidia Rises After GTC 2026](https://finance.yahoo.com/news/stock-market-today-march-16-212544538.html)
- [earezki.com — NVIDIA (NVDA): GTC Keynote Poised to Counter Export Restriction Fears](https://earezki.com/ai-financial-news/2026-03-17-nvda/)

**Prepared for personal investment research purposes only. Does not constitute investment advice.**
