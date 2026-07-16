"""Practice simulator for a Plenful-style 'boolean control policy' coding assessment.

Mirrors the described task shape: a physics-based sim with gravity, a per-frame
boolean action decision, and an automated runner that scores your policy across
several standardized scenarios. Not the real assessment -- built from the job's
description to practice the reactive-vs-predictive design tradeoff under a clock.

Run with: python simulator.py
"""
import importlib
import random
import sys


class Scenario:
    def __init__(self, name, gravity, flap_impulse, scroll_speed, gap_height,
                 screen_height, obstacle_spacing, num_obstacles, start_y=None, seed=0):
        self.name = name
        self.gravity = gravity
        self.flap_impulse = flap_impulse
        self.scroll_speed = scroll_speed
        self.gap_height = gap_height
        self.screen_height = screen_height
        self.obstacle_spacing = obstacle_spacing
        self.num_obstacles = num_obstacles
        self.start_y = start_y if start_y is not None else screen_height / 2
        self.seed = seed


def make_obstacles(scenario):
    rng = random.Random(scenario.seed)
    obstacles = []
    x = float(scenario.obstacle_spacing)
    for _ in range(scenario.num_obstacles):
        margin = scenario.gap_height / 2 + 10
        gap_center = rng.uniform(margin, scenario.screen_height - margin)
        obstacles.append({
            "x": x,
            "gap_top": gap_center - scenario.gap_height / 2,
            "gap_bottom": gap_center + scenario.gap_height / 2,
        })
        x += scenario.obstacle_spacing
    return obstacles


def run_scenario(policy_fn, scenario, max_frames=2000, verbose=False):
    y = scenario.start_y
    vy = 0.0
    obstacles = make_obstacles(scenario)
    cleared = 0
    frame = 0

    while frame < max_frames:
        frame += 1

        # gravity always applies first
        vy += scenario.gravity

        next_obstacle = obstacles[0] if obstacles else None
        state = {
            "y": y,
            "vy": vy,
            "gravity": scenario.gravity,
            "flap_impulse": scenario.flap_impulse,
            "screen_height": scenario.screen_height,
            "frame": frame,
            "next_gap_x": next_obstacle["x"] if next_obstacle else None,
            "next_gap_top": next_obstacle["gap_top"] if next_obstacle else None,
            "next_gap_bottom": next_obstacle["gap_bottom"] if next_obstacle else None,
        }

        action = policy_fn(state)
        if action:
            vy = scenario.flap_impulse  # discrete flap: sets velocity, does not add

        y += vy

        if y < 0 or y > scenario.screen_height:
            return {"passed": False, "frame": frame, "reason": "out_of_bounds", "cleared": cleared}

        for obs in obstacles:
            obs["x"] -= scenario.scroll_speed

        if obstacles and obstacles[0]["x"] <= 0:
            obs = obstacles.pop(0)
            if not (obs["gap_top"] <= y <= obs["gap_bottom"]):
                return {"passed": False, "frame": frame, "reason": "collision", "cleared": cleared}
            cleared += 1

        if not obstacles:
            return {"passed": True, "frame": frame, "reason": "cleared_all", "cleared": cleared}

        if verbose:
            print(f"frame={frame:4d} y={y:7.2f} vy={vy:7.2f} action={action}")

    return {"passed": False, "frame": frame, "reason": "timeout", "cleared": cleared}


SCENARIOS = [
    Scenario("baseline", gravity=1.0, flap_impulse=-8.0, scroll_speed=4.0,
             gap_height=90, screen_height=400, obstacle_spacing=150, num_obstacles=8, seed=1),
    Scenario("tight_gaps", gravity=1.0, flap_impulse=-8.0, scroll_speed=4.0,
             gap_height=55, screen_height=400, obstacle_spacing=150, num_obstacles=8, seed=2),
    Scenario("heavy_gravity", gravity=1.8, flap_impulse=-9.0, scroll_speed=4.0,
             gap_height=90, screen_height=400, obstacle_spacing=160, num_obstacles=8, seed=3),
    Scenario("weak_flap", gravity=1.0, flap_impulse=-5.5, scroll_speed=4.0,
             gap_height=90, screen_height=400, obstacle_spacing=150, num_obstacles=8, seed=4),
    Scenario("fast_scroll_dense", gravity=1.2, flap_impulse=-8.0, scroll_speed=7.0,
             gap_height=70, screen_height=400, obstacle_spacing=110, num_obstacles=10, seed=5),
]


def main():
    sys.path.insert(0, ".")
    import policy
    importlib.reload(policy)

    passed = 0
    for scenario in SCENARIOS:
        result = run_scenario(policy.decide_action, scenario)
        status = "PASS" if result["passed"] else "FAIL"
        print(f"[{status}] {scenario.name:20s} cleared={result['cleared']:2d}/{scenario.num_obstacles:<2d} "
              f"reason={result['reason']:<12s} frame={result['frame']}")
        if result["passed"]:
            passed += 1

    print(f"\n{passed}/{len(SCENARIOS)} scenarios passed")


if __name__ == "__main__":
    main()
