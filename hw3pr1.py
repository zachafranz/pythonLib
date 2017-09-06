'''
Name: Zach Franz
hw3pr1.py - Lab problem: "Lights On!
This homework runs a console game called "Lights On!" in which a random list of 0's and 1's is generated (randomBinaryList)
and then the player must get all the values to be 1 by runnning the game (runGenerations).
'''

# function to run 'game'
# function to check for win
# function to flip bits of list according to user input
# function to flip selected and surrounding squares
# function to generate random list of 0's and 1's

import time           # provides time.sleep(0.5)
from random import *  # provides choice([0,1]), etc.
import sys            # larger recursive stack
sys.setrecursionlimit(100000) # 100,000 deep - in theory

def runGenerations(aList):
    ''' runGenerations keeps running the evolve function. '''
    print(aList)            # display the list, aList
    time.sleep(0.25)         # pause a bit
##    newList = evolve(aList) # evolve aList into newList
    if isAllOnes(aList):
        print('You Won in this many turns: ')
        return 0
    else:
        newList = evolve(aList)
        return 1 + runGenerations(newList) # recur

def isAllOnes(aList):
    ''' Returns true if all elements of the input list are equal to 1. Otherwise returns false.'''
    ones_list = [x for x in aList if x==1]
    if len(ones_list) == len(aList):
        return True
    else:
        return False

def evolve(aList):
    ''' evolve takes in a list of integers, aList, and returns a new list of integers considered to be the "next generation". '''
    n = len(aList)  # n now holds the size of the list aList
    x = int(input("Enter an index to change: "))  # Get numeric input from user
    return [setNewElement(aList, i, x) for i in range(n)]   # Return new list by calling setNewElement on each element.

def setNewElement(aList, i, x = 0):
    """ setNewElement returns the NEW list's ith element. If the ith element is next to or is the chosen column without being out-of-bounds of the list, the ith bit is flipped.
          input aList: any list of integers
          input i: the index of the new element to return
          input x: the user's chosen column
    """
    if x < 0 or x > len(aList)-1:   # If the user input is out-of-bounds, return the original.
        return aList[i] 
    elif i == x:                # If we are at the user's chosen column, flip the bit.
        return 1-aList[i]
    elif i == x-1 and x-1 >= 0: # If we are at the index to the left but not out-of-bouds, flip the bit.
        return 1-aList[i]
    elif i == x+1 and x+1 <= len(aList)-1:  # If we are at the index to the right but not out-of-bounds, flip the bit.
        return 1-aList[i]
    else:                       # If we are at any other 'passive' bit, return the original.
        return aList[i]

def randomBinaryList(n):
    ''' Returns a list of 0's or 1's the length of the input number. '''
    return [choice([0,1]) for i in range(n)]
