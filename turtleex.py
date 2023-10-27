import turtle
scr = turtle.Screen()
scr.bgcolor("grey")
t = turtle.Turtle()
import random
#060


for i in range(4):

    t.right(90)
    t.forward(50)


#061



t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
#062

r = 90
t.circle(r)


#063
t.fillcolor("black")
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()
t.penup()
t.forward(100)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()
t.penup()
t.forward(100)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.right(90)
t.forward(50)
t.end_fill()

#064
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)
t.forward(200)
t.right(144)

#065
t.left(90)
t.forward(200)
t.right(90)
t.penup()
t.forward(100)
t.pendown()
t.forward(150)
t.right(90)
t.forward(100)
t.right(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.penup()
t.forward(100)
t.pendown()
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(180)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)

#066
l = ["green", "blue", "black", "yellow", "red", "purple"]

for i in range(8):
    w = random.choice(l)
    t.color(w)
    t.right(45)
    t.forward(150)
 
#067
for i in range(12):
    t.right(30)
    for i in range(8):
        t.right(45)
        t.forward(150)

#068
