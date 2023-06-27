#!/usr/bin/python3

""" class square defining a square"""


class Square:

    """shows theres a rep square"""

    def __init__(self, size=0):
        """square to be initialized.

        Arguments:
            size(int):new square size
        """

        self.size = size

    @property  # define method size to get size
    def size(self):
        """find square size."""

        return (self.__size)

    @size.setter  # def method to set size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value  # private instance

    def area(self):
        """ area of the square."""

        return (self.__size * self.__size)  # area now
