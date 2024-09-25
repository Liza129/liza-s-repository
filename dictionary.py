sentence = input("Enter a sentence: ")
answer = int(input("if you want to calculate frequency of the words enter 1, if characters in a sentence enter 2: "))
while answer != 1 and answer != 2:
    answer = int(input("incorrect answer!\nif you want to calculate frequency of the words enter 1, if characters in a sentence enter 2: "))
if answer == 1:
    sentence = sentence.lower()
    sentence = sentence.split()
    l = []
    dic = {}
    for i in sentence:
        c = sentence.count(i)
        l.append(c)
    c = 0
    for i in sentence:
        if sentence[c] not in dic:
            dic[sentence[c]] = l[c]
        c += 1
    print("Word     Count")
    for key,value in dic.items():
        print(f'{key} --- {value}')
elif answer == 2:
    sentence = sentence.lower()
    l = []
    dic = {}
    for i in sentence:
        c = sentence.count(i)
        l.append(c)
    c = 0
    for i in sentence:
        if sentence[c] not in dic and sentence[c] != " ":
            dic[sentence[c]] = l[c]
        c += 1
    print("Word     Count")
    for key,value in dic.items():
        print(f'{key} --- {value}')

    
