def AND_gate(a,b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0
#and_g = AND_gate(a,b)
 def OR_gate(a,b):
     if a ==1 or b == 1:
         return 1
    else:
        return 0
def NOT_gate(x):
    if x == 1:
        return 0
    elif x == 0:
        return 1
def NAND_gate(a,b):
    if a == 1 and b == 1:
        return 0
    else:
        return 1
def NOR_gate(a,b):
    if a ==1 or b == 1:
         return 0
    else:
        return 1
def XOR_gate(a,b):
    if a == 1 and b == 1:
        return 0
    elif a ==1 or b == 1:
         return 1
    else:
        return 0
def XNOR_gate(a,b):
    if a == 1 and b == 1:
        return 1
    elif a ==1 or b == 1:
         return 0
    else:
        return 1

    
    