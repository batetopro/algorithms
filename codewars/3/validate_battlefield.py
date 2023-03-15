"""

https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7/

"""
import unittest


class ValidateBattlefieldTest(unittest.TestCase):
    def test_simple(self):
        battle_field = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                       [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                       [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertTrue(validate_battlefield(battle_field))

    def test_missing(self):
        battle_field = [[0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.assertFalse(validate_battlefield(battle_field))

    def test_overflow(self):
        battle_field = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [1, 1, 1, 1, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                        [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                        [1, 0, 0, 0, 0, 0, 1, 0, 0, 0]]
        self.assertTrue(validate_battlefield(battle_field))



def print_matrix(matrix):
    for row in matrix:
        for c in row:
            print(c, end="\t")
        print()
    print("=" * 50)


sizes = {4 : 1, 3: 2, 2: 3, 1: 4}
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def get_empty_visited(field):
    visited = [[0 for _ in range(len(field[0]))] for __ in range(len(field))]
    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if c == 0:
                visited[i][j] = -1
                continue
    return visited


def get_numbered_ships(field):
    result = get_empty_visited(field)
    ctr = 0

    for i, row in enumerate(field):
        for j, c in enumerate(row):
            if result[i][j] != 0: continue
            ctr += 1
            q = [(i, j)]
            while q:
                pos = q.pop(0)
                result[pos[0]][pos[1]] = ctr
                for direction in directions:
                    u = pos[0] + direction[0]
                    v = pos[1] + direction[1]

                    if u < 0 or v < 0 or u >= len(field) or v >= len(field[0]): continue

                    if result[u][v] != 0: continue
                    q.append((u,v))
    return result


def get_ships(field, numbered):
    visited = get_empty_visited(field)
    ships = []
    for i, row in enumerate(numbered):
        for j, c in enumerate(row):
            if numbered[i][j] <= 0: continue
            if visited[i][j] != 0: continue
            ship = set()
            q = [(i, j)]
            while q:
                pos = q.pop(0)
                ship.add(pos)
                visited[pos[0]][pos[1]] = 1
                for direction in directions:
                    u = pos[0] + direction[0]
                    v = pos[1] + direction[1]
                    if u < 0 or v < 0 or u >= len(field) or v >= len(field[0]) \
                            or numbered[u][v] != c or visited[u][v] != 0:
                        continue
                    q.append((u,v))
            ships.append(ship)
    return ships


def get_ship_size(ship):
    min_i = min([p[0] for p in ship])
    max_i = max([p[0] for p in ship])
    min_j = min([p[1] for p in ship])
    max_j = max([p[1] for p in ship])

    d_i = max_i - min_i + 1
    d_j = max_j - min_j + 1

    if d_i > 1:
        if d_j == 1: return d_i
        else: return False

    if d_i == 1: return d_j
    else: return False


def validate_battlefield(field):
    numbered = get_numbered_ships(field)
    ships = get_ships(field, numbered)

    counter = {}
    for ship in ships:
        size = get_ship_size(ship)
        if size is False:
            return False

        if size not in counter:
            counter[size] = 0
        counter[size] += 1

    for key in sizes:
        if key not in counter:
            return False

    for key in counter:
        if key not in sizes:
            return False
        if sizes[key] != counter[key]:
            return False

    return True


if __name__ == "__main__":
    unittest.main()
