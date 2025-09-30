'''
a step carried out before or after a test
* setUpModule() function runs before all test methods in the test module.
* tearDownModule() function runs after all methods in the test module.
'''

import unittest

def setUpModule():
    print('running setUpModule')

def tearDownModule():
    print('running tearDownModule')

class TestMyModule(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(5+5, 10)

    def test_case_2(self):
        self.assertEqual(1+1, 2)