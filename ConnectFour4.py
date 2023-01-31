import random  
from ConnectFour3 import *


class AIPlayer(Player):
    """one that uses techniques from AI to choose its next move"""
    
    
    def __init__(self, checker, tiebreak, lookahead):
        """construct a new AIPlayer object"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        
        self.tiebreak = tiebreak
        self.lookahead = lookahead
        

    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        ai = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return ai
    

    def max_score_column(self, scores):
        """returns the index of the column with the maximum score"""
        score = []
        maxscores = max(scores)
        for s in range(len(scores)):
            if scores[s] == maxscores:
                score += [s]
        #tiebreak score index
        if self.tiebreak == 'RANDOM':
            return random.choice(score)
        elif self.tiebreak == 'LEFT':
            return score[0]
        elif self.tiebreak == 'RIGHT':
            return score[-1]


    def scores_for(self, b):
        """determines the called AIPlayer's scores for the columns in b- returns a list containing one score for each column"""
        scores  = [50] * b.width
        for col in range(b.width):
            #current column full
            if b.can_add_to(col) == False:
                scores[col] = -1
            #already win for AIPlayer
            elif b.is_win_for(self.checker) == True:
                scores[col] = 100
            #already win for player's opponent
            elif b.is_win_for(self.opponent_checker()) == True:
                scores[col] = 0
            #lookahead of 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                #add checker
                b.add_checker(self.checker, col)
                #opponent with self.lookahead - 1
                oponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = oponent.scores_for(b)
                #what score self should use for the current column
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                elif max(opp_scores) == 50:
                    scores[col] = 50
                b.remove_checker(col)
        return scores


    def next_move(self, b):
        """overrides the next_moves method that is inherited from Player- return the called AIPlayer's judgement of its best possible move"""
        self.num_moves += 1
        return self.max_score_column(self.scores_for(b))
    
                
                
        
    
        
        