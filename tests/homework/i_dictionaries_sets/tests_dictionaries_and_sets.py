#

import unittest

class TestSetOperations(unittest.TestCase):
    def setUp(self):
        self.baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
        self.basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

    def test_intersection(self):
        intersection_result = self.baseball.intersection(self.basketball)
        expected_intersection = {'Carmen', 'Alicia'}
        self.assertEquals(intersection_result, expected_intersection)

    def test_union(self):
        union_result = self.baseball.union(self.basketball)
        expected_union = {'Jodi', 'Carmen', 'Aida', 'Alicia', 'Eva', 'Sarah'}
        self.assertEquals(union_result, expected_union)

    def test_difference_baseball(self):
        difference_result = self.baseball.difference(self.basketball)
        expected_difference = {'Jodi', 'Aida'}
        self.assertEquals(difference_result, expected_difference)

    def test_difference_basketball(self):
        difference_result = self.basketball.difference(self.baseball)
        expected_difference = {'Eva', 'Sarah'}
        self.assertEquals(difference_result, expected_difference)

    def test_symmetric_difference(self):
        symmetric_difference_result = self.baseball.symmetric_difference(self.basketball)
        expected_symmetric_difference = {'Jodi', 'Eva', 'Aida', 'Sarah'}
        self.assertEquals(symmetric_difference_result, expected_symmetric_difference)






















'''''
import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}  # Initialize an empty inventory dictionary

        # Adding Widget1 with quantity of 10
        add_inventory(inventory, 'Widget1', 10)
        self.assertEqual(inventory['Widget1'], 10)

        # Update existing Widget1 with quantity of 25
        add_inventory(inventory, 'Widget1', 25)
        self.assertEqual(inventory['Widget1'], 35)

        # Update existing Widget1 with negative quantity
        add_inventory(inventory, 'Widget1', -10)
        self.assertEqual(inventory['Widget1'], 25)

    def test_remove_inventory_widget(self):
        inventory = {}  # Initialize an empty inventory dictionary

        # two widgets with quantities of your choice
        add_inventory(inventory, 'Widget1', 10)
        add_inventory(inventory, 'Widget2', 15)

        # Removing Widget1
        result = remove_inventory_widget(inventory, 'Widget1')
        self.assertEqual(result, 'Record deleted')
        self.assertEqual(len(inventory), 1)  # Length of dictionary should be 1
        self.assertIn('Widget2', inventory)  # Widget2 should still exist
'''        