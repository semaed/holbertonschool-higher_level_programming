#!/usr/bin/python3
"""Module that contains a class BaseGeometry"""


class BaseGeometry:
    """A class with public instance methods area
    and integer_validator"""

    def area(self):
        """Method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if not isinstance(name, str):
            if type(value) is not int:
                raise TypeError("{} must be an integer".format(name))
            if value <= 0:
                raise ValueError("{} must be greater than 0".format(name))
