"""

https://www.codewars.com/kata/583203e6eb35d7980400002a

"""
import unittest


class CountSmileysTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(count_smileys([]), 0)
        self.assertEqual(count_smileys([':D', ':~)', ';~D', ':)']), 4)
        self.assertEqual(count_smileys([':)', ':(', ':D', ':O', ':;']), 2)
        self.assertEqual(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)


def count_smileys(arr):
    smileys = [
        ":)", ":-)", ":~)",
        ":D", ":-D", ":~D",
        ";)", ";-)", ";~)",
        ";D", ";-D", ";~D",
    ]

    result = 0
    for w in arr:
        if w in smileys:
            result += 1
    return result


if __name__ == "__main__":
    unittest.main()
