import unittest

from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

'''
The length parameter should be either an int or float. 
If you pass the value that is not in these types, 
the Square constructor should raise a TypeError exception.
'''

#To test if the Square constructor raises the TypeError exception, 
# you use the assertRaises() method in a context manager like this:


import unittest

from square import Square


class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square('10')

    def test_lenth_with_zero_or_negative(self):
        self.assertRaise(ValueError)
        square = Square(0)
        square = Square(1)

# python -m unittest -v

'''
The test_length_with_wrong_type() method expected that the Square constructor
 raises a TypeError exception. However, it didn’t.

 To pass the test, you need to raise an exception if the type of the length property is not int or float in the Square constructor:

 #square.py
class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')

        self.length = length

    def area(self):
        return self.length * self.length
'''

# python -m unittest -v


'''
The following example adds a test that expects a ValueError exception
 if the length is zero or negative:
'''

    # def test_lenth_with_zero_or_negative(self):
    #     self.assertRaise(ValueError)
    #     square = Square(0)
    #     square = Square(1)

# python -m unittest -v

'''
To make the test pass, you add another check to the Square() constructor:

# square.py
class Square:
    def __init__(self, length) -> None:
        if type(length) not in [int, float]:
            raise TypeError('Length must be an integer or float')
        if length < 0:
            raise ValueError('Length must not be negative')

        self.length = length

    def area(self):
        return self.length * self.length

'''