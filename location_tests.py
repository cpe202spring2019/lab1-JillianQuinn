import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        other = Location("SLO", 35.3, -120.7)
        self.assertEqual(loc, other)

        loc = Location("SLO",  35.3, -120.7)
        other = loc
        self.assertEqual(loc, other)


if __name__ == "__main__":
        unittest.main()
