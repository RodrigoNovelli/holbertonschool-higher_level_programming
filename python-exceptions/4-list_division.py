#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    c = 0
    new_list = [0] * list_length
    for i in range(0, list_length):
        try:
            c = my_list_1[i] / my_list_2[i]
        except TypeError:
            c = 0
            print("wrong type")
            continue
        except IndexError:
            c = 0
            print("out of range")
            continue
        except ZeroDivisionError:
            c = 0
            print("division by 0")
            continue
        finally:
            new_list[i] = c
    return (new_list)
