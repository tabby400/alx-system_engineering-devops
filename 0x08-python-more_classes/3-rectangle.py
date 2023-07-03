#!/usr/bin/python3

"""is a definition of rectangle class."""


class Rectangle:
    """is a representation of a rectangle a rectangle."""

    def __init__(self, width=0, height=0):

        """a rectangle is now initialized.

        Arguements:
            height(int): height of rectangle.
            width(int): width of  rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """retriving the width."""
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
        """retrieving the height."""
        return self.__height

    @height.setter
    def height(self, value):  # setting height
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle is returned."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width + self.__width) + (self.__height * 2))

    def __str__(self):
        """is able to return rectangle printed in form of
        #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for s in range(self.__height):
            [shape.append('#') for k in range(self.__width)]
            if s != self.__height - 1:  # not current line
                shape.append("\n")
        return ("".join(shape))
