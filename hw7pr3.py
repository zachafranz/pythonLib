# hw7pr3.py
# Lab 7
#
# Name: Zach Franz

def menu():
    """ Prints a menu of options. 
    """ 
    print("(0) Input a new list")
    print("(1) Print the current list")
    print("(2) Find the average price")
    print("(3) Find the standard deviation")
    print("(4) Find the min and its day")
    print("(5) Find the max and its day")
    print("(6) Your TTS investment plan")
    print("(7) Did the 2015-2016 Warriors lose the NBA finals after being up 3-1 with the first ever unanimous MVP?")
    print("(9) Quit")

def getNewList(): 
    """ Gets a new list. 
    """ 
    return eval(input("Enter a new list: "))

def printList(aList):
    ''' Prints the current list.
    >>> aList = [111,222,333]
    >>> printList(aList)
    Day Price--- -----
    0   111
    1   222
    2   333
    >>> printList([])
    Day Price--- -----
    '''
    c = 0
    print("Day Price--- -----")
    for i in aList:
        print(c," ",i)
        c += 1

def avgPrice(aList):
    ''' computes average price
    >>> aList = [100,200,300]
    >>> avgPrice(aList)
    200.0
    >>> avgPrice([])
    No items in list!
    '''
    if len(aList) <= 0:
        print("No items in list!")
    else:
        total = 0
        for i in aList:
            total += i
        return total/len(aList)

def stdDev(aList):
    ''' Finds standard deviation of a list
    >>> stdDev([])
    No items in list!
    >>> stdDev([20,10,30])
    8.16496580927726
    '''
    if len(aList) <= 0:
        print("No items in list!")
    else:
        listAvg = avgPrice(aList)
        numerator = 0
        for i in aList:
            numerator += (i-listAvg)**2
        return (numerator/len(aList))**0.5

def minVal(aList):
    ''' finds min value and index or indicies
    >>> minVal([1,2,3,4])
    [1, [0]]
    >>> minVal([1,2,3,1])
    [1, [0, 3]]
    '''
    if len(aList) <= 0:
        print("No items in list!")
    else:
        minNum = min(aList)
        minDays = []
        c = 0
        for i in aList:
            if i == minNum:
                minDays.append(c)
            c += 1
        return [minNum,minDays]

def maxVal(aList):
    ''' finds max value and index or indicies
    >>> maxVal([1,2,3,4])
    [4, [3]]
    >>> maxVal([3,2,3,1])
    [3, [0, 2]]
    '''
    if len(aList) <= 0:
        print("No items in list!")
    else:
        maxNum = max(aList)
        maxDays = []
        c = 0
        for i in aList:
            if i == maxNum:
                maxDays.append(c)
            c += 1
        return [maxNum,maxDays]

def list2Str(aList):
    '''
    converts list of non-strings to format 1, 2, 3, and 4
    or 1 and 2
    or 1
    '''
    if len(aList) == 0:
        return ''
    elif len(aList) == 1:
        return str(aList[0])
    elif len(aList) == 2:
        return str(aList[0])+' and '+str(aList[1])
    else:
        c = 0
        retStr = ''
        for i in aList:
            if c == len(aList)-1:
                retStr += 'and ' + str(i)
            else:
                retStr += str(i) + ', '
            c += 1
        return retStr

def invtTTS(aList):
    ''' computes which day to buy and sell stock should you project the future!!
    >>> invtTTS([6,5,4,3,2,1])
    [0, 0, 0, 0, 0]
    >>> invtTTS([3,7,12,3,0,4])
    [0, 3, 2, 12, 9]
    '''
    # defaults to buy and sell day one should the price never drop
    day_buy = 0
    cur_min_i = 0
    day_sell = 0
    cur_min_ii = 0
    cur_low_diff = 0
    
    day = 0
    for i in aList:
        day2 = 0
        for ii in aList[day:]:
            diff = ii-i
            if diff > cur_low_diff:
                cur_min_i = i
                cur_min_ii = ii
                cur_low_diff = diff
                day_buy = day
                day_sell = day2+day
            day2 += 1
        day += 1
    return [day_buy, cur_min_i, day_sell, cur_min_ii,cur_low_diff]

def doubleList(aList): 
    """ Doubles the elements in a list. 
    """ 
    return [2 * x for x in aList]


def tts(): 
    """ Presents a menu for user interaction. 
    """ 
    aList = [ ] 
    while True: 
        menu() 
        choice = int(input("Choose an option: ")) 
        print() 
        if choice == 0: 
            aList = getNewList() 
        elif choice == 1:
            printList(aList)
            print()
        elif choice == 2:
            print('The average price is ',avgPrice(aList))
            print()
        elif choice == 3:
            print('The st. deviation is ',stdDev(aList))
            print()
        elif choice == 4:
            minValAndDays = minVal(aList)
            days = minValAndDays[1]
            print('The min is',minValAndDays[0],'on day(s)',list2Str(days))
            print()
        elif choice == 5:
            maxValAndDays = minVal(aList)
            days = maxValAndDays[1]
            print('The max is',maxValAndDays[0],'on day(s)',list2Str(days))
            print()
        elif choice == 6:
            dayPriceROI = invtTTS(aList)
            print('Buy on day',dayPriceROI[0],'at',dayPriceROI[1],'. Sell on day',dayPriceROI[2],'at',dayPriceROI[3],'for',dayPriceROI[4],'bananas')
            print()
        elif choice == 7:
            print('-_-')
            print()
        elif choice == 9: 
            break 
        else: 
            print("That's not on the menu!") 
    print("Bye!")


import doctest
doctest.testmod()
