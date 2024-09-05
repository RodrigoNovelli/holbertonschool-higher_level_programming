#!/usr/bin/python3
def pow(a, b):
    j = 1
    if b > 0:
        for i in range(1, b + 1):
            j = j * a
    else:
        for i in range(1, abs(b) + 1):
            j = j * a
            if i == abs(b):
                j = 1 / j
    return (j)
