#!/usr/bin/python3
def print_last_digit(number):
    if isinstance(number, str):
        print("Traceback (most recent call last):", end="")
        return ("")
    else:
        strn = str(number)
        for i in range(0, len(strn)):
            if i == len(strn) - 1:
                print("{}" .format(strn[i]), end="")
            else:
                continue
        return (strn[i])
