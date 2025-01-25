#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    print(new_dict)
    return new_dict
