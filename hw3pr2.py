'''
Name: Zach Franz
hw3pr2.py
Ciphers
'''

def encipher(s,n):
    ''' Returns a Caesar cipher of an input string by an input shift number.'''
    n = n%26        # Reduce shift to a number lower than the number of letters in the alphabet.
    new_s = ""      # Prepare new string.
    
    # For all the letters in the input string, shift lower case, shift upper case, and do not shift non-letter characters.
    # If the shifted letters extend past the last letter of the alphabet, wrap around to the beginning.
    for i in s:
        if "a" <= i <= "z":
            if ord(i)+n > ord("z"):
                new_s += chr(ord(i)+n-26)
            else:
                new_s += chr(ord(i)+n)
        elif "A" <= i <= "Z":
            if ord(i)+n > ord("Z"):
                new_s += chr(ord(i)+n-26)
            else:
                new_s += chr(ord(i)+n)
        else:
            new_s += i

    return new_s
        
def decipher(s):
    ''' Returns best decipher attempt by testing each Caesar Cipher shift case (one for each letter), calculating total letter frequencies for each shift, and returning the highest total shift text.'''

    total = 0   # total letter frequency score
    # For each shift possibility, shift the input text and determine total text letter frequency.
    for ii in range(0,26):
        new_s = encipher(s,ii)
        new_total = 0

        # Get total text letter frequency
        for i in new_s:
            new_total += letterFrequency(i)

        # If the current total is larger than the previous higher total, assign it to the higher total. Keep track of the shift used.
        if new_total > total:
            magic_n = ii
            total = new_total

    # Using the shift of the highest score shift, decipher and return the text by shifting it back.
    return encipher(s,magic_n)
    
 
def letterFrequency(c):
    ''' Determines the frequency (percent) at which a letter occurs in English
    text.  If the letter is not alphabetic, return 0.  See Letter Frequency
    in Wikipedia.
    '''
    # If the input is upper case, make it lower case.
    if 'A' <= c <= 'Z':
        c = c.lower()

    # If by now the input is not a lower case letter, it is not a letter, return 0.
    if c < 'a' or c > 'z':
        return 0

    # All 26 letter frequencies in english text via Wiki
    frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094,\
                   6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507,\
                   1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.36,\
                   0.15, 1.974, 0.074]

    # Return the input letter frequency
    return frequencies[ord(c) - ord('a')]
