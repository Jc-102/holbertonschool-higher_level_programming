#!/usr/bin/python3
"""Unittests for max_integer([..])."""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Max of a list in ascending order."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Max of a list in random order."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Max is the first element."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_max_in_middle(self):
        """Max is in the middle of the list."""
        self.assertEqual(max_integer([1, 2, 9, 3, 4]), 9)

    def test_empty_list(self):
        """An empty list returns None."""
        self.assertIsNone(max_integer([]))

    def test_no_argument(self):
        """No argument uses the default empty list and returns None."""
        self.assertIsNone(max_integer())

    def test_one_element(self):
        """A list with one element returns that element."""
        self.assertEqual(max_integer([7]), 7)

    def test_all_negative(self):
        """Max of a list of negative numbers."""
        self.assertEqual(max_integer([-4, -2, -9, -1]), -1)

    def test_mixed_signs(self):
        """Max of a list with negative and positive numbers."""
        self.assertEqual(max_integer([-5, 0, 5, -10]), 5)

    def test_duplicates(self):
        """Max when the biggest value appears more than once."""
        self.assertEqual(max_integer([3, 7, 7, 1]), 7)

    def test_all_same(self):
        """Max of a list where every element is the same."""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        """Max of a list of floats."""
        self.assertEqual(max_integer([1.5, 3.7, 2.2]), 3.7)

    def test_ints_and_floats(self):
        """Max of a list mixing integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 2]), 2.5)

    def test_big_numbers(self):
        """Max with very large integers."""
        self.assertEqual(max_integer([10 ** 20, 10 ** 21, 5]), 10 ** 21)

    def test_string(self):
        """A string returns its highest character."""
        self.assertEqual(max_integer("Holberton"), "t")

    def test_list_of_strings(self):
        """A list of strings returns the alphabetically biggest one."""
        self.assertEqual(max_integer(["a", "c", "b"]), "c")

    def test_empty_string(self):
        """An empty string returns None."""
        self.assertIsNone(max_integer(""))

    def test_mixed_types(self):
        """Comparing numbers and strings raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])

    def test_none(self):
        """None is not a list and raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_integer_argument(self):
        """An integer is not a list and raises a TypeError."""
        with self.assertRaises(TypeError):
            max_integer(5)


if __name__ == '__main__':
    unittest.main()
