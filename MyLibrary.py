#p1
print("A programme to find the greatest of 3 values")
n1 = int(input("Enter the first value: "))
n2 = int(input("Enter the second value: "))
n3 = int(input("Enter the third value: "))

def greatestof3Values1(a,b,c):
    if a > b and a > c:
        response = str(a) + "is the greatest value"
    elif b > a and b > c:
        response = str(b) + "is the greatest value"
    else:
        response = str(c) + "is the greatest value"
    return response
greatestof3Values1(n1,n2,n3)

def greatestof3Values2(A,B,C):
    if A > B:
        if A > C:
            response = str(A) + "is the greatest value"
        else:
            response = str(C) + "is the greatest value"
    else:
        if B > C:
            response = str(B) + "is the greatest value"
        else:
            response = str(C) + "is the greatest value"
    return response
greatestof3Values2(n1,n2,n3)


def greatestof3Values3():
    maximum = n1
    if maximum < n2:
        maximum = n2
    if maximum < n3:
        maximum = n3
    response = str(maximum) + " is the greatest value"
    return response
