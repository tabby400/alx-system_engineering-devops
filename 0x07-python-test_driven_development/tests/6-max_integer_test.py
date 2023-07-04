#!/usr/bin/python3

# 6-max_integer_test.py
"""Using unittests for the function def max_integer(list=[]):"""

import unittest
max_int = __import__('6-max_integer').max_integer


class maxinttest(unittest.TestCase):
    """function uses unnitest for max integer."""

    def test_ordered_list(self):
        """Testing an ordered int list."""
        order = [1, 2, 3, 4, 5]
        self.assertEqual(max_int(order),5)

    def test_unordered_list(self):
        """Testing of not ordered list"""
        unorder = [1, 2, 4, 3, 5]
        self.assertEqual(max_int(unorder), 5)

    def test_empty_list(self):
        """empty list test."""
        empt = []
        self.assertEqual(max_int(empt), None)
    
    def test_max_at_begginning(self):
        """Starting with maximum int test."""
        max_start = [5, 4, 3, 2, 1]
        self.assertEqual(max_int(max_start), 5)

    def test_one_element_list(self):
        """testing with one  element."""
        single = [5]
        self.assertEqual(max_int(single), 5)

    def test_floats(self):
        """a float list test."""
        flot = [4.3, -7.23, 6.546, 12.1, 2.0]
        self.assertEqual(max_int(flot), 12.1)

    def test_ints_and_floats(self):
        """integer and float list."""
        flot_ints = [4.78, 5.5, 9, 21, -6]
        self.assertEqual(max_int(flot_ints), 21)

    def test_string(self):
        """string test."""
        strings = "Korean"
        self.assertEqual(max_int(strings), 'r')

    def test_empty_string(self):
        """empty str."""
        self.assertEqual(max_int(""), None)
    
    def test_list_of_strings(self):
        """list of strings test."""
        liststr = ["Wait", "for", "my", "sister"]
        self.assertEqual(max_int(liststr), "sister")


if __name__ == '__main__':
    unittest.main()
