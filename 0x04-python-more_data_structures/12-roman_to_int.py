#!/usr/bin/python3

def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0

    info = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    integer = [info[n] for n in roman_string] + [0]
    converted = 0

    for x in range(len(integer) - 1):
        if integer[x] >= integer[x+1]:
            converted = converted + integer[x]
        else:
            converted = converted - integer[x]

    return converted
