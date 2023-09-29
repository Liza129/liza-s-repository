#012

num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
if num_1 > num_2:
    print(num_2)
    print(num_1)
else:
    print(num_1)
    print(num_2)



#013
usernum = input("Enter the number that is under 20: ")
usernum = int(usernum)
if usernum >= 20:
    print("Too high")
else:
    print("Thank you")


#014


user_num = input("Enter a number between 10 and 20 (inclusive): ")
user_num = int(user_num)
if user_num >=10 and user_num <=20:
    print("Thank you")
else:
    print("Incorrect answer")


#015

colour = input("Enter your favourite colour: ")
if colour == "red" or colour == "RED" or colour == "Red":
    print("l like red too")
else:
    print("l don't like ", colour + ", l prefer red")




#016

rain = input("Is it raining?")
rain = rain.lower()
if rain == "yes":
    windy = input("Is it windy?")
    windy = windy.lower()
    if windy == "yes":
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy your day")







#017

userage = input("How old are you? ")
userage = int(userage)
if userage >= 18:
    print("You can vote")
elif userage == 17:
    print("You can learn to drive")
elif userage == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick-or-Treating")







# 018


usrn = input("Enter a number:")
usrn = int(usrn)
if usrn < 10:
    print("Too low")
elif usrn >= 10 and usrn <= 20:
    print("Correct")
else:
    print("Too high")





#019

inpt = input("Enter 1, 2 or 3: ")
inpt = int(inpt)
if inpt == 1:
    print("Thank you")
elif inpt == 2:
    print("Well done")
elif inpt == 3:
    print("Correct")
else:
    print("Error massage")











