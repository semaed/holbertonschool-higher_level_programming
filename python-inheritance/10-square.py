#!/usr/bin/python3
"""Module that contains a class BaseGeometry and a class Rectangle"""


class BaseGeometry:
    """A class with public instance methods area
    and integer_validator"""

    def area(self):
        """Method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if isinstance(name, str):
            if type(value) is not int:
                raise TypeError(f"{name} must be an integer")
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization method for Rectangle"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Method that returns the area of the square"""
        return self.__size ** 2
