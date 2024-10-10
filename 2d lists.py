
l = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
#097
row = int(input("Enter a row: "))
column = int(input("Enter a column: "))
print(l[row-1][column-1])
#098
row = int(input("Enter a row: "))
print(l[row-1])
v = int(input("Enter a new value: "))
l[row-1].append(v)
print(l[row-1])
#100

d = {"John":{"N":3056,"S":8463,"E":8441,"W":2694},"Tom":{"N":4832,"S":6786,"E":4737,"W":3612},"Anne":{"N":5239,"S":4802,"E":5820,"W":1859},"Fiona":{"N":3904,"S":3645,"E":8821,"W":2451}}
#101
n = input("Enter a name: ")
r = input("ENter a region: ")
print(d[n][r])
n = input("Enter a name: ")
r = input("ENter a region: ")
s = int(input("Enter new sales: "))
d[n][r] = s
print(d)
#102

d = {"Name":[],"Age":[],"Shoe size":[]}
for i in range(4):
    s = input("Enter name,age and shoe size: ")
    s = s.split()
    print(s)
    d["Name"].append(s[0])
    d["Age"].append(s[1])
    d["Shoe size"].append(s[2])

print(d["Name"],d["Age"])
p = input("Enter a person you want to delete: ")
i = d["Name"].index(p)
d["Name"].pop(i)
d["Age"].pop(i)
d["Shoe size"].pop(i)
print(d)