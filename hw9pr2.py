#
# hw9pr2.py - Connect Four
#
# Name: Zach Franz
#

class Board:
    """ A user-defined data structure that
        stores and manipulates dates
    """

    def __init__(self, width, height):
        """ the constructor for objects of type Board
        """
        self.data = [[' ' for i in range(width)] for j in range(height)]
        self.height = height
        self.width = width

    def __repr__(self): 
        """ Returns a string representation for an object of type Board. 
        """ 
        s = '' # the string to return 
        for row in range(self.height): 
            s += '|'    # add the spacer character 
            for col in range(self.width): 
                s += self.data[row][col] + '|' 
            s += '\n' 
     
        # *** You add the bottom of the board 
        # and the numbers underneath here ***
        s += '-'
        for col in range(self.width):
            s += '--'
        s += '\n'
        for col in range(self.width):
            s+= ' ' + str(col%10)

        return s      # the board is complete, return it

    def addMove(self,col,xo):
        """ Returns the connect four board with an 'xo' input to the specified column 'col'."""
        assert(xo == 'X' or xo == 'O')
        for i in range(self.height):
            if self.data[self.height-i-1][col] == ' ':
                self.data[self.height-i-1][col] = xo
                return

    def clear(self):
        """ Clears the connect four Board."""
        self.data = [[' ' for i in range(self.width)] for j in range(self.height)]

    def setBoard(self, moveString): 
        """ Takes in a string of columns and places alternating 
            checkers in those columns, starting with 'X'. 

            For example, call board.setBoard('0123456') to see 'X's and 
            'O's alternate on the bottom row, or 
            board.setBoard('000000') to see them alternate in the left
            column. 

            moveString must be a string of integers. 
        """ 
        nextChar = 'X'    # start by playing 'X' 
        for colString in moveString: 
            col = int(colString) 
            if 0 <= col < self.width:
                self.addMove(col, nextChar)
            if nextChar == 'X':
                nextChar = 'O'
            else:
                nextChar = 'X'

    def isMoveLegal(self, col):
        """ Returns True if the connect four move is legal (would be on the board). Returns False otherwise."""
        if col in range(self.width):
            if self.data[0][col] == ' ':
                return True
        return False

    def isFull(self):
        """ Returns True if the connect four Board is full. Returns False otherwise."""
        for col in range(self.width):
            if self.isMoveLegal(col):
                return False
        return True

    def deleteMove(self,col):
        """ Returns the connect four Board with the uppermost X or O removed."""
        for i in range(self.height):
            if self.data[i][col] == 'X' or self.data[i][col] == 'O':
                self.data[i][col] = ' '
                return
            
    def isHorizontalWin(self, ox): 
       """ Returns True if there is a horizontal win for player 'xo'. Returns False otherwise.""" 
       for row in range(self.height): 
           for col in range(self.width - 3): 
               if (self.data[row][col] == self.data[row][col + 1] ==
                   self.data[row][col + 2] == self.data[row][col + 3] == ox):
                   return True 
       return False

    def isVerticalWin(self, ox): 
       """ Returns True if there is a vertical win for player 'xo'. Returns False otherwise.""" 
       for col in range(self.width): 
           for row in range(self.height - 3): 
               if (self.data[row][col] == self.data[row+1][col] ==
                   self.data[row + 2][col] == self.data[row + 3][col] == ox):
                   return True 
       return False

    def isPosSlopeDiagWin(self, ox): 
       """ Returns True if there is a positive sloping diagonal win for player 'xo'. Returns False otherwise."""
       for row in range(self.height - 3):
           for col in range(self.width - 3):
               if self.data[row+3][col] == self.data[row + 2][col + 1] ==\
                  self.data[row + 1][col + 2] == self.data[row][col + 3] == ox:
                   return True 
       return False

    def isNegSlopeDiagWin(self, ox): 
       """ Returns True if there is a negative sloping diagonal win for player 'xo'. Returns False otherwise.""" 
       for row in range(self.height - 3):
           for col in range(self.width - 3):
               if self.data[row + 3][col + 3] == self.data[row + 2][col + 2] ==\
                  self.data[row + 1][col + 1] == self.data[row][col] == ox:
                   return True 
       return False

    def isWinFor(self,xo):
        """ Returns True if player 'xo' has one or more of the four winning conditions. Returns False otherwise."""
        assert(xo == 'X' or xo == 'O')
        if self.isHorizontalWin(xo) or self.isVerticalWin(xo) or\
           self.isPosSlopeDiagWin(xo) or self.isNegSlopeDiagWin(xo):
            return True
        else:
            return False

    def hostGame(self):
        """ Iniates and hosts a connect four game. """
        print()
        print('Welcome to Connect Four!')
        print()
        turn = 'X'
        while True:
            print(self)
            print()
            if turn == 'X':
                col = int(input("X's choice:  "))
                self.addMove(col,'X')
                if self.isWinFor('X'):
                    print(self)
                    print("X wins!")
                    break
                turn = 'O'
            elif turn == 'O':
                col = int(input("O's choice:  "))
                self.addMove(col,'O')
                if self.isWinFor('X'):
                    print(self)
                    print("O wins!")
                    break
                turn = 'X'

def menu():
    """ Prints a menu of options. 
    """ 
    print("(1) Create Board ")
    print("(2) Play Game ")
    print("(3) Print Board ")
    print("(4) Add move ")
    print("(5) Delete move ")
    print("(6) Clear board ")
    print("(7) Set board ")
    print("(8) Move Legality?")
    print("(9) Is Full?")
    print("(10) Is Win For?")
    print("(11) Quit")

def connect4():
    while True:
        print()
        menu()
        print()
        choice = int(input("Choose an option: ")) 
        print()
        if choice == 1:
            width = int(input("Choose an width (7): "))
            height = int(input("Choose an height (6): ")) 
            board = Board(width, height)
        elif choice == 2:
            board.hostGame()
        elif choice == 3:
            print(board)
        elif choice == 4:
            col = int(input("Choose an column: "))
            xo = input("Choose an player ('X'/'O'): ")
            board.addMove(col,xo)
        elif choice == 5:
            col = int(input("Choose an column: "))
            board.deleteMove(col)
        elif choice == 6:
            board.clear()
        elif choice == 7:
            setString = input("Enter a string: ")
            board.setBoard(setString)
        elif choice == 8:
            col = input("Pick a column: ")
            board.isMoveLegal(col)
        elif choice == 9:
            board.isFull()
        elif choice == 10:
            team = input("What Team ('X'/'O')?: ")
            board.isWinFor(team)
        elif choice == 11:
            break
        else:
            print("That is not on the menu.")

import doctest
doctest.testmod()
