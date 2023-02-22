"""

https://www.codewars.com/kata/52597aa56021e91c93000cb0

"""
import unittest


class MoveZerosTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(move_zeros(
            [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
            [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
        self.assertEqual(move_zeros(
            [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(move_zeros([0, 0]), [0, 0])
        self.assertEqual(move_zeros([0]), [0])
        self.assertEqual(move_zeros([]), [])


def move_zeros(lst):
    zeros, nums = [], []

    for x in lst:
        if x == 0:
            zeros.append(x)
        else:
            nums.append(x)

    return nums + zeros


if __name__ == "__main__":
    unittest.main()
