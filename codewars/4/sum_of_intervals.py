"""

https://www.codewars.com/kata/52b7ed099cdc285c300001cd

"""

import unittest


class SumOfIntervalsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(sum_of_intervals([(1, 4), (7, 10), (3, 5)]), 7)

        self.assertEqual(sum_of_intervals([(1, 5)]), 4)
        self.assertEqual(sum_of_intervals([(1, 5), (6, 10)]), 8)
        self.assertEqual(sum_of_intervals([(1, 5), (1, 5)]), 4)

        self.assertEqual(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]), 2_000_000_000)
        self.assertEqual(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]), 100_000_030)


def sum_of_intervals(intervals):
    if len(intervals) == 0:
        return 0

    intervals = sorted(intervals)
    merged = [intervals[0]]

    if len(intervals) > 0:
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= merged[-1][1]:
                if interval[1] >= merged[-1][1]:
                    last = merged.pop()
                    merged.append((last[0], interval[1]))
                else:
                    continue
            else:
                merged.append(interval)

    result = 0
    for interval in merged:
        result += interval[1] - interval[0]
    return result


if __name__ == "__main__":
    unittest.main()
