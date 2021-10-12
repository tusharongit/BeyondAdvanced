# random guessing game

from random import randint
myNum = randint(0,100)
numOfGuesses = 1

num_list_sq = [num**2 for num in range(0,10)]
#print("Squares:", num_list_sq)

num_list_ev = [num for num in range(0,100,2)] # [num for num in range(0,100) if num%2==0]
#print("Evens:", num_list_ev)

num_list_od = [num for num in range(1,100,2)] # [num for num in range(0,100) if num%2==1]
#print("Odds:", num_list_od)

num_list_pr = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
#print("Primes:", num_list_pr)

if (myNum in num_list_sq):
    clue="The number is a sqaure"

if (myNum in num_list_ev):
    clue="The number is an even number"

if (myNum in num_list_od):
    clue="The number is an odd number"

if (myNum in num_list_pr):
    clue="The number is a prime"

guessNum = int(input("Guess the number (-1 to quit): "))

while guessNum != myNum:
    if guessNum == -1:
        print ("Oh you gave up!")
        break
    elif guessNum > myNum:
        print ("Too high!")
    else:
        print ("Too low!")
    
    if (guessNum == -2) | (numOfGuesses == 3):
        print (clue)

    numOfGuesses+=1
    guessNum = int(input("Guess the number (-1 to quit OR -2 to get a clue): "))

print ("The number was ", myNum)
print ("You took", numOfGuesses, "attempts")
