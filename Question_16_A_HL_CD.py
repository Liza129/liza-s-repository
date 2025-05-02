#Question_16_A_HL
#Enter your name here:

s = 0

sentence = input("Please enter a sentence: ")

for i in sentence.lower():
    if i == "s":
        s += 1
print("The number of s's was: ", s, "\n")

print("Your sentence was:", sentence)
print("Your lowercase sentence is:", sentence.lower())

v = "euioa"
counter_v = 0 
for i in sentence.lower():
    for x in v: 
        if i == x:
            counter_v += 1
print("The number of vowels was:", counter_v, "\n")

l = 0
d = 0

for i in sentence:
    if i.isalpha():
        l += 1
    elif i.isdigit():
        d += 1
print("The number of letters was:", l)
print("The number of digits was:",d, "\n")

s = sentence.split()
print("The number of words was:", len(s))