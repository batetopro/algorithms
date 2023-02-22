""""

https://www.codewars.com/kata/526d84b98f428f14a60008da/python

"""
import unittest


class DigitalRootTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(hamming(1), 1)
        self.assertEqual(hamming(2), 2)
        self.assertEqual(hamming(3), 3)
        self.assertEqual(hamming(4), 4)
        self.assertEqual(hamming(5), 5)
        self.assertEqual(hamming(6), 6)
        self.assertEqual(hamming(7), 8)
        self.assertEqual(hamming(8), 9)
        self.assertEqual(hamming(9), 10)
        self.assertEqual(hamming(10), 12)
        self.assertEqual(hamming(11), 15)
        self.assertEqual(hamming(12), 16)
        self.assertEqual(hamming(13), 18)
        self.assertEqual(hamming(14), 20)
        self.assertEqual(hamming(15), 24)
        self.assertEqual(hamming(16), 25)
        self.assertEqual(hamming(17), 27)
        self.assertEqual(hamming(18), 30)
        self.assertEqual(hamming(19), 32)


def hamming(n):
    """Returns the nth hamming number"""
    import heapq

    h = 1
    q = [h]
    for i in range(n):
        h = heapq.heappop(q)
        while q and q[0] == h:
            heapq.heappop(q)
        for num in [2, 3, 5]:
            heapq.heappush(q, h * num)

    return h

if __name__ == "__main__":
    unittest.main()
