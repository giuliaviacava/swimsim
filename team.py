### swimsim/team.py

class Team:
    # Initializes team using name of team, creates empty list to store all swimmers on team, set team score to 0
    def __init__(self, name):
        self.name = name
        self.swimmers = []
        self.score = 0

    # Add a swimmer to the team's list of swimmers
    def add_swimmer(self, swimmer):
        self.swimmers.append(swimmer)

    # Increase team score by the given number of points
    def add_points(self, points):
        self.score += points

    # Return a string showing the team name and current score
    def __str__(self):
        return f"Team({self.name}, score={self.score})"
