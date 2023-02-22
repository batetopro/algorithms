"""

https://www.codewars.com/kata/5526fc09a1bbd946250002dc

"""
import unittest


class FindOutlierTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(find_outlier([2, 4, 6, 8, 10, 3]), 3)
        self.assertEqual(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
        self.assertEqual(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)


def find_outlier(integers):
    even = set()
    odd = set()

    for num in integers:
        if num % 2 == 0:
            even.add(num)
        else:
            odd.add(num)

    if len(odd) == 1:
        return odd.pop()
    else:
        return even.pop()

if __name__ == "__main__":
    unittest.main()
