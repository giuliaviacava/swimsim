### swimsim/meet.py

'''
Meet object
assign teams
simulate all events
convert times from seconds, milliseconds back to minutes, seconds, milliseconds
print all results
'''
from event import Event

class Meet:
    def __init__(self, teams, event_names):
        self.teams = teams
        self.event_names = event_names
        self.events = [Event(name) for name in event_names]
