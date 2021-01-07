name = input("What is your name?")
print("Hello", name)

km_to_destination = int(input("How many kilometers is your destination?"))

## time with bike average speed = 18km/h
preparation_time_bike = int(input("How long does it take to get your bike (in minutes)?"))
additional_time_bike = int(input("How long does it take to park your bike and walk to the destination (in minutes)?"))
total_time_bike_minutes = (km_to_destination / 18) * 60 + preparation_time_bike + additional_time_bike
print(total_time_bike_minutes)
print("Thanks for answering", name, "the total time it takes for you to get to your destination by bike is", total_time_bike_minutes, "minutes")

## time with car average speed = 100km/h
preparation_time_car = int(input("How long does it take to get your car (in minutes)?"))
additional_time_car = int(input("How long does it take to park your car and walk to the destination (in minutes)?"))
total_time_car_minutes = (km_to_destination / 100) * 60 + preparation_time_car + additional_time_car
print(total_time_car_minutes)
print("Thanks for answering", name, "the total time it takes for you to get to your destination by car is", total_time_car_minutes, "minutes")

## time with train average speed = 120km/h
preparation_time_train = int(input("How long does it take to get to the train station (in minutes)?"))
additional_time_train = int(input("How long does it take to walk to the destination from the train station (in minutes)?"))
total_time_train_minutes = (km_to_destination / 120) * 60 + preparation_time_train + additional_time_train
print(total_time_train_minutes)
print("Thanks for answering", name, "the total time it takes for you to get to your destination by train is", total_time_train_minutes, "minutes")

## time to walk average speed = 5km/h
preparation_time_walking = int(input("How long does it take to get out of the house (in minutes)?"))
total_time_walking_minutes = (km_to_destination / 5) * 60 + preparation_time_walking
print(total_time_walking_minutes)
print("Thanks for answering", name, "the total time it takes for you to get to your destination if you walk is", total_time_walking_minutes, "minutes")

