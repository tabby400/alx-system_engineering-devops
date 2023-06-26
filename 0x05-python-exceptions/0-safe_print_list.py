#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """fuction printing x elements in a list.

    arguements:
        my_list=[]: list elements are printed from
        x:no of elements to print
    return:
        no of printed elements
    """

    total = 0
    for p in range(x):
        try:
            print("{}".format(my_list[p]), end="")
            total = total + 1
        except IndexError:
            break  # halt prog
    print(" ")
    return(total)
