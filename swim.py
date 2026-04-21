### swimsim/swim.py

class Swimmer:
    # Initializes swimmer using name of swimmer, name of team, dictionary of best times, creates empty list for their assigned events
    def __init__(self, name, team, best_times):
        self.name = name
        self.team = team
        self.best_times = best_times
        self.assigned_events = []

    # Checks if swimmer has a recorded time in given event
    def can_swim(self, event_name):
        return event_name in self.best_times

    # Returns swimmer's best time for given event
    def best_time_for(self, event_name):
        return self.best_times.get(event_name)

    # Returns True if number of assigned events is less than max allowed
    def has_room(self):
        return len(self.assigned_events) < 3

    # Returns True if event is already assigned to swimmer
    def is_assigned(self, event_name):
        return event_name in self.assigned_events

    '''Assigns swimmer to an event
    Returns false if swimmer can't swim the event, is already assigned to the event, or has no room for the event
    Otherwise, adds event to assigned_events list and returns true
    '''
    def assign_event(self, event_name):
        if not self.can_swim(event_name):
            return False
        if self.is_assigned(event_name):
            return False
        if not self.has_room():
            return False

        self.assigned_events.append(event_name)
        return True

    # Return a string showing swimmer name and team name
    def __str__(self):
        return f"Swimmer({self.name}, {self.team})"
