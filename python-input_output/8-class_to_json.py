#!/usr/bin/python3
"""
This module contains a function that
returns a dictionay description with simple
data structure for JSOn serialization.
"""


def get_json_description(obj):
    """
    Returns a dictionary
     fo JSON serialization.
    """
    return obj.__dict__
