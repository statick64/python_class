height = float(input("input height: "))
wieght = float(input("input wieght: "))
def bmi(wieght,height):
    work_bmi = wieght/(height**2)
    opt_weight = optimalweight(height)
    print(f"your optimal weight is {opt_weight}")
    check_overweight(work_bmi)
    return work_bmi


def check_overweight(bmi):
    if bmi < 18.5:
        print("underweight")
    elif bmi > 24.9:
        print("overweight")
    else:
        print("your ok")

def optimalweight(height):
    optimal_weight = 21.7 * (height**2)
    return optimal_weight
    
    
bmi(wieght,height)