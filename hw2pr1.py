'''Name: Zach Franz
hw2pr1.py
Lab 2 - Writing Recursive Functions
'''


def mult(n,m):
    ''' Returns the value of n times m using recursion.'''
    # If m is positive or negative we want to bring it to 0 by adding n (or negative n) to itself m times.
    if m > 0:
        m = m - 1
        return n + mult(n,m)
    elif m < 0:
        m = m + 1
        return -n + mult(n,m)
    else:
        return 0

def dotProduct(list1,list2):
    ''' Returns the dot product of two lists using recursion. '''
    # If the lists are equal length we can perform the dot product by multiplying the first values of each list, slicing off the first values, and calling the function again.
    if len(list1) != len(list2):
        return 0.0
    elif len(list1) > 0:
        return float((list1[0]*list2[0])) + dotProduct(list1[1:],list2[1:])
    else:
        return float(0)

def myIndex(element,sequence):
    ''' Returns the index of the first occurance of an element in an array using recursion. If the element does not occur, it returns the length of the array.'''
    if len(sequence) == 0:
        return len(sequence)
    elif element == sequence[0]:
        return 0
    else:
        return 1 + myIndex(element,sequence[1:])

def letterScore(letter):
    ''' Returns the score of a letter in the game of Scrabble.'''
    if letter in 'aeilnorstu':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'cmp':
        return 3
    elif letter in 'fhvwy':
        return 4
    elif letter == 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        return 0

def scrabbleScore(s):
    ''' Returns the score of a word in the game of Scrabble using recursion.'''
    if len(s) > 0:
        return letterScore(s[0])+scrabbleScore(s[1:])
    else:
        return 0
