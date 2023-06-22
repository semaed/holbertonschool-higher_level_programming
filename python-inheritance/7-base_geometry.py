#!/usr/bin/python3
"""Module that contains a class BaseGeometry and a class Rectangle"""


class BaseGeometry:
    """A class with public instance methods area
    and integer_validator
    """

    def area(self):
        """Method that raises an Exception with a message"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method that validates value"""

        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
