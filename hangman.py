import random
#name = input("Enter your name: ")
l_e = ["fork"]
l_h = ["computer"]
score = 0
chance = 8
Guesses = []
chosen_w = ""
Cor_orInCor = ""

hg = [" -------------", "\n       O      |", "\n              |", "\n     / | \\   |", "\n       |      |", "\n              |", "\n    /    \\   |", "\n           -------"]


list_ch = input("Do you want to guess a hard word or easy. Enter h or e: ")
def list_ch_F(d,e,g,i):
    if d == "h":
        e = random.choice(g)
    elif d == "e":
        e = random.choice(i)
    response = e
    return response
chosen_w = list_ch_F(list_ch,chosen_w,l_h,l_e)
        

hidden_w = [chosen_w]

num_letters = len(chosen_w)

def hid_wF(k):
    k.clear()
    for i in range(num_letters):
        k.append("_")
    response = k
    return response
hidden_w = hid_wF(hidden_w)

print("You need to guess this word ", hidden_w)
letter = input("Enter a letter you think is in this word: ")

def incerting_letter_F(h,a1,a2):
    count = 0
    for i in a1:
        if h == i:
            a2[count] = h
        count += 1
    response = a2
    return response
hidden_w = incerting_letter_F(letter,chosen_w,hidden_w)

     


def C_InC_letter_F(m):
    if letter in m:
        Cor_orInCor = "Correct"
    elif letter not in m:
        Cor_orInCor = "Incorrect"
    response = Cor_orInCor
    return response


def hangmanF(hg,letter,k,l):
    m = ""
    if k == "Incorrect":
        for i in range(8-l):
            m = m+hg[i]
    response = m
    return response



def scoresF(a,v):
    if v == "Correct":
        a += 1
    response = a
    return response


 
def chancesF(b,x):
    if x == "Incorrect":
        b -= 1
    response = b
    return response


def guessesF(c,z):
    if z == "Incorrect":
        if letter not in c:
            c.append(letter)
    response = c
    return response
Cor_orInCor = C_InC_letter_F(chosen_w)
chance = chancesF(chance, Cor_orInCor)
p_hg = hangmanF(hg,letter,Cor_orInCor,chance)
score = scoresF(score, Cor_orInCor)

guess = guessesF(Guesses, Cor_orInCor)


if Cor_orInCor == "Correct":
    print("Yes, this letter is in the word")
    print(hidden_w)
elif Cor_orInCor == "Incorrect":
    print("No, this letter isn't in the word")
    print(p_hg)
    print("List of incorrect words: ", guess)
print("Your score is: ", score)
print("You have ", chance, "chances left")
    

while chance > 0:
    print("You need to guess this word ", hidden_w)
    letter = input("Enter a letter you think is in this word: ")
    Cor_orInCor = C_InC_letter_F(chosen_w)
    chance = chancesF(chance, Cor_orInCor)
    p_hg = hangmanF(hg,letter,Cor_orInCor,chance)
    score = scoresF(score, Cor_orInCor)

    guess = guessesF(Guesses, Cor_orInCor)

    if Cor_orInCor == "Correct":
        print("Yes, this letter is in the word")
        print(hidden_w)
    elif Cor_orInCor == "Incorrect":
        print("No, this letter isn't in the word")
        print(p_hg)
        print("List of incorrect words: ", guess)
    print("Your score is: ", score)
    print("You have ", chance, "chances left")
    

if chance == 0:
    print("You have no chances left \nThe word you were guessing was: ", chosen_w)


    
    
    
    
     

    
    