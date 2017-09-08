'''
Name: Zach Franz
hw4pr1.py
'''

def isOdd(integer):
    ''' Returns true if the input is an odd number and false if the input is an even number. '''
    if integer%2 == 0:
        return False
    else:
        return True

def numToBinary(anInteger):
    ''' Returns the binary conversion of a base 10 integer. Returns an empty string if the number is not greater than 0. '''
    if anInteger > 0:
        if isOdd(anInteger):
            return numToBinary((anInteger-1)/2) + "1"
        else:
            return numToBinary(anInteger/2) + "0"
    else:
        return ""

def binaryToNum(binaryString):
    ''' Returns base 10 integer from binary string.'''
    # Reverse process as numToBinary
    if len(binaryString) > 0:
        if int(binaryString[-1]) == 0:
            return binaryToNum(binaryString[:-1])*2
        else:
            return binaryToNum(binaryString[:-1])*2 + 1
    else:
        return 0

def increment(s):
    ''' Returns binary string incremented by 1 (base 10) with 8 total bits.'''
    # Convert number to base 10, add 1, and convert back to binary
    ans = numToBinary(binaryToNum(s)+1)
    # Add necessary number of 0's to the front for a total of 8 bits
    ledZeros = (8-len(ans))*'0'
    tot = ledZeros + ans
    # Return
    return tot[-8:]


def numToTernary(anInteger):
    ''' Returns the ternary string conversion of a base 10 integer. Returns an empty string if the number is not greater than 0. '''
    if anInteger > 0:
        if anInteger%3 == 0:
            return numToTernary(anInteger/3) + "0"
        elif anInteger%3 == 1:
            return numToTernary((anInteger-1)/3) + "1"
        elif anInteger%3 == 2:
            return numToTernary((anInteger-2)/3) + "2"
    else:
        return ""

def ternaryToNum(s):
    ''' Returns a base 10 number from a ternary string.'''
    if len(s) > 0:
        if int(s[-1]) == 0:
            return ternaryToNum(s[:-1])*3
        elif int(s[-1]) == 1:
            return ternaryToNum(s[:-1])*3 + 1
        elif int(s[-1]) == 2:
            return ternaryToNum(s[:-1])*3 + 2
    else:
        return 0

def numToBaseB(anInteger,n):
    ''' Returns a string of a given base from an input integer.'''
    if anInteger > 0:
        num = anInteger % n
        strNum = str(num)
        newInt = int((anInteger-num)/n)
        return numToBaseB(newInt,n) + strNum
    else:
        return ""

def baseBToNum (s,n):
    '''Returns a number of a given base from an input string.'''
    if len(s) > 0:
        return baseBToNum(s[:-1],n) *n + int(s[-1])
    else:
        return 0

def baseToBase(baseA, baseB, stringInBaseA) :
    ''' Returns a string in a given base from an input string of an input base.'''
    return numToBaseB(baseBToNum(stringInBaseA,baseA),baseB)
    
def add(s,t):
    ''' Returns the binary string summation of two input binary strings.'''
    num1 = baseBToNum(s,2)
    num2 = baseBToNum(t,2)
    return numToBaseB((num1+num2),2)

def add1(binStr):
    ''' Returns the binary string of adding 1 to an input binary string.'''
    num = baseBToNum(binStr,2)
    return numToBaseB(num+1,2)
    
def addBinary(s1,s2):
    ''' Returns the binary string summation of two input binary string without conversion out of binary.'''
    if len(s1) > 0 and len(s2) > 0:     # If both binary strings still have bits left
        if s1[-1]+s2[-1] == '11':       # If both least significant bits are 1
            return addBinary(s1[:-1],add1(s2[:-1])) + '0'
        else:
            return addBinary(s1[:-1],s2[:-1]) + str(int(s1[-1])+int(s2[-1]))

    # If only 1 of either string has bits left
    elif len(s1) > 0:
        return addBinary(s1[:-1],s2[:-1]) + str(s1[-1])     # Is okay becuase s='',s[:-1] --> ''
    elif len(s2) > 0:
        return addBinary(s1[:-1],s2[:-1]) + str(s2[-1])

    # If neither string has bits left
    else:
        return ""
