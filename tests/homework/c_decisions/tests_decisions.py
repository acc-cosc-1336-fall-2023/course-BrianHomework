#
import unittest

from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_get_options_ratio():

    # Test case 1: option is 50 and total is 100
        assert get_options_ratio(50, 100) == 0.5

    # Test case 2: option is 75 and total is 100
        assert get_options_ratio(75, 100) == 0.75

    # Test case 3: option is 0 and total is 100
        assert get_options_ratio(0, 100) == 0.0

    # Test case 4: option is 100 and total is 100
        assert get_options_ratio(100, 100) == 1.0

    # Test case 5: option is 25 and total is 50
        assert get_options_ratio(25, 50) == 0.5

    # Test case 6: option is 0 and total is 0 (edge case)
        assert get_options_ratio(0, 0) == 0.0

        print("All test cases passed")


    def test_get_faculty_rating():
    # Test case 1: ratio is 0.95
        assert get_faculty_rating(0.95) == "Excellent"

    # Test case 2: ratio is 0.85
        assert get_faculty_rating(0.85) == "Very good"

    # Test case 3: ratio is 0.75
        assert get_faculty_rating(0.75) == "Good"

    # Test case 4: ratio is 0.65
        assert get_faculty_rating(0.65) == "Needs improvement"

    # Test case 5: ratio is 0.55
        assert get_faculty_rating(0.55) == "Unacceptable"

    # Test case 6: ratio is 1 (edge case)
        assert get_faculty_rating(1) == "Excellent"

    # Test case 7: ratio is 0 (edge case)
        assert get_faculty_rating(0) == "Unacceptable"

        print("All test cases passed")