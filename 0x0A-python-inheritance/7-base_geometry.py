#!/usr/bin/python3
"""explains a function used to create a base geometry
class
"""


class BaseGeometry:
    """the class Baseeometry"""

    def area(self):
        """here an exeption is raised that area
        is not implemented
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """function used to validate value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:  # not negative
            raise ValueError("{} must be greater than 0".format(name))
