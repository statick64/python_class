person = input("Enter your name: ")
print("Hello", person)
age_string = input("Enter your age: ")
age = int(age_string)
number_of_year_left = 100 - age
year_person_was_born = 1919 + number_of_year_left ##using 1919 as base year
year_as_at_100 = year_person_was_born + 100
print(person,"would be 100 at year", year_as_at_100)

number_of_prints = input("input another number: ")
name = (str(person) + " would be 100 at year " + str(year_as_at_100) + "\n")
print(name * int(number_of_prints))
