import random
guesses = 1
all_colours = ["yellow","green","blue","orange","black","purple"]
compl = []
info = ""
correct_correct= 0
correct_wrong = 0
count = 0
list_for_user = []
for i in range(4):
    compl.append(random.choice(all_colours))
print(compl)
userl = input("Enter list of colours: ")
userl = userl.split()
#print(userl)
def correct_colour(count,compl,info,correct_wrong,correct_correct,list_for_user,userl):
    for i in userl:
        if i in compl:
            if compl[count] == i:
                correct_correct += 1
                info = "colour", count+1, "is on the correct position"
                list_for_user.append(info)
            else:
                correct_wrong += 1
                info = "colour", count+1, "is on the wrong position"
                list_for_user.append(info)
        else:
            info = "colour", count+1, "is incorrect"
            list_for_user.append(info)
        count += 1
    return list_for_user, correct_wrong, correct_correct
list_for_user, correct_wrong, correct_correct = correct_colour(count,compl,info,correct_wrong,correct_correct,list_for_user,userl)
#print(list_for_user, correct_wrong, correct_correct)
print("Correct colours in the correct place:", correct_correct,"\nCorrect colours but incorrect place:", correct_wrong,"\n", list_for_user)
while correct_correct != 4:
    userl = ",".join(str(i) for i in userl)
    userl = input("Enter list of colours: ")
    userl = userl.split()
    list_for_user.clear()
    correct_correct= 0
    correct_wrong = 0
    list_for_user, correct_wrong, correct_correct = correct_colour(count,compl,info,correct_wrong,correct_correct,list_for_user,userl)
    guesses += 1
    print("Correct colours in the correct place:", correct_correct,"\nCorrect colours but incorrect place:", correct_wrong,"\n", list_for_user)
print("You guessed all colours.\nIt took you", guesses, "guesses.")

    
    
                
            
            