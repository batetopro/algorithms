"""

https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1

"""
import unittest


class DuplicateCountTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(duplicate_count(""), 0)
        self.assertEqual(duplicate_count("abcde"), 0)
        self.assertEqual(duplicate_count("abcdeaa"), 1)
        self.assertEqual(duplicate_count("abcdeaB"), 2)
        self.assertEqual(duplicate_count("Indivisibilities"), 2)


def duplicate_count(text):
    data = {}
    for c in text.lower():
        if c not in data:
            data[c] = 0
        data[c] += 1

    count = 0
    for cnt in data.values():
        if cnt > 1:
            count += 1

    return count

    pass


if __name__ == "__main__":
    unittest.main()
