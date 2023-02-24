""""

https://www.codewars.com/kata/51c8e37cee245da6b40000bd

"""
import unittest


class StripCommentsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),
                         'apples, pears\ngrapes\nbananas')
        self.assertEqual(strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
        self.assertEqual(strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')


def strip_comments(string, markers):
    lines = []
    for line in string.splitlines():
        for m in markers:
            line = line.split(m)[0].rstrip()
        lines.append(line)
    return "\n".join(lines)


if __name__ == "__main__":
    unittest.main()
