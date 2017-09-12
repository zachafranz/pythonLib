#
# hw8pr2.py
#
# Name: Zach Franz
#


def menu():
    """ Prints a menu of options. 
    """ 
    print("(1) Enter a 2D array as list of lists ")
    print("(2) Print the array in rectangular form ")
    print("(3) Multiply an array row by a constant ")
    print("(4) Add one row into another ")
    print("(5) Add a multiple of one row to another ")
    print("(6) Transpose the 2D array ")
    print("(9) Quit")

def enterValues():
    return eval(input("Please type/paste a 2D list of lists: "))

def printArray(array2D):
    ''' Prints the input array.'''
    i = 0
    for row in array2D:
        j = 0
        for col in row:
            print("{:8.3f}".format(array2D[i][j]), end = "")
            j += 1
        print()
        i += 1

def multiplyRow(a, row, multiplier):
    ''' Returns an input array with a input row multiplied by a given number.'''
    for j in range(len(a[row])):
        a[row][j] = a[row][j]*multiplier
                
def addSourceRowToDestinationRow(a, sourceRow, destRow):
    ''' Returns an input array with a input source row added to a input destination row.'''
    for j in range(len(a[destRow])):
        a[destRow][j] += a[sourceRow][j]

def addMultipleOfSourceRowToDestRow(a, multiplier, sourceRow, destRow):
    ''' Returns an input array with a input source row, times a multiplier, added to a input destination row.'''
    for j in range(len(a[destRow])):
        a[destRow][j] += a[sourceRow][j]*multiplier

def copy(board):
    """ Returns the copy of an array."""
    height = len(board)
    width = len(board[0])

    copyBoard = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            copyBoard[row][col] = board[row][col]
    return copyBoard

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

def transpose(a):
    ''' Returns the transposed array of input array "a".'''
##    height = len(a)
##    width = len(a[0])
##    aTrans = [[0]*height]*width
##    for i in range(height):
##        for j in range(width):
##            print(i)
##            print(j)
##            print(a[i][j])
##            aTrans[j][i] = a[i][j]
##            print(aTrans)
##            print()
##    return aTrans

    height = len(a)
    width = len(a[0])

    copyBoard = createBoard(height, width)
    for row in range(height):
        for col in range(width):
            copyBoard[col][row] = a[row][col]
    return copyBoard

def matrix():
    a = [[2.0, 4.0, 5.0, 34.0],
         [2.0, 7.0, 4.0, 36.0],
         [3.0, 5.0, 4.0, 35.0]]
    while True:
        print()
        printArray(a)
        print()
        menu()
        choice = int(input("Choose an option: ")) 
        print()
        if choice == 1:
            a = enterValues()
        elif choice == 2:
            printArray(a)
        elif choice == 3:
            row = int(input("Row? "))
            multiplier = int(input("Multiplier? "))
            multiplyRow(a, row, multiplier)
        elif choice == 4:
            sourceRow = int(input("Source Row? "))
            destRow = int(input("Destination Row? "))
            addSourceRowToDestinationRow(a, sourceRow, destRow)
        elif choice == 5:
            sourceRow = int(input("Source Row? "))
            destRow = int(input("Destination Row? "))
            multiplier = int(input("Multiplier? "))
            addMultipleOfSourceRowToDestRow(a, multiplier, sourceRow, destRow)
        elif choice == 6:
            transpose(a)
        elif choice == 9:
            break
        else:
            print("That is not on the menu.")
