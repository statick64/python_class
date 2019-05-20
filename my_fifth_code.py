name = "ada"
age = 30
relationship = "friends"
discount = 0.15
price = 40000
original_price = 40000
discount_percent = discount * price
new_price = original_price - discount_percent
sentence = "Hello " + (name) + " "+ "because we are " + (relationship) + " " + "will drop the price from " + str(original_price) + " to " + str(int(new_price)) + " at a discount of " + str(int(discount_percent))

print (sentence)
print ("baby, baby cant you see this world's for you and me it's  alright")
