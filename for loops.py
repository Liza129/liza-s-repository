#035


name = input("Enter your name: ")
for i in range(3):
    print(name)





#036

uname = input("Enter your name: ")
number = input("Enter a number: ")
number = int(number)
for i in range(number):
    print(uname)




#037

us_name = input("Enter your name: ")
for i in us_name:
    print(i)





#038

usr_name = input("Enter your name: ")
usr_num = input("Enter a number: ")
usr_num = int(usr_num)
for i in usr_name:
    print(i * usr_num)







# 039

num_user = input("Enter a number between 1 and 12: ")
num_user = int(num_user)
for i in range(num_user):
    print(i)




# 040
numbl50 = input("Enter a number below 50: ")
numbl50 = int(numbl50)
for i in range(50, numbl50, -1):
    print(i)

    
#041

nameuser = input("Enter your name: ")
numberuser = input("Enter your number: ")
numberuser = int(numberuser)
if numberuser < 10:
    for i in range(numberuser):
        print(nameuser)
else:
    for i in range(3):
        print("Too high")







#042

total_to_0 = 0
for i in range(5):
    f_n = input("Enter the number: ")
    f_n = int(f_n)
    f_b = input("Do you want to add this number to a total? ")
    f_b = f_b.lower()
    if f_b == "yes":
        total_to_0 += f_n
print(total_to_0)







#043


direction = input("Enter the direction that you want to count (up or down)")
direction = direction.lower()
if direction == "up":
    topnum = input("Enter the top number: ")
    topnum = int(topnum)
    for i in range(1, topnum):
        print(i)
elif direction == "down":
    numbelow20 = input("Enter a number below 20: ")
    numbelow20 = int(numbelow20)
    for i in range(20, numbelow20, -1):
        print(i)
else:
    print("I don't understand")



#044
invited_people = input("Enter the number of pople you want to invite to a party: ")
invited_people = int(invited_people)
if invited_people < 10:
    for i in range(invited_people):
        person = input("Enter the name: ")
        print(person, "has been invited")
elif invited_people >= 10:
    print("Too many people")