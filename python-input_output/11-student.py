#!/usr/bin/python3
""" Module has define a student class """


class Student:
    """Define student class """

    def __init__(self, first_name, last_name, age):
        """ Instanses """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Retrives dictionary"""
        if attrs is None:
            return self.__dict__
        else:
            dict_res = {}
            for item in attrs:
                if item in self.__dict__:
                    dict_res[item] = self.__dict__[item]
            return dict_res

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance"""
        for key, value in json.items():
            setattr(self, key, value)
