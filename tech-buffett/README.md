# Tech-Savvy Warren Buffett — Claude Code Agent

A long-term value investor agent for Claude Code. Researches and runs a virtual portfolio of individual tech / disruptor stocks under strict, non-negotiable rules. State lives in markdown; research artifacts live in Word and Excel files; every action is logged forever.

## Install

Drop this folder anywhere and open it in Claude Code. The agent is defined at:

```
.claude/agents/tech-buffett.md
```

Claude Code will pick it up automatically as a project subagent. Invoke it with:

```
> use the tech-buffett agent
```

or just describe what you want and let Claude route to it.

## Layout

```
tech-buffett/
├── .claude/agents/tech-buffett.md   ← agent definition & full ruleset
├── state/
│   ├── portfolio.md                 ← cash, holdings, infusions, dividends
│   ├── action-history.md            ← append-only log, never edited
│   └── candidates.md                ← latest ranked scan, replaced each scan
└── research/
    ├── scans/                       ← raw scan notes, dated
    ├── initiations/                 ← Initiation of Coverage .docx files
    ├── deep-dives/                  ← long-form .docx write-ups
    └── dcf/                         ← DCF .xlsx models
```

## The Rules in One Page

**Universe:** individual stocks only, NYSE or Nasdaq only, tech/disruptors only. No ETFs, ever.

**Cash:** $1,000 deposited externally every Monday. You may add ad-hoc infusions whenever you want — just tell the agent and it will record them. The agent never deposits its own cash.

**Trading:** real-time prices only, U.S. market hours only, no backdating. Fractional shares to one decimal place. Max 10 holdings.

**Allocation target:** roughly 1/3 large cap (≥$10B), 1/3 mid cap ($2B–$10B), 1/3 small cap ($300M–$2B), measured at market value on each buy date. Allowed to deviate while the portfolio is still being built out.

**One action per day**, chosen from:

| # | Action | Prereq | Output |
|---|---|---|---|
| 1 | Quick Scan | none | replaces `candidates.md` + dated scan note |
| 2 | Initiation of Coverage | candidate exists | `research/initiations/INIT-{TICKER}-DATE.docx` |
| 3 | Deep Dive | Initiation done for this ticker | `research/deep-dives/DEEP-{TICKER}-DATE.docx` |
| 4 | DCF (10yr, perpetuity + exit-multiple, from 10-K/10-Q) | Deep Dive done for this ticker | `research/dcf/DCF-{TICKER}-DATE.xlsx` |
| 5 | Buy | DCF done for this ticker within last 60 days | updates `portfolio.md` + `action-history.md` |
| 6 | Rebalance | 6 months since portfolio start, then ≥6 months between | up to 3 buys + 3 sells |

**Buy cadence:** ≤ 1 per week, 1 company per buy.
**Sell cadence:** ≤ 1 per month outside a rebalance, 1 company per sell.

**Hard no's:** no ETFs, no non-tech, no off-hours trades, no fabricated prices or financials, no editing history.

## How a typical day looks

```
You: tech-buffett, what's the plan today?

Agent: [reads portfolio.md, action-history.md, candidates.md]
       Today is <date>. Markets are <open/closed>. This week I have not yet
       used my buy. I last scanned 9 days ago. Three candidates have full
       Init+DeepDive+DCF stacks current within 60 days: NVDA, MNDY, CFLT.
       Cash on hand: $X. Allocation drift: light on small cap.
       
       Recommended action today: Action 5 — buy CFLT.
       Rationale: <one paragraph>. Want me to proceed?
```

## Notes on the Word / Excel docs

The agent uses Anthropic's built-in document skills (`docx` and `xlsx`) to produce real .docx and .xlsx files — not markdown pretending to be Office. DCFs include both perpetuity and exit-multiple terminal value tabs, with a 10-year explicit forecast and clearly labeled assumption cells you can challenge.

## Telling the agent about an infusion

Just say so:

> "I'm dropping another $500 in today as a special infusion."

The agent will record it in `portfolio.md` and `action-history.md` as a bookkeeping event. This does **not** consume your one daily action.
