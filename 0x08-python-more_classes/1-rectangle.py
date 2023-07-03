#!/usr/bin/python3

"""involves definition of a rectangle class"""


class Rectangle:
    """is a rep of a rectangle."""

    def __init__(self, width=0, height=0):

        """A new rectangle is initialized.
        Arguements:
            height(int): height of the new rectangle.
            width(int): width of the new rectangle.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieve the width of the rectangle."""
        return self.__width  # private instance

    @width.setter
    def width(self, value):  # setting it
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving the height then set it."""
        return self.__height  # private instance

    @height.setter
    def height(self, value):  # setting height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
