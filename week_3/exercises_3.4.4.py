# exercise 1
number_days = int(input("Please enter a day number ranging from 0 to 6"))

if number_days == 0:
    print("Sunday")
elif number_days == 1:
    print ("Monday")
elif number_days == 2:
    print("Tuesday")
elif number_days == 3:
    print ("Wednesday")
elif number_days == 4:
    print("Thursday")
elif number_days == 5:
    print ("Friday")
elif number_days == 6:
    print("Saturday")

# exercise 2
leaving_day = int(input("On what day were you leaving?"))
staying = int(input("How many days were you there?"))
day_of_return = (leaving_day + staying)
print(day_of_return)

# exercise 3, 4, 5 see notes

# exercise 6
marks = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
for grade in marks:
    if grade >= 75:
        print("first")
    elif grade >= 70:
        print("upper second")
    elif grade >= 60:
        print("second")
    elif grade >= 50:
        print("third")
    elif grade >= 45:
        print("F1 supp")
    elif grade >= 40:
        print("F2")
    else:
        print("F3")

# exercise 7 - don't get this one

# exercise 8

# exercise 11
for _ in range(1000):
    print("We like Python's turtles!")

# exercise 12
for months in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
    month = "One of the months of the year is " + months
    print(month)

# exercise 12 his answer
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]

for month in month_names:
    print("One of the months of the year is", month)

# exercise 13 - she is just spinning around and heading in north-west direction in the end?
import turtle
window = turtle.Screen()
tess = turtle.Turtle()
tess.setheading(90)
tess.left(3)
window.mainloop()

# exercise 14
numbers = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for number in numbers:
    print(number)

for number in numbers:
    print(number, number**2)

total = 0
for number in numbers:
    total += number
    print(total)

product = 1
for number in numbers:
    product *= number
    print(product)

# exercise 15
import turtle

screen = turtle.Screen()
poly = turtle.Turtle()

# Equilateral triangle
poly.color("red")
for _ in range(3):
    poly.forward(60)
    poly.left(120)

# Square
poly.color("orange")
for _ in range(4):
    poly.forward(90)
    poly.left(90)

# Hexagon
poly.color("green")
for _ in range(6):
    poly.forward(120)
    poly.left(60)

# Octagon
poly.color("blue")
for _ in range(8):
    poly.forward(150)
    poly.left(45)

screen.exitonclick()

# exercise 16
import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

turns = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for turn in turns:
    pirate.left(turn)
    pirate.forward(100)

# exercise 17
import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

steps = [160, -43, 270, -97, -43, 200, -940, 17, -86]

heading = 0
for step in steps:
    pirate.left(step)
    pirate.forward(100)
    heading += step

print("The final heading is", heading % 360)

screen.exitonclick()

# exercise 18
import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

for _ in range(18):
    pirate.right(20)
    pirate.forward(50)

# exercise 19

# exercise 20
import turtle

screen = turtle.Screen()
don = turtle.Turtle()   # Starry, starry night

don.left(36)
for _ in range(5):
    don.forward(100)
    don.left(180 - 36)

don.hideturtle()

screen.exitonclick()

# exercise 21
import turtle

screen = turtle.Screen()
cogsworth = turtle.Turtle()

screen.bgcolor("limegreen")

cogsworth.shape("turtle")
cogsworth.penup()
cogsworth.color("blue")
cogsworth.pensize(3)
cogsworth.left(90)

for _ in range(12):
    cogsworth.forward(150)
    cogsworth.pendown()
    cogsworth.forward(10)
    cogsworth.penup()
    cogsworth.forward(20)
    cogsworth.stamp()
    cogsworth.goto(0, 0)
    cogsworth.right(360 / 12)

screen.exitonclick()

# exercise 22 - done

# exercise 23
numbers = [12, 3, 4, 5, 6]
count = 0

for number in numbers:
    if number % 2 == 1
        count += 1
    if number % 2 == 0
        continue

# exercise 23
numbers = [13, -3, 13, 7, -25]
count = 0

for number in numbers:
    if number % 2 != 0:
        count += 1

print("There are", count, "odd numbers in the list")

# exercise 24
sum = 0

for number in numbers:
    if number % 2 == 0:
        sum += number
print("The sum of the even number is:", sum)

# exercise 25
sum_negatives = 0

for number in numbers:
    if number < 0:
        sum_negatives += number
print("The sum of the negative numbers is:", sum_negatives)

# exercise 26
words = ["hello", "goodbye", "ciao", "ola", "goedemorgen", "goedenavond"]
words_length_5_count = 0

for word in words:
    if len(word) == 5:
        words_length_5_count += 1
print("Count of words with a length of 5 is:", words_length_5_count)

# exercise 27
sum_odd_numbers_without_first = 0
for number in numbers:
    if number % 2 == 0:
        break
    sum_odd_numbers_without_first += number
print("The sum of odd numbers without the first one is:", sum_odd_numbers_without_first)

# exercise 28
names = ["quinn", "finn", "rachel", "sam", "artie", "mercedes"]
count_names = 0

for name in names:
    if name == "sam":
        break
    count_names += 1
print("How many names are there until Sam comes:", count_names)

# exercise 29
import math

n = 25
threshold = 1e-7
approximation = n / 25

while True:
    better = (approximation + (n / approximation)) / 2
    print("approximation:", better)
    if abs(approximation - better) < threshold:
        print("Best:", better)
        break
    approximation = better

# exercise 31
n = 12

for number_prime in range(2, n // 2):
    if n % number_prime == 0:
        print(number_prime, "is a divisor of", n, "therefore it is not a prime")
        print(False)
        break
    else:
        print("No divisor found for", n, "therefore it is a prime number")
        print(True)

# exercise 32
import turtle

screen = turtle.Screen()
pirate = turtle.Turtle()

steps = [(160, 20), (-43, 10), (270, 8), (-43, 12)]

for angle, distance in steps:
    pirate.left(angle)
    pirate.forward(distance)

# exercise 33
pirate.left(90)
pirate.forward(100)
pirate.right(45)
pirate.forward(100)
pirate.left(45)
















