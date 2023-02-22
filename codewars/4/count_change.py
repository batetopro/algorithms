"""

https://www.codewars.com/kata/541af676b589989aed0009e7

"""
import unittest


class CountChangeTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_change(4, [1, 2]), 3)
        self.assertEqual(count_change(10, [5, 2, 3]), 4)
        self.assertEqual(count_change(11, [5, 7]), 0)


def count_change(money, coins):
    if money < 0:
        return 0

    if not coins:
        return 0

    dp = [0] * (money + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, money + 1):
            dp[i] += dp[i - coin]

    return dp[-1]


if __name__ == "__main__":
    unittest.main()