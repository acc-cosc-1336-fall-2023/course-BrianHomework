#

#Test 3 rolls
import unittest

from src.homework.j_classes.class_a import Die

class TestDie(unittest.TestCase):
    def test_get_rolled_value(self):
        die = Die()
        for _ in range(3):
            die.roll()
            rolled_value = die.get_rolled_value()
            self.assertTrue(1 <= rolled_value <= 6, f"Invalid rolled value: {rolled_value}")