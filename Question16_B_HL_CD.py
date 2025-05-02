#Question_16_B_HL
#Enter your name here:

import random
print("Welcome to my shop")
total = 0
item_list = []
item_prices = []

l = l = input("Please enter the item or enter 'stop':")

while l.lower() != "stop":
    p = float(input("Please enter the price of the item:"))
    item_list.append(l)
    item_prices.append(p)
    print("The current total is €",sum(item_prices))
    l = input("Please enter the item or enter 'stop':")
print("Your items are:",item_list )
print("The prices are:",item_prices )
print("Grand total €", sum(item_prices) )


rand = random.choice(item_list)
print("Your random item to be checked is:",rand, "\n")

index_min = item_prices.index(min(item_prices))
index_max = item_prices.index(max(item_prices))

print("The most expensive item is:", item_list[index_max])
print("The cheapest item is:",item_list[index_min])