#!/usr/bin/python3

"""Defining a class student by names and age."""


class Student:
    """is a representation of a student."""

    def __init__(self, first_name, last_name, age):
        """a new student is now initialized.

        Arguements:
            age: age of student
            last_name : student last name
            first_name : student first name
        """

        self.age = age  # public instance
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """a dictionary description of the student is achieved"""
        return (self.__dict__)
