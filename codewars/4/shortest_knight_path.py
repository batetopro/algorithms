"""

https://www.codewars.com/kata/549ee8b47111a81214000941

"""
import unittest


class ShortestKnightPathTest(unittest.TestCase):
    def test_a1(self):
        self.assertEqual(knight('a1', 'c1'), 2)
        self.assertEqual(knight('a1', 'f1'), 3)
        self.assertEqual(knight('a1', 'f3'), 3)
        self.assertEqual(knight('a1', 'f4'), 4)
        self.assertEqual(knight('a1', 'f7'), 5)

    def test_c8_b5(self):
        self.assertEqual(knight('c8', 'b5'), 2)

    def test_a6_h6(self):
        self.assertEqual(knight('a6', 'h6'), 5)


dirs = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2), (2, -1), (2, 1)]


def print_matrix(M):
    for i, row in enumerate(M):
        for j, char in enumerate(row):
            print(char, end=" ")
        print()
    print("=" * 50)


def parse_pos(pos):
    return ord(pos[0]) - ord('a'), int(pos[1]) - 1


def knight(p1, p2):

    n = 8
    board = []
    for k in range(n):
        board.append([0] * n)

    q = [(parse_pos(p1), 1)]
    while q:
        p, t = q.pop(0)
        board[p[1]][p[0]] = t
        for d in dirs:
            i = p[0] - d[0]
            j = p[1] - d[1]
            if i < 0 or j < 0 or i >= n or j >= n:
                continue
            if board[j][i] != 0:
                continue
            q.append(((i, j), t + 1))

    # print(p1, p2)
    # print_matrix(board)

    end = parse_pos(p2)
    return board[end[1]][end[0]] - 1


if __name__ == "__main__":
    unittest.main()
