#!/usr/bin/python3
def best_score(a_dictionary):
    i = 0
    best_student = ''
    if a_dictionary is None:
        return None
    else:
        for k in a_dictionary:
            if i == 0:
                bestscore = a_dictionary[k]
            elif a_dictionary[k] > bestscore:
                bestscore = a_dictionary[k]
                best_student = k
            else:
                pass
            i += 1
        return best_student
