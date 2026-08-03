# youtube-earnings-decks

Single-file HTML earnings-briefing decks for a YouTube channel, built and maintained by the `earnings-briefing` subagent.

## Project layout

```
youtube-earnings-decks/
├── .claude/agents/earnings-briefing.md   ← agent definition & full ruleset
├── pltr/
│   ├── pltr-earnings-briefing-v2.html    ← current deck (published as an Artifact)
│   └── pltr-earnings-briefing.html       ← earlier version, kept for reference
└── <ticker>/                             ← one folder per company, added as needed
```

## How to use

Invoke the subagent for all deck work:

```
use the earnings-briefing agent
```

## The one rule that matters most

**Never fabricate data.** Every historical figure in a deck must come from a fetched, verified source (SEC filing, company press release, or a cross-checked aggregator) — never from memory, estimation, or "reconstruction." See the agent definition for the full policy; it exists because of a real incident where invented quarterly financials shipped in a deck with only a caption-level disclaimer, which is not an acceptable substitute for real data.

## Design system notes

- Dark, cinematic, scroll-snap slide deck. New company decks should copy the CSS/structure of the most recent existing deck rather than reinventing the visual language.
- Every slide reserves a bottom-right "webcam gutter" so the presenter's facecam never covers content.
- Charts follow the `dataviz` skill's method (form → color → validate → marks → interaction → accessibility pass).
- Slides are numbered via corner-tag + eyebrow + agenda list, kept in sync on every structural edit.
- Verification is done via static checks (tag-balance greps, diff review) rather than loading the page in a browser, unless a visual/layout-precision check is specifically needed.
