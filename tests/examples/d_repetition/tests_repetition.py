import unittest

from src.examples.d_repetition.repetition import for_sum_of_squares, get_sum_for, sum_of_squares, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_sum_of_squares(self):
        self.assertEqual(sum_of_squares(-1), 0)
        self.assertEqual(sum_of_squares(3), 14)
        self.assertEqual(sum_of_squares(4), 30)
        self.assertEqual(sum_of_squares(5), 55)

    def test_for_sum_of_squares(self):
        self.assertEqual(for_sum_of_squares(3), 14)
        self.assertEqual(for_sum_of_squares(4), 30)
        self.assertEqual(for_sum_of_squares(5), 55)
        
    def test_get_sum_for(self):
        self.assertEqual(get_sum_for(3), 6)
        self.assertEqual(get_sum_for(4), 10)
        self.assertEqual(get_sum_for(5), 15)
'''
    def test_get_sum_while(self):
        self.assertEqual(get_sum_for(3), 6)

    def tes_get_sum_for(self):
        self.assertEqual(get_sum_for(3), 6)
        self.assertEqual(get_sum_for(4), 15)
'''