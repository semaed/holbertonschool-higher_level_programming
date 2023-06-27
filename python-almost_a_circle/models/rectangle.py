#!/usr/bin/python3
"""
This module contains the Base class.
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialize Rectangle instance

        Args:
            width (int): width of the Rectangle
            height (int): height of the Rectangle
            x (int, optional): x of the Rectangle. Defaults to 0.
            y (int, optional): y of the Rectangle. Defaults to 0.
            id (int, optional): id of the Rectangle. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for width

        Args:
            value (int): value to set width to
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for height

        Args:
            value (int): value to set height to
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for x

        Args:
            value (int): value to set x to
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for y

        Args:
            value (int): value to set y to
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Method to calculate area of the Rectangle

        Returns:
            int: Area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Method to print the Rectangle using '#' character
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            for j in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """
        Method to print the string representation of the Rectangle
        """
        id_str = str(self.id)
        x_str = str(self.__x)
        y_str = str(self.__y)
        width_str = str(self.__width)
        height_str = str(self.__height)

        rectangle_str = "[Rectangle] (" + id_str + ") " + x_str + \
            "/" + y_str + " - " + width_str + "/" + height_str
        return rectangle_str

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute

        Args:
            *args (ints): values to assign to id, width, height, x, y (in that
              order) **kwargs: dictionary of attributes and their values
              to assign
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for attr, value in zip(attributes, args):
                setattr(self, attr, value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Method to return the dictionary representation of a Rectangle
        """
        return {'id': self.id, 'width': self.__width, 'height': self.__height,
                'x': self.__x, 'y': self.__y}
