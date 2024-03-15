def isbn10Toisbn13(isbn):
    add_n = 0
    c = 1
    isbn = isbn[:-1]
    isbn = "978" + isbn
    for i in isbn:
        i = int(i)
        if c % 2 == 0:
            i = i * 3
        add_n += i
        c += 1
    add_n = add_n % 10
    if add_n == 0:
        check_d = 0
    else:
        check_d = 10 - add_n
    isbn = isbn + str(check_d)
    l = isbn
    l = l[:3] + str("-") + l[3:]
    l = l[:5] + str("-") + l[5:]
    l = l[:11] + str("-") + l[11:]
    l = l[:15] + str("-") + l[15]
    return l
isbn = input("Enter your ISBN-10: ")
ISBN_13 = isbn10Toisbn13(isbn)
print("Your ISBN-13 will look like this: ", ISBN_13)



#isbn = "1853261580"