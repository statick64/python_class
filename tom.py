while True:
    programe = int(input("What would you love to do: \n1. For year you would be 100  \n2. To run pythagorays Thoerem  \n3. To add 2 Fractions enter \n4. To check if there is a vowel a in your sentence \n5. To print your name a 1000 times \n6. To find the square of the number \n7. To know if a number is divisible by 15: "))
    print(" ")

    if programe == 1:
        variable_input = input("Enter your name: ")
        print("Hello", variable_input)
        age_string = input("Enter your age: ")
        age = int(age_string)
        number_of_year_left = 100 - age
        year_person_was_born = 1919 + number_of_year_left ##using 1919 as base year
        year_as_at_100 = year_person_was_born + 100
        print(variable_input,"would be 100 at year", year_as_at_100)
        print(str(" "))

        number_of_prints = input("input another number 1- 100: ")
        name = (str(variable_input) + " would be 100 at year " + str(year_as_at_100) + "\n")
        print(name *  int(number_of_prints))
        print(str(" "))
    elif programe == 2:
        num1 = int(input("input a: "))
        num2 = int(input("input b: "))
        c = (num1**2 + num2**2)**0.5
        print(c)
        print(str(" "))
    elif programe == 3:
        from fractions import Fraction
        num1 = int(Fraction(input("input first fraction with / in between: ")))
        num2 = int(Fraction(input("input second fraction with / in between: ")))
        c = (Fraction(num1)) + (Fraction(num2))
        print (Fraction(c))
        print(str(" "))
    elif programe == 4:
        name = input("input: ")
        co_a = name.count("a")
        if co_a >= 1:
            print("There are " + str(co_a) + " a's in your sentence")
            print(str(" "))
        else:
            print("There are no a's in your sentence")
            print(str(" "))
    elif programe == 5:
        name = input("input name: ")
        m = (name + "\n")
        print(m * 1000)
        print(str(" "))
    elif programe == 6:
        num = int(input("input number: "))
        print(num**2)
        print(str(" "))
    elif programe == 7:
        num = int(input("input number: "))
        if num % 15 == 0:
            print("Number is divisible by 15")
            print(str(" "))
        else:
            print("Number is not divisible by 15")
            print(str(" "))
    else:
        print("Please input a valid number")