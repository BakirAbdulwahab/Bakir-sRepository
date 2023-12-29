import random

print("Welcome to our Hangman Game!")
print("----------------------------")

wordBank = ["update", "strike", "clerk", "accompany", "exploit", "banana", "sailor", "pan", "conception", "polite", "thought", "stimulation", "gradual", "straight", "discount", "regard", "deny", "retire", "carbon", "relinquish"]

randomWord = random.choice(wordBank)

for x in randomWord:
    print("_", end = " ")


def printHangman(wrong):
    if(wrong == 0):
        print("\n+--+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 1):
        print("\n+--+")
        print(" 0  |")
        print("    |")
        print("    |")
        print("   ===")
    elif(wrong == 2):
        print("\n+--+")
        print(" 0  |")
        print(" |  |")
        print("    |")
        print("   ===")
    elif(wrong == 3):
        print("\n+--+")
        print(" 0  |")
        print(" |\ |")
        print("    |")
        print("   ===")
    elif(wrong == 4):
        print("\n+--+")
        print(" 0  |")
        print("/|\ |")
        print("    |")
        print("   ===")
    elif(wrong == 5):
        print("\n+--+")
        print(" 0  |")
        print("/|\ |")
        print("  \ |")
        print("   ===")
    elif(wrong == 6):
        print("\n+--+")
        print(" 0  |")
        print("/|\ |")
        print("/ \ |")
        print("   ===")




def printWord(guessedLetters):
    letterCounter = 0
    correctLettersCounter = 0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[letterCounter], end = " ")
            correctLettersCounter+=1
        else:
            print(" ", end = " ")
        letterCounter+=1
    return correctLettersCounter

def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end = " ")


lengthOfRandomWord = len(randomWord)
wrongLetterChosen = 0
currentGuessIndex = 0
currentLettersGuessed = []
lettersCorrect = 0

while (wrongLetterChosen != 6 and lettersCorrect != lengthOfRandomWord):
    print("\nLetters you have guessed: ")
    for letter in currentLettersGuessed:
        print(letter, end = " ")
    
    letterGuessed = input("\nPlease guess a letter: ")
    
    if (randomWord[currentGuessIndex] == letterGuessed):
        printHangman(wrongLetterChosen)
        currentGuessIndex+=1
        currentLettersGuessed.append(letterGuessed)
        lettersCorrect = printWord(currentLettersGuessed)
        printLines()
    else:
        wrongLetterChosen+=1
        currentLettersGuessed.append(letterGuessed)
        printHangman(wrongLetterChosen)
        lettersCorrect = printWord(currentLettersGuessed)
        printLines()

print("\nGame Over! Thank you for playing!")