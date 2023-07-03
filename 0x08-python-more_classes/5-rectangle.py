#!/usr/bin/python3
"""this is a definition of a rectangle class."""


class Rectangle:
    """is a representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """ new rectangle is initialized
        Arguement:
            height(int): height of  new rectangle.
            width(int): width of  new rectangle.
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieve the width of a rectangle"""
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
        """height of the rectangle being retrieved."""
        return self.__height  # private instance

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the exact area of rectangle is retrieved."""
        return (self.__height * self.__width)

    def perimeter(self):
        """ the exact perimeter of the rectangle is returned."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width + self.__width) + (self.__height * 2))

    def __str__(self):
        """rectangle is returned in the printed form in form of
        #
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for t in range(self.__height):
            [shape.append('#') for y in range(self.__width)]
            if t != self.__height - 1:  # not same row
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """string representation of rectangle is returned."""

        shape = "Rectangle(" + str(self.__width)
        shape = shape + ", " + str(self.__height) + ")"
        return shape

    def __del__(self):
        """for every deletion of rectangle print the message."""
        print("Bye rectangle...")
