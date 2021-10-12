# random guessing game

from random import randint
myNum = randint(0,100)
numOfGuesses = 1
guessNum = int(input("Guess the number (-1 to quit): "))

while guessNum != myNum:
    if guessNum == -1:
        print ("Oh bother!")
        break
    elif guessNum > myNum:
        print ("Too high!")
    else:
        print ("Too low!")
    
    if (guessNum == -2) | (numOfGuesses == 3):
        if myNum%2 == 0:
            print ("Clue: it is an even number")
        else:
            print ("Clue: it is an odd number")
    numOfGuesses+=1
    guessNum = int(input("Guess the number (-1 to quit OR -2 to get a clue): "))

print ("The number was ", myNum)
print ("You took", numOfGuesses, "attempts")
