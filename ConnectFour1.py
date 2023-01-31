class Board:
    """ a data type for a Connect Four board with arbitrary dimensions"""   
    
    def __init__(self, height, width):
        """contructs a new Board object by initializing attributes (height, width, and slots)"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]


    def __repr__(self):
        """ Returns a string that represents a Board object. """
        s = ''  
        for row in range(self.height):
            s += '|'  

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  


        
        for h in range(self.width):
            s += '--'
        s += '-'
        s += '\n'
        for cl in range(self.width):
            labels = [' 0 ', '1 ', '2 ', '3 ', '4 ', '5 ', '6 ', '7 ', '8 ', '9 ']
            if cl > 9:
                cl = cl % 10
            s += labels[cl]
        
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1
        self.slots[row][col] = checker

    
    def reset(self):
        """reset the Board object on which is called by setting all slots to contain a space character"""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'


    def can_add_to(self, col):
        """returns True if it's valid to place a checker in the column col on the calling Board object, otherwise return False"""
        row = 0
        if col < 0:
            return False
        elif col >= self.width:
            return False
        elif self.slots[row][col] == ' ':
            return True
        else:
            return False
        

    def is_full(self):
        """returns True if the called Board object is completely full of checkers, otherwise return False"""
        for row in range(self.height):
            for col in range(self.width):
                if self.slots[row][col] == ' ':
                    return False
        return True


    def remove_checker(self, col):
        """removes the top checker from column col of the called Board object. If column is empty, nothing happens"""
        for row in range(self.height):
            if self.slots[row][col] != ' ':
                self.slots[row][col] = ' '
                break
            

    def is_win_for(self, checker):
        """accepts a parameter checker that is either 'X' or 'O', and returns True if there are 4 consecutive slots containing checker on the board, otherwise return False"""
        assert(checker == 'X' or checker == 'O')
        
        if checker == 'X':
            horiz = self.is_horizontal_win('X')
            vert = self.is_vertical_win('X')
            ddiag = self.is_down_diagonal_win('X')
            udiag = self.is_up_diagonal_win('X')
            if horiz == True or vert == True or ddiag == True or udiag == True:
                return True
            else:
                return False
        elif checker == 'O':
            horiz = self.is_horizontal_win('O')
            vert = self.is_vertical_win('O')
            ddiag = self.is_down_diagonal_win('O')
            udiag = self.is_up_diagonal_win('O')
            if horiz == True or vert == True or ddiag == True or udiag == True:
                return True
            else:
                return False
            

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker"""
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
        return False


    def is_vertical_win(self, checker):
        """Checks for a vertical win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                        return True
        return False
    

    def is_down_diagonal_win(self, checker):
        """Checks for diagonals that go down from left to right win for the specified checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                        return True
        return False
    

    def is_up_diagonal_win(self, checker):
        """Checks for diagonals that go up from left to right win for the specified checker"""
        for row in range(3, self.height):   
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                       return True
        return False
    
#test function  
def test():
    b = Board(6, 7)
    print(b)
