"""

https://www.codewars.com/kata/5262119038c0985a5b00029f

"""
import unittest


class IsPrimeTest(unittest.TestCase):
    def test_simple(self):
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(73))
        self.assertFalse(is_prime(75))
        self.assertFalse(is_prime(-1))


import math


def is_prime(num):
    if num <= 1: return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    unittest.main()
