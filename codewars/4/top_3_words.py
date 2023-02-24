""""

https://www.codewars.com/kata/51e056fe544cf36c410000fb

"""
import unittest


class Top3WordsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
        self.assertEqual(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
        self.assertEqual(top_3_words("  //wont won't won't "), ["won't", "wont"])
        self.assertEqual(top_3_words("  , e   .. "), ["e"])
        self.assertEqual(top_3_words("  ...  "), [])
        self.assertEqual(top_3_words("  '  "), [])
        self.assertEqual(top_3_words("  '''  "), [])
        self.assertEqual(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
        mind, there lived not long since one of those gentlemen that keep a lance
        in the lance-rack, an old buckler, a lean hack, and a greyhound for
        coursing. An olla of rather more beef than mutton, a salad on most
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
        on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])



def top_3_words(text):
    parsed = []
    for c in text.lower():
        if c.isalpha() or c == "'":
            parsed.append(c)
        else:
            parsed.append(" ")
    parsed = "".join(parsed)

    frequencies = {}
    for word in parsed.split(" "):
        word = word.strip()
        if not word:
            continue

        letters = 0
        for c in word:
            if c.isalpha():
                letters += 1
        if letters == 0:
            continue

        if word not in frequencies:
            frequencies[word] = 0
        frequencies[word] += 1


    result = []
    for item in sorted(frequencies.items(), key=lambda x: x[1])[-3:]:
        result.append(item[0])
    return list(reversed(result))

if __name__ == "__main__":
    unittest.main()
