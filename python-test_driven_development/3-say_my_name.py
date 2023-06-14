#!/usr/bin/python3
"""
This module contains a function that prints a full name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints a string with a first name and a last name.
      Args:
        first_name: The first name to print. Must be a string.
        last_name: The last name to print. Must be a string. Defaults to an
        empty string.
    Raises:
        TypeError: If either first_name or last_name are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
