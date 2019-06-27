import time
import random
while True:
    print("\n\nAvailable items: Bread : N20   Mango: N50     Catfish: N15     Love: N5000000 \n")
    main_choice = int(input("\nWhat would you love to do \n1. View cart\n2. Add to cart\n3. Remove from cart: "))

    Main_cart = []
    price = []

    stop = 1         #To break the first while loop
    if main_choice == 2:            #If input is exactly 2 run this block of code
        
        while stop == 1:            
            
            choice = input("\nWhat would you like to add to your shopping cart: ")
            small_chioce = choice.lower()
           
            if small_chioce == "bread":            # Code to add bread to cart
                time.sleep(1)
                Main_cart.append("Bread")
                price.append("N20")
                time.sleep(1)
                print("\nprocessing.....\n")
                print(Main_cart)
                time.sleep(1)
                print(f"{choice} has been added to your cart\n")
            elif small_chioce == "mango":          # Code to add mango to cart
                time.sleep(1)
                Main_cart.append("Mango")
                price.append("N50")
                time.sleep(1)
                print("\nprocessing.....\n")
                print(Main_cart)
                time.sleep(1)
                print(f"{choice} has been added to your cart\n")
            elif small_chioce == "catfish":          # Code to add catfish to cart
                time.sleep(1)
                Main_cart.append("Catfish")
                price.append("N15")
                time.sleep(1)
                print("\nprocessing.....\n")
                time.sleep(1)
                print(f"{choice} has been added to your cart\n")
            elif small_chioce == "love":             # Code to add love to cart
                time.sleep(1)
                Main_cart.append("Love")
                price.append("N500000")
                time.sleep(1)
                print("\nprocessing.....\n")
                time.sleep(1)
                print(f"{choice} has been added to your cart\n")
            else:
                print("not on the list")
                continue            #if chioce is not on the list go back to the begining
            stop_2 = 1              #break second while loop
            while stop_2 == 1:
                sub_chioce = input("Would you like to add any more items to your shoping cart yes/no: ")
                sub_chioces = sub_chioce.lower()
                if sub_chioces == "yes":
                    stop_2 -=1      #break loop and go back to first while loop
                    continue
                elif sub_chioces == "no":
                        stop -= 1       #break both loops and go back to first code
                        stop_2 -= 1
                else:
                    print("\nplease input yes or no\n")
        second_chioce = input("\nProceed to checkout yes or no : ")
        if second_chioce == 'no':       #If no go back to add to cart
            print("\nTaking you back to the shop\n")
            time.sleep(5)
            continue
        else:
            Third_chioce = input("\nContinue yes or no : ")
            print("\nPROCESSING\n")
            stop_3 = 0              #To break third while loop
            while stop_3 <= 2:
                print(".")
                time.sleep(1)       #To print out "." 3 times at one second interval
                stop_3 += 1
            print("\nGENERATING CAPTCHA\n")
            stop_4 = 0
            while stop_4 <= 3:
                print(".")
                time.sleep(1)
                stop_4 += 1
            print("\nEnter the captcha given below.\n")
            captcha = random.randint(111111,999999)
            print(f"\nCaptcha: {captcha}\n")
            user_6 = int(input("input captcha here: "))
            if user_6 != captcha:
                print("ABORTING IN 5 SECONDS.")
            f = 0
            print("\nAWAITING IMFORMATION.\n")
            while f <= 5:
                print(".")
                time.sleep(1)
                f += 1
            print("\nTRANSACTION SUCCESSFUL.\n")
    elif main_choice == 1:
        print(Main_cart)
