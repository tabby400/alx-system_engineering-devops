#!/usr/bin/python3

"""this is a definition of a square class"""
from models.rectangle import Rectangle  # import class Rectangle


class Square(Rectangle):
    """involves an idea or representation of a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """a square is initialized.
        Arguement:
            size(int): size of the square initialized
            y(int): y coordinate of square.
            x(int): x coordinate of square
            id(int): id of the initialized square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieving the size of the square."""
        return (self.width)

    @size.setter
    def size(self, value):
        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """Updating the square initialized
        Arguement:
            *args(ints): the attributes of the square
                - argument one shows the id attribute
                - arguement two shows the size attribute
                - arguement three shows the x attribute
                - arguement four shows the y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            q = 0
            for arg in args:
                if q == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif l == 1:
                    self.size = arg
                elif l == 2:
                    self.x = arg
                elif l == 3:
                    self.y = arg
                l = l + 1

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """bringing back the dictionary representation of the square
        that was initialized."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returning the string rep of the initialized square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
