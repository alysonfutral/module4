import unittest
from generators import fibonacci

class TestFibonacciGenerator(unittest.TestCase):
    def test_range_five(self):
        fibonacci_generator = fibonacci()
        # use next to find next element to test from generator
        range_five = [next(fibonacci_generator) for _ in range(5)]
        self.assertEqual(range_five, [1, 1, 2, 3, 5])

    def test_range_ten(self):
        fibonacci_generator = fibonacci()
        range_ten = [next(fibonacci_generator) for _ in range(10)]
        # use next to find next element to test from generator
        self.assertEqual(range_ten, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

    def test_range_15(self):
        fibonacci_generator = fibonacci()
        range_fifteen = [next(fibonacci_generator) for _ in range(15)]
        # use next to find next element to test from generator
        self.assertEqual(range_fifteen, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610])



if __name__ == '__main__':
    unittest.main()
