#!/usr/bin/python3
"""
This is the test file for the module max_integer.
"""

import unittest
from max_integer import max_integer  # replace 'max_integer' with your module name

class TestMaxInteger(unittest.TestCase):
    """
    Defines a class for testing the function max_integer.
    """
        def test_max_integer(self):
        """
        Tests for the function max_integer.
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([1]), 1)
        
        with self.assertRaises(TypeError):
            max_integer([1, 2, 'three', 4])
if __name__ == '__main__':
    unittest.main()