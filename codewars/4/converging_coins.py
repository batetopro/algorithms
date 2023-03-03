"""

https://www.codewars.com/kata/5f5bef3534d5ad00232c0fa8

"""


import unittest


class ConvergingCoinsTest(unittest.TestCase):
    def test_1_step_from_center(self):
        g = {1: {4}, 2: {4}, 3: {4}, 4: {1, 2, 3}}
        self.assertEqual(converge(g, 1, 2, 3), 1)

    def test_2_step_from_center(self):
        g = {
            0: {5, 1, 3},
            1: {0, 2},
            2: {1},
            3: {0, 4},
            4: {3},
            5: {6, 0},
            6: {5},
        }
        self.assertEqual(converge(g, 2, 4, 6), 2)

    def test_triangle(self):
        g = {
            1: {2, 3},
            2: {1, 3},
            3: {1, 2},
        }
        self.assertEqual(converge(g, 1, 2, 3), 2)

    def test_line(self):
        g = {
            1: {2},
            2: {1, 3},
            3: {2},
        }
        self.assertEqual(converge(g, 1, 2, 3), None)


def converge(g, u1, u2, u3):
    if u1 == u2 == u3:
        return 0
    pos = [{u1}, {u2}, {u3}]
    visited = [pos]

    for i in range(len(g)):
        new_pos = [set(), set(), set()]
        for j, coin in enumerate(pos):
            for v in coin:
                for n in g[v]:
                    new_pos[j].add(n)
        pos = new_pos

        if pos[0].intersection(pos[1].intersection(pos[2])):
            return i + 1
        if pos in visited:
            return None
        visited.append(pos)
    return i


if __name__ == "__main__":
    unittest.main()
