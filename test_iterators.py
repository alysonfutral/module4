import unittest

from iterators import OddIterator, Last


class TestOddIterator(unittest.TestCase):
    def test_odd_iterator(self):
        # Test with a list of integers
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_output = [1, 3, 5, 7, 9]
        odd_it = OddIterator(numbers)
        actual_output = list(odd_it) # return list containing values
        self.assertEqual(actual_output, expected_output)

        # Test with a range of integers
        expected_output = [1, 3, 5, 7, 9]
        odd_it_range = OddIterator(range(1, 11))
        actual_output = list(odd_it_range)

        self.assertEqual(actual_output, expected_output)

    def test_last(self):
        # Test Last with a list of integers
        last_iter = Last([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3)
        expected_output = [8, 9, 10]
        actual_output = next(last_iter) # get next value in order to get last elements
        self.assertEqual(actual_output, expected_output)

    def test_last_count_error(self):
        # check the possibilities of count being larger than range
        last_iter = Last([1, 2, 3], 10)
        expected_output = [1, 2, 3]
        actual_output = next(last_iter)
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()
