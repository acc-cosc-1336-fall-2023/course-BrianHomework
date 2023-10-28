#
import unittest

from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory = {}  # Initialize an empty inventory dictionary

        # Adding Widget1 with quantity of 10
        add_inventory(inventory, 'Widget1', 10)
        self.assertEqual(inventory['Widget1'], 10)

        # Updating the existing Widget1 with quantity of 25
        add_inventory(inventory, 'Widget1', 25)
        self.assertEqual(inventory['Widget1'], 35)

        # Updating the existing Widget1 with a negative quantity
        add_inventory(inventory, 'Widget1', -10)
        self.assertEqual(inventory['Widget1'], 25)

    def test_remove_inventory_widget(self):
        inventory = {}  # Initialize an empty inventory dictionary

        # Adding two widgets with quantities of your choice
        add_inventory(inventory, 'Widget1', 10)
        add_inventory(inventory, 'Widget2', 15)

        # Removing Widget1
        result = remove_inventory_widget(inventory, 'Widget1')
        self.assertEqual(result, 'Record deleted')
        self.assertEqual(len(inventory), 1)  # Length of dictionary should be 1
        self.assertIn('Widget2', inventory)  # Widget2 should still exist