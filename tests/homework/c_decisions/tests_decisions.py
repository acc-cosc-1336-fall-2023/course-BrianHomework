#

import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):


    def test_get_options_ratio(self):

    # Test case 1: option is 50 and total is 100
        self.assertEqual(get_options_ratio(5, 20), 0.25)

    # Test case 2: option is 75 and total is 100
        self.assertEqual(get_options_ratio(10, 20), 0.5)


    def test_get_faculty_rating(self):
    # Test case 1: ratio is 0.95
        self.assertEqual(get_faculty_rating(.90), "Excellent")

    # Test case 2: ratio is 0.85
        self.assertEqual(get_faculty_rating(0.85), "Very Good")

    # Test case 3: ratio is 0.75
        self.assertEqual(get_faculty_rating(0.75), "Good")

    # Test case 4: ratio is 0.65
        self.assertEqual(get_faculty_rating(0.65), "Needs Improvement")

    # Test case 5: ratio is 0.55
        self.assertEqual(get_faculty_rating(0.55), "Unacceptable")

    # Test case 7: ratio is 0 (edge case)
        self.assertEqual(get_faculty_rating(0), "Unacceptable")
