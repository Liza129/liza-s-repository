action = input("If you want to use mean press 'm', median 'd', mode 'o', frequency 'f', top 5 numbers 't', last 5 numbers 'l' ")
count = 1
l = []
inp = input(str(count) + "Enter a number to a list, when you finish just enter lettr 'y':")
l.append(float(inp))
while inp != "y" and count != 20:
    count += 1
    inp = input(str(count) + "Enter a number to a list, when you finish just enter lettr 'y'")
    l.append(float(inp))
def mean(l):
    sum_all = 0
    c = 1
    for i in l:
        sum_all += float(i)
        c += 1
    mean = sum_all/c
    return mean

def median(l):
    l.sort()
    if len(l) % 2 != 0:
        index = (len(l) + 1)/2
        median = l[index - 1]
    else:
        index1 = len(l)/2
        index2 = index1 - 1
        median = (float(l[index1]) + float(l[index2]))/2
    return median

def mode(l):
    max_f = 0
    
    return mode

def frequency(l):
    return frequency
    
def top5(l):
    l.sort()
    l = l[::-1]
    top5 = l[0:5]
    top5 = top5[::-1]
    return top5

def last5(l):
    l = l[::-1]
    last5 = l[0:5]
    return last5
