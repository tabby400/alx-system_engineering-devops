#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """function prints the first x elements
    only integers

    Arguements:
        my_list[]: list with the elements
        x: no of elements to be printed
    Return: total elements printed
    """

    total = 0

    for p in range(0, x):
        try:
            print("{:d}".format(my_list[p]), end="")
            total = total + 1
        except(ValueError, TypeError):
            continue
    print("")
    return (total)
