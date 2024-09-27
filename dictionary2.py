
#105
new = open("numbers.txt", "w")
new.write("1,1,1,1,1")
new.close()
#106

f = open("names.txt", "w")
f.write("Liza\nAnna\nAlice\nAlex\nCamila")
f.close()
#107

n = open("C:\\Users\\21YBratushkin.ACC\\Documents\\names.txt","r")
for i in n:
    print(i)
n.close()
#108

d = open("C:\\Users\\21YBratushkin.ACC\\Documents\\names.txt","a")
user = input("Enter a new name: ")
d.write(user)
d.close()
#109
option = int(input("1) Create a new file\n2)Display the file\n3)Add a new item to the file\nMake a selection 1,2, or 3: "))
while option != 1 and option != 2 and option != 3:
    print("erroooorrrrrrrrr!!!!!!!!!!")
    option = int(input("1) Create a new file\n2)Display the file\n3)Add a new item to the file\nMake a selection 1,2, or 3: "))
while option == 1 or option == 2 or option == 3:
    if option == 1:
        sub = input("Enter a school subject:")
        nf = open("subject.txt", "w")
        nf.write("\n"+sub)
        #nf.close()
    elif option == 2:
        nf = open("C:\\Users\\21YBratushkin.ACC\\Documents\\subject.txt","r")
        for i in nf:
            print(i)
        #nf.close()
    elif option == 3:
        sub = input("Enter a school subject:")
        nf = open("C:\\Users\\21YBratushkin.ACC\\Documents\\subject.txt", "a")
        nf.write("\n"+sub)
        nf.close()
        nf = open("C:\\Users\\21YBratushkin.ACC\\Documents\\subject.txt","r")
        for i in nf:
            print(i)
    option = int(input("1) Create a new file\n2)Display the file\n3)Add a new item to the file\nMake a selection 1,2, or 3: "))
#110

n = open("C:\\Users\\21YBratushkin.ACC\\Documents\\names.txt","r")
for i in n:
    print(i)
user = input("Enter one of the names: ")
f = open("names2.txt", "w")
f.write(user)
f.close()
n.close()


