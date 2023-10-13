m = input("Enter a message you want to translate: ")
k = input("Enter a key number: ")
k = int(k)
code = input("Do you want to encode or decode the message: ")
a = "abcdefghijklmnopqrstuvwxyz"
g = ""
h = ""

for i in m:
    if i.isalpha():
        
        index = a.index(i)
        index += k
        if index > 25:
            index = index%26
        g = g + a[index]
        index_de = index - 2*k
        h = h + a[index_de]
    else:
        g = g + i
if code == "encode":
    g = g.upper()
    print(g)

elif code == "decode":
    h = h.lower()
    print(h)
else:
    print("i don't understand you")
   
