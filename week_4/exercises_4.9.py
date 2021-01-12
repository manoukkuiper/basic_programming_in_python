# exercise 1
import turtle

nick = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("hotpink")
window.title("Squares")
nick.color("yellow")

def draw_square (animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)
        window.bgcolor("hotpink")
        animal.color("yellow")

def draw_more_squares (animal, size):
    for _ in range (5):
        draw_square(animal, size)
        animal.penup()
        animal.forward(50)
        animal.pendown()

draw_more_squares(nick, 20)

# exercise 2
import turtle

def draw_square(animal, size):
    for _ in range(4):
        animal.forward(size)
        animal.left(90)

def move_turtle(animal, left, down):
    animal.penup()
    animal.right(90)
    animal.forward(down)
    animal.left(90)
    animal.backward(left)
    animal.pendown()

screen = turtle.Screen()
poly = turtle.Turtle()

for i in range(5):
    draw_square(poly, (i + 1) * 20)
    move_turtle(poly, 10, 10)

# exercise 3
import turtle

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360/n)

screen = turtle.Screen()
tess = turtle.Turtle()

draw_poly(tess, 8, 50)

# exercise 4
import turtle

def draw_poly(animal, sides, size):
    for _ in range(sides):
        animal.forward(size)
        animal.left(360 / sides)


screen = turtle.Screen()
nick = turtle.Turtle()

number_of_squares = 20
for _ in range(number_of_squares):
    draw_poly(nick, 4, 50)
    nick.left(360 / number_of_squares)

screen.exitonclick()

# exercise 5
import turtle

screen = turtle.Screen()
nick = turtle.Turtle()

nick.penup()
nick.setposition(-150, 0)
nick.pendown()

number_of_revolutions = 20
for i in range(number_of_revolutions * 4):
    nick.forward(i * 3)
    nick.right(90)

nick.penup()
nick.setposition(150, 0)
nick.pendown()

for i in range(number_of_revolutions * 4):
    nick.forward(i * 3)
    nick.right(89)

screen.exitonclick()

# exercise 6
import turtle

screen = turtle.Screen()
nick = turtle.Turtle()

def draw_poly(t, n, sz):
    for _ in range(n):
        t.forward(sz)
        t.left(360 / n)

def draw_equitriangle(t, sz):
    draw_poly(t, 3, sz)

draw_equitriangle(nick, 20)
screen.exitonclick()

# exercise 7
def sum_to(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum

print(sum_to(50))

# exercise 8
import math
def area_of_circle(r):
    a = math.pi * (r ** 2)
    return a
print(area_of_circle(34))

# exercise 9
import turtle

screen = turtle.Screen()
nick = turtle.Turtle()

def draw_star(animal, degrees, size):
    for _ in range(5):
        animal.forward(size)
        animal.left(degrees)

draw_star(nick, -144, 100)

# exercise 10
nick = turtle.Turtle()
colors = ["yellow", "green", "red", "pink", "purple", "blue"]

def draw_star(animal, degrees, size):
    for _ in range(5):
        animal.pensize(10)
        animal.color(colors[_ % len(colors)])
        animal.forward(size)
        animal.left(degrees)

def draw_multiple_stars(animal, forward, turn):
    for _ in range(5):
        draw_star(animal, -144, 100)
        animal.penup()
        animal.forward(forward)
        animal.right(turn)
        nick.pendown()

window.mainloop()
draw_multiple_stars(nick, 350, 144)






