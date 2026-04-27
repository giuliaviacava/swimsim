### swimsim/meet.py

from event import Event
from lineupbuilder import assign_all_teams
from simulator import simulate_event
from simulator import SCORING

# Converts from seconds into minutes, seconds, milliseconds
def format_time(seconds):
    if seconds < 60:
        return f"{seconds:.2f}"
    minutes = int(seconds // 60)
    remaining = seconds % 60
    return f"{minutes}:{remaining:05.2f}"


class Meet:
    def __init__(self, teams, event_names):
        self.teams = teams
        self.event_names = event_names
        self.events = [Event(name) for name in event_names]

    def assign_events(self):
        assign_all_teams(self.teams, self.event_names)
        self.check_assignments()

    def check_assignments(self):
        print("\n===== EVENT ASSIGNMENTS =====")
        for team in self.teams.values():
            print(f"\n{team.name}")
            for swimmer in team.swimmers:
                print(f"{swimmer.name}: {swimmer.assigned_events}")

                if len(swimmer.best_times) >= 3:
                    if len(swimmer.assigned_events) != 3:
                        print(
                            f"WARNING: {swimmer.name} should have 3 events "
                            f"but has {len(swimmer.assigned_events)}"
                        )

    def build_event_entries(self):
        for event in self.events:

            for team in self.teams.values():
                for swimmer in team.swimmers:
                    if event.name in swimmer.assigned_events:
                        event.add_entry(swimmer)

    def simulate_meet(self):
        self.build_event_entries()

        for event in self.events:
            simulate_event(event, self.teams)
            self.print_event_results(event)

    def print_event_results(self, event):
        print(f"\n===== {event.name} =====")

        if not event.results:
            print("No swimmers entered.")
            return

        for place, (swimmer, time) in enumerate(event.results, start=1):
            formatted_time = format_time(time)

            if place <= len(SCORING):
                points = SCORING[place - 1]
                print(f"{place}. {swimmer.name} ({swimmer.team}) - {formatted_time} [+{points} pts]")
            else:
                print(f"{place}. {swimmer.name} ({swimmer.team}) - {formatted_time}")

    def print_final_results(self):
        print("\n===== FINAL TEAM SCORES =====")

        ranked_teams = sorted(
            self.teams.values(),
            key=lambda team: team.score,
            reverse=True
        )

        for team in ranked_teams:
            print(f"{team.name}: {team.score}")

        if ranked_teams:
            print(f"\nWinner: {ranked_teams[0].name}")
