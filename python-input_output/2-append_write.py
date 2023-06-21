#!/usr/bin/python3
"""
This module contains a function that
appends a strint to the end of a
text file (UTF8) and returns the
number of caracters added.
"""


def append_write(filename="", text=""):
    """
    Function that append a strin into (UTF8)
    and returns number or characters
    added.
    """
    with open(filename, 'a') as f:
        return f.write(text)
