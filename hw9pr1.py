#
# hw9pr1.py - Dates
#
# Name: Zach Franz
#

class Date:
    """ A user-defined data structure that
        stores and manipulates dates
    """

    def __init__(self, month, day, year):
        """ the constructor for objects of type Date
        >>> date1 = Date(11, 3, 2015)
        >>> date1.month
        11
        >>> date1.day
        3
        >>> date1.year
        2015
        """
        self.month = month
        self.day = day
        self.year = year


    def __repr__(self):
        """ Returns a string REPResentation for the
            object of type Date that calls it (named self).
        >>> date1 = Date(11, 3, 2015)
        >>> print(date1)
        11/03/2015
        """
        return "{:02d}/{:02d}/{:04d}".format(self.month, self.day, self.year)


    def isLeapYear(self):
        """ Returns True if the calling object is
            in a leap year; False otherwise.
        >>> date1 = Date(11, 3, 2015)
        >>> date1.isLeapYear()
        False
        >>> date1 = Date(11, 3, 2012)
        >>> date1.isLeapYear()
        True
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the calling object (self).
        >>> date1 = Date(11, 3, 2015)
        >>> newDate = date1.copy()
        >>> print(newDate)
        11/03/2015
        """
        newDate = Date(self.month, self.day, self.year)
        return newDate

    def isEqual(self, date2):
        """ Decides if self and date2 represent the same calendar date..
        >>> date1 = Date(11, 3, 2015)
        >>> newDate = date1.copy()
        >>> date1.isEqual(newDate)
        True
        """
        return self.year == date2.year and self.month == date2.month \
               and self.day == date2.day

    def daysInMonth(self):
        """ Returns amount of days in given month.
        """
        if self.isLeapYear():
            DAYS_IN_MONTH = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return DAYS_IN_MONTH[self.month]

    def tomorrow(self):
        """ Returns the day after the input day.
        >>> date1 = Date(1,1,2017)
        >>> date1.tomorrow()
        >>> print(date1)
        01/02/2017
        >>> date1 = Date(1,31,2017)
        >>> date1.tomorrow()
        >>> print(date1)
        02/01/2017
        >>> date1 = Date(2,28,2012)
        >>> date1.tomorrow()
        >>> print(date1)
        02/29/2012
        >>> date1 = Date(12,31,2012)
        >>> date1.tomorrow()
        >>> print(date1)
        01/01/2013
        """
        if self.daysInMonth() != self.day:
            # change day only and return
            self.day += 1
        else:
            # change day to 1
            self.day = 1
            # Will need to change month
            if self.month != 12:
                # change month only and return
                self.month += 1
            else:
                # change month to 1
                self.month = 1
                # increase year
                self.year += 1

    def yesterday(self):
        """ Returns the day prior to the input day.
        """
        if self.day != 1:
            # change day only and done
            self.day -= 1
        else:
            # Day will depend on month and year
            if self.month != 1:
                # Change month
                self.month -= 1
                # day depends on year
                self.day = self.daysInMonth()
            else:
                # subtract year, set month to 12, find day
                self.year -= 1
                self.month = 12
                self.day = self.daysInMonth()

    def addNDays(self,n):
        """ Prints the current day and each 'n' days after."""
        print(self)
        for i in range(n):
            self.tomorrow()
            print(self)

    def subNDays(self, n):
        """ Prints the current day and each 'n' days prior."""
        print(self)
        for i in range(n):
            self.yesterday()
            print(self)

    def isBefore(self, date2):
        """ Returns True if 'date2' is chronologically prior to the current date object. Returns False otherwise."""
        if self.year < date2.year:
            return True
        elif self.year == date2.year:
            if self.month < date2.month:
                return True
            elif self.month == date2.month:
                if self.day < date2.day:
                    return True
        return False

    def isAfter(self, date2):
        """ Returns True if 'date2' is chronologically after to the current date object. Returns False otherwise."""
        if self.year > date2.year:
            return True
        elif self.year == date2.year:
            if self.month > date2.month:
                return True
            elif self.month == self.month:
                if self.day > date2.day:
                    return True
        return False

    def diff(self,date2):
        """ Returns the difference in days between 'date2' and the current Date object."""
        newSelf = self.copy()
        newDate2 = date2.copy()
        dayCount = 0
        if newSelf.isBefore(newDate2):
            while not newSelf.isEqual(newDate2):
                newSelf.tomorrow()
                dayCount -= 1
            return dayCount
        elif newSelf.isAfter(newDate2):
            while not newSelf.isEqual(newDate2):
                newSelf.yesterday()
                dayCount += 1
            return dayCount
        return dayCount

    def dayOfWeek(self):
        """ Returns the day of the week of the Date object. """
        testDate = Date(4,23,2017) #Sunday
        days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        return days[self.diff(testDate)%7]

def newYearDayCounter():
    """ Prints the total number of each New Year's day of the week for the next 100 years. """
 
    # Set each counter to zero.
 
    dayOfWeekCounter = {}   # initialize a Python dictionary
    dayOfWeekCounter["Sunday"]    = 0
    dayOfWeekCounter["Monday"]    = 0
    dayOfWeekCounter["Tuesday"]   = 0
    dayOfWeekCounter["Wednesday"] = 0
    dayOfWeekCounter["Thursday"]  = 0
    dayOfWeekCounter["Friday"]    = 0
    dayOfWeekCounter["Saturday"]  = 0
 
    # Count the day of the week on January 1 for the next 100 years.
 
    for year in range(2017, 2118):    # We've passed the new year's day for the current year.
        date = Date(1, 1, year)
        print('Current date is', date)
        weekday = date.dayOfWeek()
        dayOfWeekCounter[weekday] += 1
 
    print('totals are', dayOfWeekCounter)
        
import doctest
doctest.testmod()
