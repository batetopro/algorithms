""""

https://www.codewars.com/kata/593ff8b39e1cc4bae9000070

"""
import unittest


class LCSTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(lcs("", ""), "")
        self.assertEqual(lcs("abc", ""), "")
        self.assertEqual(lcs("", "abc"), "")
        self.assertEqual(lcs("a", "b"), "")
        self.assertEqual(lcs("a", "a"), "a")
        self.assertEqual(lcs("abc", "a"), "a")
        self.assertEqual(lcs("abc", "ac"), "ac")
        self.assertEqual(lcs("abcdef", "abc"), "abc")
        self.assertEqual(lcs("abcdef", "acf"), "acf")
        self.assertEqual(lcs("anothertest", "notatest"), "nottest")
        self.assertEqual(lcs("132535365", "123456789"), "12356")
        self.assertEqual(lcs("nothardlythefinaltest", "zzzfinallyzzz"), "final")
        self.assertEqual(lcs("abcdefghijklmnopq", "apcdefghijklmnobq"), "acdefghijklmnoq")


def backtrack(dp, x, y, i, j):
    if i == 0 or j == 0:
        return ""
    if x[i - 1] == y[j - 1]:
        return backtrack(dp, x, y, i - 1, j - 1) + x[i - 1]
    if dp[i][j - 1] > dp[i -1][j]:
        return backtrack(dp, x, y, i, j - 1)
    return backtrack(dp, x, y, i - 1, j)

def lcs(x, y):
    if not x or not y:
        return ""

    m = len(x)
    n = len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    return backtrack(dp, x, y, m, n)

if __name__ == "__main__":
    unittest.main()
