import random

from configuration import SCORING, MIN_VARIATION, MAX_VARIATION


def generate_swimmer_time(swimmer, event_name):
    """
    Generate a simulated race time for one swimmer.

    Steps:
    - start with best time
    - apply a random race-day variation
    - return simulated time
    """

    best_time = swimmer.best_time_for(event_name)

    variation = random.uniform(MIN_VARIATION, MAX_VARIATION)
    simulated_time = best_time * (1 + variation)

    return simulated_time


def simulate_event(event, teams):
    """
    Simulate one event:
    - generate times
    - sort by time
    - assign points
    """

    results = []

    for swimmer in event.entries:
        sim_time = generate_swimmer_time(swimmer, event.name)
        results.append((swimmer, sim_time))

    results.sort(key=lambda result: result[1])
    event.set_results(results)

    for place, (swimmer, _) in enumerate(results[:len(SCORING)]):
        points = SCORING[place]
        teams[swimmer.team].add_points(points)
