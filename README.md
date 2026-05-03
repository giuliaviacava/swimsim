SwimSim — Ivy League Dual Meet Simulator
SwimSim is a Python-based simulator that models a women's collegiate dual swim meet between any two Ivy League schools. It uses real swimmer roster data (best times from competition), builds optimal event lineups for each team, simulates race-day performance with realistic time variation, and outputs a full meet result with point totals and a winner.


TO RUN:
Just type: python main.py


What is a Dual Meet?
A dual meet is a head-to-head swim competition between exactly two teams. Swimmers compete across a set of standard events, and points are awarded based on finishing place. The team with the most total points at the end wins. Each swimmer may enter a maximum of 3 events, and up to 4 swimmers per team may enter each individual event.
Scoring System: (1st: 9 pts) (2nd: 4 pts) (3rd: 3 pts) (4th: 2 pts) (5th: 1 pt) (6th+: 0 pts)


Project Features
- Reads real roster and best-time data for all 8 Ivy League women's swim programs
- Automatically assigns each swimmer to up to 3 optimal events using projected placement logic
- Simulates race-day performance with realistic time variation (swimmers can go a best time or have a slightly off day)
- Scores each event using standard dual meet point rules
- Prints a full meet recap: event results, point awards, team totals, and winner


File Structure
swimsim/
- main.py              Entry point — user input, team loading, runs meet
- swim.py              Swimmer class — name, team, best times, event assignments
- team.py              Team class — roster management, score tracking
- event.py             Event class — entries and results for a single event
- meet.py              Meet class — runs lineup assignment, simulates events
- lineupbuilder.py     Lineup logic — assigns each swimmer to their best 3 events
- simulator.py         Race simulation — generates race times and awards points
- configuration.py     List of events and scoring values
- rosters.txt          Swimmer data — names, teams, best times across all events


main.py
The script the user runs.
- Prints a welcome message and lists Ivy League schools
- Prompts the user to select two different Ivy League schools
- Parses through the roster text file and builds all team/swimmer objects
- Filters down to only the two selected teams
- Creates a Meet object and runs the full simulation pipeline

swim.py
Each swimmer object stores: 
- Their name and team name
- A dictionary of {event_name: best_time_in_seconds} for every event they have a recorded time in
- A list of assigned events (populated by the lineup builder)

team.py
- Stores a list of Swimmer objects and a running points total, points are added via add_points() as events are simulated

event.py
- Represents one swimming event, holds a list of swimmers entered and a list of results (swimmer, time pairs) after simulation

meet.py
- Holds the two competing teams and one Event object per event
- Uses method from lineupbuilder to assign each swimmer's events
- Adds assigned swimmer to each event, runs the simulation, and prints results (converts seconds to M:SS.ms display format)
- Sorts teams by score and declares a winner

lineupbuilder.py
For each swimmer: 
- Loops through every event the swimmer is capable of swimming
- Computes a projected placement by comparing the swimmer's best time against the best times of all other swimmers entered from both teams
- Stores (projected_place, best_time, event_name) tuples
- Sorts by projected placement (best to worst)
- Assigns the top 3 events where the swimmer is projected to do best

simulator.py
For each swimmer in an event:
- Best time is multiplied by a variation drawn from a truncated normal distribution centered at +1% above their best time with a standard deviation of 1.5%. This makes ordinary swims common, PRs rare but possible, and disaster races very rare. Hard limits of −2% and +6%
- Results are sorted fastest to slowest
- The top 5 finishers receive points according to scoring system, points are added to the swimmer's team total

configuration.py
Defines the master list of 13 swim events and the dual meet scoring system. Putting these variables here makes it easy call them in other files.

rosters.txt
A text file with one row per swimmer. The columns are:
name, team, 50 Free, 100 Free, 200 Free, 500 Free, 1000 Free, 100 Back, 200 Back, 100 Breast, 200 Breast, 100 Fly, 200 Fly, 200 IM, 400 IM
Times are stored in decimal seconds. Events where a swimmer has no recorded time are marked NA. We used AI to help format this file by inputting swimmer data from Swimcloud into ChatGPT and asking it to organize the information according to the specified column format.
