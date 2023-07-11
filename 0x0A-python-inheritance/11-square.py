#!/usr/bin/python3

"""Definition of a square which is a subclass of
class rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):  # base class is rectangle
    """is a representation of a square."""

    def __init__(self, size):
        """a square is initialized

        Arguements:
            size(int): size of the square.
        """

        self.integer_validator("size", size)
        super().__init__(size, size)  # using constructor
        self.__size = size
