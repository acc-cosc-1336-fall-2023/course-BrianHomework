import unittest

from src.examples.h_strings.strings import concat_strings, search_in_string, slice_string, slice_w_step_value, test_config

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

    def test_concat_strings(self):
        self.assertEqual(concat_strings("abc", "def"), "abcdef")
        self.assertEqual("abc"+"def", "abcdef")

    def test_slice_string(self):
        self.assertEqual(slice_string("Patty Lynn Smith"), "Lynn")

    def test_slice_string(self):
        name = "Patty Lynn Smith"
        self.assertEqual(slice_string(name), "Lynn")
        self.assertEqual(name[11:], "Smith")

    def test_slice_step_value(self):
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.assertEqual(slice_w_step_value(letters), "ACEGIKMOQSUWY")

    def test_compare_strings(self):
        #Python cmpare ASCII numerical values in string comparisons
        str1 = "c" #ASCII 99
        str2 = "p" #ASCII 112

        self.assertEqual(str1 < str2, True)
        self.assertEqual(str2 < str1, False)
        self.assertEqual('c++' == "C++", False)
        #self.assertEqual('C++' == "C++", False) #This one will produce a Failed test since we say False when is True
    
    def test_search_in_string(self):
        str1 = "abc"
        str2 = "abcdef"

        self.assertEqual(search_in_string(str1, str2), True)
        self.assertEqual(search_in_string("efg", str2), False)

