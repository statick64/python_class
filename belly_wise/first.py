data = input("input data in format example:  1/2 + 3/4: ")
def change(data):
    first_split = data.split("+")
    first_num = first_split[0]
    second_num = first_split[1]
    second_split = first_num.split("/")
    third_split = second_num.split("/")
    num1 = second_split[0]
    den1 = second_split[1]
    num2 = third_split[0]
    den2 = third_split[1]
    solution1 = den3(den1,den2) 
    solution2 = num3(num1,num2,den1,den2)
    ans = (f"{solution2}/{solution1}")
    return ans


def den3(den1,den2):
    cal1 = int(den1) * int(den2)
    return cal1

def num3(num1,num2,den1,den2):
    cal2 = (int(num1) * int(den2)) + (int(num2) * int(den1))
    return cal2

   

print(change(data))
