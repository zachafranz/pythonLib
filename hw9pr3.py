#
# hw9pr3.py - Markov Dictionary
#
# Name: Zach Franz
#

import random

def wordCount(fileName = None):
    """ Prints the number of words in the text input
    """
    text = getText(fileName)

    # text is a bunch of space-separated words

    listOfWords = text.split()
    print("The list of words is", listOfWords)
    numWords = len(listOfWords)
    print("There are", numWords, "words.")

def getText(fileName = None):
    """ Returns some text from either a file or the keyboard.
        The text will be a string containing whitespace separated words.
    """
    if fileName == None:
        text = getTextFromKeyboard()
    else:
        text = getTextFromFile(fileName)
    return text

def getTextFromKeyboard():
    """ Reads text from the keyboard until a line with just 42 is entered.
    """
    text = ""
    print("Enter lots o' text. End with a plain '42' line.")
    while True:
        nextLine = input()
        if nextLine == "42":
            break
        text += nextLine + " "
    return text

def getTextFromFile(fileName):
    """ Returns text from a file named fileName.
    """
    file = open(fileName, "r")
    text = file.read()
    file.close()
    return text

def removePunctuationAndLowerCase(listOfWords):
    """ Returns words in listOfWords in lowercase with puctuation removed.
    """
    newList = []
    for word in listOfWords:
        word = word.lower()
        for punc in ".,`'\"~!@#$%^&*();:<>|\\/?}{][_+=-":
            word = word.replace(punc, '')
        if word != "":
            newList += [word]
    return newList

def createDictOfWordCounts(listOfWords):
    """ Returns a dictionary containing the number of times each word appeared.
    """
    wordCounterDict = {}
    for word in listOfWords:
        if word in wordCounterDict:
            wordCounterDict[word] += 1
        else:
            wordCounterDict[word] = 1
    return wordCounterDict

def printResults(sortedList):
    """ Prints each word in sortedList and the number of times it occurred.
        Print at most MAX words.
    """
    MAX = 40
    count = 0
    for item in sortedList:
        if item[1] > 1:
            print("{:12s} --> {:3d} times".format(item[0], item[1]))
        else:
            print("{:12s} --> {:3d} time".format(item[0], item[1]))
        count += 1
        if count > MAX:
            break
    return

def vocabCount(fileName = None):
    """ Counts the word frequency of input text.  The text may come from a
        file or the keyboard.
    """
    text = getText(fileName)
    listOfWords = text.split()
    listOfWords = removePunctuationAndLowerCase(listOfWords)
    numWords = len(listOfWords)
    print("There are", numWords, "words.")

    wordCounterDict = createDictOfWordCounts(listOfWords)
    numDistinctWords = len(wordCounterDict)
    print("There are", numDistinctWords, "distinct words.")

    sortedList = sorted(wordCounterDict.items(), key = lambda x: x[1],
                        reverse = True)
    printResults(sortedList)

    # challenges:
    #   how to get the list of distinct words?
    #   how to get the max-appearing word?

def createDictionary(filename):
    """ From an input text file, creates a markov type dictionary where for each word entry there is a corresponding list
        of words that followed the entered word in the text file as well as the frequency at which that word followed the entered word.
    """
    # Get Text
    text = getTextFromFile(filename)
    
    # Split text into list
    listOfWords = text.split()
    
    # Make all lower case
    for i in range(len(listOfWords)):
        listOfWords[i] = listOfWords[i].lower()
    
    # Start Dictionary
    markovDict = {}
    firstWord = True
    for word in listOfWords:
        
        # If first word, add word to $ key 
        if firstWord:
            # if already some first words, add to list, else begin list
            if '$' in markovDict:
                markovDict['$'] += [word]
            else:
                markovDict['$'] = [word]
            # Set first word false
            firstWord = False
        else:
            # Same logic
            if prevWord in markovDict:
                markovDict[prevWord] += [word]
            else:
                markovDict[prevWord] = [word]

        # Check if word is last word, set firstWord true,
        # else set prev_word = word
        if isLastWord(word):
            firstWord = True
        else:
            prevWord = word

    # return
    return markovDict
            
def isLastWord(word):
    """ Retruns true if the input word is that last of a sentence.
    """
    # Check empty and return false if empty
    if len(word) > 0:
        if word[-1] == '.' or word[-1] == '!' or word[-1] == '?':
            return True
        else:
            return False
    else:
        return False

def generateText(wordDict, numWords):
    """ Prints random text from a ."""
    text = []
    newSent = True
    for i in range(numWords):
        # If new sentence, add start word, otherwise add follow word
        if newSent:
            text += [random.choice(wordDict['$'])]
        else:
            text += [random.choice(wordDict[text[i-1]])]

        # Check if latest word is end word and set newSent accordingly
        if isLastWord(text[-1]):
            newSent = True
        else:
            newSent = False

    # return
    for i in text:
        print(i," ",end="")
        
