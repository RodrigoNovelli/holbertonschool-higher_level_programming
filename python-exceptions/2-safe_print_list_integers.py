#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    if my_list is None:
        my_list = ""
    for i in range(0, x):
        try:
            print("{:d}" .format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            counter += 1
    print()
    return (counter)
