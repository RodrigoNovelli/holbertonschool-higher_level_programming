#!/usr/bin/python3
def best_score(a_dictionary):
    max_v = 0
    max_k = ""
    if a_dictionary is None or not a_dictionary:
        return (None)
    else:
        for k, v in a_dictionary.items():
            if v > max_v:
                max_v = v
                max_k = k
            else:
                continue
        return (max_k)
