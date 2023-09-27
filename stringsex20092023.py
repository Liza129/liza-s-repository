#020
name = input("Enter your name: ")
name = len(name)
print("The length of your name is",name)




#021
fn = input("Enter your First name: ")
sc = input("Enter your Second name: ")
fulln = fn+" "+sc
fullnint = len(fulln)
fullnint-=1
print("Your full name is", fulln, "and it's length is", fullnint)




#022
fn1 = input("Enter your First name in lower case: ")
sc1 = input("Enter your Second name in lower case: ")
fn1 = fn1.upper()
sc1 = sc1.upper()
tcn = fn1 + " " + sc1
print("Your full name in title case is", tcn)


#023
nrhyme = input("Enter the first line of the nursery rhyme: ")
nrhymeint = len(nrhyme)

print("The length of your nursery rhyme is ", nrhymeint)

startn = input("Enter the starting number: ")
endn = input("Enter the ending number: ")

startn = int(startn)
endn = int(endn)
startn-=1


user_selection = nrhyme[startn:endn]
print(user_selection)









#024
user_w = input("Enter any word: ")
user_w = user_w.upper()
print(user_w)






#025
user_fn = input("Enter your First name: ")
user_fn_int = len(user_fn)
if user_fn_int < 5:
    user_sn = input("Enter your Surname: ")
    user_fullname = user_fn + user_sn
    user_fullname =  user_fullname.upper()
    print(user_fullname)
else:
    user_fn = user_fn.lower()
    print(user_fn)





#026
user_word = input("Enter a word and l will translate it into Pig Latin: ")
user_word_int = len (user_word)
firstl = user_word [0]
vowel = "a e i o u y"
if firstl in vowel:
    new_word_v = user_word + "way"
    new_word_v = new_word_v.lower()
    print(new_word_v)
else:
    new_word_c = user_word[1:] + firstl + "ay"
    new_word_c = new_word_c.lower()
    print(new_word_c)


