import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)


    def test_length_with_wrong_type(self):
        with self.assertRaises(TypeError):
            square = Square("10")

#Running tests without calling unittest.main()
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#python -m unittest , -m stands for module
# for more info
# python -m unittest -v


