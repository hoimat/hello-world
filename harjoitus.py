import random

def Guessing():
    TheNumber = random.randint(1, 100)
    TotalGuesses = 1
    Guess = int(input('Your guess is: '))
    
    while Guess != TheNumber:
        TotalGuesses += 1
        if Guess < TheNumber:
            Guess = int(input("It's higher, guess again: "))
        elif Guess > TheNumber:
            Guess = int(input("It's lower, guess again: "))

    if Guess is TheNumber:
        print("That's right, you win! You guessed", TotalGuesses, 'times')

Start = input('Do you want to play a number guessing game? y/n: ')

while Start != 'y':
    if Start is 'n':
        print("Okay, so we're done here.")
        break
    else:
        Start = input('Write just y or n, try again: ')
if Start is 'y':
    Guessing()
