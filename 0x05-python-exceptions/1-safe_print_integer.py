#!/usr/bin/python3

def safe_print_integer(value):
    """function prints int with d format.

    arguements:
    value: integer to be printed

    Return: True otherwise False if TypeError

    """

    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
