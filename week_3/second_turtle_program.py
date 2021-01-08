# Tess and Alex together

import turtle

window = turtle.Screen()
window.bgcolor("hotpink")
window.title("Tess and Alex")

tess = turtle.Turtle()
tess.color("yellow")
tess.pensize(5)

tess.penup()
size = 20
for _ in range(30):
    tess.stamp()
    size = size + 3
    tess.forward(120)


alex = turtle.Turtle()
alex.shape("turtle")
alex.speed(10)

tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)

tess.right(180)
tess.forward(80)

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

alex.penup()
alex.forward(100)
alex.pendown()


window.mainloop()



