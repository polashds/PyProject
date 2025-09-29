import unittest
from square import Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        square = Square(10)
        area = square.area()
        self.assertEqual(area, 100)

#Running tests without calling unittest.main()
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
#python -m unittest , -m stands for module
# for more info
# python -m unittest -v