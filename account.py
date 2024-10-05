dic = {"ID":[],"Password":[]}
def pas_check(pas):
        l = [0,0,0,0,0]
        d = ["!","£","$","%","&","*","#"]
        if len(pas) >= 8:
            l[0] += 1
        for i in pas:
            if i.islower():
                l[1] += 1
            elif i.isupper():
                l[2] += 1
            elif i.isdigit():
                l[3] += 1
            elif i in d:
                l[4] += 1
        if 0 in l:
            return False
        else:
            return True
def file(dic):
    f = open("Passwords.csv","w")
    f.write("ID,Password\n")
    for i in range(len(dic["ID"])):
        f.write(f"{dic['ID'][i]},{dic['Password'][i]}")
    f.close()
choice = input("Choose an option and enter a number\n1)Create a new User ID\n2)Change a password\n3)Display all users IDs\n4)Quit\n")
choice = choice.strip()

while choice != "4":
    
    if choice == "1":
        idu = input("ENter your ID: ")
        for i in dic["ID"]:
            if i == idu:
                idu = input("This ID already exists, enter a different one: ")
        pas = input("Enter a password: ")
        while pas_check(pas) == False:
            print("Password must include 8 characters, upper case, lower case, number and a special character")
            pas = input("Enter a password: ")
        dic["ID"].append(idu)
        dic["Password"].append(pas)
        file(dic)
        print("\nA new user ID has been created!!")
    elif choice == "2":
        idu = input("ENter your ID: ")
        k = True
        while k == True:
            if idu in dic["ID"]:
                k = False
                pas = input("Enter a new password: ")
                while pas_check(pas) == False:
                    print("Password must include 8 characters, upper case, lower case, number and a special character")
                    pas = input("Enter a password: ")
            else:
                idu = input("This ID does not exist, enter a different one: ")
        index = dic["ID"].index(idu)
        dic["Password"][index] = pas
        file(dic)
        print("\nPassword is updated")
    elif choice == "3":
        f = open("Passwords.csv","r")
        for i in f:
            print(i)
        f.close()
    else:
        print("Errorrrrrrrrrr!!!!")
    choice = input("Choose an option and enter a number\n1)Create a new User ID\n2)Change a password\n3)Display all users IDs\n4)Quit\n")
    choice = choice.strip()
print("byeeeeee")