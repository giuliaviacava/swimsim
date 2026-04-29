### swimsim/lineupbuilder.py

from configuration import SCORING

MAX_PER_EVENT= 4

# Estimate where a given swimmer would place in the dual meet for this event using everyone's best times
def projected_place(swimmer, event_name, teams):
    all_times = []
    # Loop through each swimmer on each team, if swimmer has time in given event add their best time to list
    for team in teams.values():
        for other_swimmer in team.swimmers:
            if other_swimmer.can_swim(event_name):
                all_times.append(other_swimmer.best_time_for(event_name))
    # Sort times from fastest to slowest
    all_times.sort()
    # Get best time of a given swimmer, count how many swimmers are faster than this swimmer, return estimated placement
    swimmer_time = swimmer.best_time_for(event_name)
    place = 1
    for time in all_times:
        if time < swimmer_time:
            place += 1
        else:
            break
    return place

# Assign events for one team
def assign_events_for_team(team, teams, event_names, event_counts):
    # For every swimmer on a given team, loop through every event
    for swimmer in team.swimmers:
        possible_events = []
        for event_name in event_names:
            if not swimmer.can_swim(event_name):
                continue
            if event_counts[team.name].get(event_name, 0) >= MAX_PER_EVENT: 
                continue
                # Get swimmer's estimated placement in this event, their best time, then store (place, time, event) in list of possible events they could swim
            place = projected_place(swimmer, event_name, teams)
            best_time = swimmer.best_time_for(event_name)
            possible_events.append((place, best_time, event_name))
        # Sort events by best placement
        possible_events.sort()
        # Assign swimmer to 3 events
        for place, best_time, event_name in possible_events:
            if len(swimmer.assigned_events) >= 3:
                break
            if event_counts[team.name].get(event_name, 0) >= MAX_PER_EVENT: 
                continue
            if swimmer.assign_event(event_name):
                event_counts[team.name][event_name]=\
                    event_counts[team.name].get(event_name, 0)+1

# Assign events for each team
def assign_all_teams(teams, event_names):
    event_counts = {team_name: {} for team_name in teams}
    for team in teams.values():
        assign_events_for_team(team, teams, event_names, event_counts)
