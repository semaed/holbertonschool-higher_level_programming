#!/usr/bin/python3
"""
This module contains a function that
return the JSON representation of
an object (string).
"""
import json


def to_json_string(my_obj):
    """
    Function that returns a JSON
     representation of an object
    """
    json_str = json.dumps(my_obj)
    return json_str
