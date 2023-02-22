"""

https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

"""
import unittest


class RangeExtractionTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(solution([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]), '-6,-3-1,3-5,7-11,14,15,17-20')
        self.assertEqual(solution([-3,-2,-1,2,10,15,16,18,19,20]), '-3--1,2,10,15,16,18-20')


def solution(args):
    args = sorted(args)
    partitions = []
    partition = []

    for num in args:
        if not partition:
            partition.append(num)
            continue

        if partition[-1] + 1 == num:
            partition.append(num)
        else:
            partitions.append(partition[:])
            partition = [num]

    if partition:
        partitions.append(partition)

    result = []
    for partition in partitions:
        if len(partition) == 1:
            result.append(str(partition[0]))
        elif len(partition) == 2:
            result.append(str(partition[0]))
            result.append(str(partition[1]))
        else:
            result.append("{}-{}".format(partition[0], partition[-1]))

    return ",".join(result)



if __name__ == "__main__":
    unittest.main()
