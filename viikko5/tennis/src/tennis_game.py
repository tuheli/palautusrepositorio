class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_draw_score(self):
        if self.player1_score == 0:
            return "Love-All"
        if self.player1_score == 1:
            return "Fifteen-All"
        if self.player1_score == 2:
            return "Thirty-All"
        
        return "Deuce"
    
    def get_win_score(self):
        score_distance = self.player1_score - self. player2_score

        if score_distance >= 2:
            return "Win for player1"
        
        return "Win for player2"
    
    def get_advantage_score(self):
        score_distance = self.player1_score - self. player2_score

        if score_distance == 1:
            return "Advantage player1"
        
        return "Advantage player2"
    
    def get_normal_score(self):
        score_names = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty',
        }

        return f'{score_names.get(self.player1_score)}-{score_names.get(self.player2_score)}'

    def get_score(self):
        is_draw = self.player1_score == self.player2_score
        if is_draw:
            return self.get_draw_score()

        score_difference = abs(self.player1_score - self.player2_score)
        is_win = (self.player1_score >= 4 or self.player2_score >= 4) and score_difference >= 2
        if is_win:
            return self.get_win_score()
        
        is_advantage = self.player1_score >= 4 or self.player2_score >= 4
        if is_advantage:
            return self.get_advantage_score()
        
        return self.get_normal_score()
