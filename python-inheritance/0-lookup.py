#!/usr/bin/python3
""" Module to lookup attributes and methods of an object"""


def lookup(obj):
    """Returns the list of available attributes and methods of an object
    Args:
        obj (any): the object to inspect
    Returns:
        list: a list of strings containing the names of the available
              attributes and methods of the object
    """
    return dir(obj)
