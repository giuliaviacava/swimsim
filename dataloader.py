import csv

from swim import Swimmer
from team import Team
from configuration import EVENTS


def load_teams_from_csv(filename):
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
