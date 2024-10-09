n = 5
def fac(n):
    if n<= 1:
        return 1
    else:
        return n * fac(n-1)
print(fac(n))
l = [2,-3,4,5,-78]
def sum_n(l):
    if len(l) == 0:
        return 0
    else:
        return 1 + sum_n(l[1:])
print(sum_n(l))
c = 0
def nonneg(l,c):
    if len(l) == 0:
        return 0
    else:
        if l[c] < 0:
            return 0 + nonneg(l[1:],c)
        else:
            return l[c] + nonneg(l[1:],c)
    c += 1
print(nonneg(l,c))
j = "hfsjsj"
def has_digit(j):
    if len(j) == 0:
        return False
    if j[0].isdigit():
        return True
    else:
        return has_digit(j[1:])
print(has_digit(j))
     
    
    

