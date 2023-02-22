"""

https://www.codewars.com/kata/537529f42993de0e0b00181f

"""
import unittest


class AlphabetPositionTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_inversions([]), 0)
        self.assertEqual(count_inversions([1,2,3]), 0)
        self.assertEqual(count_inversions([2,1,3]), 1)
        self.assertEqual(count_inversions([6,5,4,3,2,1]), 15)
        self.assertEqual(count_inversions([6,5,4,3,3,3,3,2,1]), 30)


def count_inversions(array):
    counter = 0
    for i in range(len(array)-1):
        for j in range(i+1, len(array)):
            if array[i] > array[j]:
                counter += 1
    return counter


if __name__ == "__main__":
    unittest.main()
