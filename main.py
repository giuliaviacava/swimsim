import csv

from swim import Swimmer
from team import Team
from meet import Meet
from configuration import EVENTS


def load_teams_from_txt(filename):
    teams = {}

    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"].strip()
            team_name = row["team"].strip()

            best_times = {}
            for event in EVENTS:
                value = row[event].strip()
                if value != "NA":
                    best_times[event] = float(value)

            swimmer = Swimmer(name, team_name, best_times)

            if team_name not in teams:
                teams[team_name] = Team(team_name)

            teams[team_name].add_swimmer(swimmer)

    return teams


def main():
    filename = "rosters.txt"

    all_teams = load_teams_from_txt(filename)

    selected_team_names = ["Harvard", "Princeton"]
    teams = {}

    for team_name in selected_team_names:
        if team_name not in all_teams:
            print(f"Error: team '{team_name}' not found in {filename}")
            return
        teams[team_name] = all_teams[team_name]

    meet = Meet(teams, EVENTS)
    meet.assign_events()
    meet.simulate_meet()
    meet.print_final_results()


if __name__ == "__main__":
    main()
