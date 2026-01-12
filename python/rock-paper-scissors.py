# Rock Paper Scissors Game

# import statements
import time
import random

# computer guess logci
raw = random.randint(1,3)
if raw == 1:
    decision = 'Rock'
elif raw == 2:
    decision = 'Paper'
else:
    decision = 'Scissors'
# Game logic
print('Rock...')
time.sleep(1)
print('Paper')
time.sleep(1)
print('Scissors \n')
time.sleep(2)
print(decision)
userint = input('What did you get?')

# winning game logic

# game tie logic
if userint in ('Rock', 'rock') and decision == 'Rock':
    print("It's a tie. Try again ")
if userint in ('scissors', 'Scissors') and decision == 'Scissors':
    print("It's a tie. Try again ")
if userint in ('Paper', 'paper') and decision == 'Paper':
    print("It's a tie. Try again ")

# game beat logic

# computer beat logic
if userint in ('Paper', 'paper') and decision == 'Scissors':
    print("Scissors beats paper! Computer wins.")
if userint in ('scissors', 'Scissors') and decision == 'Rock':
    print("Rock beats scissors! Computer wins.")
if userint in ('rock', 'Rock') and decision == 'Paper':
    print("Paper beats rock! Computer wins.")

# user beat logic
if userint in ('scissors', 'Scissors') and decision == 'Paper':
    print("Scissors beats Paper. You win!")
if userint in ('Rock', 'rock') and decision == 'Scissors':
    print("Rock beats scissors. You win!")
if userint in ('Paper', 'paper') and decision == 'Rock':
    print("Paper beats rock. You win!")