import unittest

from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

# First, remove the if block that calls the unittest.main() function:
# Second, execute the following command to run the test:
# python -m unittest

'''
This command discovers all the test classes whose names start with Test* 
located in the test_* file and execute the test methods that start with test*. 
the -m option stands for the module.
'''

'''
To display more information, you can add -v option to the above command. 
v stands for verbosity. It’s like calling the unittest.main() with 
verbosity argument with value 2.
'''

# python -m unittest -v