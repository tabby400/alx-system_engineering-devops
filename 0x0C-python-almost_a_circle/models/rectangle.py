#!/usr/bin/python3

"""this is the definition of a
rectangle class."""

from models.base import Base  # using function in a module


class Rectangle(Base):
    """is a representation of a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """a new rectangle is initialized
        Arguements:
            heightint): height of the rectangle.
            width(int): width of the rectangle.
            y(int): y coordinate of the rectangle.
            x(int): x coordinate of the rectangle.
            id(int): The id of the rectangle.
        Raises:
            TypeError: when the width or the height is not an integer
            TypeError: when x or y is not an integer
            ValueError: when width or height is <= 0.
            ValueError: when x or y is < 0.
        """

        self.height = height
        self.width = width
        self.y = y
        self.x = x
        super().__init__(id)

    @property
    def width(self):
        """retrieving the width of a rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:  # if its not an integer
            raise TypeError("width must be an integer")
        if value <= 0:  # less than 0
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """retrieving the width of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:  # if its not int
            raise TypeError("height must be an integer")
        if value <= 0:  # if less than 0
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """retrieving the y coordinate of the rectangle"""
        return (self.__x)

    @x.setter
    def x(self, value):
        if type(value) != int:  # if not an int
            raise TypeError("x must be an integer")
        if value < 0:  # if less than 0
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """retrieving the x coordinate."""
        return (self.__y)

    @y.setter
    def y(self, value):
        if type(value) != int:  # if not an int
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):  # area of the rectangle
        """getting the area of the rectangle."""
        return (self.height * self.width)

    def display(self):
        """Printing the rectangle using #"""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for g in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for d in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updating the rectangle, variable
        length ofarguements.
        Arguements:
            *args(int):the height,width x, y attibutes.
                - one arg is the id attribute
                - the other arg is width attribute
                - arg 3 is height attribute
                - arg 4 is x attribute
                - arg 5 is to be y attribute
            **kwargs(dict):key/value pairs introduced
        """

        if args and len(args) != 0:
            arg_ind = 0
            for arg in args:
                if arg_ind == 0:
                    if arg is None:
                        self.__init__(self.height, self.width, self.x, self.y)
                    else:
                        self.id = arg
                elif arg_ind == 1:
                    self.width = arg
                elif arg_ind == 2:
                    self.height = arg
                elif arg_ind == 3:
                    self.x = arg
                elif arg_ind == 4:
                    self.y = arg
                arg_ind = arg_ind + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = value
                elif key == "height":  # the height
                    self.width = value
                elif key == "width":  # the width
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """ returning the rep in form of a dictionary"""
        return {
            "id": self.id,
            "height": self.height,
            "width": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """returning the string rep of the rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
