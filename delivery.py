takeaway_menu = ["1. Pad Thai","2. Chicken Tikka Masala","3. Pepperoni Pizza","4. Veggie Burger with Fries","5. Burrito Bowl"]
takeaway_prices = [12.99, 14.50,  9.99,  15.99,  11.50]
delivery_fee = 5.00
free_delivery_price = 30.00
total_price = 0

print("Welcome to the takeaway delivery service.")
print("Here's our menu.")
for item in takeaway_menu:
    print(item)

quantity = int(input("How many items would you like to purchase?"))
order = []
for i in range(quantity):
    choice = int(input("Enter the menu number of the item you wish to add to your order: "))
    order.append(choice)
name = input("Please enter your name: ")
print("Thank you,",name," order is as follows")

for item in order:
    print(takeaway_menu[item-1])
"""  
for i in order:
    total_price += takeaway_prices[i-1]
print("The total price of an order will be: ", total_price)
if total_price < free_delivery_price:
    total_price += delivery fee
    print("Your order is less than 30 euro, so we added a delivery fee of 5 euro and now the total price of an order will be: ", total_price)
else:
    print("The delivery is free")
"""
def get_bill_total(total_price):
    for i in order:
        total_price += takeaway_prices[i-1]
    total_price_U = total_price
    if total_price < free_delivery_price:
        total_price += delivery_fee
        response = "Your order is less than 30 euro, so we added a delivery fee of 5 euro and now the total price of an order will be: " + str(total_price)
    else:
        response = "The delivery is free"
    return total_price_U, response, total_price
total_price_U, response, total_price = get_bill_total(total_price)
total_price = str(round(total_price,2))
total_price_U = str(round(total_price_U,2))
print("The total price of an order will be: ", total_price_U)
print(response)
        