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








