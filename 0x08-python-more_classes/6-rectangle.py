#!/usr/bin/python3
"""this is a definition of a rectangle class"""


class Rectangle:
    """the representation of a rectangle.

    Attributes:
        number_of_instances(int):number of instances of the rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """the new rectangle is initialized

        Arguements:
            height(int): height of the new rectangle.
            width(int): width of  new rectangle.
        """
        type(self).number_of_instances = type(self).number_of_instances + 1
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrieving the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):  # setting it
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieving the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):  # setting the height
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """area of the rectangle is returned."""
        return (self.__height * self.__width)

    def perimeter(self):
        """the perimeter of the rectangle is returned"""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return (self.__width * 2) + (self.__height + self.__height)

    def __str__(self):
        """the printed form of the rectangle is returned in form of
        #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for f in range(self.__height):
            [shape.append('#') for p in range(self.__width)]
            if f != self.__height - 1:
                rect.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """the string representation of the rectangle is returned"""
        shape = "Rectangle(" + str(self.__width)
        shape = shape + ", " + str(self.__height) + ")"
        return shape

    def __del__(self):
        """a message is printed for every deletion of the rectangle."""
        type(self).number_of_instances = type(self).number_of_instances - 1
        print("Bye rectangle...")
