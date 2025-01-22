#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        for value in range(len(my_list)):
            if value == 0:
                num_max = my_list[value]
            elif my_list[value] > num_max:
                num_max = my_list[value]
            else:
                pass
        return num_max
    else:
        return None
