"""

https://www.codewars.com/kata/5629db57620258aa9d000014

"""
import unittest


class StringsMixTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(mix("Are they here", "yes, they are here"), "2:eeeee/2:yy/=:hh/=:rr")
        self.assertEqual(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"), '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz')
        self.assertEqual(mix("looping is fun but dangerous", "less dangerous than coding"), "1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg")
        self.assertEqual(mix(" In many languages", " there's a pair of functions"), "1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt")
        self.assertEqual(mix("Lords of the Fallen", "gamekult"), "1:ee/1:ll/1:oo")
        self.assertEqual(mix("codewars", "codewars"), "")
        self.assertEqual(mix("A generation must confront the looming ", "codewarrs"), "1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr")


def count_chars(s):
    counter = {}
    for letter in s:
        if not letter.isalpha() or not letter.islower():
            continue
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return {letter: count for letter, count in counter.items() if count > 1}


def merge_counts(left, right):
    merged = {}
    for letter, count in left.items():
        merged[letter] = ('1', count)

    for letter, count in right.items():
        if letter in merged:
            if merged[letter][1] == count:
                merged[letter] = ('=', count)
            elif merged[letter][1] < count:
                merged[letter] = ('2', count)
            continue
        merged[letter] = ('2', count)

    result = [(item[1], "{}:{}".format(item[0], letter * item[1])) for letter, item in merged.items()]
    def cmp(a, b):
        if a[0] < b[0]: return 1
        if a[0] > b[0]: return -1

        if a[1] < b[1]: return -1
        if a[1] > b[1]: return 1
        return 0

    from functools import cmp_to_key
    return sorted(result, key=cmp_to_key(cmp))


def mix(s1, s2):
    merged = merge_counts(count_chars(s1), count_chars(s2))
    return "/".join([item[1] for item in merged])



if __name__ == "__main__":
    unittest.main()
