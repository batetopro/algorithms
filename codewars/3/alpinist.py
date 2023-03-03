"""

https://www.codewars.com/kata/576986639772456f6f00030c

"""
import unittest


class AlpinistTest(unittest.TestCase):
    def test_simple(self):
        a = "\n".join([
            "000",
            "000",
            "000"
        ])
        self.assertEqual(path_finder(a), 0)

        b = "\n".join([
            "010",
            "010",
            "010"
        ])
        self.assertEqual(path_finder(b), 2)

        c = "\n".join([
            "010",
            "101",
            "010"
        ])
        self.assertEqual(path_finder(c), 4)

        d = "\n".join([
            "0707",
            "7070",
            "0707",
            "7070"
        ])
        self.assertEqual(path_finder(d), 42)

        e = "\n".join([
            "700000",
            "077770",
            "077770",
            "077770",
            "077770",
            "000007"
        ])
        self.assertEqual(path_finder(e), 14)

        f = "\n".join([
            "777000",
            "007000",
            "007000",
            "007000",
            "007000",
            "007777"
        ])
        self.assertEqual(path_finder(f), 0)

        g = "\n".join([
            "000000",
            "000000",
            "000000",
            "000010",
            "000109",
            "001010"
        ])
        self.assertEqual(path_finder(g), 4)


def print_matrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end="\t")
        print()


directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def prepare_data(area):
    matrix = [[int(c) for c in row] for row in area.splitlines()]
    visited = [[False for c in row] for row in area.splitlines()]
    return matrix, visited


def path_finder(area):
    matrix, visited = prepare_data(area)
    n = len(matrix)

    visited[0][0] = 0
    q = [(0, 0),]
    while q:
        p = q.pop(0)
        for direction in directions:
            i = p[0] + direction[0]
            j = p[1] + direction[1]
            if i < 0 or i >= n or j < 0 or j >= n:
                continue

            h = visited[p[0]][p[1]] + abs(matrix[p[0]][p[1]] - matrix[i][j])

            if visited[i][j] is not False and visited[i][j] <= h:
                continue

            visited[i][j] = h
            q.append((i,j))

    return visited[-1][-1]


if __name__ == "__main__":
    unittest.main()
