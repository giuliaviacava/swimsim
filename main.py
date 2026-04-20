from swim import Swimmer
from team import Team
from meet import Meet
from configuration import EVENTS

def get_teams(filename):
    teams = {}
    with open(filename, "r", encoding="utf-8") as file:
        header = file.readline().strip().split(",")
        while True:
            line = file.readline()
            if line == "":
                break
            parts = line.strip().split(",")

            row = dict(zip(header, parts))
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
    ivy_schools = ["Harvard", "Princeton", "Yale", "Brown", "UPenn", "Columbia", "Cornell", "Dartmouth"]
    print("WELCOME TO THE IVY LEAGUE DUAL MEET SIMULATOR! \nYour options are: Harvard, Princeton, Yale, Brown, UPenn, Columbia, Cornell, Dartmouth\n")
    while True:
        school1 = input("Choose School #1: ").strip()
        if school1 not in ivy_schools:
            print("Sorry, but this is an Ivy League dual meet simulator. Please choose an Ivy League school.")
            continue
        break
    while True:
        school2 = input("Choose School #2: ").strip()
        if school2 == school1:
            print("You already chose this school for School #1, please choose a different school for School #2.")
            continue
        if school2 not in ivy_schools:
            print("Sorry, but this is an Ivy League dual meet simulator. Please choose an Ivy League school.")
            continue
        break
    all_teams = get_teams(filename)
    teams = {school1: all_teams[school1], school2: all_teams[school2],}

    meet = Meet(teams, EVENTS)
    meet.assign_events()
    meet.simulate_meet()
    meet.print_final_results()

if __name__ == "__main__":
    main()
