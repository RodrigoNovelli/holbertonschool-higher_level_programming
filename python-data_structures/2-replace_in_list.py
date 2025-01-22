#!/bin/usr/python3
'''
def replace_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
'''
#!/bin/usr/python3
def replace_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):  # Check if idx is out of bounds
        return my_list
    else:
        new_list = my_list.copy()  # Create a copy of the list
        new_list[idx] = element  # Replace the element
        return new_list  # Return the modified list
