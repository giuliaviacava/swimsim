from configuration import EVENTS
from dataloader import load_teams_from_csv
from meet import Meet


def main():
    filename = "rosters.txt"

    all_teams = load_teams_from_csv(filename)

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
