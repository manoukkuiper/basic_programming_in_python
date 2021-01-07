#exercises week 2


word_1 = "All"
word_2 = "work"
word_3 = "and"
word_4 = "no"
word_5 = "play"
word_6 = "make"
word_7 = "Jack"
word_8 = "a"
word_9 = "dull"
word_10 = "boy"

print(word_1, word_2, word_3, word_4, word_5, word_6, word_7, word_8, word_9, word_10)

print(6*(1-2))

bruce = 6
print(bruce+4)

## exercise 5
principal_amount = 5000
annual_nominal_interst_rate = 1.4
number_compounded_per_year = 3
number_of_years = 36

final_amount = principal_amount*(1+annual_nominal_interst_rate/number_compounded_per_year)**number_compounded_per_year*number_of_years
print(final_amount)

## exercise 6
print(5%2)
print(9%5)
print(15%12)
print(12%15)
print(6%6)
print(0%7)


## exercise 7
time_right_now = 14
alarm_clock_time = 51
time_till_alarm_precise = time_right_now + alarm_clock_time / 24
print(time_till_alarm_precise)

time_till_alarm_hours = time_right_now + alarm_clock_time // 24
print(time_till_alarm_hours)

## exercise 8
time = (int(input('What is the current time?')))
waiting = (int(input('How many hours do you want to wait?')))
end_time = (time + waiting) / 24
print(end_time)
