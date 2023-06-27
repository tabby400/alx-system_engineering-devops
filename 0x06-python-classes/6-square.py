#!/usr/bin/python3

"""class Square to define square."""


class Square:
    """shows its a square."""

    def __init__(self, size=0, position=(0, 0)):
        """square init

        Arguements:
            size(int):new square size
            position (int, int):new square pos
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """retrieve square size."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        elif value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """retrieve position of square."""
        return (self.__position)

    @position.setter
    def position(self, value):

        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(cord, int) for cord in value) or
                not all(cord >= 0 for cord in value)):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """returns  area of square."""
        return (self.__size ** 2)

    def my_print(self):
        """Printing  with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for p in range(0, self.__position[1])]
        for p in range(0, self.__size):
            [print(" ", end="") for x in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")
