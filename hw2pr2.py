'''Name: Zach Franz
hw2pr2.py
Lab 2 - Writing Recursive Functions
'''

import random

def randomStep():
    ''' Returns either -1 or 1 at random. '''
    return random.choice([-1, 1])

def walkerPosition(start,numberSteps):
    ''' Prints the current position at each step and then prints the final position again. '''
    print('start is '+str(start))
    if numberSteps > 0:
        start = start + randomStep()
        numberSteps -= 1
        return walkerPosition(start,numberSteps)
    else:
        return start

def randomWalkSteps(start,low,high):
    '''
    Prints Bobs random movement one step randomly forward or backward until he ends up at the low or high position.
    Returns the number of steps it took Bob to reach the low or high number.
    '''
    print(' ' * start + 'Bob')      # print visual representation of Bobs location

    # If Bob is at or beyond the low or high stop the recursion and return the final count. Otherwise continue onward.
    if start >= high:
        return 0
    elif start <= low:
        return 0
    else:
        start = start + randomStep()
        return 1 + randomWalkSteps(start,low,high)

def walkerPositionPlain(start,numberSteps):
    ''' Returns the final position (start-poorly named) after moving an input number of steps each randomly either forward or backward.'''
    if numberSteps > 0:     # If we still have steps to move, make a random step and decrease the count
        start = start + randomStep()
        numberSteps -= 1
        return walkerPositionPlain(start,numberSteps)   # Call for another step
    else:
        return start        # If we have no more steps to move return the position

def displacementTest():
    ''' Prints the averaged signed displacement over 1000 trails for moving 5, 10, and 20 steps.'''
    trials = 1000;          # number of trials
    for n in [5,10,20]:
        disList = [walkerPositionPlain(40,n)-40 for x in range(trials)]     # 40 is an arbitrary poistion
        avg = sum(disList)/trials       # averaging the displacement of each trial
        print('Averaged-signed displacement for '+str(n)+' steps is '+str(avg))     # print
        
    
