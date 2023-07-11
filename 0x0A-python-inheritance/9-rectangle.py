#!/usr/bin/python3

"""Definition of a class rectangle inheriting from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """is a representation of a rectangle with use of
    BaseGeometry."""

    def __init__(self, width, height):
        """Intialization of a rectangle

        Arguements:
            width(int): width of the rectangle.
            height(int):  height of the rectangle.
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """area of the rectangle is returned"""
        return self.__height * self.__width

    def __str__(self):
        """ print() and str() of rectangle is returned."""

        string_ret = "[" + str(self.__class__.__name__) + "] "
        string_ret = string_ret + str(self.__width) + "/" + str(self.__height)
        return (string_ret)
