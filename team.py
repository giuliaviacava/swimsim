class Team:
    """
    Represents one team.
    Stores:
    - name
    - swimmers
    - score
    """

    def __init__(self, name):
        self.name = name
        self.swimmers = []
        self.score = 0

    def add_swimmer(self, swimmer):
        self.swimmers.append(swimmer)

    def add_points(self, points):
        self.score += points

    def reset_score(self):
        self.score = 0

    def clear_all_assignments(self):
        for swimmer in self.swimmers:
            swimmer.clear_assignments()

    def __repr__(self):
        return f"Team(name={self.name}, score={self.score})"
