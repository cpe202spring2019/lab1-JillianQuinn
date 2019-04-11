import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

        """Whole number check."""
        loc = Location('Mercer Island', 20, 19)
        self.assertEqual(repr(loc), "Location('Mercer Island', 20, 19)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        loc2 = Location("SLO", 35.3, -120.7)
        loc3 = loc
        loc4 = Location("Mercer Island", 20, 19)
        """Test same location."""
        self.assertEqual(loc, loc2)
        self.assertTrue(loc == loc2)
        """Test different locations."""
        self.assertFalse(loc == loc4)
        """Test same pointed location."""
        self.assertTrue(loc == loc3)
        """Test wrong type."""
        self.assertFalse(loc == "SLO")

    def test_init(self):
        loc = Location("SLO", 35.3, -120.7)
        """Test the name"""
        self.assertEqual(loc.name, "SLO")
        """Test the lat."""
        self.assertAlmostEqual(loc.lat, 35.3)
        """Test the lon."""
        self.assertAlmostEqual(loc.lon, -120.7)


if __name__ == "__main__":
    unittest.main()
