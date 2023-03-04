""""

https://www.codewars.com/kata/55983863da40caa2c900004e

"""
import unittest


class NextBiggerTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(next_bigger(  21),   -1)
        self.assertEqual(next_bigger(  12),   21)
        self.assertEqual(next_bigger( 513),  531)
        self.assertEqual(next_bigger(2017), 2071)
        self.assertEqual(next_bigger( 414),  441)
        self.assertEqual(next_bigger( 144),  414)


def next_bigger(n):
    s = str(n)
    if len(s) <= 1:
        return -1

    i = 1
    for i in range(len(s) - 1, 0, -1):
        if int(s[i]) > int(s[i - 1]):
            break

    if i == 1 and int(s[i]) <= int(s[i - 1]):
        return -1

    x = int(s[i - 1])
    smallest = i
    for j in range(i+1, len(s)):
        if x < int(s[j]) < int(s[smallest]):
            smallest = j

    s = list(s)
    s[smallest], s[i-1] = s[i-1], s[smallest]
    s = "".join(s)

    x = 0
    for j in range(i):
        x = x * 10 + int(s[j])

    s = "".join(sorted(list(s[i:]), key=lambda c: int(c)))

    for j in range(len(s)):
        x = x * 10 + int(s[j])

    return x


if __name__ == "__main__":
    unittest.main()
