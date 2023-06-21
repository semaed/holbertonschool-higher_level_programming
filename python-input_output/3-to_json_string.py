#!/usr/bin/python3
import json
"""
This module contains a function that
return the JSON representation of
an object (string).
"""


def to_json_string(my_obj):
    str = my_obj
    json_str = json.dumps(str)
    print(json_str)
