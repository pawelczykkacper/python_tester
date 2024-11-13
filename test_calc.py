import unittest
from calc import addition, substraction, multiplication, division

class MyTestCase(unittest.TestCase):
    def test_addtition(self):
        self.assertEqual(addition(2,3),5)
        self.assertEqual(addition(-1, 1), 0)
        self.assertEqual(addition(-1, -1), -2)
    def test_substraction(self):
        self.assertEqual(substraction(10,5),5)
        self.assertEqual(substraction(0, 5), -5)
        self.assertEqual(substraction(-2, -8), 6)
    def test_multiplication(self):
        self.assertEqual(multiplication(3,4),12)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(0, 100), 0)
    def test_division(self):
        self.assertEqual(division(10, 2), 5)
        self.assertEqual(division(-10, 2 ), -5 )
        self.assertEqual(division(5, 2), 2.5)
    def test_exception(self):
        with self.assertRaises(ValueError):
            division(1, 0)

if __name__ == '__main__':
    unittest.main()

