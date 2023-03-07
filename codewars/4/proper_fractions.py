"""

https://www.codewars.com/kata/55b7bb74a0256d4467000070

"""
import unittest


class ProperFractionsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(proper_fractions(1), 0)
        self.assertEqual(proper_fractions(2), 1)
        self.assertEqual(proper_fractions(5), 4)
        self.assertEqual(proper_fractions(15), 8)
        self.assertEqual(proper_fractions(25), 20)


def is_prime(n):
    if n == 0 or n == 1:
        return False
    i = 2
    while i <= n ** 0.5:
        if n % i == 0:
            return False
        i += 1
    return True


def proper_fractions(n):
    if n == 1: return 0
    result = 1
    m = n
    l = int(n ** 0.5) + 1

    for i in range(1, l):
        if not is_prime(i): continue
        if m % i == 0:
            result *= i - 1
            m //= i
        while m % i == 0:
            result *= i
            m //= i

    if m > 1:
        result *= m - 1
    return result



if __name__ == "__main__":
    unittest.main()
