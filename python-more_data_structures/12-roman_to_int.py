#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_map = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
        }
    int_value = 0
    prev_value = 0
    current_value = 0
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    elif not roman_string:
        return 0
    else:
        for letter in reversed(roman_string):
            current_value = roman_map[letter]
            if current_value >= prev_value:
                int_value += current_value
            else:
                int_value -= current_value
            prev_value = current_value
        return int_value
