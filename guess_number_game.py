# Guessing Number Game

from random import randint
x = randint(1, 100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guesses = []
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
    if len(guesses) >= 2:
        if abs(guesses[-2] - x) > abs(num - x):
            print("WARMER!")
        elif abs(guesses[-2] - x) < abs(num - x):
            print("COLDER!")
    else:
        if num in range(x - 10, x):
            print("WARM!")
        else:
            print("COLD!")
