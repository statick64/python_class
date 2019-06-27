import time
import random

item = ["Laptop","T-Shirt","Pants"] #You may add your own items
cost = ["Rs 35600","Rs 2000","Rs 1200"] #You may add your own price of your items but make sure you update the program necessarily. 
x = []
l = []
print()
for i,j in zip(item,cost):
    print(i,"=",j)
    print()
choice = 'y' or 'n'
count = 0

while choice == 'y' or choice == 'YES' or choice == 'yes' or choice =='Y':
    print()
    user_1 = input("Enter the name of the item which you would like to purchase : ")
    print()    
    user_2 = int(input("Enter the cost of the item which you would like to purchase : {} ".format("Rs")))
    print()
    if user_2 == 35600 or user_2 == 2000 or user_2 == 1200:
        l.append(user_2)
    else:
        print()
        print("DONT CHEAT. ABOTING IN 5 SECONDS.")
        time.sleep(5)
        break
    if user_1 in item:
        x.append(user_1)
        print()
        print(user_1,"has been added to your cart.")
        print()
        count += 1
    else:
        print()
        print("Item not found.Try restarting the app.")
    choice = input("Do you want to add any other item to your cart : ")

while choice == 'n' or choice == 'no' or choice == 'NO' or choice == 'N':
    print()
    print("There are",count,"items in your cart")
    print()
    print("Total : {}".format("Rs"),sum(l))
    print()
    user_4 = input("Proceed to checkout (y/n) : ")
    if user_4 == 'n':
        print()
        print("ABORTING IN 5 SECONDS")
        time.sleep(5)
        break
    else:
        print()
        user_5 = input("Select payment method (Credit/Debit) : ")
        print()
        print("PROCESSING")
        r = 0
        while r <= 2:
            print(".")
            time.sleep(1)
            r += 1
        print()
        print("GENERATING CAPTCHA")
        b = 0
        while b <= 3:
            print(".")
            time.sleep(1)
            b += 1
        print()
        print("Enter the captcha given below.")
        print()
        captcha = random.randint(111111,999999)
        print(captcha)
        print()
        user_6 = input()
        if user_6 != captcha:
            "ABORTING IN 5 SECONDS."
        else:
            continue
        f = 0
        print()
        print("AWAITING IMFORMATION.")
        while f <= 5:
            print(".")
            time.sleep(1)
            f += 1
        print()
        print("TRANSACTION SUCCESSFUL.")
        print()
        print("Thank You for choosing Muhammed©")
        break