##
import unittest

from src.homework.e_functions.value_return import get_hour
from src.homework.e_functions.value_return import get_minutes
from src.homework.e_functions.value_return import get_seconds


class Test_Config(unittest.TestCase):


    def test_get_hour_3800(self):
        self.assertEqual(get_hour(3800), 1)

    def test_get_hour_3600(self):
        self.assertEqual(get_hour(3600), 1)

    def test_get_minutes_3800(self):
        self.assertEqual(get_minutes(3800), 3)

    def test_get_minutes_3600(self):
        self.assertEqual(get_minutes(3600), 0)

    def test_get_seconds_3800(self):
        self.assertEqual(get_seconds(3800), 20)

    def test_get_seconds_3600(self):
        self.assertEqual(get_seconds(3600), 0)