import turtle
# Alex the turtle
# questions for participants
background_color = input("What do you want Alexs background color te be?")
alex_color = input("What do you want Alex's color to be?")


window = turtle.Screen()
alex = turtle.Turtle()

window.bgcolor(background_color)
window.title("Hello, Alex")
alex.color(alex_color)
alex.pensize(10)

alex.forward(50)
alex.left(90)
alex.forward(30)

window.mainloop()

# Tess the turtle

background_color_tess = input("What do you want the background color of Tess to be?")
tess_color = input("What do you want Tess' color to be?")


window = turtle.Screen()
tess = turtle.Turtle()

window.bgcolor(background_color_tess)
window.title("Hello, Tess")
tess.color(tess_color)
tess.pensize(3)

tess.forward(30)
tess.left(120)
tess.forward(23)

window.mainloop()

# Tess and Alex together

window = turtle.Screen()
window.bgcolor("hotpink")
window.title("Tess and Alex")

tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5)

alex = turtle.Turtle()

tess.forward(80)
tess.left(120)
tess.forward(80)