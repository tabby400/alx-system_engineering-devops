#!/usr/bin/python3
"""this is a definition of a rectangle class"""


class Rectangle:
    """the representation of a rectangle.

    Attributes:
        number_of_instances(int):number of instances of the rectangle
        print_symbol: the string representation symbol
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """new rectangle is initialized

        Arguements:
            height(int): height of  new rectangle.
            width(int): width ofnew rectangle.
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
        """ is retrieving the height of the rectangle."""
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns rectangle whose area is greater.

        Arguements:
            rect_1(rectangle): first rectangle.
            rect_2(rectangle): second rectangle.
        Raises:
            TypeError:  when rect_1 or rect_2 turns out to not be rectangle
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
 
        return rect_2

    @classmethod  # new rectangle instance
    def square(cls, size=0):
        """used to return a new rectangle instance width and height same

        Arguements:
            size(int): height and width of rectangle
        """
        return (cls(size, size))  # class within class method

    def __str__(self):

        """the printed form of the rectangle is returned in form of
        #.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        shape = []
        for t in range(self.__height):
            [shape.append(str(self.print_symbol)) for p in range(self.__width)]
            if t != self.__height - 1:  # not same row
                shape.append("\n")
        return ("".join(shape))

    def __repr__(self):
        """the string representation of rectangle is returned"""
        shape = "Rectangle(" + str(self.__width)
        shape = shape + ", " + str(self.__height) + ")"
        return shape

    def __del__(self):
        """message is printed for every deletion of the rectangle."""
        type(self).number_of_instances = type(self).number_of_instances - 1
        print("Bye rectangle...")
