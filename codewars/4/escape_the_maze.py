"""

https://www.codewars.com/kata/5877027d885d4f6144000404

"""
import unittest


class EscapeTheMazeTest(unittest.TestCase):
    def test_simple(self):
        basic_mazes = list()
        basic_mazes.append([
            '# #',
            ' > ',
            '# #'
        ])
        basic_mazes.append([
            '###########',
            '#>        #',
            '######### #'
        ])
        basic_mazes.append([
            '# #########',
            '#        >#',
            '###########'
        ])
        basic_mazes.append([
            '# #########',
            '#    ^    #',
            '######### #'
        ])
        basic_mazes.append([
            '####### #',
            '#>#   # #',
            '#   #   #',
            '#########'
        ])
        basic_mazes.append([
            '##########',
            '#        #',
            '#  ##### #',
            '#  #   # #',
            '#  #^# # #',
            '#  ### # #',
            '#      # #',
            '######## #'
        ])
        basic_mazes.append([
            "#########################################",
            "#<    #       #     #         # #   #   #",
            "##### # ##### # ### # # ##### # # # ### #",
            "# #   #   #   #   #   # #     #   #   # #",
            "# # # ### # ########### # ####### # # # #",
            "#   #   # # #       #   # #   #   # #   #",
            "####### # # # ##### # ### # # # #########",
            "#   #     # #     # #   #   # # #       #",
            "# # ####### ### ### ##### ### # ####### #",
            "# #             #   #     #   #   #   # #",
            "# ############### ### ##### ##### # # # #",
            "#               #     #   #   #   # #   #",
            "##### ####### # ######### # # # ### #####",
            "#   # #   #   # #         # # # #       #",
            "# # # # # # ### # # ####### # # ### ### #",
            "# # #   # # #     #   #     # #     #   #",
            "# # ##### # # ####### # ##### ####### # #",
            "# #     # # # #   # # #     # #       # #",
            "# ##### ### # ### # # ##### # # ### ### #",
            "#     #     #     #   #     #   #   #    ",
            "#########################################"
        ])
        for maze in basic_mazes:
            escape(maze)


dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
orientations = ["^", ">", "v", "<"]


def print_matrix(M):
    for i, row in enumerate(M):
        for j, char in enumerate(row):
            print(char, end=" ")
        print()

def get_start_pos(maze):
    for i, row in enumerate(maze):
        for j, char in enumerate(row):
            if char in "^<v>":
                return i, j

def is_free(maze, i, j):
    return maze[i][j] != "#"

def is_escape_pos(maze, i, j):
    if not is_free(maze, i, j):
        return False
    if i <= 0 or j <= 0:
        return True
    if i >= len(maze) - 1 or j >= len(maze[0]) - 1:
        return True
    return False

def is_valid(maze, i, j):
    if i < 0 or j < 0:
        return False
    if i > len(maze) - 1 or j > len(maze[0]) - 1:
        return False
    if not is_free(maze, i, j):
        return False
    return True

def get_best_escape_pos(maze, bfs):
    score = None
    end = None
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if not is_escape_pos(maze, i, j):
                continue
            if not bfs[i][j]:
                continue
            if not end or score > bfs[i][j]:
                end = (i, j)
                score = bfs[i][j]
    return end

def build_bfs(maze, bfs):
    q = [(get_start_pos(maze), 1)]
    while q:
        p, t = q.pop(0)
        bfs[p[0]][p[1]] = t
        for d in dirs:
            x = p[0] + d[0]
            y = p[1] + d[1]
            if is_valid(maze, x, y) and not bfs[x][y]:
                q.append(((x, y), t + 1))

def build_path(maze, bfs):
    end = get_best_escape_pos(maze, bfs)
    if end is None:
        return []

    k = bfs[end[0]][end[1]]
    path = [end]
    while k > 1:
        p = path[-1]
        for d in dirs:
            x = p[0] + d[0]
            y = p[1] + d[1]
            if not is_valid(maze, x, y):
                continue
            if k - 1 == bfs[x][y]:
                path.append((x,y))
                continue
        k -= 1

    return list(reversed(path))

def encode_path(maze, path):
    if not path:
        return []

    s = maze[path[0][0]][path[0][1]]
    e = []
    for i in range(1, len(path)):
        delta = (path[i][0]-path[i-1][0], path[i][1]-path[i-1][1])
        for idx, d in enumerate(dirs):
            if delta[0] == d[0] and delta[1] == d[1]:
                break

        for j, o in enumerate(orientations):
            if s == o:
                break

        ctr = 0
        while s != orientations[idx]:
            ctr += 1
            j = (j + 1) % len(dirs)
            s = orientations[j]

        if ctr == 1:
            e.append("R")
        elif ctr == 2:
            e.append("B")
        elif ctr == 3:
            e.append("L")

        # print(path[i-1], path[i], delta, idx, orientations[idx], j, s)
        e.append("F")

    return e


def escape(maze):
    bfs = []
    for i, row in enumerate(maze):
        bfs.append([0] * len(row))
    build_bfs(maze, bfs)
    path = build_path(maze, bfs)
    encoded = encode_path(maze, path)

    # print_matrix(maze)
    # print(encoded)
    # print("=" * 20)
    return encoded


if __name__ == "__main__":
    unittest.main()
