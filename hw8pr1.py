#
# hw8pr1.py - Game of Life lab
#
# Name: Zach Franz
#

import random
from gameOfLife import *

# I DID NOT CREATE AND DO NOT TAKE CREDIT FOR ANY FUNCTIONS IN THE gameOfLife FILE. - ZF

def createOneRow(width):
    """ Returns one row of zeros of width 'width'."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ Returns one array of zeros of width 'width' and height 'height'."""
    board = []
    for i in range(height):
        board = board+[createOneRow(width)]
    return board
    # or
##    board = [createOneRow(width)]*height
##    board = [[0 for i in range(width)] for i in range(height)]
##    board = [[0 for i in range(width)]]*height
##    board = [[0]*width]*height

def printBoard(board): 
    """ this function prints the 2D list-of-lists board 
        without spaces using end = '' feature.
    """ 
    for row in board: 
        for col in row: 
            print(col, end = '') # Don't print a space at end and
                                 #    don't go to next line. 
        print()                  # Go to next line.

def diagonalize(width, height): 
    """ Creates an empty board and modifies that board 
        so that it has a diagonal strip of "on" cells.
    >>> board = diagonalize(7, 6)
    >>> board
    [[1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0]]

    >>> printBoard(board)
    1000000
    0100000
    0010000
    0001000
    0000100
    0000010
    
    """ 
    board = createBoard(width, height) 
    
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                board[row][col] = 1 
            else: 
                board[row][col] = 0 
    return board

def innerCells(width, height):
    """ Returns an array with 'width' columns and 'height' rows with all the border elements equal to 0 and the non-border elements equal to 1.
    >>> board = innerCells(5, 5)
    >>> printBoard(board)
    00000
    01110
    01110
    01110
    00000
    """
    board = createBoard(width, height) 
    
    for row in range(height): 
        for col in range(width): 
            if (row != 0 and row != height-1) and (col != 0 and col != width-1): 
                board[row][col] = 1 
            else: 
                board[row][col] = 0 
    return board

def randomCells(width, height):
    """ Returns an array with 'width' columns and 'height' rows with all the border elements equal to 0 and the non-border elements randomly equal to 1 or 0."""
    board = createBoard(width, height) 
    
    for row in range(height): 
        for col in range(width): 
            if (row != 0 and row != height-1) and (col != 0 and col != width-1):
                if random.random() <= 0.5:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
            else: 
                board[row][col] = 0 
    return board

def copy(board):
    """ Returns a copy of the input board.
    >>> board = createBoard(2, 2)
    >>> board2 = copy(board)
    >>> printBoard(board2)
    00
    00
    >>> board[0][0] = 1
    >>> printBoard(board)
    10
    00
    >>> printBoard(board2)
    00
    00
    """
    height = len(board)
    width = len(board[0])

    copyBoard = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            copyBoard[row][col] = board[row][col]
    return copyBoard

def innerReverse(board):
    """ Returns a copy of the input board with all the inner bits flipped.
    >>> b = createBoard(3,4)
    >>> b[1][1] = 1
    >>> printBoard(b)
    000
    010
    000
    000
    >>> b2 = innerReverse(b)
    >>> printBoard(b2)
    000
    000
    010
    000
    """
    height = len(board)
    width = len(board[0])

    copyBoard = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if (row != 0 and row != height-1) and (col != 0 and col != width-1):
                copyBoard[row][col] = 1 - board[row][col]
            else:
                copyBoard[row][col] = 0
    return copyBoard

def countNeighbors(b,r,c):
    """ Returns the sum of the surrounding elements of a singular element at row(r) and column(c) on a board(b).
    """
    return (sum(b[r-1][c-1:c+2]) +
            b[r][c-1] + b[r][c+1] +
            sum(b[r+1][c-1:c+2]))
    

def nextLifeGeneration(board):
    """ Returns the next state of the board based on the rules of the 'game of life' game."""
    height = len(board)
    width = len(board[0])

    nextBoard = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            if (row != 0 and row != height-1) and (col != 0 and col != width-1):
                if countNeighbors(board,row,col) < 2:
                    nextBoard[row][col] = 0
                elif countNeighbors(board,row,col) > 3:
                    nextBoard[row][col] = 0
                elif countNeighbors(board,row,col) == 3:
                    nextBoard[row][col] = 1
                else:
                    nextBoard[row][col] = board[row][col]
            else:
                nextBoard[row][col] = 0
                
    return nextBoard

import doctest
doctest.testmod()

