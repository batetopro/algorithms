"""

https://www.codewars.com/kata/546f922b54af40e1e90001da

"""
import unittest
from random import randint


class AlphabetPositionTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(alphabet_position("The sunset sets at twelve o' clock."), "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11")
        self.assertEqual(alphabet_position("The narwhal bacons at midnight."), "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20")

        number_test = ""
        for item in range(10):
            number_test += str(randint(1, 9))
        self.assertEqual(alphabet_position(number_test), "")


import string
def alphabet_position(text):
    letters = []

    for char in text.lower():
        if not char.isalpha():
            continue

        letters.append(str(string.ascii_lowercase.index(char) + 1))

    return " ".join(letters)


if __name__ == "__main__":
    unittest.main()
