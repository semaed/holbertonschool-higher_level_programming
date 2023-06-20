#!/usr/bin/python3
"""Module that checks if an object is an instance
of a class that inherited (directly or indirectly)
from the specified class."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class, otherwise False.
    """
    return any(issubclass(base, a_class) for base in type(obj).__bases__)
