count_list = [1,2,3,a,5,6,7,8,b,10]
for key in cart:
            price = cart[key]["price"]
            quantity = cart[key]["quantity"]
            print(int(price)* quantity)