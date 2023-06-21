#!/usr/bin/python3
"""This module contains a function 'write_file'
that write a string to (UTF8) and return the
number of characters written."""


def write_file(filename="", text=""):
    """
    Function that writes a strin into (UTF8)
    and returns number or characters
    written
    it to stdout.
    """
    with open(filename, 'w') as f:
        return f.write(text)
