
#1
n = input("Enter your name: ")
print("Hello ", n)
#2

int1 = int(input("Enter an integer: "))
int2 = int(input("Enter an integer: "))
s = int1 + int2
print("The sum of this two integers is: ", s)

#3

t1 = int(input("Enter a Celsius temperature: "))
f = 9/5*t1+32
print("The temperature in Fahrenheit is", f)

#4
p = int(input("Enter a principle: "))
r = int(input("Enter a rate: "))
t = int(input("Enter time: "))
def simple_interestF(p,r,t):
    si = p*r*t/100
    response = si
    return response
si = simple_interestF(p,r,t)
print("Simplest interest is ", si)


#5
s = int(input("Enter the amount of seconds: "))
h = s//60//60
m = s//60
print("seconds: ", s, "\nminutes: ", m, "\nhours: ", h)

#6,7
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num1,num2 = num2,num1
print(num1, num2)


#8
rad = int(input("Enter a radius: "))
p = 3.14
a = p*rad**2
c = 2*p*rad
print("area is: ", a, "\ncircumference: ", c)

#9
l = int(input("Enter the length: "))
w = int(input("Enter the width: "))
a = l*w
p = 2*(l+w)
print("area: ", a, "\nperimeter: ", p )


#10
a = 3
b = 4
c = 5
s = (a+b+c)/2
a = s*(s-a)*(s-b)*(s-c)
a = a**0.5
print("area is : ", a)

#11
p = 45
r = 50
t = 5
c = p*(1+r/100)**t-p
print("compound interest is : ", c)

