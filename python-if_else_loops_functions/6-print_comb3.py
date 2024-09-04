#!/usr/bin/python3
for number in range(0, 10):
    for num in range(number + 1, 10):
        if num == 9 and number == 8:
            print("{0}{1}".format(number, num))
        else: 
            print("{0}{1}".format(number, num), end=", ")
