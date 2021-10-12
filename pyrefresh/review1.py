# user guesses a random number

t_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
t_sq =  ( num**2 for num in range (1,10))
t_odds = ( num for num in range (0,100) if num%2 != 0)
t_evens = ( num*2 for num in range (0,50))


from random import randint
r = randint(0,100)

userin = 0
tries = 0
i = 0

while i != -1:
    userin = input('Guess a random number between 0 and 100: (-1 to quit; -2 for hint) ')

    if userin.isalpha():
        print('C\'mon... That\'s not a number!')
#        break
    else:
        i = int(float(userin))
        if i == -1:
            print('You quit after ', tries, ' tries!')
        elif i == r:
            print(i , 'You guessed it right! You took ', tries, ' tries.')
            #print('Play on again...')
            break
        elif i == -2 :
            if r in t_primes:
                print('HINT: is a prime number')
            elif r in t_sq:
                print('HINT: is a square number')
            elif r in t_evens:
                print('HINT: is an even number, but it\'s not a square')
            elif r in t_odds:
                print('HINT: is an odd number, but it\'s not a square, not a prime')
        elif i > r :
            print(i , 'is too high!  Go low...')
        elif i < r :
            print(i , 'is too low!  Go high...')
        tries += 1

        