#!/usr/bin/python3

"""defining a square using class square"""


class Square:
    """ shows its a square"""

    def __init__(self, size):
        """square to be init.

        Aruements:
            Size(int):square new size
        """

        self.size = size

    @property
    def size(self):
        """retrieve square size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """returns square area."""
        return self.__size ** 2

    def my_print(self):
        """printing wit #."""

        if self.__size == 0:
            print("")
        else:
            for p in range(0, self.__size):  # len
                [print("#", end="") for x in range(self.__size)]
                print("")
