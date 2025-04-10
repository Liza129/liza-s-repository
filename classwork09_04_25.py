#fibonacci

num1_2 = 1
inp = int(input("Enter a number: "))
l = [num1_2,num1_2]
if inp == 1 or inp == 2:
    print("The number is ",num1_2)
else:
    c = 0
    for i in range(inp-2):
        number = l[c]+l[c+1]
        l.append(number)
        c += 1
    print(l)
    print("The number is ", l[-1])

#file
f = open("book.txt","r")
dic = {}
for i in f:
    i = i.strip().split()
    for x in i:
        if x in dic:
            dic[x]+=1
        else:
            dic[x]= 1
dic = dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
c = 0
for i in dic:
    if c < 10:
        print(f'{i}    {dic[i]}')
    else:
        break
    c += 1