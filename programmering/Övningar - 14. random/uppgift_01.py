# Uppgift 1
import random

var = random.randint(1, 100)
guess = None
while guess != var:
    guess = int(input("Guess the number: "))
    if guess == var:
        print("Congrats you FUCKER")
    elif guess > var:
        print("Too FKN high")
    else:
        print("Too FKN low")
