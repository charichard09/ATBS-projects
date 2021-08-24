# Practice debugging a preprogrammed buggy program
# Program is one that "tosses" a coin, and gives the user 2 chances to guess heads or tails
# Date: 6-25-21 Dev: Richard C.

import random
guess = ''
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails: ")
    guess = input()
toss = random.randint(0,1) #0 is tails, 1 is heads

# Convert int toss to string heads or tails equivalent
if toss == 1:
    toss = "heads"
else:
    toss = "tails"

# Remove 1 letter from guesss

if toss == guess:
    print("You got it!")
else:
    print("Nope! Guess again!")
    guess = input()
    if toss == guess:
        print("You got it!")
    else:
        print("Nope. You are really bad at this game.")