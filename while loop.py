#045

total = 0
while total <= 50:
    number = input("Enter the number")
    number = int(number)
    total = total + number
    print("The total is ", total)



# 046

n = input("Enter a number ")
n = int(n)
while n < 5:
    n = input("Enter a number ")
    n = int(n)
print("The last number you entered was ", n)


#047

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
num_sum = num1 + num2
t = num_sum
print("The sum of your two numbers is ", num_sum, "do you want to add another number?")
ans = input("Enter 'y' if you would like to add another number and 'n' if you don't: ")
ans = ans.lower()
while ans == "y":
    num3 = int(input("Enter another number: "))
    t += num3
    print("do you want to add another number?")
    ans = input("Enter 'y' if you would like to add another number and 'n' if you don't")
    
print("The total number is ", t)
 



#048
count = 0
name1 = input("Enter the name of somebody you want to invite to a party: ")
print(name1, "has been invited")
count += 1
answ = input(" Do you want to invite anybody else? Enter 'y' if you want to and 'n' if you do't ")
answ = answ.lower()
while answ == "y":
    name2 = input("Enter the name of a person: ")
    print(name2, "has been invited")
    count += 1
    answ = input(" Do you want to invite anybody else? Enter 'y' if you want to and 'n' if you do't ")
    answ = answ.lower()
print("You invited ", count, "people")



#049

compnum = 50
count1 = 0
number1 = int(input("Enter a number: "))
while not number1 == compnum:
    count1 += 1
    if compnum > 50:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    number1 = int(input("Enter another number: "))

print("Well done, you took", count1, "attempts")




#050

nb = input("Enter a number between 10 and 20: ")
nb = int(nb)
while  nb < 10 or nb > 20:
    if nb < 10:
        print("Too low")
    elif nb > 20:
        print("Too high")
    else:
        break
    print("Try again")
    nb = input("Enter a number between 10 and 20: ")
    nb  = int(nb)
print("Thank you")



#051

b = 10
b_1 = 9
print("There are", b, "green bottles hanging on the wall, ", b, "green bottles hanging on the wall, and if 1 green bottle should exidentally fall")
answer = input("How many bottles will be hanging on the wall: ")
answer = int(answer)
while b > 1:
    if answer == b_1:
        print("There will be", b_1, "green bottles hanging on the wall")
        b -= 1
        b_1 -= 1
    else:
        print("No try again")
    
    print("There are", b, "green bottles hanging on the wall, ", b, "green bottles hanging on the wall, and if 1 green bottle should exidentally fall")
    answer = input("How many bottles will be hanging on the wall: ")
    answer = int(answer)
    
print("There are no more bottles hanging on the wall")
