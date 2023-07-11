#!/usr/bin/python3


"""Definition of a student class."""


class Student:
    """is a representation of a student."""

    def __init__(self, first_name, last_name, age):
        """a student is now initialized

        Arguements:
            age: age of the student
            last_name: last name of student
            first_name: first name of student.
        """
        self.age = age  # public instance
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """a dictionary description of a student is done

        Arguements:
            attrs(list): attributes to be represented
        """
        if (type(attrs) == list and
                all(type(att) == str for att in attrs)):
            return {p: getattr(self, p) for p in attrs if hasattr(self, p)}

        return (self.__dict__)
