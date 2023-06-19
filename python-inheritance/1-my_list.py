#!/usr/bin/python3
"""Module to define MyList class"""


class MyList(list):
    """MyList class that inherits from list
    """

    def print_sorted(self):
        """Prints the list in ascending sorted order.
        """
        print(sorted(self))
