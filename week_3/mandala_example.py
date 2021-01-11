import turtle

paper = turtle.Screen()
leonardo = turtle.Turtle()

leonardo.pensize(10)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for index in range(12):
    leonardo.color(colors[index % len(colors)])
    if index % 2 == 0:
        leonardo.forward(100)
    else:
        leonardo.forward(50)
    leonardo.left(30)

paper.exitonclick()

# example book on for loops
students = ("John", ["History", "Math"]), ("Manouk", ["Python", "Major Thesis"])
for name, subjects in students:
    print(name, "takes", len(subjects), "courses")

