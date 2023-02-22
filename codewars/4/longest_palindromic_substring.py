"""

https://www.codewars.com/kata/5dcde0b9fcb0d100349cb5c0

"""
import unittest


class HexStringToRGBTest(unittest.TestCase):
    def test_odd_length(self):
        self.assertEqual(longest_palindrome('babad'), 'bab')
        self.assertEqual(longest_palindrome('madam'), 'madam')
        self.assertEqual(longest_palindrome('dde'), 'dd')
        self.assertEqual(longest_palindrome('ababbab'), 'babbab')
        self.assertEqual(longest_palindrome('abababa'), 'abababa')

    def test_even_length(self):
        self.assertEqual(longest_palindrome('banana'), 'anana')
        self.assertEqual(longest_palindrome('abba'), 'abba')
        self.assertEqual(longest_palindrome('cbbd'), 'bb')
        self.assertEqual(longest_palindrome('zz'), 'zz')
        self.assertEqual(longest_palindrome('dddd'), 'dddd')

    def test_sample(self):
        self.assertEqual(longest_palindrome(''), '')
        self.assertEqual(longest_palindrome('abcdefghijklmnopqrstuvwxyz'), 'a')
        self.assertEqual(longest_palindrome('ttaaftffftfaafatf'), 'aaftffftfaa')
        self.assertEqual(longest_palindrome('bbaaacc'), 'aaa')
        self.assertEqual(longest_palindrome('m'), 'm')

    def test_sample_performance(self):
        self.assertEqual(longest_palindrome('a' * 10000), 'a' * 10000)
        for i in [1000, 2000, 3000]:
            self.assertEqual(longest_palindrome('ab' * i + 'a'), 'ab' * i + 'a')


def updated_string(s):
    new_s = ["#"]
    for char in s:
        new_s.append(char)
        new_s.append("#")
    return "".join(new_s)

def longest_palindrome(s):
    s = updated_string(s)
    LPS = [0] * len(s)
    C = 0
    R = 0

    for i in range(len(s)):
        mirror = 2 * C - i
        if R > i:
            LPS[i] = min(R-i, LPS[mirror])
        else:
            LPS[i] = 0

        try:
            while s[i + 1 + LPS[i]] == s[i - 1 - LPS[i]]:
                LPS[i] += 1
        except:
            pass

        if i + LPS[i] > R:
            C = i
            R = i + LPS[i]

    r, c = max(LPS), LPS.index(max(LPS))
    return s[c - r : c + r].replace("#", "")


if __name__ == "__main__":
    unittest.main()
