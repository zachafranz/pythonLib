# hw7pr2.py
# Lab 7
#
# Name: Zach Franz

import math
import random

def throw1dart():
    ''' Returns true if a random pair of x and y values between -1 and 1 fall in the unit circle.'''
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)
##    print(x)
##    print(y)
    if x**2 + y**2 <= 1**2:
        return True
    else:
        return False

def forPi(n):
    ''' Returns an estimate for Pi after n iterations of random "dart throwing".http://www.cs.wustl.edu/~cytron/cs101/Lectures/5.html'''
    c_hit = 0
    pi_est = 0
    for i in range(n):
        if throw1dart():
            c_hit += 1
        pi_est = (c_hit/(i+1))*4
        print(str(i) + " dart(s) thrown " + str(c_hit) + " dart(s) hit " + str(pi_est) + " is the pi estimate")
    return pi_est

def whilePi(error):
    ''' Returns the number of iterations taken to estimate Pi by "dart throwing" to a certain error.''' 
    c_drts = 0
    c_hit = 0
    pi_est = 0
    while abs(math.pi-pi_est) >= error and c_drts <= 100:
        c_drts += 1
        if throw1dart():
            c_hit += 1
        pi_est = (c_hit/(c_drts+1))*4
        print(str(c_drts) + " dart(s) thrown " + str(c_hit) + " dart(s) hit " + str(pi_est) + " is the pi estimate")
    return c_drts
