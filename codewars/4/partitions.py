""""

https://www.codewars.com/kata/546d5028ddbcbd4b8d001254

"""
import unittest


class PartitionsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(partitions(1), 1)
        self.assertEqual(partitions(5), 7)
        self.assertEqual(partitions(10), 42)
        self.assertEqual(partitions(25), 1958)


def partitions(n):
    dp = [0] * (n + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]

    return dp[-1]


if __name__ == "__main__":
    unittest.main()