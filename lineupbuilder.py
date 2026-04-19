from configuration import MAX_EVENTS_PER_SWIMMER, ENTRIES_PER_TEAM_PER_EVENT


def assign_events_for_team(team, event_names):
    """
    Force every swimmer into exactly 3 real events if possible.

    Pass 1:
    - Give every swimmer 3 events based on their best available times.

    Pass 2:
    - Fill remaining event slots with the fastest available swimmers,
      while still respecting max 3 events per swimmer.
    """

    for swimmer in team.swimmers:
        swimmer.clear_assignments()

    event_entries = {event_name: [] for event_name in event_names}

    # PASS 1: guarantee each swimmer gets up to 3 real events
    for swimmer in team.swimmers:
        possible_events = [
            event_name for event_name in event_names
            if swimmer.can_swim(event_name)
        ]

        possible_events.sort(key=lambda event_name: swimmer.best_time_for(event_name))

        for event_name in possible_events:
            if len(swimmer.assigned_events) >= MAX_EVENTS_PER_SWIMMER:
                break

            # only add if swimmer not already assigned there
            if event_name not in swimmer.assigned_events:
                swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                event_entries[event_name].append(swimmer)

    # PASS 2: trim overcrowded events by keeping the fastest swimmers
    for event_name in event_names:
        event_entries[event_name].sort(key=lambda swimmer: swimmer.best_time_for(event_name))

        while len(event_entries[event_name]) > ENTRIES_PER_TEAM_PER_EVENT:
            removed_swimmer = event_entries[event_name].pop()
            removed_swimmer.assigned_events.remove(event_name)

    # PASS 3: after trimming, restore everyone back to 3 events if possible
    changed = True
    while changed:
        changed = False

        for swimmer in team.swimmers:
            if len(swimmer.assigned_events) >= MAX_EVENTS_PER_SWIMMER:
                continue

            possible_events = [
                event_name for event_name in event_names
                if swimmer.can_swim(event_name)
                and event_name not in swimmer.assigned_events
            ]

            possible_events.sort(key=lambda event_name: swimmer.best_time_for(event_name))

            for event_name in possible_events:
                # open slot
                if len(event_entries[event_name]) < ENTRIES_PER_TEAM_PER_EVENT:
                    swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                    event_entries[event_name].append(swimmer)
                    changed = True
                    break

                # otherwise replace the slowest swimmer in that event,
                # but only if the slowest swimmer has more than 3 events? no,
                # since we cap at 3, only replace if they are slower and can be repaired later
                slowest_swimmer = max(
                    event_entries[event_name],
                    key=lambda s: s.best_time_for(event_name)
                )

                if swimmer.best_time_for(event_name) < slowest_swimmer.best_time_for(event_name):
                    event_entries[event_name].remove(slowest_swimmer)
                    slowest_swimmer.assigned_events.remove(event_name)

                    swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                    event_entries[event_name].append(swimmer)
                    changed = True
                    break

    # FINAL PASS: one more repair attempt for anyone still below 3
    for swimmer in team.swimmers:
        while len(swimmer.assigned_events) < MAX_EVENTS_PER_SWIMMER:
            possible_events = [
                event_name for event_name in event_names
                if swimmer.can_swim(event_name)
                and event_name not in swimmer.assigned_events
            ]

            if not possible_events:
                break

            possible_events.sort(key=lambda event_name: swimmer.best_time_for(event_name))

            assigned = False

            for event_name in possible_events:
                if len(event_entries[event_name]) < ENTRIES_PER_TEAM_PER_EVENT:
                    swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)
                    event_entries[event_name].append(swimmer)
                    assigned = True
                    break

            if not assigned:
                break


def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, event_names)
