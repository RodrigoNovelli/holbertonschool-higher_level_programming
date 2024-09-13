#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    if my_list is None or x is None:
        return (counter)
    for i in range(0, x):
        try:
            element = my_list[i]
            if isinstance(element, int):
                print("{:d}" .format(my_list[i]), end="")
                counter += 1
        except ValueError as e:
            continue
    print()
    return (counter)
