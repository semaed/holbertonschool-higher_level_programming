import unittest
from models.base import Base
from os import path
import os


class TestBase(unittest.TestCase):
    def test_id_assignment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    def test_id_assignment_with_arg(self):
        b3 = Base(12)
        self.assertEqual(b3.id, 12)

    def test_to_json_string(self):
        dict = {'id': 12}
        json_dict = Base.to_json_string([dict])
        self.assertEqual(json_dict, '[{"id": 12}]')

    def test_to_json_string_none_or_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        json_str = '[{"id": 12}]'
        dict = Base.from_json_string(json_str)
        self.assertEqual(dict, [{'id': 12}])

    def test_from_json_string_none_or_empty(self):
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])

    def test_save_to_file(self):
        b1 = Base(1)
        Base.save_to_file([b1])
        self.assertTrue(path.isfile("Base.json"))

    def test_load_from_file(self):
        b1 = Base(1)
        Base.save_to_file([b1])
        objs = Base.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)

    def tearDown(self):
        try:
            os.remove("Base.json")
        except:
            pass
