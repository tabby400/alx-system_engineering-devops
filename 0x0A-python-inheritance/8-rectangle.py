#!/usr/bin/python3

"""Involves class rectangle inheriting BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """is a rep of a rectangle through BaseGeometry."""

    def __init__(self, width, height):
        """A rectangle is initialized.

        Arguements:
            width: width of the rectangle.
            height: height of the rectangle.
        """

        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
