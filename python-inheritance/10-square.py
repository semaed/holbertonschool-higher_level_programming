#!/usr/bin/python3
"""Module that contains a class BaseGeometry,
a class Rectangle, and a class Square"""


class BaseGeometry:
    """A class with public instance methods area
    and integer_validator"""

    def area(self):
        """Method that raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method that validates value"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """A class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Initialization method for Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """Method that returns the rectangle description"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """A class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Initialization method for Square"""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Method that returns the square description"""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                       self._Rectangle__height)
