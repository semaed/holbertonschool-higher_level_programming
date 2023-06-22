#!/usr/bin/python3
"""module for a class called Base Geometry with public instance methods
"""


class BaseGeometry:
    """class with exceptions
    """

    def area(self):
        """defines the area of the geometry

        Raises:
            Exception: error message for user
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """method that validates value"""

        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
