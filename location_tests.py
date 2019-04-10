import unittest
from location import *


class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        """Test the string representation format"""
        self.assertEqual(repr(loc), "Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc = Location("SLO", 35.3, -120.7)
        other = Location("SLO", 35.3, -120.7)
        """Test the equal function for different locations, same values"""
        self.assertEqual(loc, other)

        loc = Location("SLO",  35.3, -120.7)
        other = loc
        """Test the equal function for same location"""
        self.assertEqual(loc, other)
    
    def test_init(self):
        loc = Location("SLO",  35.3, -120.7)
        """Test the name"""
        self.assertEqual(loc.name, "SLO")
        """Test the lat."""
        self.assertEqual(loc.lat, 35.3)
        """Test the lon."""
        self.assertEqual(loc.long, -120.7)


if __name__ == "__main__":
        unittest.main()
