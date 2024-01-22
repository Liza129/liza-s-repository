def biToDecimal(b_0):
    mult = 1
    sum_n = 0
    b = b_0[::-1]
    for i in b:
        i = int(i)
        sum_n += i * mult
        mult = mult*2
    response = sum_n
    return response


def decimalToBi(d_0):
    remaind = []
    while d_0 != 0 :
        modul = d_0
        modul = modul%2
        if modul == 0:
            remaind.append(0)
        else:
            remaind.append(1)
        d_0 = d_0//2
    remaind = remaind[::-1]
    response = remaind
    return response


def addToBi(b1,b2):
    b1 = b1[::-1]
    b2 = b2[::-1]
    st1 = str(b1)
    st2 = str(b2)
    l1 = len(st1)
    l2 = len(st2)
    c = 0
    count = 0
    sum_n = 0
    sum_bi = []
    #
    if l1 > l2:
        small = b2
        big = b1
        b = l1
    elif l2 > l1:
        small = b1
        big = b2
        b = l2
    elif l1 == l2:
        small = b2
        big = b1
        b = l1
    # 
    for i in small:
        i = int(i)
        sum_n = i + int(b2[count]) + c
        if sum_n == 0 or sum_n == 1:
            c = 0
            sum_bi.append(sum_n)
        elif sum_n == 2:
            c = 1
            sum_bi.append(0)
        elif sum_n == 3:
            c = 1
            sum_bi.append(1)
        count += 1
    #
    if l1 == l2:
        if c == 1:
            sum_bi.append(1)
    else:
        b_rest = big[count:]
        for i in b_rest:
            i = int(i)
            sum_n = i + c
            if sum_n == 0 or sum_n == 1:
                c = 0
                sum_bi.append(sum_n)
            elif sum_n == 2:
                c = 1
                sum_bi.append(0)
            count += 1
            
    #
    sum_bi = sum_bi[::-1]
    response = sum_bi
    return response


