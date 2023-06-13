#!/usr/bin/python3
"""
This module defines a class 'Square'.
"""


class Square:
    """
    A class that defines a square with a private instance attribute 'size'.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of Square with 'size' as an attribute.

        Args:
            size: The size of the new square instance. Defaults to 0.
                Raises:
                    TypeError: If 'size' is not an integer.
                    ValueError: If 'size' is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
