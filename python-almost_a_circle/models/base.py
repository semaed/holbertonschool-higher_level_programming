#!/usr/bin/python3
"""
This module contains the Base class.
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialize Base instance

        Args:
            id (int, optional): id to assign to
             the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries (list): list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            for obj in list_objs:
                list_dicts.append(cls.to_dictionary(obj))
        with open(filename, 'w') as file:
            file.write(cls.to_json_string(list_dicts))
