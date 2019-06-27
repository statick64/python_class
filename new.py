from hunter import naira_dollar,dollar_naira

chioce = int(input("\nNaira to dollar enter 1\nDollar to naira enter 2: "))



if chioce == 1:
    naira = int(input("input naira: "))
    naira_dollar(naira)
elif chioce == 2:
    dollar = int(input("input dollar: "))
    dollar_naira(dollar)
else:
    print("wrong input")