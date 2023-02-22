"""

https://www.codewars.com/kata/541c8630095125aba6000c00

"""
import unittest


class DigitalRootTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(digital_root(16), 7)
        self.assertEqual(digital_root(942), 6)
        self.assertEqual(digital_root(132189), 6)
        self.assertEqual(digital_root(493193), 2)


def digital_root(n):
    result = 0
    while n > 0:
        result += n % 10
        n //= 10

    if result >= 10:
        return digital_root(result)

    return result



if __name__ == "__main__":
    unittest.main()
