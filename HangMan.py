import random

wordList = ['heineken', 'television', 'house', 'table', 'pizza', 'bar', 'cat', 'car', 'supermarket', 'volkswagen', 'bmw']
listLenght = len(wordList) - 1
chosenWord = random.randint(0, listLenght)
theWord = wordList[chosenWord]
wordLenght = len(theWord)
theWordLetters = list(theWord)
allowedGuesses = 5
wrongGuessTotal = 0
underscores = "_" * wordLenght
letterSituation = list(underscores)

print("Hi! This game's idea is to guess letters from a random word. You win if you get the whole word\n"
      "and lose if you make", allowedGuesses, "wrong guesses. Hint: The word is ", wordLenght, " letters long word\n")

while wrongGuessTotal < allowedGuesses:
    guess = input('Make a guess: \n')

    if guess in theWordLetters:
        letterLocations = [i for i in range(wordLenght) if theWordLetters[i] == guess]
        numberOfLetters = (len(letterLocations))
        x = 0
        while numberOfLetters > x:
            change = letterLocations[x]
            letterSituation[change] = guess
            x += 1

        if '_' not in letterSituation:
            print(theWord, 'is the right word! You won!')
            break
        print(*letterSituation)

    elif guess not in theWordLetters:
        wrongGuessTotal += 1
        if wrongGuessTotal < allowedGuesses:
            print('Wrong guess, you have ', str(allowedGuesses - wrongGuessTotal), ' tries left')
        else:
            break

if(wrongGuessTotal == allowedGuesses):
    print('You guessed wrong', allowedGuesses, 'times, you lose! The right word was ', theWord)