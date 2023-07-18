#!/usr/bin/python3

""" Definition of a base class of all of the other classes in
the project"""

import json
import csv


class Base:

    """ is a representation of a base object
    Attributes
    __nb_objects(int): this is the count of the instances
    of the base class
    """

    __nb_objects = 0

    def __init__(self, id=None):

        """a new base object is initialized.
        Arguement:
            id(int): the specific id of the base
            instanced
        """
        if id is not None:
            self.id = id  # the id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects  # incremented nb object

    @staticmethod
    def to_json_string(list_dictionaries):
        """is used to return the JSON string rep of
        list dictionaries.

        Arguements:
            list_dictionaries(list): is a list of dictionaries.
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)  # to JSON format

    @staticmethod
    def from_json_string(json_string):
        """Function used to return list of the JSON string
        representation
        Arguemnts:
            json_string: JSON string which is a list of dictionaries
        Returns:
            an empty list if JSON string is empty or None, otherwise
            returns thethe exact python list
        """

        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)  # to python list

    @classmethod
    def save_to_file(cls, list_objs):
        """function that is used to write to a file the JSON
        representation of list_objs.

        Arguements:
            list_objs(list): the list inhesrits instances
            of base
        """
        output_file = cls.__name__ + ".json"  # name of class gotten
        with open(output_file, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                dictionary_list = [x.to_dictionary() for x in list_objs]
                jsonfile.write(Base.to_json_string(dictionary_list))

    @classmethod
    def create(cls, **dictionary):
        """ function which returns an instance of all the attributes
        already set
        Arguements:
            **dictionary: attribute key values to be initialized
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                instance = cls(1, 1)
            else:
                instance = cls(1)
            instance.update(**dictionary)
            return (instance)

    @classmethod
    def load_from_file(cls):
        """function used to load data froma file which
        has JSON strings.

        Returns:
            an empty list if the file does not exist, otherwise
            bring back a list of instances
        """
        output_file = str(cls.__name__) + ".json"
        try:
            with open(output_file, "r") as json_f:
                dictionary_list = Base.from_json_string(json_f.read())
                return [cls.create(**x) for x in dictionary_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """saving the the csv serialized list of objects to a file.

        Arguements:
            list_objs(list): A list of inherited Base instances.
        """
        filenm = cls.__name__ + ".csv"  # in csv form
        with open(filenm, "w", newline="") as csvf:
            if list_objs is None or list_objs == []:
                csvf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attnames = ["id", "width", "height", "x", "y"]
                else:
                    attnames = ["id", "size", "x", "y"]
                csv_writer = csv.DictWriter(csvf, fieldnames=attnames)
                for obj in list_objs:
                    csv_writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """function used in returning a class list fro the
        csv file

        Returns:
            an empty list if file does not exist, otherwise;
            a list with classes instanced
        """
        filenm = cls.__name__ + ".csv"  # the name
        try:
            with open(filenm, "r", newline="") as csvf:
                if cls.__name__ == "Rectangle":
                    attnames = ["id", "width", "height", "x", "y"]
                else:
                    attnames = ["id", "size", "x", "y"]
                    list_dictionary = csv.DictReader(csvf, fieldnames=attnames)
                    list_dictionary = [
                            dict([k, int(val)] for k, val in d.items())
                            for d in list_dictionary
                    ]
                return [cls.create(**d) for d in list_dictionary]
        except IOError:
            return []
