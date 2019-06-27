chioce = int(input("Naira to dollar enter 1\nDollar to naira enter 2: "))


def dollar_naira(dollar):
    conversion = dollar * 305
    print(f"{dollar} dollar is equal to {conversion} naira")

def naira_dollar(dollar):
    conversion = naira / 305
    print(f"{dollar} naira is equal to {conversion} dollar")

if chioce == 1:
    naira = int(input("input naira: "))
    naira_dollar(naira)
elif chioce == 2:
    dollar = int(input("input dollar: "))
    dollar_naira(dollar)
else:
    print("wrong input")