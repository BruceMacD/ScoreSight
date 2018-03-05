# store each running game as an object with both teams and their scores
class GameStatus:
    def __init__(self, team_a, team_b, score_a, score_b):
        self.team_a = team_a
        self.team_b = team_b
        self.score_a = score_a
        self.score_b = score_b
