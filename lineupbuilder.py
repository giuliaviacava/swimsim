### swimsim/lineupbuilder.py

from configuration import SCORING

# Estimate where a given swimmer would place in the dual meet for this event using everyone's best times
def projected_place(swimmer, event_name, teams):
    all_times = []

    for team in teams.values():
        for other_swimmer in team.swimmers:
            if other_swimmer.can_swim(event_name):
                all_times.append(other_swimmer.best_time_for(event_name))
    all_times.sort()
    swimmer_time = swimmer.best_time_for(event_name)
    place = 1
    for time in all_times:
        if time < swimmer_time:
            place += 1
        else:
            break
    return place

def assign_events_for_team(team, teams, event_names):
    for swimmer in team.swimmers:
        possible_events = []

        for event_name in event_names:
            if swimmer.can_swim(event_name):
                place = projected_place(swimmer, event_name, teams)
                best_time = swimmer.best_time_for(event_name)
                possible_events.append((place, best_time, event_name))

        possible_events.sort()

        for place, best_time, event_name in possible_events:
            if len(swimmer.assigned_events) >= 3:
                break
            swimmer.assign_event(event_name)

def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, teams, event_names)
