"""
This code generates a random number between 0 and 20 and if a person guesses the right number then they win
else if the number is less then it prints Too Low or if the number is higher than secret then it prints Too High.
"""

from random import randrange

secret = randrange(20)
while True:
    inputNum = int(input("Guess a number between 0 and 20: "))
    if secret == inputNum:
        print("You won")
        break
    elif secret > inputNum:
        print("Too Low")
    else:
        print("Too High")