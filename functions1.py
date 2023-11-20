import random

def triple(x,y,z): #()parameters
    print("hello")
    return x+y+z
    
result = triple(2,3,4)  # ()Arguments
print(result)

#118

def someNum():
    x = input("Enter a number: ")
    x = int(x)
    return x
num = someNum()

def countNum(value):
    for i in range(1,value+1):
        print (i)
countNum(num)

#119

def randNum():
    l = input("Enter a low number: ")
    l = int(l)
    h = input("Enter a high number: ")
    h = int(h)
    comp_num = random.randint(l,h)
    return comp_num
comp_num = randNum()
def guessNum():
    print("l am thinking of a number...")
    ug = input("Enter a number I'm thinking of: ")
    ug = int(ug)
    return ug
ug = guessNum()
def checkProgramme(a,b):
    while b != a:
        b = input("Enter a number I'm thinking of: ")
        b = int(b)
checkProgramme(comp_num, ug)         
print("Correct you win")

#120
print("1) Addition \n2) Subtraction")
ua = input("Enter 1 or 2: ")
ua = int(ua)

num1 = ""
num2 = ""
sumnum = ""
num3 = ""
num4 = ""
minnum = ""

num1 = random.randint(5,20)
num2 = random.randint(5,20)

def ifEnterA1(a,b):
    c = a + b
    return c
sumnum = ifEnterA1(num1, num2)
sumnum = str(sumnum)

num3 = random.randint(25,50)
num4 = random.randint(1,25)

def ifEnterA2(a,b):
    c = a - b
    return c
minnum = ifEnterA2(num3, num4)
minnum = str(minnum)

if ua == 1:
    usAns = input("Add this two numbers:" + str(num1) + " and " + str(num2))
    print("Your answer is " + str(usAns) + ", and the correct answer is " + str(sumnum))###
elif ua == 2:
    usAns2 = input("Subtract this two numbers:" + str(num3) + "and "+ str(num4))
    print("Your answer is " + str(usAns2) + ", and the correct answer is " + str(minnum))###
else:
    print("Error")
    
def checkProgramme():
    if ua == 1:
        if usAns == sumnum:
            response = "Correct"
        elif usAns != sumnum:
            response = "Incorrect, the answer is " + str(sumnum)
        else:
            response = "Error"
    elif ua == 2:
        if usAns2 == minnum:
            response = "Correct"
        elif usAns2 != minnum:
            response = "Incorrect, the answer is " + str(minnum)
        else:
            response = "Error"
    else:
        response = "You didn't select a relevant option"
    return response
print(checkProgramme())

#121
l = []
def listProgramme(l):
    userAns = input("If you want to add a name to a list (enter 'a'), change a name (enter 'c'), delete a name (enter 'd'), view all names in a list (enter 'v'), or end the programme (enter 'e'): ")
    if userAns == 'a':
        add = input("Enter a name you would like to add: ")
        l.append(add)
    elif userAns == 'c':
        print(l)
        elem = input("Enter an element you would like to change: ")
        e_index = l.index(elem)
        change_on = input("Enter a name you want to write insted: ")
        l[e_index] = change_on
    elif userAns == 'd':
        print(l)
        pop = input("Enter the position of an item you want to delete: ")
        pop = int(pop)
        pop -= 1
        l.pop(pop)
        print(l)
    elif userAns == 'v':
        print(l)
    return userAns
userAns = listProgramme(l)

while userAns != 'e':
    userAns = listProgramme(l)
    
    

        
        
        
    