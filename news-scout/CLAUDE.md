# news-scout

A news research agent that scans for recent (24–48 hour) headlines and summaries across a watchlist of tech companies and topics, for use as YouTube channel content sourcing.

## Project layout

```
news-scout/
├── .claude/agents/news-scout.md   ← agent definition & full ruleset
├── watchlist.md                   ← companies, tickers, and topic categories to monitor
├── seen-stories.md                ← append-only deduplication log
└── scans/                         ← write-only per-run output files (never read back)
```

## How to use

Invoke the subagent for all news scanning:

```
use the news-scout agent
```

### Invocation modes

1. **Full watchlist scan** — scans every entry in watchlist.md
2. **Targeted scan** — "scan NVDA and TSLA" / "scan for news on [ticker]"
3. **Category scan** — "scan for AI regulation news" / "what's new in semiconductors"
4. **General scan** — "what's new in tech today"

## Key constraints (enforced by the agent)

- Only surfaces stories from the last 24–48 hours
- Deduplicates against seen-stories.md (URL-first; headline fallback)
- Appends all surfaced stories to seen-stories.md after every run
- seen-stories.md is append-only — never edit or delete past entries
- Every run also writes its full output to a new file under scans/ (e.g. scans/2026-07-08-1423.md) — write-only, never read back by the agent, purely a saved copy for the user
- watchlist.md carries an IR/Newsroom link per company, checked alongside general search each scan; new tickers added without one get looked up and filled in automatically before their first scan
- Output is always ranked by priority (P1 → P4), with YouTube angle tags
- No financial data aggregators or SEC filings — qualitative news sources only
