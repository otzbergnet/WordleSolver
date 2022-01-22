import os
import re

# badLetters are NOT in the word
badLetters = []

# goodLetters are either green or yellow
goodLetters = []
greenLetters = []
yellowLetters = []

# records the position of green and yellow letters
greenPosition = {}
yellowPosition = {}

def getCommon5():
    data = []
    file = open('common5.txt')
    for line in file:
        data.append(line.strip().lower())
    return data

def makePositionPattern():
    thePosition = ""
    position = 0
    while position < 5:
        if position in greenPosition:
            thePosition += greenPosition[position]
        else:
            thePosition += "."
        position += 1
    return thePosition
    
def makeNotPositionPattern():
    notPosition = ""
    position = 0
    while position < 5:
        if position in yellowPosition:
            notPosition += "[^"+yellowPosition[position]+"]"
        else:
            notPosition += "."
        position += 1
    return notPosition

def makeExcludePattern():
    exclude = ''.join(badLetters)
    pattern = "^[^"+exclude+"]{5}$"
    return pattern

def handleNotPositionPattern(word):
    notPosition = makeNotPositionPattern()
    # print(notPosition)
    return re.search(notPosition, word)

def handlePositionPattern(word):
    positionPattern = makePositionPattern()
    print(positionPattern)
    return re.search(positionPattern, word)

def matchesExcludePattern(word):
    excludePattern = makeExcludePattern()
    # print(excludePattern)
    return re.search(excludePattern, word)

def matchesIncludePattern(word):
    required = ''.join(goodLetters)
    # print(required)
    length = len(required)
    includes = False
    i = 0
    while i < length:
        if required[i] in word:
            includes = True
        else:
            return False
        i += 1
    return includes

def evaluateMatchingRules(word):
    if (
    matchesExcludePattern(word) 
    and matchesIncludePattern(word) 
    and handlePositionPattern(word) 
    and handleNotPositionPattern(word)
    ):
        return True
    else:
        return False

def printWords(commonWords, uncommonWords):
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(uncommonWords) > 15 and len(commonWords) > 0:
        print("We found so many words, that we'll show you common words only")
        print("this should help you pick your next guess\n")
        for word in commonWords:
            print(word)
    elif len(uncommonWords) > 15 and len(commonWords) == 0:
        print("We found many words, but surprisingly no common words\n")
        for word in uncommonWords:
            print(word)
    else:
        if len(commonWords) > 0:
            print("Here are common word matches\n")
            for word in commonWords:
                print(word)
        if len(uncommonWords) > 0:
            print("\nHere are uncommon words\n")
            for word in uncommonWords:
                print (word)
        if len(commonWords) == 0 and len(uncommonWords) == 0:
            print("oops that should not have happened")
            exit(1)

def runProcess():
    commonWords = []
    uncommonWords = []
    
    common5 = getCommon5()

    file = open("word-list-5.txt", "r")
    for line in file:
        word = line.strip().lower()
        if len(word) == 5:
            if(evaluateMatchingRules(word)):
                if(word in common5):
                    commonWords.append(word)
                else:
                    uncommonWords.append(word)
    printWords(commonWords,uncommonWords)

def interview():
    global badLetters
    global goodLetters
    global greenLetters
    global yellowLetters
    global greenPosition
    global yellowPosition

    print("\n--------------------------")
    guess = input("What was your guess: ")
    if guess == "quit" or guess == "win":
        exit(1)
    green = input("Green Tile Letters: ")
    yellow = input("Yellow Title Letters: ")

    # add all green letters to good letters
    for letter in green:
        if letter not in goodLetters:
            goodLetters.append(letter)
        # ensure our green letter array is correct
        if letter in goodLetters:
            greenLetters.append(letter)
        # ensure our yellow letter array is correct
        if letter in yellowLetters:
            yellowLetters.remove(letter)
    
    #yellow letters are also good letters
    for letter in yellow:
        if letter not in goodLetters:
            goodLetters.append(letter)
        if letter not in yellowLetters:
            yellowLetters.append(letter)

    # identify if any green letter shows up more than once in guess
    guessLetterRegister = []
    duplicateGuessLetter = []
    for letter in guess:
        if letter in guessLetterRegister:
            duplicateGuessLetter.append(letter)
        guessLetterRegister.append(letter)
    
    duplicateLetterLocation = {}
    if len(duplicateGuessLetter) > 0:
        for letter in duplicateGuessLetter:
            print("your guess contains the letter "+letter+" multiple times")
            print("please provide its position")
            duplicateLetterLocation[letter] = int(input("Location: "))-1

    # try to figure out the position of green letters
    postCount = 0
    for letter in guess:
        if letter not in goodLetters:
            badLetters.append(letter)
        if letter in greenLetters:
            if letter in duplicateLetterLocation:
                if postCount == duplicateLetterLocation[letter]:
                    greenPosition[postCount] = letter                    
            else:
                greenPosition[postCount] = letter
        if letter in yellowLetters:
            if postCount in yellowPosition:
                newLetters = yellowPosition[postCount] + letter
            else:
                newLetters = letter
            yellowPosition[postCount] = newLetters
        postCount += 1

    runProcess()
    interview()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    interview()


if __name__ == "__main__":
   main()