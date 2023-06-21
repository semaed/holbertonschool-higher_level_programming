#!/usr/bin/python3
"""
This module contains a function 'read_file'
that reads a text file (UTF8) and prints
it to stdout.
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints
    it to stdout.
    Args:
        filename (str): The name of the file to read
        Defaults to "".
    """
    with open(filename, 'r') as f:
        for line in f:
            print(line, end="")
