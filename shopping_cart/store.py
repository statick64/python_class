import ast


class Shop:
    
    def product_list(self):
        file_ = open("shop.txt","r+")
        product_list = ast.literal_eval(file_.readline())
                
        return product_list

    def add(self):
        raw_input = input("Please enter product name seperate with a (/): ")
        product = raw_input.split("/")
        p_name, p_price, p_quantity = product[0], product[1], int(product[2])
        original_product = self.product_list()
        original_product[p_name] = {
                                    "name":p_name,
                                    "price": p_price,
                                    "quantity":p_quantity
                                    }
        self.write_to_file(original_product)
        print(f"{p_name} : {p_quantity} has been added to shelf successfully")
    
    def remove_from_shop(self):
        raw_input = input("Please enter product name: ")
        removed_product = self.product_list()
        del removed_product[raw_input]
        self.write_to_file(removed_product)
        print(f"{raw_input} has been removed")
    
    def change_product_quantity(self):
        raw_input = input("please enter product name and quatity you whis to replace seperate with a (/): ")
        product = raw_input.split("/")
        p_name, p_quantity = product[0], int(product[1])
        changed_quantity = self.product_list()
        changed_quantity[p_name]["quantity"] = p_quantity
        self.write_to_file(changed_quantity)
        print(f"{p_name} quantity has been changed to {p_quantity}")
    
    def change_product_price(self):
        raw_input = input("please enter product name and price you whis to replace seperate with a (/): ")
        product = raw_input.split("/")
        p_name, p_price = product[0], product[1]
        changed_quantity = self.product_list()
        changed_quantity[p_name]["price"] = p_price
        self.write_to_file(changed_quantity)
        print(f"{p_name} quantity has been changed to {p_price}")

    def write_to_file(self, new_products):
        file_ = open("shop.txt", "w")
        file_.write(str(new_products))


    def get_single_product(self,required_product):
        all_products = self.product_list()
        single_product = all_products[required_product]
        return single_product
    
class User:

    def __init__(self,username):
        self.username = username
        self.shop = Shop()
    
    def read_file_cart(self,required):
        file_ = open("user.txt", "r+")
        all_users = ast.literal_eval(file_.readline())
        current_user = all_users[self.username]
        if required == "all":
            return all_users
        else:
            return  current_user[required]
    
    def read_file(self):
        file_ = open("user.txt", "r+")
        all_users = ast.literal_eval(file_.readline())
        return all_users
    
    def add_new_user(self):
        raw_input = input("Please enter product name/balance seperated by slash(/) : ")
        users = raw_input.split("/")
        username, user_balance = users[0], users[1],
        all_users = self.read_file()
        all_users[username] = {
                                    "username": username,
                                    "balance": user_balance,
                                    "cart": {}  
                                }
        self.write(all_users)
        print(f"user{all_users[username]} has been created")
    
    
    def balance(self):
        balance = self.read_file_cart("balance")
        print(f"Your wallet has {balance}  ")
        return balance
    
    def cart(self):
        cart = self.read_file_cart("cart")

        for key in cart:
            print((cart[key]["name"]).center(10), str(cart[key]["price"]).center(5), str(cart[key]["quantity"]).center(2))
        if len(cart) == 0:
            print(f"{self.username}'s cart is empty'")
        return cart
    
    def new_cart(self):
        cart = self.read_file_cart("cart")
        return cart
    
    def add_to_cart(self):
        selected_prod = input("Please enter your product of choice and amount to be added and  seperate with (/): ")
        new_selected_prod = selected_prod.split("/")
        sp_name, sp_amount = new_selected_prod[0], new_selected_prod[1]
        fetched_product = self.shop.get_single_product(sp_name)
        fetched_product["quantity"] = int(sp_amount)
        shop = self.shop
        cart = self.cart()

        if cart.get(fetched_product["name"], False) :
            cart[fetched_product["name"]]["quantity"] += fetched_product["quantity"]
        else:
            cart[fetched_product["name"]] = fetched_product 
        all_users = self.read_file_cart("all")
        all_users[self.username]["cart"] = cart

        self.write(all_users)
        print(f"New product {fetched_product['name']} successfully added to cart")
    
    def total_price(self):
        cart = self.new_cart()
        sum_total = 0
        for key in cart:
            price = cart[key]["price"]
            qauntity = cart[key]["quantity"]
            total = (int(price) * qauntity)
            sum_total += total
        full_total = sum_total
        print(f"The total price of your cart is {full_total}")

        return full_total
    
    def payment(self):
        balance = self.balance()
        price = self.total_price()
        amount = int(balance) - price
        if price > int(balance):
            print("you do not have suficient funds to carry out this operation")
        else:
            print(f"your wallet has {amount}")
        all_users = self.read_file_cart("all")
        all_users[self.username]["balance"]= amount
        self.write(all_users)
        return all_users




    def remove_from_cart(self):
        selected_prod = input("Please enter your product of choice : ")
        cart = self.cart()
        del cart[selected_prod]
        all_users = self.read_file_cart("all")
        all_users[self.username]["cart"] = cart
        self.write(all_users)
        print(f"{selected_prod} has successfully been removed from cart")


    def write(self, data):
        file_ = open("user.txt", "w")
        file_.write(str(data))
    


#active_shop = Shop()
#active_shop.add()
active_user = User("koko")
active_user.add_to_cart()
#active_user.amount_of_cart()






