"""

https://www.codewars.com/kata/5282b48bb70058e4c4000fa7

"""
import unittest


class HexStringToRGBTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(hex_string_to_RGB("#FF9933"), {'r': 255, 'g': 153, 'b': 51})
        self.assertEqual(hex_string_to_RGB("#beaded"), {'r': 190, 'g': 173, 'b': 237})
        self.assertEqual(hex_string_to_RGB("#000000"), {'r': 0, 'g': 0, 'b': 0})
        self.assertEqual(hex_string_to_RGB("#111111"), {'r': 17, 'g': 17, 'b': 17})
        self.assertEqual(hex_string_to_RGB("#Fa3456"), {'r': 250, 'g': 52, 'b': 86})


def parse(num):
    return int(num, 16)


def hex_string_to_RGB(hex_string):
    return {
        "r": parse(hex_string[1:3]),
        "g": parse(hex_string[3:5]),
        "b": parse(hex_string[5:]),
    }


if __name__ == "__main__":
    unittest.main()
