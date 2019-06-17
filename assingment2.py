position = 0
for numbers in range(100,999):
    sum_of_numbers = numbers+numbers+numbers
    new_sum_numbers = str(sum_of_numbers)
    last_number = (new_sum_numbers[2],new_sum_numbers[2],new_sum_numbers[2])
    new_string =""
    jioned_last_number = new_string.join(last_number)
    position +=1
    if sum_of_numbers == int(jioned_last_number):
        if position == position:
                new_numbers = str(numbers)
                if new_numbers[0] != new_numbers[1] and new_numbers[1] != new_numbers[2] and new_numbers[0] != new_numbers[2]:
                        new_sum_numbers = str(sum_of_numbers)
                        if new_numbers[2] in new_sum_numbers:
                                print(f"\nThe number that when added to itself three times would give you its last number is {new_numbers}\n")