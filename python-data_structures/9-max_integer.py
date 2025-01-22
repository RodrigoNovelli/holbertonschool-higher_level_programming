#!/usr/bin/python3
def max_integer(my_list=[]):
    num_max = 0
    if len(my_list) != 0:
        for value in range(len(my_list)):
            if my_list[value] > num_max:
                num_max = my_list[value]
            else:
                pass
        return num_max
    else:
        return None
