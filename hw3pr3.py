'''
Name: Zach Franz
hw3pr3.py
'''

def binaryListSort(aList):
    ''' Returns a sorted binary list (0's first, 1's second).'''
    # Recursively add 1's to the end and 0's to the beginning
    if len(aList) > 0:
        if aList[0] == 1:
            return binaryListSort(aList[1:]) + [aList[0]]
        elif aList[0] == 0:
            return [aList[0]] + binaryListSort(aList[1:])
    else:
        return []
    
def insertOne(element, aList):
    ''' Returns a sorted list with an inserted element into its proper place.
    input: element is an item to be inserted; aList is a sorted list.
    output: A sorted list.
    '''
    # Recursively add list elemetns to the list until the inserted element is less than the current list element at which point push the element and rest of the list.
    if len(aList) == 0:
        return [element]
    elif element < aList[0]:
        return [element] + aList
    else:
        return aList[0:1] + insertOne(element, aList[1:])

def sort(aList):
    ''' Returns a sorted list from the input list.'''
    # Recursively goes through the input list inserting each element. 
    if len(aList) > 0:
        return insertOne(aList[0],sort(aList[1:]))
    else:
        return []

def jottoScore(s1,s2):
    ''' Returns number of one-for-one character matches between two input strings.'''
    # Recursively check for the current s1 character in string s2, and if so increase the counter and remove character from sting s2.
    if len(s1) > 0:
        if s1[0] in s2:
            new_s2 = remFirstInstStr(s1[0],s2)
            return 1 + jottoScore(s1[1:],new_s2)
        else:
            return 0 + jottoScore(s1[1:],s2)
    else:
        return 0
            
def remFirstInstStr(element,aList):
    ''' Returns list with the first instance of a character removed.'''
    # Loops through string checking for equality and first instance. If one is not true, add the current string character to the output string.
    notFirst = False
    new_aList = ''
    for i in aList:
        if element == i and not notFirst:
            notFirst = True
        else:
            new_aList += i
    return new_aList
            
            
