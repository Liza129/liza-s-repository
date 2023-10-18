#052
import random
m = random.randint(1,100)
print(m)

#053
import random
q = ["apple", "orange", "banana", "pineapple", "mango"]
w = random.choice(q)
print(w)

#054
import random
e = ["h", "t"]
r =  random.choice(e)
choice_u = input("Enter h or t: ")
if choice_u == r:
    print("You win")
else:
    print("Bad luck")
    
print("Computer selected ", r)

#055
import random
t = random.randint(1,5)
y = input("Enter a number: ")
y = int(y)
if y == t:
    print("Well done")
else:
    if y > t:
        print("Too high")
    elif y < t:
        print("Too low")
    u = input("Enter a second number: ")
    u = int(u)
    if u == t:
        print("Correct")
    else:
        print("You lose")

#056
import random
i = random.randint(1,10)
print(i)
o = input("Enter a number: ")
o = int(o)
while o != i:
    print("Bad luck")
    o = input("Enter a number: ")
    o = int(o)
    
print("Correct")

# 057
import random
i = random.randint(1,10)
print(i)
o = input("Enter a number: ")
o = int(o)
while o != i:
    print("Bad luck")
    if o > i:
        print("Too high")
    elif o < i:
        print("Too low") 
    o = input("Enter a number: ")
    o = int(o)
    
print("Correct")


#058
import random
points = 0
for i in range(5):
    p = random.randint(1,100)
    p = str(p)
    d = int(p)
    a = random.randint(1,100)
    a = str(a)
    f = int(p)
    sum_n = d + f
    sum_n = int(sum_n)
    s = input("Enter the answer, "+ a+ "+"+p+ "= ")
    s = int(s)
    if s == sum_n:
        points += 1
print("You got ", points, "out of five")

#059
import random
g = ["blue", "green", "orange", "yellow", "white"]
print(g)
h = random.choice(g)
j = input("Enter a colour: ")
while j != h:
    if h == "blue":
        print("You are probably feeling blue right now")
    elif h == "green":
        print("l bet you are green with envy")
    elif h == "orange":
        print("Your face is orange")
    elif h == "yellow":
        print("You look like Sun")
    elif h == "white":
        print("The office paper is very white")
    j = input("Enter a colour: ")
if j == h:
    print("Well done")
