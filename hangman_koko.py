import time
name = input("Bromida insert your name: ")
print(f"\nWelcome {name}, oya begin dey guess\n")

time.sleep(1)
print("Oya begin ")
time.sleep(0.5)
word = ["brother","mother","sister","mister","father"]
turns = 10
guesses = ""
while turns < 0:
    import random
    failed = 0
    for char in random.choice(word):
        if char in guesses:
            print(char)
        else:
            print("_")
            failed += 1
        if failed == 0:
            print("\nWe have a winner\n")
    guess = input("Guess a letter: ")
    guesses += guess
    if guess not in word:
        turns -= 1
        print("\nTry again\n")
        print(f"You have {turns} left\n")
        if turns == 0:
            print("You loose")