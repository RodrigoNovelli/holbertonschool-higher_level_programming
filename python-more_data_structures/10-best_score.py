#!/usr/bin/python3
def best_score(my_dict):
    i = 0
    best_student = ''
    if my_dict is None or not my_dict:
        return None
    else:
        for k, v in my_dict.items:
            if i == 0:
                bestscore = k
            elif v > bestscore:
                bestscore = v
                best_student = k
            else:
                continue
            i += 1
        return best_student
