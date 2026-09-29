# tech-buffett

A virtual long-term tech investing portfolio managed by the `tech-buffett` subagent.

## Project layout

```
tech-buffett/
├── .claude/agents/tech-buffett.md   ← agent definition & full ruleset
├── state/
│   ├── portfolio.md                 ← cash, holdings, cost basis, infusion log
│   ├── action-history.md            ← append-only action log (never edited)
│   └── candidates.md                ← latest ranked scan (replaced each scan)
└── research/
    ├── scans/                       ← raw scan notes, one .md per scan
    ├── initiations/                 ← Initiation of Coverage .docx files
    ├── deep-dives/                  ← long-form deep dive .docx write-ups
    └── dcf/                         ← DCF .xlsx models
```

## How to use

Invoke the subagent for all portfolio work:

```
use the tech-buffett agent
```

The agent reads the state files at the start of every session, determines what actions are legal today, proposes one action, and waits for confirmation before executing any trade.

## Key constraints (enforced by the agent)

- One action per day (scan, initiation, deep dive, DCF, buy, or sell/rebalance)
- Buy cadence: at most once per week, one company per buy
- Sell cadence: at most once per month outside a rebalance
- Max 10 holdings at any time
- All trades require a live price during U.S. market hours (9:30–4:00 ET)
- Buys require a DCF completed within the last six months (graduated margin-of-safety: +10–15% at 2–4 months, +20–25% at 4–6 months)
- Allocation target: ~1/3 large cap, ~1/3 mid cap, ~1/3 small cap
- No ETFs, no OTC, no non-tech companies, ever
- `state/action-history.md` is append-only — never edit past entries

## Cash infusions

$1,000 is deposited every Monday. Ad-hoc infusions can be added anytime — just tell the agent and it will record them as bookkeeping (does not consume the daily action).

## Related agent: dcf-creator

Ad hoc, standalone DCF and multiples valuations (personal "build me a valuation of X" requests that aren't a tech-buffett portfolio action) are handled by a separate sibling agent, `dcf-creator`, at `../dcf-creator/`. It was spun off from tech-buffett on 2026-09-28 and owns:

- `../dcf-creator/extracts/` — raw financial-data extracts pulled live from the web (tech-buffett's own `research/filings/` extracts are separate and still user-supplied-only, per the Filing Extracts policy below — check both before asking the user to supply a filing).
- `../dcf-creator/valuations/` — finished DCF and multiples write-ups.

A dcf-creator valuation is informational only and does **not** qualify a stock for this portfolio — that still requires tech-buffett's own Init → Deep Dive → DCF pipeline (Actions 2-4), run by tech-buffett itself, with a DCF completed within the last six months per the graduated margin-of-safety rule above.
