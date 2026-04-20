### swimsim/configuration.py
'''
Defines what events exist, how scoring works, participation limits, random add/drop time variations
'''

EVENTS = ["50 Free", "100 Free", "200 Free", "500 Free", "1000 Free", "100 Back", "200 Back", "100 Breast", "200 Breast", "100 Fly", "200 Fly", "200 IM", "400 IM",]
SCORING = [9, 4, 3, 2, 1]

MAX_EVENTS_PER_SWIMMER = 3
ENTRIES_PER_TEAM_PER_EVENT = 3

MIN_VARIATION = -0.02
MAX_VARIATION = 0.05
