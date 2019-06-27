import time
import random
name = input("Bromida insert your name: ")
print(f"\nWelcome {name}, oya begin dey guess\n")
word = ["brother","mother","sister","mister","father"]
guesses = ""    
turns = 10
while turns>= 0:
    failed = 0
    for char in random.choice(word):
        if char in guesses:
            print(char, end="")
        else:
            print("_",end="")
            failed += 1
        if failed == 0:
            print("\nWe have a winner\n")
        guess = input("Guess a letter: ")
        guesses = guess
        if guess not in word:
            turns -= 1
            print("\nTry again\n")
            print(f"You have {turns} left\n")
        if turns == 0:
            print("You loose")