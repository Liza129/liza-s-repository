import myCircleArea
def prefix(a):
    a = "un" + a
    return a
def pastfix(b):
    b = b + "s"
    return b
d = int(input("Enter a diameter:"))
#def circle_area(d):
    #return (d/2)**2*3.14
g = myCircleArea.circle_area(d)
print("The area of a circle od diametre",d, "is",g)
h = int(input("Enter the height"))
w= int(input("Enter the width"))
def rec_a(h,w):
    return h*w
j = rec_a(h,w)
print("The area of such rectangle is ",j)
choice = input("1. Area of Circle\n2. Perimeter of circle\n3. Area of rectangle\n4. Perimeter of rectangle")
if choice == "1":
    d = int(input("Enter a diameter:"))
    g = myCircleArea.circle_area(d)
    print("The area of such circle is ",g)
elif choice == "2":
    d = int(input("Enter a diameter:"))
    #def per(d):
        #return 2*3.14*(d/2)
    g = myCircleArea.per(d)
    print("The perimeter of such circle is ",g)
elif choice == "3":
    h = int(input("Enter the height"))
    w= int(input("Enter the width"))
    g = rec_a(h,w)
    print("The area of such rectangle is ",g)
else:
    h = int(input("Enter the height"))
    w= int(input("Enter the width"))
    #def per_r(h,w):
        #return 2*(h+w)
    g = myCircleArea.per_r(h,w)
    print("The perimeter of such rectangle is ",g)
def middle_char(a):
    s = len(a)//2
    return a[s]
a = "cat"
g = middle_char(a)
print(g)
