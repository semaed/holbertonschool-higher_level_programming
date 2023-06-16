#!/usr/bin/python3
"""
This module contains a unittest class for the function max_integer().
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    A unittest class for max_integer()
    """

    def test_basic(self):
        """
        Test normal cases for the function.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertRaises(TypeError, max_integer())


if __name__ == '__main__':
    unittest.main()
