num = int(input("Enter a number: "))
c = 0
for i in range(num):
    if i % 2 != 0:
        c += i
print(c)
s = 0
for i in range(10):
    s = s + 1/(i+1)
print(s)