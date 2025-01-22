#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    boolean = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            boolean.append(True)
        else:
            boolean.append(False)
    return boolean
