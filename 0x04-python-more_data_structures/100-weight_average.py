#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    top = 0
    bottom = 0

    for item in my_list:
        top = top + item[0] * item[1]
        bottom = bottom + item[1]

    return (top / bottom)
