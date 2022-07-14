import unittest

from my_sum import sum

class TestSum(unittest.TestCase):

    def test_sum_int(self):
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_sum_float(self):
        data = [2.2, 1.2, 3.1]
        result = sum(data)
        self.assertEqual(result, 6.5)
        self.assertEqual(sum([2.2, 2.2, 2.2]), 6.6)

    def test_sum_string(self):
        self.assertRaises(ValueError, sum, [1, 2, 'a'])



if __name__ == '__main__':
    unittest.main()