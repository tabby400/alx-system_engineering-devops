#!/usr/bin/python3

# 4-print_square.py

"""explains more on a function that prints squares."""


def print_square(size):
    """function used in square printing with #

    Arguements:
        size(int): leads up to height and width of square
    Raises:
        TypeError: If the size is not an int
        ValueError: If size is not >= 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for x in range(size):
        [print("#", end="") for k in range(size)]
        print("")  # height and width
