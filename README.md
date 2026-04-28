##🏊 SwimSim — Ivy League Dual Meet Simulator##
SwimSim is a Python-based simulator that models a women's collegiate dual swim meet between any two Ivy League schools. It uses real 
swimmer roster data (best times from competition), automatically builds optimal event lineups for each team, simulates race-day 
performance with realistic time variation, and outputs a full meet result with point totals and a winner.

##What is a Dual Meet?##
A dual meet is a head-to-head swim competition between exactly two teams. Swimmers compete across a set of standard events, and points are 
awarded based on finishing place. The team with the most total points at the end wins. Each swimmer may enter a maximum of 3 events.

Project Features

-Reads real roster and best-time data for all 8 Ivy League women's swim programs
-Automatically assigns each swimmer to up to 3 optimal events using projected placement logic
-Simulates race-day performance with realistic time variation (swimmers can go a best time or have a slightly off day)
-Scores each event using standard dual meet point rules
-Prints a full meet recap: event results, point awards, team totals, and winner
-Fully modular — each concern (data, lineup logic, simulation, scoring) lives in its own file


File Structure
swimsim/
├── main.py              # Entry point — user input, team loading, meet orchestration
├── swim.py              # Swimmer class — name, team, best times, event assignments
├── team.py              # Team class — roster management, score tracking
├── event.py             # Event class — entries and results for a single event
├── meet.py              # Meet class — orchestrates lineup assignment, simulation, output
├── lineupbuilder.py     # Lineup logic — assigns each swimmer to their best 3 events
├── simulator.py         # Race simulation — generates race times and awards points
├── configuration.py     # Central config — list of events and scoring values
└── rosters.txt          # Swimmer data — names, teams, best times across all events


##main.py — Entry Point##
The script the user runs. It:
-Prints a welcome message and lists valid schools
-Prompts the user to select two different Ivy League schools
-Calls get_teams() to parse the roster file and build all team/swimmer objects
-Filters down to only the two selected teams
-Creates a Meet object and runs the full simulation pipeline

##swim.py — Swimmer##
The Swimmer class is the core data object. Each swimmer stores:
-Their name and team name
-A dictionary of {event_name: best_time_in_seconds} for every event they have a recorded time in
-A list of assigned events (populated by the lineup builder)

Key methods: can_swim(event), best_time_for(event), assign_event(event), has_room(), is_assigned(event).

##team.py — Team##
The Team class stores a list of Swimmer objects and a running points total. Points are added via add_points() as events are simulated.

##event.py — Event##
Each Event object represents one swimming event (e.g., "100 Free"). It holds a list of swimmers entered and a list of results (swimmer, time pairs) after simulation.

##meet.py — Meet##
The Meet class ties everything together:
-Holds the two competing teams and one Event object per event
-assign_events() delegates to lineupbuilder to fill each swimmer's schedule
-simulate_meet() populates each event with its assigned swimmers, runs the simulation, and prints results
-print_final_results() sorts teams by score and declares a winner
-format_time() converts raw seconds to M:SS.ms display format

##lineupbuilder.py — Lineup Assignment##
This module handles the strategic question: which 3 events should each swimmer compete in?
For every swimmer, it:
-Loops through every event the swimmer is capable of swimming
-Computes a projected placement by comparing the swimmer's best time against the best times of all other swimmers entered from both teams
-Stores (projected_place, best_time, event_name) tuples
-Sorts by projected placement (ascending — best expected finish first)
-Assigns the top 3 events where the swimmer is projected to do best

projected_place() counts how many swimmers have a faster best time in that event, giving a rough competitive ranking before the meet begins.

##simulator.py — Race Simulation##
This is where the randomness lives. For each swimmer in an event:
-Their best time is multiplied by a random factor drawn uniformly from [-2%, +5%], meaning that swimmers always have a chance to go a personal 
best (-2%) but are more likely to swim slightly slower than their best (+5% upside is larger)
-Results are sorted fastest to slowest
-The top 5 finishers receive points per the SCORING list; points are added to the swimmer's team total

##configuration.py — Configuration##
Defines the master list of 13 swim events and the dual meet scoring array. Centralizing these here makes it easy to adjust without touching simulation logic.

##rosters.txt — Data File##
A CSV-formatted file with one row per swimmer. Columns are:
name, team, 50 Free, 100 Free, 200 Free, 500 Free, 1000 Free, 100 Back, 200 Back, 100 Breast, 200 Breast, 100 Fly, 200 Fly, 200 IM, 400 IM
Times are stored in decimal seconds (e.g., 49.47 for a 49.47-second 100 Free). Events where a swimmer has no recorded time are marked NA.

