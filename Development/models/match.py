class Match:

    def __init__(self, team_1, score_1, score_2, team_2, id = None):
        self.team_1 = team_1
        self.score_1 = score_1
        self.score_2 = score_2
        self.team_2 = team_2
        self.id = id 

    def win_loss(self):
        if self.score_1 > self.score_2:
            return self.team_1
        if self.score_2 > self.score_1:
            return self.team_2
        if self.score_1 == self.score_2:
            return "Draw"