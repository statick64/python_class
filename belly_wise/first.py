data = input("input data in format example:  1/2 + 3/4: ")
def change(a):
    first_split = data.split("+")
    first_num = first_split[0]
    second_num = first_split[1]
    second_split = first_num.split("/")
    third_split = second_num.split("/")
    num1 = second_split[0]
    den1 = second_split[1]
    num2 = third_split[0]
    den2 = third_split[1]
    return int(num1),int(num2),int(den1),int(den2)

def den3(den1,den2):
    cal1 = den1 * den2
    return cal1

def num3(num1,num2,den1,den2):
    cal2 = (num1 * den2) + (num2 * den1)
    return cal2

def lcm(num3,den3):
        for i in range(1,10):
                if num3 % i == 0 and den3 % i == 0:
                        a = num3/i
                        b = den3/i
        print(f"{int(a)}/{int(b)}")


def fraction(data):
    splitted_fraction = change(data)
    resolved_denum = den3(splitted_fraction[2], splitted_fraction[3]) 
    resolved_numerator = num3(splitted_fraction[0],splitted_fraction[3],splitted_fraction[1],splitted_fraction[2])
    lcm(resolved_denum,resolved_numerator)
    return resolved_denum,resolved_numerator

fraction(data)


