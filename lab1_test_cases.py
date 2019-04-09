import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Testing for a ValueError with a None list."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
            max_list_iter(None)
        """Testing for list length of 0."""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
        """Testing for a sorted list."""
        tlist = [1, 3, 4, 5, 7]
        self.assertEqual(max_list_iter(tlist), 7)
        """Testing for an unsorted list."""
        tlist = [10, 4, 7]
        self.assertEqual(max_list_iter(tlist), 10)
        """Testing for a list with duplicates."""
        tlist = [1, 4, 4, 4]
        self.assertEqual(max_list_iter(tlist), 4)

    def test_reverse_rec(self):
        """"Testing an ordered list."""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        """"Testing when the list has duplicates."""
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])
        """Testing a list with one value."""
        self.assertEqual(reverse_rec([1]), [1])
        """Testing a empty list"""
        self.assertEqual(reverse_rec([]), [])
        """Testing for a ValueError with a None list."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        """Testing a sorted simple list, val is middle of list."""
        list_val =[0, 1, 2, 3, 4, 7, 8, 9, 10]
        low = 0
        high = len(list_val) - 1
        self.assertEqual(bin_search(4, 0, len(list_val) - 1, list_val), 4)
        """Val is first in list."""
        self.assertEqual(bin_search(0, 0, len(list_val) - 1, list_val), 0)
        """Val is last in list."""
        self.assertEqual(bin_search(10, 0, len(list_val) - 1, list_val), 8)
        """Val is in top half of list."""
        self.assertEqual(bin_search(8, 0, len(list_val) - 1, list_val), 6)
        """Val is in bottom half of list."""
        self.assertEqual(bin_search(1, 0, len(list_val) - 1, list_val), 1)
        """Testing for a ValueError with a None list."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 0, 0, tlist)


if __name__ == "__main__":
    unittest.main()

