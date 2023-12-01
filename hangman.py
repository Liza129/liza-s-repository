import random
#name = input("Enter your name: ")
l_e = ["fork"]
l_h = ["computer"]
score = 0
chances = 10
Guesses = []
chosen_w = ""
list_ch = input("Do you want to guess a hard word or easy. Enter h or e: ")
def list_ch_F(d,e,g,i):
    if d == "h":
        e = random.choice(g)
    elif d == "e":
        e = rendom.choice(i)
    response = e
    return response
chosen_w = list_ch_F(list_ch,chosen_w,l_h,
         

def scoresF(a):
    if letter = "Correct":
        a += 1
        response = a
    return response
score = scoresF(score)

 
def chancesF(b):
    if letter = "Incorrect":
        b -= 1
        response = b
    return response
chance = chancesF(chances)

def guessesF(c):
    if letter = "Incorrect":
        c.append(letter)
    response = c
    return response
guess = guessesF(Guesses)


    
    