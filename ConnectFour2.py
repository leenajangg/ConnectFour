from ConnectFour1 import Board


class Player:
    def __init__(self, checker):
        """constructs a new Player object by initializing 2 attributes (checker, num_moves)"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0
    
    def __repr__(self):
        """returns a string representing a Player object"""
        po = 'Player ' + self.checker
        return po
    
    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s opponent"""
        if self.checker == 'X':
            return 'O'
        elif self.checker == 'O':
            return 'X'
        
    def next_move(self, b):
        """returns the column where the player wants to make the next move"""        
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if b.can_add_to(col) == True:
                return col
            else:
                print('Try again!')
            
        
