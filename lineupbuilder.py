from configuration import MAX_EVENTS_PER_SWIMMER, ENTRIES_PER_TEAM_PER_EVENT


def assign_events_for_team(team, event_names):
    """
    Each team builds its own strongest lineup without looking at the opponent.

    Strategy:
    - clear old assignments
    - repeatedly choose the fastest remaining legal swim
    - respect:
        * max 3 events per swimmer
        * max 3 entries per team per event
    """

    for swimmer in team.swimmers:
        swimmer.clear_assignments()

    event_entry_counts = {event_name: 0 for event_name in event_names}

    while True:
        best_choice = None
        best_time = None

        for swimmer in team.swimmers:
            if not swimmer.has_room(MAX_EVENTS_PER_SWIMMER):
                continue

            for event_name in event_names:
                if not swimmer.can_swim(event_name):
                    continue
                if swimmer.is_assigned(event_name):
                    continue
                if event_entry_counts[event_name] >= ENTRIES_PER_TEAM_PER_EVENT:
                    continue

                time = swimmer.best_time_for(event_name)

                if best_time is None or time < best_time:
                    best_time = time
                    best_choice = (swimmer, event_name)

        if best_choice is None:
            break

        swimmer, event_name = best_choice
        swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
        event_entry_counts[event_name] += 1


def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, event_names)
