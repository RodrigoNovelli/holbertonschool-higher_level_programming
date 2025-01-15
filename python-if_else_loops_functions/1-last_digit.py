#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    last_digit = number % 10
else:
    last_digit = number * -1 % 10
    last_digit = last_digit * -1
str = "Last digit of {} is {} and".format(number, last_digit)
if last_digit > 5:
    print(str + " is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(str + " is less than 6 and not 0")
else:
    print(str + " is 0")
