"""

https://www.codewars.com/kata/530e15517bc88ac656000716

"""
import unittest


class Rot13Test(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(rot13('test'), 'grfg')
        self.assertEqual(rot13('Test'), 'Grfg')
        self.assertEqual(rot13('aA bB zZ 1234 *!?%'), 'nN oO mM 1234 *!?%')


def rot13(message):
    table = str.maketrans(
        'ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz',
        'NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm')
    return message.translate(table)


if __name__ == "__main__":
    unittest.main()
