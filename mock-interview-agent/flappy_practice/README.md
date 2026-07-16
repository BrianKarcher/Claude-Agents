# Flappy-bird control policy practice

Practice harness for the Plenful "AI-Assisted Advanced Coding Assessment" shape:
implement a per-frame boolean control policy for a gravity-based physics sim,
scored automatically across several standardized scenarios. See
`../company_intel/` for other company prep; this is scoped to the coding round only.

## Run it

```
python simulator.py
```

This runs your `decide_action` from `policy.py` against 5 scenarios with varied
gravity, flap strength, gap size, and obstacle density, and prints pass/fail per
scenario plus how many obstacles you cleared before failing.

## The contract

Each frame you get a `state` dict (see the docstring in `policy.py`) and return
`True` (flap) or `False` (do nothing). Gravity always applies; a flap sets your
vertical velocity directly (it does not stack with gravity that frame).

## Suggested practice flow

1. Get a naive threshold policy passing `baseline` first (e.g. flap when below
   some fixed height). Confirm the loop and contract make sense.
2. Notice it breaks on `tight_gaps` or `fast_scroll_dense` — those are tuned to
   punish policies that don't project a few frames ahead.
3. Rewrite using a lookahead: simulate your next 1-2 frames with and without
   flapping, and pick whichever keeps you inside the gap band (and doesn't
   overshoot toward the ceiling next).
4. Once all 5 pass, try editing `SCENARIOS` in `simulator.py` with more extreme
   constants (higher gravity, smaller gaps) to see where your policy breaks —
   this is the kind of generalization the real assessment is likely checking.

## Time-box it like the real thing

Give yourself 60 minutes total, including reading this file cold, to simulate
the actual assessment conditions.
