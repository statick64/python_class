while True:
    programe = int(input("\nWhat would you love to do: \n1. For year you would be 100  \n2. To run pythagoras Thoery calculator  \n3. To add 2 Fractions  \n4. To check the number of vowels in a sentence \n5. To print your name 1000 times \n6. To find the square of a number \n7. To know if a number is divisible by 15 \n8. To print 12 multiples table for a given number \n9. To check if a number is even or odd \n10. To reverse a word: "))

    if programe is 1:
        print("\n1. 100 Year Calculator\n")
        import datetime
        current_date = datetime.datetime.now()
        variable_input = input("Enter your name: ")
        print("Hello", variable_input)
        age_string = int(input("Enter your age: "))
        new_age = 100 - age_string
        newest_age = new_age + current_date.year
        print(f"variable_input would be 100 at year {newest_age}")
        print(str(" "))

        number_of_prints = input("input another number 1- 100: ")
        name = (f"{variable_input} would be 100 at year {newest_age}  \n")
        print(name *  int(number_of_prints))
        print(str(" "))
    elif programe == 2:
        print("\n2. Pythagoras Thoery Calculator\n")
        num1 = int(input("input a: "))
        num2 = int(input("input b: "))
        c = (num1**2 + num2**2)**0.5
        print(c)
        print(str(" "))
    elif programe == 3:
        print("\n3. Adding 2 Fractions\n")
        data = input("input data in format 1/2 + 3/4: ")
        first_split = data.split("+")
        first_num = first_split[0]
        second_num = first_split[1]
        second_split = first_num.split("/")
        third_split = second_num.split("/")
        num1 = second_split[0]
        den1 = second_split[1]
        num2 = third_split[0]
        den2 = third_split[1]
        den3 = int(den1) * int(den2)
        num3 = (int(num1) * int(den2)) + (int(num2) * int(den1))
        ans = (f"{num3}/{den3}")
        print((ans))
        print(str(" "))
    elif programe == 4:
        print("\n4. Number Of Vowels In A Sentence\n")
        name = input("input a sentence or a word: ")
        co_a = name.count("a")
        co_e = name.count("e")
        co_i = name.count("i")
        co_o = name.count("o")
        co_u = name.count("u")
        co_vowels = (co_a + co_e + co_i + co_o + co_u)
        if co_vowels >= 1:
            print(f"There are  {co_vowels}  vowels in your sentence")
            print(str(" "))
        else:
            print("There are no vowels in your sentence")
            print(str(" "))
    elif programe == 5:
        print("\n5. Print Your Name 100 times\n")
        name = input("input name: ")
        m = (name + "\n")
        print(m * 1000)
        print(str(" "))
    elif programe == 6:
        print("\n6. To Calculate The Square Of A Number")
        num = int(input("input number: "))
        print(num**2)
        print(str(" "))
    elif programe == 7:
        print("\n7. To calculate If A Number Is Divisible By 15\n")
        num = int(input("input number: "))
        if num % 15 == 0:
            print("Number is divisible by 15")
            print(str(" "))
        else:
            print("Number is not divisible by 15")
            print(str(" "))
    elif programe == 8:
        print("\n8. To Print 12 Multiples Table For A Given Number\n")
        num1 = int(input("input number: "))
        for i in range(1,13):
            print(f"{num1} * {i} = {i* num1}")
            print(str(" "))
    elif programe == 9:
        print("\nProgram To Tell If A Number Is Even Or Odd\n")
        num1 = int(input("Enter an integer: "))
        if num1 % 2 == 0:
            print(f"Output {num1} is even")
        else:
            print(f"Output {num1} is odd")
    elif programe == 10:
        print("\nProgram To Reverse A Word\n")
        word = input("input word: ")
        bad = ("".join(reversed(word)))
        if word == bad:
            print(f"{word} and {bad} are the same")
        else:
            print(f"{word} and {bad} are not the same")
    else:
        print("Please input a valid number")