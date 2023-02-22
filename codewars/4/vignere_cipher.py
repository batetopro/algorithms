"""

https://www.codewars.com/kata/52d1bd3694d26f8d6e0000d3/train/python

"""
import unittest


class HexStringToRGBTest(unittest.TestCase):
    def test_simple(self):
        abc = "abcdefghijklmnopqrstuvwxyz"
        key = "password"
        c = VigenereCipher(key, abc)
        self.assertEqual(c.encode('codewars'), 'rovwsoiv')
        self.assertEqual(c.decode('rovwsoiv'), 'codewars')
        self.assertEqual(c.encode('waffles'), 'laxxhsj')
        self.assertEqual(c.decode('laxxhsj'), 'waffles')
        self.assertEqual(c.encode('CODEWARS'), 'CODEWARS')
        self.assertEqual(c.decode('CODEWARS'), 'CODEWARS')


class VigenereCipher(object):
    @property
    def key(self):
        return self._key

    @property
    def alphabet(self):
        return self._alphabet

    def __init__(self, key, alphabet):
        self._key = key
        self._alphabet = alphabet

    def encode(self, text):
        ciphertext = ''
        for idx, letter in enumerate(text):
            try:
                p = self.alphabet.index(letter)
            except ValueError:
                ciphertext += letter
                continue
            k = self.alphabet.index(self.key[idx % len(self.key)])
            c = (p + k) % len(self.alphabet)
            ciphertext += self.alphabet[c]
        return ciphertext

    def decode(self, text):
        plaintext = ''
        for idx, letter in enumerate(text):
            try:
                p = self.alphabet.index(letter)
            except ValueError:
                plaintext += letter
                continue
            k = self.alphabet.index(self.key[idx % len(self.key)])
            c = (p - k) % len(self.alphabet)
            plaintext += self.alphabet[c]
        return plaintext


if __name__ == "__main__":
    unittest.main()
