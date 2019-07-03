import ast





class Shop:
    
    def product_list(self):
        file_ = open("shop.txt","r+")
        product_list = ast.literal_eval(file_.readline())
                
        return product_list

    def add(self):
        raw_input = input("Please enter product name")

