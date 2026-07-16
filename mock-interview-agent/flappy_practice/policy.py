"""Implement your per-frame control policy here.

State contract (mirrors what the real assessment likely provides):
    y               -- current vertical position (0 = top of screen, increases downward)
    vy              -- current vertical velocity for this frame (positive = falling)
    gravity         -- per-frame gravity acceleration added to vy every frame
    flap_impulse    -- velocity applied if you return True this frame (sets vy, does not add)
    screen_height   -- bottom boundary; y must stay within [0, screen_height]
    frame           -- current frame number
    next_gap_x      -- horizontal distance to the next obstacle (None if no more obstacles)
    next_gap_top    -- top y-coordinate of the next gap
    next_gap_bottom -- bottom y-coordinate of the next gap

Return True to flap, False to do nothing (gravity only applies).
"""


def decide_action(state: dict) -> bool:
    return False
