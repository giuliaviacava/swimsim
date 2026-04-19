class Swimmer:
    def __init__(self, name, team, best_times):
        self.name = name
        self.team = team
        self.best_times = best_times
        self.assigned_events = []

    def can_swim(self, event_name):
        return event_name in self.best_times

    def best_time_for(self, event_name):
        return self.best_times.get(event_name)

    def has_room(self, max_events):
        return len(self.assigned_events) < max_events

    def is_assigned(self, event_name):
        return event_name in self.assigned_events

    def assign_event(self, event_name, max_events):
        if not self.can_swim(event_name):
            return False
        if self.is_assigned(event_name):
            return False
        if not self.has_room(max_events):
            return False

        self.assigned_events.append(event_name)
        return True

    def clear_assignments(self):
        self.assigned_events = []

    def __repr__(self):
        return f"Swimmer({self.name}, {self.team})"
