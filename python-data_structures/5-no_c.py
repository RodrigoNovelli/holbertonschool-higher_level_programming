#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        if my_string[i] == 63 or my_string[i] == 43:
            list.remove(my_string[i])
        else:
            continue
