# dcf-creator

An ad hoc DCF and multiples-valuation builder for individual stocks, managed by the `dcf-creator` subagent. Spun off from `tech-buffett` on 2026-09-28 to give personal, one-off "build me a valuation" requests their own home, separate from tech-buffett's formal, six-action-per-day, user-supplied-filings-only portfolio pipeline.

## Project layout

```
dcf-creator/
├── .claude/agents/dcf-creator.md   ← agent definition & full ruleset
├── extracts/                       ← raw financial-data extracts (10-K/10-Q
│                                      highlights, earnings-release summaries,
│                                      transcripts, strategic context) pulled
│                                      live from the web
└── valuations/                     ← finished DCF and multiples-valuation
                                       write-ups (plain text, ASCII tables)
```

Both folders were seeded on 2026-09-28 by moving everything DCF/valuation-related out of `tech-buffett/personal/` (extracts and their finished write-ups together, so every valuation stays self-contained with its own sources). tech-buffett/personal/ retains only non-DCF personal work (slideshow outlines, deep-dive drafts, the Tesla Cybercab robotaxi financial-modeling project, etc.).

## How to use

Invoke the subagent for any one-off valuation request:

```
use the dcf-creator agent
```

Tell it the ticker and, if relevant, what kind of valuation (DCF is the default; ask for a companion multiples/sum-of-the-parts valuation explicitly if you want one, or it may offer one where segments are structurally different enough to warrant it). It will check `extracts/` (and tech-buffett's `research/filings/`) for data it already has before pulling anything new, save whatever it pulls as a reusable extract, and produce a full scenario-based valuation in `valuations/`.

## Key differences from tech-buffett's own DCF action

- **Fetches data live from the web.** tech-buffett's formal pipeline requires the user to supply filings directly and refuses to fetch them — that restriction exists to keep the portfolio's official DCFs anchored to exactly what the user hands over. dcf-creator exists specifically so ad hoc requests don't need that friction.
- **No action-cadence limit, no six-action list, no portfolio gating.** Build as many valuations as asked, whenever asked.
- **Errs conservative when unsure**, rather than tech-buffett's "semi-conservative — lean conservative without strangling the model." See the agent definition for what that means concretely.
- **Always pulls segment-level historical financials**, not just consolidated — this was inconsistently done in past ad hoc work and is now a hard requirement.
- **Does not, by itself, qualify anything for the tech-buffett portfolio.** A dcf-creator valuation is informational. Buying still requires tech-buffett's own Init → Deep Dive → DCF pipeline, run by tech-buffett, with a DCF completed within the last six months per CLAUDE.md's graduated margin-of-safety rule.

## Relationship to tech-buffett

The two agents share data, not process:

- tech-buffett's formal research pipeline (`../tech-buffett/research/filings/`, `research/dcf/`, etc.) is completely unaffected by dcf-creator — it still only works from filings the user supplies directly, and its DCFs are the only ones that gate a portfolio purchase.
- When tech-buffett needs financial data for a ticker dcf-creator has already extracted, it should check `../dcf-creator/extracts/` before asking the user to supply a filing — reading a file dcf-creator already produced isn't "fetching from the web," so it doesn't violate tech-buffett's hard-stop rule.
- When dcf-creator needs data for a ticker tech-buffett has already covered, it should check `../tech-buffett/research/filings/` before pulling fresh data itself.
