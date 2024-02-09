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
    response = "".join(str(x) for x in remaind)
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

def hexToDec(h):
    x = 0
    mult = 0
    dec_h_n = 0
    sum_h_d = 0
    h_0 = h[::-1]
    letters = ["A","B","C","D","E","F"]
    numbers = [10,11,12,13,14,15]
    for i in h_0:
        if i in letters:
            x = letters.index(i)
            i = numbers[x]
        else:
            i = int(i)
        sum_h_d = i * (16**mult)
        dec_h_n += sum_h_d
        mult += 1
    response = dec_h_n
    return response

def decimalToHex(d_h):
    hexid = []
    while d_h != 0 :
        modul = d_h%16
        if modul == 0:
            hexid.append(0)
        else:
            hexid.append(modul)
        d_h = d_h // 16   
    hexid = hexid[::-1]
    response = "".join(str(x) for x in hexid)
    return response

def hexToBin(h_b):
    bin_h = []
    h_b = h_b[::-1]
    letters = ["A","B","C","D","E","F"]
    numbers = [10,11,12,13,14,15]
    for i in h_b:
        if i.isalpha():
            if i in letters:
                x = letters.index(i)
                i = numbers[x]
        else:
            i = int(i)
        while i != 0 :
            modul = i
            modul = modul%2
            if modul == 0:
                bin_h.append(0)
            else:
                bin_h.append(1)
            i = i//2
        while len(bin_h)%4 != 0:
            bin_h.append(0)
    bin_h = bin_h[::-1]
    while bin_h[0] != 1:
        bin_h.pop(0)
    response = "".join(str(x) for x in bin_h)
    return response
     
def binToHex(b_h):
    b_h = list(b_h)
    b_h = b_h[::-1]
    dex = []
    four_l = []
    
    letters = ["A","B","C","D","E","F"]
    numbers = [10,11,12,13,14,15]
    
    while len(b_h) % 4 != 0:
        b_h.append(0)
        
    for i in b_h:
        four_l.append(i)
        dex_n = 0
        while len(four_l) % 4 == 0 and len(four_l) != 0:
            for i in four_l:
                dex_n = dex_n*2 + int(i)
            four_l.clear()
            dex.append(dex_n)
        
    
    count = 0
    for i in dex:
        
        if i > 9:
                 
            x = numbers.index(i)
            i = letters[x]
            dex[count] = i
        count +=1  
                        
    response = "".join(str(x) for x in dex)
 
