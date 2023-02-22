"""

https://www.codewars.com/kata/54ce4c6804fcc440a1000ecb/python

"""
import unittest


class BurrowsWheelerTransformationTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(encode("bananabar"), ("nnbbraaaa", 4))
        self.assertEqual(encode("Humble Bundle"), ("e emnllbduuHB", 2))
        self.assertEqual(encode("Mellow Yellow"), ("ww MYeelllloo", 1))
        self.assertEqual(decode("nnbbraaaa", 4), "bananabar")
        self.assertEqual(decode("e emnllbduuHB", 2), "Humble Bundle")
        self.assertEqual(decode("ww MYeelllloo", 1), "Mellow Yellow")


def encode(s):
    rows = []
    for k in range(len(s)):
        rows.append(s[len(s) - k:] + s[:len(s) - k])

    rows = sorted(rows)

    result = []
    idx = None
    for k, r in enumerate(rows):
        result += r[-1]
        if idx is None and r == s:
            idx = k

    return "".join(result), idx

def decode(s, n):
    if not s:
        return ""
    """
    table = [""] * len(s)
    for _ in range(len(s)):
        table = sorted([s[i] + table[i] for i in range(len(s))])
    return table[n]
    """
    def row(k):
        permutation = sorted([(t,i) for i, t in enumerate(s)])
        for _ in s:
            t, k = permutation[k]
            yield t
    return "".join(row(n))


if __name__ == "__main__":
    unittest.main()
