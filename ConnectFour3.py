from ConnectFour1 import Board
from ConnectFour2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the class Player or a subclass of Player).
          One player should use 'X' checkers and the other player should
          use 'O' checkers. """

    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b


def process_move(p, b):
    """performs all the steps involved in processing a single move by player p on board b"""
    #specify whose turn
    print(p, "'s turn")
    move = p.next_move(b)
    b.add_checker(p.checker, move)
    print()
    print(b)
    #if it's a win
    if b.is_win_for(p.checker) == True:
        print(p, "wins in", p.num_moves, "moves.")
        print("Congratulations!")
        return True
    #if it's a tie when the board is full
    if b.is_full() == True:
        print("It's a tie!")
        return True
    else:
        return False
    

class RandomPlayer(Player):
    """can be used for an unintellligent computer player that chooses at randoom from the available columns"""
   
    def next_move(self,b):
        """overrides the next_move method that's inherited from Player- return the index of the randomly selected column"""
        availablec = []
        self.num_moves += 1
        for c in range(b.width):
            if b.can_add_to(c) == True:
                availablec += [c]
        randomc = random.choice(availablec)
        return randomc
    