#!/usr/bin/python3

# 0-add_integer.py
"""explains on function that is used to add integers"""

def add_integer(a, b=98):
    """function used to provide the addition of and b
    args: if a float is encountered it is typecasted to int

    Raises:
        TypeError: when a or b is not an int or a float
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")

    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")  # if a or b are int or float

    return int(a) + int(b)
