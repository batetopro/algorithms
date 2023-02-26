"""

https://www.codewars.com/kata/5765870e190b1472ec0022a2

"""

import unittest


class PathFinderTest(unittest.TestCase):
    def test_simple(self):
        a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])
        self.assertEqual(path_finder(a), True)


directions = [(-1, 0), (0, -1), (1, 0),(0, 1)]


def parse_maze(maze):
    result = []
    for k, line in enumerate(maze.splitlines()):
        result.append([])
        for c in line:
            if c == "W":
                result[k].append(-1)
            elif c == ".":
                result[k].append(0)
    return result

def path_finder(maze):
    bfs = parse_maze(maze)

    q = [(0,0)]
    bfs[0][0] = 1
    while len(q) > 0:
        x, y = q.pop(0)
        for d in directions:
            i = x + d[0]
            j = y + d[1]
            if i < 0 or i >= len(bfs) or j < 0 or j >= len(bfs[0]) or bfs[i][j] != 0:
                 continue
            bfs[i][j] = bfs[x][y] + 1
            q.append((i,j))

    return bfs[-1][-1] > 0


if __name__ == "__main__":
    unittest.main()
