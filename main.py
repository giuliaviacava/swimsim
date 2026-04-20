### swimsim/main.py

from swim import Swimmer
from team import Team
from meet import Meet
from configuration import EVENTS

def get_teams(filename):
    teams = {}
    with open(filename, "r", encoding="utf-8") as file:
        # Reads 1st line, creates a list of phrases called header that were separated by commas in the original line (should be name, team, event #1, event #2, ...)
        header = file.readline().strip().split(",")

        while True:
            # Reads a line, creates a list of phrases called parts that were separated by commas in the original line
            line = file.readline()
            if line == "":
                break
            parts = line.split(",")

            # Pairs the 2 lists into a dictionary, creates list of names and list of team names
            row = dict(zip(header, parts))
            name = row["name"]
            team_name = row["team"]

            # Loops through all events, if best time exists then assign best time to event
            best_times = {}
            for event in EVENTS:
                best_time = row[event].strip()
                if best_time != "NA":
                    best_times[event] = float(best_time)

            # Creates Swimmer object, creates Team object if team name is not in list of teams, add swimmer to team
            swimmer = Swimmer(name, team_name, best_times)
            if team_name not in teams:
                teams[team_name] = Team(team_name)
            teams[team_name].add_swimmer(swimmer)
    return teams

def main():
    filename = "rosters.txt"
    ivy_schools = ["harvard", "princeton", "yale", "brown", "upenn", "columbia", "cornell", "dartmouth"]
    print("WELCOME TO THE IVY LEAGUE DUAL MEET SIMULATOR! \nYour options are: Harvard, Princeton, Yale, Brown, UPenn, Columbia, Cornell, Dartmouth\n")

    # Makes user choose 2 schools, prints error message if user types something incorrect
    while True:
        school1 = input("Choose School #1: ").strip().lowercase()
        if school1 not in ivy_schools:
            print("Sorry, but this is an Ivy League dual meet simulator. Please choose an Ivy League school.")
            continue
        break
    while True:
        school2 = input("Choose School #2: ").strip().lowercase()
        if school2 == school1:
            print("You already chose this school for School #1, please choose a different school for School #2.")
            continue
        if school2 not in ivy_schools:
            print("Sorry, but this is an Ivy League dual meet simulator. Please choose an Ivy League school.")
            continue
        break

    # Calls get_teams to read file and create all teams, then stores only the 2 selected teams
    all_teams = get_teams(filename)
    teams = {school1: all_teams[school1], school2: all_teams[school2],}

    '''
    CREATE A MEET OBJECT TO SIMULATE THE MEET
    '''

if __name__ == "__main__":
    main()
