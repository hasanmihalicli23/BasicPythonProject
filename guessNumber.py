import random

def guessNumber(x):
    randomNumber = random.randint(1, x)
    guessNumber = 0
    while guessNumber != randomNumber:
        guessNumber = int(input(f"Guess a number between 1 and {x}: "))
        if guessNumber < randomNumber:
            print("Sorry, guess again. Too low.")
        elif guessNumber > randomNumber:
            print("Sorry, guess again. Too high.")
    
    print(f"Congratulations. Congratulations. The number you guessed is {randomNumber} correct.")

guessNumber(100)