#
# hw8pr3.py
#
# Name: Zach Franz
#

def anyEqual(aList):
    """ Determines if any of the elements of a list are equal using regression
    """
    if len(aList) < 1:
        return False
    else:
        for i in aList[1:]:
            if aList[0] == i:
                return True
        return anyEqual(aList[1:])
    
def isMagic(a):
    """ Returns true if the input array is a 'magic matrix'.
    >>> a = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    >>> isMagic(a)
    True
    >>> a = [[4, 9, 2], [3, 5, 7], [8, 1, 123]]
    >>> isMagic(a)
    False
    >>> a = [[3, 5, 7], [8, 1, 6], [4, 9, 2]]
    >>> isMagic(a)
    False
    >>> a = []
    >>> isMagic(a)
    False
    """
    # Check square
    height = len(a)
    if height == 0:
        return False
    width = len(a[0])
    if width != height:
        return False
    # Check all unique
    flatList = []
    for i in range(height):
        flatList += a[i]
    if anyEqual(flatList):
        return False
    # Get base check number (use row 1)
    magicNum = sum(a[0])
    # Check rows
    for i in range(height-1):
        if sum(a[i+1]) != magicNum:
            return False
    # Check cols
    for i in range(width):
        total = 0
        for j in range(height):
            total += a[j][i]
        if total != magicNum:
            return False
    # Check Diagonals
##    total = 0
##    for i in range(width):
##        total += a[i][i]
    if sum(a[i][i] for i in range(len(a))) != magicNum:
        return False
    if sum(a[i][len(a)-1-i] for i in range(len(a))) != magicNum:
        return False
    return True

import doctest
doctest.testmod()
