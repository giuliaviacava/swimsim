### swimsim/simulator.py

import random
# Points scoring, random add/drop variations (range from dropping 2% to adding 5%)
import SCORING
MIN_VARIATION = -0.02
MAX_VARIATION = 0.05

# Generates swimmer's time by using their best time and adding the random variation
def generate_swimmer_time(swimmer, event_name):
    best_time = swimmer.best_time_for(event_name)
    return best_time * (1 + random.uniform(MIN_VARIATION, MAX_VARIATION))

def simulate_event(event, teams):
    results = []
    # Generates a simulated race time for each swimmer, stores swimmer and time together in results list
    for swimmer in event.entries:
        simulated_time = generate_swimmer_time(swimmer, event.name)
        results.append((swimmer, simulated_time))
    # Sort results from fastest to slowest time, save sorted results in event object
    results.sort(key=lambda x: x[1])
    event.set_results(results)

    # Loop through top scoring swimmers only, add those points to the swimmer's team total score
    for place, (swimmer, _) in enumerate(results[:len(SCORING)]):
        points = SCORING[place]
        teams[swimmer.team].add_points(points)
