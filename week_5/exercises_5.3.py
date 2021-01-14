# exercise 1 done

# exercise 2
import turtle
window = turtle.Screen()

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")

window.mainloop()

# I think alex and tess is the same thing. I think tess = alex now and you will get one turtle in color hotpink

# exercise 3
# this is how you make a copy, so changing b here will not change a. I will show it in the next line.
a = [1, 2, 3]
b = a[:]
b[0] = 5
print(a)
print(b)

# exercise 4
this = ["I", "am", "good"]
that = ["I", "am", "good"]
print("Test 1: (0)".format(this is that))
that = this
print("Test 2: (0)".format(this is that))

# exercise 5
vector_1 = [1, 2]
vector_2 = [2, 4]

# exercise 9
song = "The rain in Spain"

# exercise 10
def replace(s, old, new):
    return new.join(s.split(old))

print(replace("Mississippi", "i", "I"))

song = "I love spom! Spom is my favorite food. Spom, spom, yum!"

print(replace(song, "om", "am"))
print(replace(song, "o", "a"))




