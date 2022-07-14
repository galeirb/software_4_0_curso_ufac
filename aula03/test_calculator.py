import unittest

from my_sum import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator()
        result = calc.add(2, 2)
        expected = 4
        self.assertEqual(result, expected)

    def test_sub(self):
        calc = Calculator()
        result = calc.sub(2, 2)
        expected = 0
        self.assertEqual(result, expected)

    def test_mult(self):
        calc = Calculator()
        self.assertEqual(calc.mult(2, 2), 4)

    def test_div(self):
        calc = Calculator()
        self.assertEqual(calc.div(2, 2), 1)
        self.assertRaises(ZeroDivisionError, calc.div, 2, 0)

    def test_value(self):
        calc = Calculator()
        self.assertEqual(calc.add('2', '2'), 4)
        self.assertRaises(ValueError, calc.add, '2', 'a')


if __name__ == '__main__':
    unittest.main()