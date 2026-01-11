# Number Guessing Game
# by ajm19826


# import
import random

# store random numbers
rawrange1 = random.randint(1, 195)
rawrange2 = random.randint(1, 195)

# duplicate & limit reached number logic
if rawrange1 == rawrange2:
    rawrange1 = random.randint(rawrange2 + 1, 195)
if rawrange1 > 195:
    print("error: range(s) are greater then max limit. try restarting")
elif rawrange2 > 195:
    print("error: range(s) are greater then max limit. try restarting")

# guess by prograam if no errors
guess = random.randint(rawrange1, rawrange2)

# user guess defined
userguess = None
# user game input logic
print(f'I am thinking of a number between {rawrange1} & {rawrange2}... what could it be?')
userguess = input('Your Guess:')

while True:
# loop until correct
    if userguess == guess:
        print(f'You guessed it! The number was {guess}')
        break
    else:
        print('incorrect, try again...')

        try:
            userguess = int(input('Your Guess:'))
        except Exception as e:
            print(e)
