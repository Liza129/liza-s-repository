l = []
"""
count = 1
inp = input(str(count) + ".Enter a number to a list, when you finish just enter lettr 'y':")
l.append(float(inp))
while inp != "y" and count != 20:
    count += 1
    inp = input(str(count) + ".Enter a number to a list, when you finish just enter lettr 'y'")
    l.append(float(inp))
"""
f = open("C:\\Users\\lizab\\OneDrive\\Документы\\python school work\\20numbers.txt", "r")
for x in f:
    l.append(int(x))

def mean(l):
    sum_all = 0
    c = 0
    for i in l:
        sum_all += i
        c += 1
    mean = sum_all/c
    return mean
 
def median(l):
    l.sort()
    if len(l) % 2 != 0:
        index = int((len(l) + 1)/2)
        median = l[index - 1]
    else:
        index1 = int(len(l)/2)
        index2 = int(index1 - 1)
        median = (l[index1] + l[index2])/2
    return median
 
def mode(l):
    l.sort()
    only = []
    count_l2 = []
    count_l = []
    modes = []
    c = 0
    final = []
    for i in l:
        if i not in only:
            only.append(i)
    for i in only:
        num = l.count(i)
        count_l.append(num)
    for i in count_l:
        count_l2.append(i)
    sort_num = count_l
    sort_num.sort()
    sort_num = sort_num[::-1]
    for i in sort_num:
        if i < sort_num[0]:
            final = sort_num[:c]
            break
        c += 1
    for i in final:
        idx = count_l2.index(i)
        count_l2.pop(idx)
        count_l2.insert(idx,0)
        modes.append(only[idx])
    if len(modes) > 1:
        mode = "The modes are: " + ','.join(map(str,modes))
    elif len(modes) == 1:
        mode = "The mode is: " + str(modes[0])
    else:
        mode = "There is no mode in the list you enetred"
    return mode
 
def frequency(l):
    l.sort()
    only = []
    count_l = []
    for i in l:
        if i not in only:
            only.append(i)
    for i in only:
        num = l.count(i)
        count_l.append(num)
    frequency = []
    c = 0
    for i in range(len(only)):
        b = str(only[c]) + " appears : " + str(count_l[c]) + " times"
        if b not in frequency:
            frequency.append(b)
        c += 1
    return frequency
def top5(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    a.sort()
    a = a[::-1]
    top5 = a[:5]
    return top5
 
def last5(l):
    a = []
    for i in l:
        if i not in a:
            a.append(i)
    a.sort()
    last5 = a[:5]
    return last5

action = input("If you want to use mean press 'm', median 'e', mode 'o', frequency 'f', top 5 numbers 't', last 5 numbers 'l', when you finish press 's': ")
while action != "s":
    if action == "m":
        mean = mean(l)
        print("Mean number is ", mean)
    elif action == "e":
        median = median(l)
        print("Median number is ", median)
    elif action == "o":
        mode = mode(l)
        print(mode)
    elif action == "f":
        frequency = frequency(l)
        print(frequency)
    elif action == "t":
        top5 = top5(l)
        print("Top 5 numbers are ", top5)
    elif action == "l":
        last5 = last5(l)
        print("Last 5 numbers are ", last5)
    action = input("If you want to use mean press 'm', median 'e', mode 'o', frequency 'f', top 5 numbers 't', last 5 numbers 'l', when you finish press 's': ")
if action == "s":
    print("Goodbyee!!!")