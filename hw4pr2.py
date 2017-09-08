'''
Name: Zach Franz
hw4pr2.py
'''

def isOdd(integer):
    ''' Returns true if input integer is odd, otherwise returns false.'''
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
    if len(binaryString) > 0:
        if int(binaryString[-1]) == 0:
            return binaryToNum(binaryString[:-1])*2
        else:
            return binaryToNum(binaryString[:-1])*2 + 1
    else:
        return 0

def makeByte(n):
    ''' Returns a byte (minus 1 bit = 7 binary bits) from a base 10 integer.'''
    ans = numToBinary(n)
    ledZeros = (7-len(ans))*'0'
    tot = ledZeros + ans
    return tot[-7:]

def countRepElm(s):
    ''' Returns the number of times the first (index=0) character is repeated without interruption in a input string.'''
    if len(s) > 0:
        if len(s) == 1:
            return 1
        else:
            if s[0] == s[1]:
                return 1 + countRepElm(s[1:])
            else:
                return 1
    else:
        return 0

def compress(s):
    ''' Returns a compressed (in some cases) string by counting repeated bits and replacing uninterrupted repeat bit counts with numerical byte representatives with a starting bit type.'''
    if len(s) > 0:
        num = countRepElm(s)
        runSeq = s[0] + makeByte(num)
        return runSeq + compress(s[num:])
    else:
        return ''

def uncompress(c):
    ''' Returns an uncompressed string of binary bits from a compressed string input.'''
    if len(c) > 0:
        numType = c[0]
        quant = binaryToNum(c[1:8])
        walkSeq = quant*str(numType)
        return walkSeq + uncompress(c[8:])
    else:
        return '' 

'''
The largest number of bits the compression algorithm could output with a 64 bit input is
64*8=512. This would occur with the entire 64 bit input alternating every value. Each byte would
be the current bit of the 64 bit input + '0000001' == 1. A new byte for each value
'''
    
    
