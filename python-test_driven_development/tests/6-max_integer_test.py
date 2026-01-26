#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for max_integer"""

    def test_module_docstring(self):
        """Test module docstring"""
        m = __import__('6-max_integer').__doc__
        self.assertTrue(len(m) > 1)

    def test_function_docstring(self):
        """Test function docstring"""
        f = max_integer.__doc__
        self.assertTrue(len(f) > 1)

    def test_positive_integers(self):
        """Test with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_negative_integers(self):
        """Test with negative integers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_integers(self):
        """Test with mixed integers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)

    def test_empty_list(self):
        """Test with empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test with one element"""
        self.assertEqual(max_integer([5]), 5)

if __name__ == '__main__':
    unittest.main()