#!/usr/bin/python3


"""Definition of a student class."""


class Student:
    """is a representation of a student."""

    def __init__(self, first_name, last_name, age):
        """a student is now initialized

        Arguements:
            age: is the age of the student
            last_name: is the last name of student
            first_name: is thefirst name of student.
        """
        self.age = age  # public instance
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ is a dictionary description of a student is done

        Arguements:
            attrs(list): attributes to be represented
        """
        if (type(attrs) == list and
                all(type(att) == str for att in attrs)):
            return {p: getattr(self, p) for p in attrs if hasattr(self, p)}

        return (self.__dict__)

    def reload_from_json(self, json):
        """the attributes of new student are replaced

        Arguements:
            json(dict): what to replace attributes with in form
            of dictionary
        """

        for p, x in json.items():
            setattr(self, p, x)
