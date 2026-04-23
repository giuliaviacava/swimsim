### swimsim/simulator.py

import random
from configuration import SCORING

# Random add/drop variations, swimmers can drop up to 2% or add up to 5%
MIN_VARIATION = -0.02
MAX_VARIATION = 0.05

# Generates swimmer's time by using their best time and adding the random variation
def generate_swimmer_time(swimmer, event_name):
    best_time = swimmer.best_time_for(event_name)
    return best_time * (1 + random.uniform(MIN_VARIATION, MAX_VARIATION))

# Generates a time for each swimmer in the event and adds that time to a list of results
def simulate_event(event, teams):
    results = []
    for swimmer in event.entries:
        simulated_time = generate_swimmer_time(swimmer, event.name)
        results.append((swimmer, simulated_time))
    results.sort(key=lambda x: x[1])
    event.set_results(results)
    for place, (swimmer, _) in enumerate(results[:len(SCORING)]):
        points = SCORING[place]
        teams[swimmer.team].add_points(points)
