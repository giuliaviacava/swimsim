### swimsim/simulator.py

import random
# Points scoring, random add/drop variations (range from dropping 2% to adding 6% on a normal)
from configuration import SCORING

VARIATION_MEAN = 0.010
VARIATION_STD  = 0.015
VARIATION_MIN  = -0.020
VARIATION_MAX  =  0.060

def _truncated_normal(mean, std, low, high): #helper that keeps redrawing from the bell curve until it gets a value inside those hard limits
    while True:
        sample = random.gauss(mean, std)
        if low <= sample <= high:
            return sample

# Generates swimmer's time by using their best time and adding the random variation
def generate_swimmer_time(swimmer, event_name):
    best_time = swimmer.best_time_for(event_name)
    variation = _truncated_normal(
        VARIATION_MEAN,
        VARIATION_STD,
        VARIATION_MIN,
        VARIATION_MAX,
    )
    return best_time * (1.0 + variation)

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
