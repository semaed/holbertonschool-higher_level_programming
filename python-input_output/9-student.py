#!/usr/bin/python3
""" Module has define a student class """


class Student:
    """Define student class """

    def __init__(self, first_name, last_name, age):
        """ Instanses """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Retrives dictionary"""
        return self.__dict__
