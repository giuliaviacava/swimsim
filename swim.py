"""
load swimmer data

for each swimmer:
    store best times for all events they can swim

assign events before the meet starts:
    choose up to 3 events for each swimmer
    try to build the strongest overall lineup for each team (based on meet scoring system)

for each event in the meet:
    collect all swimmers assigned to that event

    for each swimmer in the event:
        start with their best time
        add a small random change to simulate race-day performance

    rank swimmers by simulated time
    give points based on place
    print event results

add up total team scores
print final winner
"""

from SwimScraper import SwimScraper as ss

class Swimmer:
    """
    Represents one swimmer.
    Stores:
    - name
    - team
    - best times (event, time)
    - assigned events (max 3)
    """


class Meet:
    """
    Represents the meet.

    Scoring:
    1st = 9, 2nd = 4, 3rd = 3, 4th = 2, 5th = 1
    """

    def load_data():
        """
        load swimmer data and create Swimmer objects
        """

    def assign_events():
        """
        assign up to 3 events per swimmer

        idea:
        - try to build strongest lineup for each team
        """

    def generate_swimmer_time():
        """
        Generate a simulated race time for ONE swimmer.
        Steps:
        - get swimmer's best time for this event
        - add a small random variation (faster or slower)
        - return the new simulated time
        """

    def simulate_event():
        """
        - loop through swimmers in this event, generate_swimmer_time() for each
        - rank swimmers
        - give points
        - print event results
        - update team scores
        """

    def simulate_meet():
        """
        - loop through all events, call simulate_event for each
        """

    def print_final_results():
        """
        print team scores and winner
        """
