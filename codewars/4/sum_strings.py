"""

https://www.codewars.com/kata/5324945e2ece5e1f32000370

"""
import unittest


class SumStringsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_strings("00103", "08567"), "8670")
        self.assertEqual(sum_strings("08567", "00103"), "8670")
        self.assertEqual(sum_strings("1", "1"), "2")
        self.assertEqual(sum_strings("123", "456"), "579")
        self.assertEqual(sum_strings('800', '9567'), '10367')
        self.assertEqual(sum_strings("99", "1"), "100")
        self.assertEqual(sum_strings('','5'), "5")


def sum_strings(x, y):
    x = x.lstrip("0")
    y = y.lstrip("0")
    if len(x) < len(y):
        return sum_strings(y, x)

    y = '0' * (len(x) - len(y)) + y

    z = []
    carry = 0
    for i in range(len(x) - 1, -1, -1):
        s = int(x[i]) + int(y[i]) + carry
        if s >= 10:
            s -= 10
            carry = 1
        else:
            carry = 0

        z.append(str(s))

    if carry:
        z.append(str(carry))

    result = "".join(reversed(z))
    if not result:
        return "0"
    return result


if __name__ == "__main__":
    unittest.main()