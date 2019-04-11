import unittest
from lab1 import *


class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Testing for a ValueError with a None list."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        """Testing for list length of 0."""
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)
        """Testing for a sorted list."""
        tlist = [1, 3, 4, 5, 7]
        self.assertEqual(max_list_iter(tlist), 7)
        """Testing for an unsorted list."""
        tlist = [10, 4, 7]
        self.assertEqual(max_list_iter(tlist), 10)
        """Testing for an unsorted list."""
        tlist = [10, 14, 7]
        self.assertEqual(max_list_iter(tlist), 14)
        """Testing for a list with duplicates."""
        tlist = [1, 4, 4, 4]
        self.assertEqual(max_list_iter(tlist), 4)
        """Testing with decimals."""
        tlist = [1.4, 7.2, 9.5]
        self.assertAlmostEqual(max_list_iter(tlist), 9.5)
        """Testing with decimals."""
        tlist = [10.4, 7.2, 9.5]
        self.assertAlmostEqual(max_list_iter(tlist), 10.4)
        """Testing with decimals."""
        tlist = [1.4, 17.2, 9.5]
        self.assertAlmostEqual(max_list_iter(tlist), 17.2)
        """Testing with one number list."""
        tlist = [1]
        self.assertEqual(max_list_iter(tlist), 1)
        """Testing with negatives."""
        tlist = [-1, -3, -4]
        self.assertEqual(max_list_iter(tlist), -1)
        """Testing with negatives."""
        tlist = [-11, -3, -14]
        self.assertEqual(max_list_iter(tlist), -3)
        """Testing with negatives."""
        tlist = [-11, -13, -4]
        self.assertEqual(max_list_iter(tlist), -4)

    def test_reverse_rec(self):
        """"Testing an ordered positive list."""
        self.assertEqual(reverse_rec([1, 2, 3]), [3, 2, 1])
        """"Testing an ordered negative list."""
        self.assertEqual(reverse_rec([-1, -2, -3]), [-3, -2, -1])
        """"Testing an ordered decimal list."""
        self.assertAlmostEqual(reverse_rec([1.5, 2.1, 3.8]), [3.8, 2.1, 1.5])
        """"Testing one negative list."""
        self.assertEqual(reverse_rec([1, 2, -3]), [-3, 2, 1])
        """"Testing when the list has duplicates."""
        self.assertEqual(reverse_rec([3, 3, 3]), [3, 3, 3])
        """Testing a list with one value."""
        self.assertEqual(reverse_rec([1]), [1])
        """Testing a list with one negative value."""
        self.assertEqual(reverse_rec([-1]), [-1])
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
        """Check empty list."""
        self.assertEqual(bin_search(1, 0, 0, []), None)
        """Check decimal list first value."""
        self.assertAlmostEqual(bin_search(1.2, 0, 3, [1.2, 1.3, 1.4, 1.5]), 0)
        """Check decimal list last value."""
        self.assertAlmostEqual(bin_search(1.5, 0, 3, [1.2, 1.3, 1.4, 1.5]), 3)
        """Check decimal list middle value."""
        self.assertAlmostEqual(bin_search(1.3, 0, 3, [1.2, 1.3, 1.4, 1.5]), 1)
        """Check decimal list middle value."""
        self.assertAlmostEqual(bin_search(1.4, 0, 3, [1.2, 1.3, 1.4, 1.5]), 2)
        """Check if not in list."""
        self.assertEqual(bin_search(12, 0, 3, [1, 2, 3, 4]), None)
        """Check negative list."""
        self.assertEqual(bin_search(-2, 0, 3, [-2, -1, 0, 1, 2]), 0)
        """Testing for a ValueError with a None list."""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(1, 0, 0, tlist)
        """Checking when the high and low value does not include the value"""
        self.assertEqual(bin_search(1, 1, 3, [1, 2, 3, 4]), None)
        """Checking when the high and low value does not include the value"""
        self.assertEqual(bin_search(4, 0, 2, [1, 2, 3, 4]), None)
        """Checking shortened list parameters"""
        self.assertEqual(bin_search(3, 0, 2, [1, 2, 3, 4]), 2)
        """Checking shortened list parameters"""
        self.assertEqual(bin_search(3, 1, 3, [1, 2, 3, 4]), 2)


if __name__ == "__main__":
    unittest.main()

