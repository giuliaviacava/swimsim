from configuration import MAX_EVENTS_PER_SWIMMER, ENTRIES_PER_TEAM_PER_EVENT


def assign_events_for_team(team, event_names):
    """
    Force every swimmer into 3 events if possible.

    Pass 1:
    - Build the strongest lineup by assigning the fastest legal swims.

    Pass 2:
    - Force each swimmer up to 3 events by replacing the slowest current
      swimmer in an event if needed.

    This guarantees swimmers get 3 events whenever they have at least 3
    available event times.
    """

    for swimmer in team.swimmers:
        swimmer.clear_assignments()

    event_entries = {event_name: [] for event_name in event_names}

    # PASS 1: strongest lineup first
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
                if len(event_entries[event_name]) >= ENTRIES_PER_TEAM_PER_EVENT:
                    continue

                time = swimmer.best_time_for(event_name)

                if best_time is None or time < best_time:
                    best_time = time
                    best_choice = (swimmer, event_name)

        if best_choice is None:
            break

        swimmer, event_name = best_choice
        swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
        event_entries[event_name].append(swimmer)

    # PASS 2: force everyone to 3 events if possible
    for swimmer in team.swimmers:
        possible_events = [
            event_name for event_name in event_names
            if swimmer.can_swim(event_name)
        ]

        while len(swimmer.assigned_events) < MAX_EVENTS_PER_SWIMMER:
            remaining_events = [
                event_name for event_name in possible_events
                if event_name not in swimmer.assigned_events
            ]

            if not remaining_events:
                break

            # Try easiest event to insert swimmer into:
            # first prefer events with open slots, then replace the slowest swimmer
            remaining_events.sort(key=lambda event_name: swimmer.best_time_for(event_name))

            assigned = False

            for event_name in remaining_events:
                # Case 1: open slot
                if len(event_entries[event_name]) < ENTRIES_PER_TEAM_PER_EVENT:
                    swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                    event_entries[event_name].append(swimmer)
                    assigned = True
                    break

                # Case 2: event is full, replace slowest swimmer if needed
                current_swimmers = event_entries[event_name]

                slowest_swimmer = max(
                    current_swimmers,
                    key=lambda s: s.best_time_for(event_name)
                )

                # Only replace someone who has more than 1 assigned event,
                # so we do not strand them with zero events.
                if len(slowest_swimmer.assigned_events) > 1:
                    current_swimmers.remove(slowest_swimmer)
                    slowest_swimmer.assigned_events.remove(event_name)

                    swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                    current_swimmers.append(swimmer)

                    assigned = True
                    break

            if not assigned:
                break


def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, event_names)
