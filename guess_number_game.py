"""
Let's use while loops to create a guessing game.

The Challenge:

Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:

If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
On a player's first turn, if their guess is
within 10 of the number, return "WARM!"
further than 10 away from the number, return "COLD!"
On all subsequent turns, if a guess is
closer to the number than the previous guess return "WARMER!"
farther from the number than the previous guess, return "COLDER!"
When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided.
"""

from random import randint
x = randint(1, 100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
y = 1
guesses = [0]
while True:
    num = int(input("Please enter a number here:"))
    if num < 1 or num > 100:
        print("OUT OF BOUNDS")
        continue
    if num == x:
        print("You've guessed correctly and it took", len(guesses), "guesses!")
        print("Your guesses are:", guesses)
        break
    guesses.append(num)
    if guesses[-2]:
        if abs(guesses[-2] - x) > abs(num - x):
            print("WARMER!")
        else:
            print("COLDER!")
    else:
        if num in range(x - 10, x):
            print("WARM!")
        else:
            print("COLD!")


