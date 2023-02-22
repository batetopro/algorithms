"""

https://www.codewars.com/kata/51689e27fe9a00b126000004

"""
import unittest


class DigitalRootTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(format_words(['one', 'two', 'three', 'four']), 'one, two, three and four')
        self.assertEqual(format_words(['one']), 'one')
        self.assertEqual(format_words(['one', '', 'three']), 'one and three')
        self.assertEqual(format_words(['', '', 'three']), 'three')
        self.assertEqual(format_words([]), '')
        self.assertEqual(format_words(None), '')
        self.assertEqual(format_words(['']), '')


def format_words(words):
    if not words:
        return ""

    filtered = [w for w in words if w]
    if len(filtered) == 0:
        return ""

    if len(filtered) == 1:
        return filtered[0]

    w1 = filtered.pop()
    w2 = filtered.pop()
    filtered.append("{} and {}".format(w2, w1))
    return ", ".join(filtered)


if __name__ == "__main__":
    unittest.main()
