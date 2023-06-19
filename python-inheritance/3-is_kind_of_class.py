#!/usr/bin/python3
"""Module that checks if an object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class."""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of,
    or if the object is an instance of a class that inherited
    from, the specified class, otherwise False.
    Returns:
    True if obj is an instance of a_class or an instance
    of a subclass of a_class, otherwise False.
    """
    return isinstance(obj, a_class)
