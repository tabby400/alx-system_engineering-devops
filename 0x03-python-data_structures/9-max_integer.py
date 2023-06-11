#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:  # is empty
        return (None)
    m = my_list[0]  # first element in list
    for p in my_list:
        if p > m:
            m = p
    return (m)
