import unittest
'''
has the test functions
''' 

#from tests.examples.c_decisions import tests_decisions
#from tests.homework.b_in_proc_out import tests_in_proc_out
##from tests.examples.a_example import tests_devprocess
#from tests.homework.c_decisions import tests_decisions
#from tests.examples.d_repetition import tests_repetition
#from tests.homework.d_repetition import tests_repetition
#from tests.homework.e_functions import tests_functions
#from tests.examples.h_strings import tests_strings
#from tests.homework.h_strings import tests_strings
#from tests.examples.h_strings import tests_strings
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)