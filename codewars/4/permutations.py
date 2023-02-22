"""

https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python

"""
import unittest
import itertools


class PermutationsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sorted(permutations('a')), ['a'])
        self.assertEqual(sorted(permutations('ab')), ['ab', 'ba'])
        self.assertEqual(sorted(permutations('aabb')), ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa'])


def permutations(s):
    perms = [''.join(p) for p in itertools.permutations(s)]
    return set(perms)


if __name__ == "__main__":
    unittest.main()
