#!/usr/bin/python3

"""Defination of a subclass of a rectangle
which is a square."""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ is a representation of a square."""

    def __init__(self, size):
        """a new square is initialized.

        Arguement:
            size(int): size of new square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)  # using constructor
        self.__size = size
