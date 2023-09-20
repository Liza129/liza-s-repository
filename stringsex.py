#task2
pangram = "The quick brown fox jumps over the  lazy dog!"
print(pangram[1:5]) #he q
print(pangram[17:19]) #ox
print(pangram[:19])#The quick brown fox
print(pangram[20:26])#jumps
print(pangram[26:])#over the lazy dog!
#print(pangram[:]) will display everything









#task3
"""
name = "Mary"
print(name[0:4])
"""







name = "Mary"
k = "k"
name = name.replace("y",k)
print(name)







#task4
"""
P1)LeavingCertificateComputerScience
P2) The fox jumps over the  lazy dog!
P3)The plural ofappleisapples (if you entered apple)
"""





word1 = "Leaving "
word2 = "Certificate "
word3 = "Computer "
word4 = "Science"
subjectName = word1 + word2 + word3 + word4
print(subjectName)



pangram = "The quick brown fox jumps over the  lazy dog!"
print(pangram[:4] + pangram [16:])


noun = input("Enter a singular noun:")
plural = "s"
print("The plural of",noun,"is", noun+plural)










#Task5

"""
[3] - d
[52:62] - 0123456789
[51:62] - Z0123456789
[26:53] - the first one
0:25 - second last
1-b
5-f
26:52 - 3rd
26 - A
"""








#Task6
#2+2=4










#task7
print("%d" %3)
print("%.2f" %3.14)
print("%s"%"Hi!")









#Task8
#Hi Hal. How are you?

msg = "Hi %s. How are you?"
name = "Hal"
print(msg%name)



import math
r = 5
sradius = pow(r,2)
print("Radius: %d, Area:%.2f" %(r, math.pi*sradius))










#Task9

nameSH = input("Enter the name:")
nameSH_int = len(nameSH)
index = nameSH_int//2 
nameSH = nameSH[0]+nameSH[index]+nameSH[-1]
print(nameSH)









m3ch1 = input("Enter the first word: ")
m3ch2 = input("Enter the second word: ")
m3ch1_int = len(m3ch1)
m3ch2_int = len(m3ch2)
index1_1 = m3ch1_int//2  #5.1
index1_2 = index1_1 - 1  #4.1
index1_3 = index1_1 + 1  #6.1
index2_1 = m3ch2_int//2  #3.2
index2_2 = index2_1 - 1  #2.2
index2_3 = index2_1 + 1  #4.2
m3ch1 = m3ch1[index1_2]+m3ch1[index1_1]+m3ch1[index1_3]
m3ch2 = m3ch2[index2_2]+m3ch2[index2_1]+m3ch2[index2_3]
print(m3ch1, m3ch2)






s1 = input("Enter the first word: ")
s2 = input("Enter the second word: ")

s1_int = len(s1)

n1 = s1_int//2

s3 = s1[:2]+s2+s1[2:]
print(s3)








sta = input("Enter the first word: ")
stj = input("Enter the second word: ")


sta_int = len(sta)
stj_int = len(stj)

na = sta_int//2
nj = stj_int//2

saj3 = sta[0]+stj[0]+sta[na]+stj[nj]+sta[-1]+stj[-1]
print(saj3)
