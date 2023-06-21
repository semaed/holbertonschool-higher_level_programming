#!/usr/bin/python3
"""
This module contains a function that
return an object represented by a
JSON string.
"""
import json


def from_json_string(my_str):
    """
    Function that returns an object
    represented by a JSON string.
    """
    json_str = json.loads(my_str)
    return json_str
