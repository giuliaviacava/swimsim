### swimsim/meet.py

from event import Event
from lineupbuilder import assign_all_teams
from simulator import simulate_event
from configuration import SCORING

class Meet:
    # Initializes meet by storing competing teams, list of events, creates Event object for each event
    def __init__(self, teams, event_names):
        self.teams = teams
        self.event_names = event_names
        self.events = [Event(name) for name in event_names]

    # Converts from seconds into minutes, seconds, milliseconds
    def format_time(self, seconds):
        if seconds < 60:
            return f"{seconds:.2f}"
        minutes = int(seconds // 60)
        remaining = seconds % 60
        return f"{minutes}:{remaining:05.2f}"

    # Assigns swimmers from each team to events (use method from lineupbuilder), prints assignments
    def assign_events(self):
        assign_all_teams(self.teams, self.event_names)
        print("\n----- EVENT ASSIGNMENTS -----")
        for team in self.teams.values():
            print(f"\n{team.name}")
            for swimmer in team.swimmers:
                print(f"{swimmer.name}: {swimmer.assigned_events}")

    # If swimmer is assigned to event then add the swimmer to event, then simulate event (using method from simulator), print event results
    def simulate_meet(self):
        for event in self.events:
            for team in self.teams.values():
                for swimmer in team.swimmers:
                    if event.name in swimmer.assigned_events:
                        event.add_entry(swimmer)

        for event in self.events:
            simulate_event(event, self.teams)
            print(f"\n----- {event.name} -----")
            if not event.results:
                print("No swimmers entered.")
                continue
            for place, (swimmer, time) in enumerate(event.results, start=1):
                formatted_time = self.format_time(time)
                if place <= len(SCORING):
                    points = SCORING[place - 1]
                    print(f"{place}. {swimmer.name} ({swimmer.team}) - {formatted_time} [+{points} pts]")
                else:
                    print(f"{place}. {swimmer.name} ({swimmer.team}) - {formatted_time}")

            print("\n  Running score:")
            for team_name, team in self.teams.items():
                print(f"  {team_name}: {team.score}")

    # Sorts teams by score from highest to lowest, prints each team and final score, then winner
    def print_final_results(self):
        print("\n----- FINAL TEAM SCORES -----")
        ranked_teams = sorted(
            self.teams.values(),
            key=lambda team: team.score,
            reverse=True
        )
        for team in ranked_teams:
            print(f"{team.name}: {team.score}")
        print(f"\nWinner: {ranked_teams[0].name}")

        print("\n----- SCORE CHART -----")
        max_score = max(team.score for team in ranked_teams)
        for team in ranked_teams:
            bar = "█" * int((team.score / max_score) * 40)
            print(f"{team.name:<12} | {bar:<40} {team.score}")
