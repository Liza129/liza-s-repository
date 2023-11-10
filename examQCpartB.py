l = [4,5,9,8,10,17,99,77]
n = len(l)
l.sort()
if n % 2 == 0:
    m1 = l[n//2]
    m2 = l[n//2 - 1]
    m = (m1 + m2)/2
else:
    m = l[n//2]


print("Median is: ", m)
