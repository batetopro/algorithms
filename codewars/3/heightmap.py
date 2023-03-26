"""

https://www.codewars.com/kata/5b98dfa088d44a8b000001c1

"""


import unittest


import numpy as np


# Test helper functions
def pretty_print(heightmap):
    size = max( len(str(v)) for r in heightmap for v in r )
    return '\n'.join( ' '.join(f'{v: >{size}}' for v in r) for r in heightmap)



class FluidHeightmapTest(unittest.TestCase):
    def pretty_test(self, heightmap, expected):
        testval = volume([r[:] for r in heightmap])
        self.assertEqual(testval, expected, 'Test for this heightmap failed!\n{0}\n'.format(pretty_print(heightmap)))

    def test_simple(self):
        self.pretty_test([[0]], 0)
        self.pretty_test([[22]], 0)
        self.pretty_test([[2, 1, 2],
                     [1, 0, 1],
                     [2, 1, 2]], 1)
        self.pretty_test([[1, 1, 1],
                     [1, 8, 1],
                     [1, 1, 1]], 0)
        self.pretty_test([[9, 9, 9, 9],
                     [9, 0, 0, 9],
                     [9, 0, 0, 9],
                     [9, 9, 9, 9]], 36)
        self.pretty_test([[9, 9, 9, 9, 9],
                     [9, 0, 1, 2, 9],
                     [9, 7, 8, 3, 9],
                     [9, 6, 5, 4, 9],
                     [9, 9, 9, 9, 9]], 45)
        self.pretty_test([[8, 8, 8, 8, 6, 6, 6, 6],
                     [8, 0, 0, 8, 6, 0, 0, 6],
                     [8, 0, 0, 8, 6, 0, 0, 6],
                     [8, 8, 8, 8, 6, 6, 6, 0]], 56)
        self.pretty_test([[ 0, 10,  0, 20,  0],
                     [20,  0, 30,  0, 40],
                     [ 0, 40,  0, 50,  0],
                     [50,  0, 60,  0, 70],
                     [ 0, 60,  0, 70,  0]], 150)
        self.pretty_test([[3, 3, 3, 3, 3],
                     [3, 0, 0, 0, 3],
                     [3, 3, 3, 0, 3],
                     [3, 0, 0, 0, 3],
                     [3, 0, 3, 3, 3],
                     [3, 0, 0, 0, 3],
                     [3, 3, 3, 0, 3]], 0)
        self.pretty_test([[3, 3, 3, 3, 3],
                     [3, 2, 2, 2, 3],
                     [3, 3, 3, 2, 3],
                     [3, 1, 1, 1, 3],
                     [3, 1, 3, 3, 3],
                     [3, 0, 0, 0, 3],
                     [3, 3, 3, 0, 3]], 0)
        f=lambda:[[3, 3, 3, 3, 3],
                  [3, 0, 0, 0, 3],
                  [3, 3, 3, 0, 3],
                  [3, 0, 0, 0, 3],
                  [3, 0, 3, 3, 3],
                  [3, 0, 0, 0, 3],
                  [3, 3, 3, 1, 3]]
        self.pretty_test(f(), 11)
        self.pretty_test(f()[::-1], 11)
        self.pretty_test([ r[::-1] for r in f()], 11)
        self.pretty_test([ r[::-1] for r in reversed(f())], 11)
        
    def test_negative(self):
        self.pretty_test([[-1]], 0)
        self.pretty_test([[3, 3, 3, 3, 3],
                     [3, 0, 0, 0, 3],
                     [3, 3, 3, 0, 3],
                     [3, 0, -2, 0, 3],
                     [3, 0, 3, 3, 3],
                     [3, 0, 0, 0, 3],
                     [3, 3, 3, 1, -3]], 13)
        self.pretty_test([[8192, 8192, 8192, 8192],
                     [8192,-8192,-8192, 8192],
                     [8192,-8192,-8192, 8192],
                     [8192, 8192, 8192, 8192]], 65536)
    
    def test_50_50(self):
        return
        # A 50x50 heightmap with 100 around the edge and 0 in the middle.
        heightmap = np.full((50, 50), 100)
        heightmap[1:49, 1:49] = 0
        self.pretty_test(heightmap, 100 * 48 * 48)


directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def get_depths(heightmap):
    depths = set()
    for row in heightmap:
        for c in row:
            depths.add(c)
    return list(sorted(depths))


def get_heights(heightmap):
    heights = []
    for row in heightmap:
        heights.append([])
        for c in row:
            heights[-1].append(0)
    return heights


def prepare_visited(heightmap, depth):
    visited = []
    for row in heightmap:
        visited.append([])
        for c in row:
            if c >= depth:
                visited[-1].append(1)
            else:
                visited[-1].append(0)
    return visited


def volume(heightmap):
    if not heightmap:
        return 0

    heights = get_heights(heightmap)
    depths = get_depths(heightmap)
    depths.pop(0)
    for depth in depths:
        visited = prepare_visited(heightmap, depth)
        for y in range(len(heightmap)):
            for x in range(len(heightmap[0])):
                if visited[y][x]: continue

                queue = [(x,y)]
                area = []
                has_edge = False

                while queue:
                    pos = queue.pop(0)
                    area.append(pos)

                    for direction in directions:
                        i = pos[0] + direction[0]
                        j = pos[1] + direction[1]

                        if i < 0 or j < 0 or i >= len(heightmap[0]) or j >= len(heightmap):
                            has_edge = True
                            continue

                        if visited[j][i]:
                            continue

                        visited[j][i] = True
                        queue.append((i, j))

                if has_edge:
                    continue

                for pos in area:
                    heights[pos[1]][pos[0]] = depth - heightmap[pos[1]][pos[0]]

    result = 0
    for row in heights:
        result += sum(row)
    return result


if __name__ == "__main__":
    unittest.main()

