number = int(input("input number you want to find divisor to "))

a = list(range(2,number)
a2 = []
for i in a:
    if i % number == 0:
        a2.append(i)
if len(a2) == 1:
    print("The only divisor for " + str(number) + "is " + a2)
elif len(a2) > 1:
    print("The numbers divisible by " + str(number) + "is " + a2)
else:
    print("no number divisible by " + str(number))