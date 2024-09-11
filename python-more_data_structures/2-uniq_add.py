#!/usr/bin/python3
def uniq_add(my_list=[]):
    check_list = []
    add = 0
    for i in my_list:
        if i not in check_list:
            add += i
            check_list.append(i)
        else:
            continue
    return (add)
