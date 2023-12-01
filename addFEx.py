#1
l = [8,2,3,0,7]
def sumValues():
    total = 0
    for i in l:
        total += i
    response = total
    return response
response = sumValues()
print(response)
#2
l = [8,2,3,-1,7]
def multiply():
    total = 1
    for i in l:
        total = i*total
    response = total
    return response
response = multiply()
print(response)

#3
string = "1234abcd"
def reverse(x):
    response = x [::-1]
    return response
response = reverse(string)
print(response)

#4
n = 4
def factorial(n):
    response = 1
    if n > 0:
        for i in range(1,n + 1):
            response = response*i
    else:
        response = "There is no factorial for a negative number or 0"
    return response
response = factorial(n)
print(response)

#5
z = 8
c = 1
v = 4
def checkRange():
    response = "False"
    if c <= v <= z:
        response = "True"
    return response
response = checkRange()
if response == "True":
    ans = "number falls within a given range"
elif response == "False":
    ans = "number does not fall within a given range"

print(ans)
#6
a = "The quick Brow Fox"
lower = 0
upper = 0
def lowerUpper(a,lower,upper):
    for i in a:
        if i.islower():
            lower += 1
        elif i.isupper():
            upper +=1
    return [lower, upper]
response = lowerUpper(a,lower,upper)
print("number of lower case characters: ", response [0], ". number of upper case characters: ", response [-1])
    
#7
l = [1,2,3,3,3,4,5]
x = []
def distinctList(l,x):
    for i in l:
        if i not in x:
            x.append(i)
    return x
unique_l = distinctList(l,x)
print(unique_l)
    
#8

def primeNumbers(c):
    c = int(c)
    response = ""
    if c >= 1:
        for i in range(2,int(c - 1)):
            if c % i == 0:
                response = "not prime"
            else: response = "prime"
    else: response = "not prime"
    return response
response = primeNumbers(7)
print(response)
#9
l = [1,2,3,4,5,6,7,8,9]
b = []
def evenNum(l,b):
    for i in l:
        if i % 2 == 0:
            b.append(i)
    return b
b = evenNum(l,b)
print(b)