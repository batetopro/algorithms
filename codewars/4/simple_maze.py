"""

https://www.codewars.com/kata/56bb9b7838dd34d7d8001b3c

"""


import unittest


class SimpleMazeTest(unittest.TestCase):
    def test_simple(self):
        maze = ["#########",
                "#k        #",
                "###########"]
        self.assertTrue(has_exit(maze))

        maze = ["k"]
        self.assertTrue(has_exit(maze))

        maze = ["###",
                "#k#",
                "###"]
        self.assertFalse(has_exit(maze))

        maze = ["###",
                "#k ",
                "###"]
        self.assertTrue(has_exit(maze))

        maze = ["k ",
                "kk"]
        self.assertRaises(Exception, has_exit, maze)

        maze = ["########",
                "# # ####",
                "# #k#   ",
                "# # # ##",
                "# # # ##",
                "#      #",
                "########"]
        self.assertTrue(has_exit(maze))

        maze = ["########",
                "# # ## #",
                "# #k#  #",
                "# # # ##",
                "# # #  #",
                "#     ##",
                "########"]
        self.assertFalse(has_exit(maze))


directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


def prepare_bfs_matrix(maze):
    width = max([len(row) for row in maze])
    matrix = []
    start = None

    for i, row in enumerate(maze):
        matrix.append([0] * width)
        for j, char in enumerate(row):
            if char == 'k':
                if start is None:
                    matrix[i][j] = 0
                    start = (i, j)
                else:
                    raise ValueError("Multiple start positions.")
            elif char == '#':
                matrix[i][j] = -1
            else:
                matrix[i][j] = 0

    if start is None:
        raise ValueError("Start position could not be found.")
    return matrix, start


def build_bfs(matrix, start):
    q = [(start, 1)]
    while q:
        p, d = q.pop()
        matrix[p[0]][p[1]] = d
        for direction in directions:
            i = p[0] + direction[0]
            j = p[1] + direction[1]
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
                return True
            if matrix[i][j] != 0:
                continue
            q.append(((i, j), d + 1))
    return False

def has_exit(maze):
    matrix, start = prepare_bfs_matrix(maze)
    return build_bfs(matrix, start)

if __name__ == "__main__":
    unittest.main()
