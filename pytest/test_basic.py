import unittest
import pytest

def add(a,b):
    return a+b

class TestMathOperations(unittest.TestCase):
    def test_add_two_positive_nubers(self):
        self.assertEqual(add(2,5),7)

    def test_add_two_negative_numbers(self):
        self.assertEqual(add(-2,-5),-7)