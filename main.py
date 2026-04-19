from configuration import EVENTS
from dataloader import load_teams_from_csv
from meet import Meet


def main():
    filename = "rosters.csv"

    teams = load_teams_from_csv(filename)

    meet = Meet(teams, EVENTS)
    meet.assign_events()
    meet.simulate_meet()
    meet.print_final_results()


if __name__ == "__main__":
    main()
