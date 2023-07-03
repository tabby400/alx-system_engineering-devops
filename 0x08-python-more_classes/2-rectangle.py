#!/usr/bin/python3
"""is a definition of a rectangle class"""


class Rectangle:
    """ is a representation of a rectangle."""

    def __init__(self, width=0, height=0):

        """A new rectangle is initialized.
        Arguements:
            height(int): height of new rectangle.
            width(int): width of new rectangle.
        """

        self.height = height
        self.width = width

    @property
    def width(self):
        """used to retrieve the width of new rectangle."""
        return self.__width

    @width.setter
    def width(self, value):  # setting width
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """used to retrieve the height"""
        return self.__height

    @height.setter
    def height(self, value):  # settimg height of rectangle
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of the rectangle is returned."""
        return (self.__width * self.__height)

    def perimeter(self):
        """the perimeter is  then returned."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (self.__width * 2) + (self.__height + self.__height)
