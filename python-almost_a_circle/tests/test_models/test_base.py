#!/usr/bin/python3
""" Module for test Base class """
import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):

    # ... other tests ...

    def test_to_json_string(self):
        """Test to_json_string method"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b1_dict = b1.to_dictionary()
        json_dict = Base.to_json_string([b1_dict])
        self.assertEqual(json_dict, json.dumps([b1_dict]))
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        """Test from_json_string method"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b1_dict = b1.to_dictionary()
        json_dict = Base.to_json_string([b1_dict])
        list_dicts = Base.from_json_string(json_dict)
        self.assertEqual(list_dicts, [b1_dict])
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string("[]"), [])
