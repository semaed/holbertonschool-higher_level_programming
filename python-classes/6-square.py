#!/usr/bin/python3
"""
This module defines a class 'Square'.
"""


class Square:
    """
    A class that defines a square with private instance attributes 'size' and
    'position', and methods for getting and setting the 'size' and 'position'
     values, calculating the area of the square, and printing the square to
     stdout.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new instance of Square with 'size' and 'position' as
         attributes.
        Args:
            size: The size of the square.
            position: The position of the square.
        """
        self.size = size
        self.position = position

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
        Args:
            value: The value to set for 'size'.
        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Returns the value of the private instance attribute 'position'.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the value of the private instance attribute 'position'.
        Args:
            value: The value to set for 'position'.
        Raises:
            TypeError: If 'value' is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Returns the current square area.
        """
        return self.size ** 2

    def my_print(self):
        """
        Prints the square using the character '#' to stdout.
        If 'size' is 0, prints an empty line.
        """
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
