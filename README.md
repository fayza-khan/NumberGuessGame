# Guess the Number

Welcome to the Number guessing game.

## Description
A random number is selected from the range of 1 to 100. The player is supposed to guess the number with hints given by the game about how close or far player is in his or her guess. Enjoy!

## How to play

1. If a player's guess is less than 1 or greater than 100, the game returns "OUT OF BOUNDS"
2. On a player's first turn, if their guess is within 10 of the target number, the game returns "WARM!", further than 10 away from the number, return "COLD!"
3. On all subsequent turns, if a guess is closer to the number than the previous guess it returns "WARMER!", farther from the number than the previous guess, else returns "COLDER!"

## About the project
### Programming Language used:
- Python 3
### Notes:
- This script is an interactive guessing game, which will ask the user to guess a number between 1 and 99.
- We are using the random module with the randint function to get a random number. The script also contains a while loop, which make the script run until the user guess the right number.

