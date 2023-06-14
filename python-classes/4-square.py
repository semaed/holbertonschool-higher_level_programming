#!/usr/bin/python3
"""
This module defines a class 'Square'.
"""


class Square:
    """
    A class that defines a square with a private instance attribute 'size',
    and methods for getting and setting the 'size' value, and for calculating
    the area of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of Square with 'size' as an attribute.
        """
        self.size = size

    @property
    def size(self):
        """
        Returns the value of the private instance attribute 'size'.
                """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the private instance attribute 'size'.
                """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
                """
        return self.size ** 2
