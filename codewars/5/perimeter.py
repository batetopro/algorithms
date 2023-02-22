"""

https://www.codewars.com/kata/559a28007caad2ac4e000083

"""
import unittest


class PerimeterTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(perimeter(5), 80)
        self.assertEqual(perimeter(7), 216)
        self.assertEqual(perimeter(20), 114624)
        self.assertEqual(perimeter(30), 14098308)
        self.assertEqual(perimeter(100), 6002082144827584333104)
        self.assertEqual(perimeter(500),
                           2362425027542282167538999091770205712168371625660854753765546783141099308400948230006358531927265833165504)


def perimeter(n):
    fn = [1,1]
    for k in range(2, n + 1):
        fn.append(fn[k-1]+fn[k-2])
    return 4 * sum(fn)


if __name__ == "__main__":
    unittest.main()
