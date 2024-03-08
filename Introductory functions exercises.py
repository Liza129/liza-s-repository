
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
def addingTwonumbers(a,b):
    total = a+b
    return total
total = addingTwonumbers(a,b)
print("The total of adding two numbers will be: ", total)

c = input("Enter a string: ")
def Un(c):
    c = "un" + c
    return c
unword = Un(c)
print(unword)

d = input("Enter a srting: ")
e = d[::-1]
def palindrom(d,e):
    if e == d:
        response = "it is a palindrom"
    else:
        response = "it is not a palindrom"
    return response
ans = palindrom(d,e)
print(ans)

f = input("Enter a list of numbers: ")
def oddEven(f):
    even = 0
    odd = 0
    total_odd_even = 0
    l_odd = []
    l_even = []
    total_odd = 0
    total_even = 0
    for i in f:
        i = int(i)
        if i % 2 == 0:
            even += 1
            l_even.append(i)
        else:
            odd += 1
            l_odd.append(i)
    total_odd_even = even + odd
    for i in l_odd:
        total_odd += int(i)
    everage_odd = total_odd / odd
    for i in l_even:
        total_even += int(i)
    everage_even = total_even / even
    return even,odd,total_odd,total_even,everage_odd,everage_even
even,odd,total_odd,total_even,everage_odd,everage_even = oddEven(f)
print(even,odd,total_odd,total_even,everage_odd,everage_even)