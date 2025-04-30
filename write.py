d = {}
d["name"] = []
d["age"] = []
d["city"] = []

for i in range(2):
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    city = input("Enter the name of the city you live in: ")
    d["name"].append(name)
    d["age"].append(age)
    d["city"].append(city)
    
print(d)

f = open("compscicsv.csv","w")
for i in d: 
    f.write(str("\n")+i + str(": "))
    for x in d[i]:
        f.write(str(x)+ str(" "))
f.close()

f = open("compscicsv.csv","r", encoding='utf-8')
print(f.read())