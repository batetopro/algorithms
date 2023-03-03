"""

https://www.codewars.com/kata/56a1c63f3bc6827e13000006

"""
import unittest


class SmallerTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(smaller([5, 4, 3, 2, 1]), [4, 3, 2, 1, 0])
        self.assertEqual(smaller([1, 2, 3]), [0, 0, 0])
        self.assertEqual(smaller([1, 2, 0]), [1, 1, 0])
        self.assertEqual(smaller([1, 2, 1]), [0, 1, 0])
        self.assertEqual(smaller([1, 1, -1, 0, 0]), [3, 3, 0, 0, 0])
        self.assertEqual(smaller([5, 4, 7, 9, 2, 4, 4, 5, 6]), [4, 1, 5, 5, 0, 0, 0, 0, 0])
        self.assertEqual(smaller([5, 4, 7, 9, 2, 4, 1, 4, 5, 6]), [5, 2, 6, 6, 1, 1, 0, 0, 0, 0])



def merge(v, ans, l, mid, h):
    t = []
    i = l
    j = mid + 1
    while i < mid + 1 and j <= h:
        if v[i][0] > v[j][0]:
            ans[v[i][1]] += (h-j+1)
            t.append(v[i])
            i += 1
        else:
            t.append(v[j])
            j += 1

    while i <= mid:
        t.append(v[i])
        i += 1

    while j <= h:
        t.append(v[j])
        j += 1

    k = 0
    i = l
    while i <= h:
        v[i] = t[k]
        i += 1
        k += 1

def merge_sort(v, ans, i, j):
    if not i < j:
        return
    mid = (i + j) // 2
    merge_sort(v, ans, i, mid)
    merge_sort(v, ans, mid + 1, j)
    merge(v, ans, i, mid, j)


def smaller(arr):
    v = [(arr[i], i) for i in range(len(arr))]
    ans = [0] * len(arr)
    merge_sort(v, ans, 0, len(arr) - 1)
    return ans


if __name__ == "__main__":
    unittest.main()
