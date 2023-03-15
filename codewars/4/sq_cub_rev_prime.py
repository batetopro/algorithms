"""

https://www.codewars.com/kata/5644a69f7849c9c097000073/

"""
import unittest


class SqCubRevPrimeTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sq_cub_rev_prime(1), 89)
        self.assertEqual(sq_cub_rev_prime(2), 271)
        self.assertEqual(sq_cub_rev_prime(3), 325)
        self.assertEqual(sq_cub_rev_prime(4), 328)
        self.assertEqual(sq_cub_rev_prime(97), 12535)


import random

def even_odd(n):
    s, d = 0, n
    while d % 2 == 0:
          s += 1
          d >>= 1
    return s, d

def Miller_Rabin(a, p):
    s, d = even_odd(p-1)
    a = pow(a, d, p)
    if a == 1: return True
    for i in range(s):
        if a == p-1: return True
        a = pow(a, 2, p)
    return False

def is_prime(p):
    if p == 2: return True
    if p <= 1 or p % 2 == 0: return False
    return all(Miller_Rabin(random.randint(2,p-1),p) for _ in range(40))


def reverse_number(num):
    reversed_num = 0
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    return reversed_num


cache = dict()
def sq_cub_rev_prime(n):
    if n in cache:
        return cache[n]

    ctr = 0
    x = 1
    while ctr < n:
        x += 1
        if is_prime(reverse_number(x * x)) and is_prime(reverse_number(x * x * x)):
            ctr += 1
            cache[ctr] = x

    return x


if __name__ == "__main__":
    unittest.main()
