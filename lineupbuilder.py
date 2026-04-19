from configuration import MAX_EVENTS_PER_SWIMMER, ENTRIES_PER_TEAM_PER_EVENT


def assign_events_for_team(team, event_names):
    """
    Simple lineup strategy:
    For each event, choose the team's fastest eligible swimmers,
    while respecting the 3-event maximum.

    This is a good first version.
    Later you can improve it to optimize globally.
    """

    for swimmer in team.swimmers:
        swimmer.clear_assignments()

    for event_name in event_names:
        eligible = [
            swimmer for swimmer in team.swimmers
            if swimmer.can_swim(event_name) and swimmer.has_room(MAX_EVENTS_PER_SWIMMER)
        ]

        eligible.sort(key=lambda swimmer: swimmer.best_time_for(event_name))

        selected = eligible[:ENTRIES_PER_TEAM_PER_EVENT]

        for swimmer in selected:
            swimmer.assign_event(event_name, MAX_EVENTS_PER_SWIMMER)


def assign_all_teams(teams, event_names):
    for team in teams.values():
        assign_events_for_team(team, event_names)
