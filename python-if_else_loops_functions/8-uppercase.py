#!/usr/bin/python3
def uppercase(str):
    if str == "":
        print("")
    else:
        for i in range(0, len(str)):
            if ord(str[i]) >= 97:
                p = ord(str[i]) - 32
                a = chr(p)
            elif ord(str[i]) < 97:
                a = str[i]
            if i == len(str) - 1:
                print("{}" .format(a))
            else:
                print("{}" .format(a), end="")
