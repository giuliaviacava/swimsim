from configuration import MAX_EVENTS_PER_SWIMMER, ENTRIES_PER_TEAM_PER_EVENT


def assign_events_for_team(team, event_names):
    """
    Assign exactly 3 events per swimmer if possible.

    Strategy:
    1. Clear previous assignments
    2. First pass: fill each event with the team's fastest swimmers
    3. Second pass: make sure every swimmer gets up to 3 events
       by adding their best remaining events
    """

    for swimmer in team.swimmers:
        swimmer.clear_assignments()

    # First pass: strongest lineup per event
    event_counts = {event_name: 0 for event_name in event_names}

    for event_name in event_names:
        eligible = [
            swimmer for swimmer in team.swimmers
            if swimmer.can_swim(event_name) and swimmer.has_room(MAX_EVENTS_PER_SWIMMER)
        ]

        eligible.sort(key=lambda swimmer: swimmer.best_time_for(event_name))

        selected = eligible[:ENTRIES_PER_TEAM_PER_EVENT]

        for swimmer in selected:
            if swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER):
                event_counts[event_name] += 1

    # Second pass: ensure each swimmer gets exactly 3 events if possible
    for swimmer in team.swimmers:
        while len(swimmer.assigned_events) < MAX_EVENTS_PER_SWIMMER:
            possible_events = [
                event_name for event_name in event_names
                if swimmer.can_swim(event_name)
                and event_name not in swimmer.assigned_events
            ]

            if not possible_events:
                break

            # Choose swimmer's fastest remaining event
            possible_events.sort(key=lambda event_name: swimmer.best_time_for(event_name))
            best_event = possible_events[0]

            swimmer.assign_event(best_event, MAX_EVENTS_PER_SWIMMER)
            event_counts[best_event] += 1


def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, event_names)
