"""

https://www.codewars.com/kata/555b1890a75b930e63000023

"""

import base64
import unittest


class CombosTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(combos(1),[[1]])
        self.assertEqual(sorted(combos(2)),[[1,1],[2]])
        self.assertEqual(sorted(combos(3)),[[1,1,1],[1,2],[3]])
        self.assertEqual(sorted(combos(4)),[[1,1,1,1],[1,1,2],[1,3],[2,2],[4]])


def walk(target, current_sum, start, combo, result):
    if current_sum > target:
        return

    if current_sum == target:
        result.append(combo[:])
        return

    for i in range(start, target+1):
        s = current_sum + i
        combo.append(i)
        walk(target, s, i, combo, result)
        combo.pop()

def combos(n):
    result = []
    walk(n, 0, 1, [], result)
    return result


if __name__ == "__main__":
    unittest.main()
