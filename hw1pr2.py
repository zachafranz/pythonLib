'''Name: Zach Franz
hw1pr2.py (Lab 1, part 2)
'''

def double(x):    
    """ Returns 2 times the numerical input (int or float) """
    return 2 * x

from math import *

def square(x):
    """ Returns the square of the numerical input(float) """
    return x**(1/2)

def interpolate(low,hi, fraction):
    """ Returns the value between the two numerical inputs (floats) by the fraction input """
    return low + ((hi-low)*fraction)

def checkEnds(aString):
    """ Returns True if the first character of input is the same as the last character. Returns False otherwise"""
    if aString[0] == aString[-1]:
        return True
    else:
        return False

def splitAndSwitch(aString):
    """ Returns string with first half of letters removed and placed after the second half. In the event of an odd character number input the first half should have less letters."""

##    Method One (Unnecessary if/else)
##    if len(aString)%2 == 0:
##        return aString[int(len(aString)/2):] + aString[0:int(len(aString)/2)]
##    else:
##        return aString[floor(len(aString)/2):] + aString[0:floor(len(aString)/2)]

##    Method Two (Better)
    return aString[floor(len(aString)/2):] + aString[0:floor(len(aString)/2)]
        
