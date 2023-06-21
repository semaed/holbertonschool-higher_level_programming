#!/usr/bin/python3
"""
This module contains a function that
creates an object from a JSON file.
"""
import json


def load_from_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)
