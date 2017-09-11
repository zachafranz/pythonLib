# hw7pr1.py
# Lab 7
#
# Name: Zach Franz

NUM_ITERATIONS = 50  # after this many tries, we assume c is in the MandelbrotSet
MAX_X = 1.0
MIN_X = -2.0
MAX_Y = 1.0
MIN_Y = -1.0

# keep this import line...
from cs5png import *

# start your Lab 7 functions here:

# I DID NOT WRITE AND DO NOT TAKE CREDIT FOR CODE ABOVE THIS LINE - ZF

def mult(c,n):
    ''' Returns the value of multiplying numbers c and n.'''
    result = 0
    for i in range(n):
        result = result + c
    return result

def update(c,n):
    ''' Returns the value of the mandelbrot function.'''
    z = 0
    for i in range(n):
        z = z**2 + c
    return z

def isInMandelbrotSet(c,n):
    ''' Does things
    >>> n = 25
    >>> c = 0 + 0j
    >>> isInMandelbrotSet(c, n)
    True
    >>> c = 3 + 4j
    >>> isInMandelbrotSet(c, n)
    False
    >>> c = 0.3 + -0.5j
    >>> isInMandelbrotSet(c, n)
    True
    >>> c = -0.7 + 0.3j
    >>> isInMandelbrotSet(c, n)
    False
    >>> c = -0.9 + 0.4j
    >>> isInMandelbrotSet(c, n)
    False
    >>> c = 0.42 + 0.2j
    >>> isInMandelbrotSet(c, 25)
    True
    >>> isInMandelbrotSet(c, 50)
    False
    '''
    #n = 25
    z = 0+0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True

def isPixelWanted(c): 
    ''' Determines if we want a pixel. ''' 
##    return col % 10 == 0 or row % 10 == 0
    return isInMandelbrotSet(c,NUM_ITERATIONS)

def testImage(): 
    ''' Demonstrates how to create and save a png file.'''
    width = 300 
    height = 200 
    image = PNGImage(width, height) 

    for col in range(width): 
        for row in range(height): 
            if isPixelWanted(col, row): 
                image.plotPoint(col, row)
    image.saveFile()

def scale(coordinate, coordinateMax, floatMin, floatMax):
    ''' Returns the scaled value of the coordinate in the coordinateMax domain to the floatMin and floatMax domain.
    >>> scale(100, 200, -2.0, 1.0)
    -0.5
    >>> scale(100, 200, -1.5, 1.5)
    0.0
    >>> scale(100, 300, -2.0, 1.0)
    -1.0
    >>> scale(25, 300, -2.0, 1.0)
    -1.75
    >>> scale(299, 300, -2.0, 1.0)
    0.9900000000000002
    '''
    return ((floatMax-floatMin)*(coordinate/coordinateMax))+floatMin

def mandelbrotSet(width, height):
    '''Saves a mandelbrot set image.'''
    image = PNGImage(width, height) 

    for col in range(width):
        x = scale(col, width, MIN_X, MAX_X)
        for row in range(height):
            y = scale(row, height, MIN_Y, MAX_Y)
            c = x + y*1j
            if isPixelWanted(c): 
                image.plotPoint(col, row,(0, 0, 255))
            else:
                image.plotPoint(col, row,(255, 255, 0))
    image.saveFile()

def pixelColor(c,n):
    ''' Determines the color of a pixel based on mandelbrot set parameters.'''
    #n = 25
    z = 0+0j
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return scale(i,NUM_ITERATIONS,0.0,255.0)
    return -1

def isColorPixelWanted(c): 
    ''' Determines if we want a colored pixel.''' 
##    return col % 10 == 0 or row % 10 == 0
    return pixelColor(c,NUM_ITERATIONS)

def mandelbrotSetColor(width, height):
    ''' Saves a mandelbrot set image with color.'''
    image = PNGImage(width, height) 

    for col in range(width):
        x = scale(col, width, MIN_X, MAX_X)
        for row in range(height):
            y = scale(row, height, MIN_Y, MAX_Y)
            c = x + y*1j
            color = isColorPixelWanted(c)
            if color == -1:
                image.plotPoint(col, row,(0, 0, 255))
            else:
                image.plotPoint(col, row,(color, color, 0))
    image.saveFile()
    

import doctest
doctest.testmod()
    
