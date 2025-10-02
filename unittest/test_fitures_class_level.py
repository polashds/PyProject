#test fixtures is a step carried out before or after a test.
# The setUpModule() function runs before all test methods in the test module.
# The tearDownModule() function runs after all methods in the test module

import unittest

class setUpModule():
    print('running setUpModule')

class tearDownModule():
    print('running tearDownModule')


class TestMyModule(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('running setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('running tearDownClass')

    def test_case_1(self):
        self.assertEqual(5+5, 10)

        def test_case_2(self):
            self.assertEqual(1+1,2)

# python -m unittest -v