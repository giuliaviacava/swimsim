class Team:
    def __init__(self, name):
        self.name = name
        self.swimmers = []
        self.score = 0

    def add_swimmer(self, swimmer):
        self.swimmers.append(swimmer)

    def add_points(self, points):
        self.score += points

    def __str__(self):
        return f"Team({self.name}, score={self.score})"
