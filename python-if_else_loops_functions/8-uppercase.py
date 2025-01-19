#!/usr/bin/env python3
def uppercase(str):
    i = 0
    if str == "":
        a = "\n"
    while i != len(str) or i == 0:
        if str != "":
            if ord(str[i]) >= 97:
                p = ord(str[i]) - 32
                a = chr(p)
            elif ord(str[i]) < 97:
                a = str[i]
        if i + 1 != len(str) or str == "":
            print("{}" . format(a), end="")
            if str == "":
                break
        else:
            print("{}" .format(a))
        i += 1
