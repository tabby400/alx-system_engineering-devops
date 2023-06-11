#!/usr/bin/python3

def no_c(my_string):
    remv_c = ""

    for x in my_string:
        if (x != 'C') and (x != 'c'):
            remv_c = remv_c + x
    return (remv_c)
