#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return(my_list)
    elif idx < (len(my_list) - 1):
        return(my_list)
    else:
        list.insert(idx, element)
        print("{}" .format(my_list[idx]))
        return(my_list)
