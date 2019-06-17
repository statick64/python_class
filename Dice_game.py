import random
rolls = 0
while rolls < 10:
    first_roll = random.randint(1,7)
    second_roll = random.randint(1,7)
    rolls += 1
    print(first_roll,second_roll)
    if first_roll == 6 and second_roll == 6:
        
        break
        
        print("You Have Won")
    else:
        
        print("You Have Lost")