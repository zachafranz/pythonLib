'''Name: Zach Franz
hw1pr3.py (Lab 1, part 3)
'''

from math import *

def convertFromSeconds(seconds):
    """ Returns the time in a list with Days, Hours, Minutes, Seconds given an input in seconds. """
    days = 0
    hours = 0
    minutes = 0
    day_sec = 60*60*24  # seconds in a day
    hour_sec = 60*60    # seconds in an hour
    min_sec = 60        # seconds in a minute

    # If seconds is greater than the amount od second in a day, calculate the number of whole days, then find the remaining seconds. Repeat for hours and minutes.
    if seconds >= day_sec:
        days = floor(seconds/day_sec)
        seconds = seconds - days*day_sec
    if seconds >= hour_sec:
        hours = floor(seconds/hour_sec)
        seconds = seconds - hours*hour_sec
    if seconds >= min_sec:
        minutes = floor(seconds/min_sec)
        seconds = seconds - minutes*min_sec

    # Create and return list.
    aList = [days,hours,minutes,seconds]
    return aList

def readSeconds(seconds):
    """ Returns a string of hours, days, minutes, and seconds given an input in seconds (integer)"""

    # Get the Days, Hours, Minutes, and seconds.
    aList = convertFromSeconds(seconds)

    # If the unit is singular add singular time unit, otherwise add plural. Add commas for everything except the last unit.
    if aList[0] == 1:
        day_str = str(aList[0]) + ' day, '
    else:
        day_str = str(aList[0]) + ' days, '
    if aList[1] == 1:
        hour_str = str(aList[1]) + ' hour, '
    else:
        hour_str = str(aList[1]) + ' hours, '
    if aList[2] == 1:
        min_str = str(aList[2]) + ' minute, '
    else:
        min_str = str(aList[2]) + ' minutes, '
    if aList[3] == 1:
        sec_str = str(aList[3]) + ' second'
    else:
        sec_str = str(aList[3]) + ' seconds'

    # Return concatenated time.
    return day_str + hour_str + min_str + sec_str

        
