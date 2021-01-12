import turtle

screen = turtle.Screen()
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
