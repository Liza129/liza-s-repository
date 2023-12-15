
#1
for i in range(1,11):
    print(i)

#2
for i in range(20,0,-1):
    print(i)

#3
for i in range(1,11):
    if i % 2 == 0:
        print(i)

#4
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)

#5
n = int(input("Enter a number: "))
for i in range(1,n+1):
    if i % 2 != 0:
        print(i)

#6
for i in range(5):
    print("Happy birthday")

#7
n = int(input("Enter a number: "))
for i in range(n+1):
    if i > 0:
        print(i**2)
        
      
#8
n = int(input("Enter a number: "))
a = 1
for i in range(n):
    s = a*n
    print(a, "mulpiply by ", n, "= ",s )
    a += 1

#9
a = 3
b = 4
for i in range(8):
    print(a)
    a += b

#10
a = 2
b = 3
for i in range(6):
    print(a)
    a = a * b

#11
n = int(input("Enter a positive number: "))
a = 0
for i in range(1,n+1):
    a += i
print(a)

#12
n = int(input("Enter a number: "))
a = 0 
for i in range(1,n+1):
    i = i**(-1)
    a += i
a = round(a,2)
print(a)

#13
a = 0
for i in range(5):
    i = int(input("Enter a number: "))
    a += i
print(a)
   
#14
n = int(input("Enter a number: "))
if n > 0:
    for i in range(1,n):
        n = n*i
    print(n)
elif n < 0:
    print("There is no factorial to a negative number")
else:
    print("factorial of 0 is 1")
    
#15
b = int(input("Enter a base number: "))
e = int(input("Enter an exponent number: "))
a = 1
for i in range(e):
    a = a * b
print(a)
 
#16
n = int(input("How many numbers would you like to enter: "))
a = 0
for i in range(1,n+1):
    i = int(input("Enter a number: "))
    while i < 0:
        print("This is an invalid value. All numbers must be positive.")
        i = int(input("Enter a number: "))    
    a += i
        
b = a/n
print("The sum of the ", n, "numbers entered is ", a, "\nThe average of the ", n," numbers entered is ", b)
    
    
