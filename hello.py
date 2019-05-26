while True:
    programe = int(input("What would you love to do: \nFor year you would be 100 enter 1\nTo run pythagorays Thoerem enter 2\nTo add 2 Fractions enter 3\nTo check if there is a vowel a in your sentence enter 4\nTo print your name a 1000 times enter 5\nTo find the square of the number enter 6\nTo know if a number is divisible by 15 enter 7: "))

    if programe == 1:
        variable_input = input("Enter your name: ")
        print("Hello", variable_input)
        age_string = input("Enter your age: ")
        age = int(age_string)
        number_of_year_left = 100 - age
        year_person_was_born = 1919 + number_of_year_left ##using 1919 as base year
        year_as_at_100 = year_person_was_born + 100
        print(variable_input,"would be 100 at year", year_as_at_100)
    elif programe == 2:
        num1 = int(input("input a: "))
        num2 = int(input("input b: "))
        c = (num1**2 + num2**2)**0.5
        print(c)
