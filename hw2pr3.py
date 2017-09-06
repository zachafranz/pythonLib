'''Name: Zach Franz
hw2pr3.py
This set of functions draws snowflakes!
'''

# ********Provided Code
from turtle import *

def spiral(initialLength, angle, multiplier):
    if initialLength > 1000 or initialLength < 1:
        return
    else:
        forward(initialLength)
        right(angle)
        initialLength = initialLength*multiplier
        spiral(initialLength, angle, multiplier)

def svTree(trunkLength, levels):
    if levels > 0:
        forward(trunkLength)
        right(30)
        svTree(trunkLength * 0.8,levels - 1)
        left(60)
        svTree(trunkLength * 0.8,levels - 1)
        right(30+180)
        forward(trunkLength)
        right(180)

# *******My Code
def snowflake(levels,sideLength):
    if levels == 0:          # The base case is just a straight line
        forward(sideLength)
    else:
        snowflake(levels-1, sideLength/3)   # Go 1/3 of the way
        left(60)
        snowflake(levels-1, sideLength/3)
        right(120)
        snowflake(levels-1, sideLength/3)
        left(60)
        snowflake(levels-1, sideLength/3)
            
def act_snowflake(levels,sideLength):
    for n in range(3):
        snowflake(levels,sideLength)
        right(120)

def main():
    ''' Cleans up the space and calls for a nice snowflake to draw.'''
    home()
    clear()
    act_snowflake(3,100)    
