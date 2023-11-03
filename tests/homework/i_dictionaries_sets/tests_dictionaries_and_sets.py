#

#sets
baseball = set(['Jodi', 'Carmen', 'Aida', 'Alicia'])
basketball = set(['Eva', 'Carmen', 'Alicia', 'Sarah'])

#Finding the intersection of the sets
intersection = baseball.intersection(basketball)
print("Students who play both sports:", intersection)  

#Finding the union of the sets
union = baseball.union(basketball)
print("Students who play either sport:", union)  

#Finding the difference of baseball and basketball sets
difference_baseball = baseball.difference(basketball)
print("Students who play baseball but not basketball:", difference_baseball)  

#Finding the difference of basketball and baseball sets
difference_basketball = basketball.difference(baseball)
print("Students who play basketball but not baseball:", difference_basketball)  
#Finding the difference of baseball and basketball sets (baseball - basketball)
difference_baseball = baseball.difference(basketball)
print("Students who play baseball but not basketball:", difference_baseball)

#Finding the symmetric difference of the sets
symmetric_difference = baseball.symmetric_difference(basketball)
print("Students who play one sport but not both:", symmetric_difference)






















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