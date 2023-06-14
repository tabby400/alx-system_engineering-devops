#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique = set(my_list)
    value = 0
    for p in unique:
        value = value + p
    return (value)
