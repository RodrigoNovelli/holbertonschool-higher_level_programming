#!/usr/bin/python3
def multiple_returns(sentence):
    tuple_a = ()
    len_string = len(sentence)
    if len_string != 0:
        first_ch = sentence[0]
    else:
        first_ch = None
    tuple_a = (len_string, first_ch)
    return tuple_a
