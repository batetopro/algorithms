"""

https://www.codewars.com/kata/561bed6a31daa8df7400000e

"""
import unittest


def check_solution_valid(solution, required, size):
    def format_pos(row, col):
        return "abcdefghij"[col] + "1234567890"[row]

    def parse_pos(pos):
        parsed_col = "abcdefghij".find(pos[0])
        parsed_row = "1234567890".find(pos[1])
        return (parsed_row, parsed_col)

    positions = solution.split(",")

    if len(positions) != size:
        print(f"Invalid number of columns: {len(positions)}, expected {size}")
        return False

    if required not in positions:
        print(f"Queen not found in required position {required} in solution {solution}")
        return False

    result = [None] * size

    for pos in positions:

        if len(pos) != 2:
            print(f"{pos} is not a valid position")
            return False

        (row, col) = parse_pos(pos)
        if not (col >= 0 and col < size and row >= 0 and row < size):
            print(f"{pos} is not a valid position for a board of size {size}")
            return False

        if result[row] is not None:
            print(f"Queen at {pos} can be attacked by queen at " + format_pos(row, result[row]))
            return False

        result[row] = col

    cols = [None] * size
    ldiag = [None] * 2 * size
    rdiag = [None] * 2 * size
    noatk = (-1, -1)
    for row in range(size):
        col = result[row]
        pos = format_pos(row, col)

        if col is None:
            print(f"No queen in row {row + 1}")
            return False

        if col < 0 or col >= size:
            print(f"Queen at {pos} is outside bounds")
            return False

        atk = cols[col] or ldiag[col + row] or rdiag[col - row + size - 1] or noatk

        if atk is not noatk:
            print(f"Queen at {pos} can be attacked by queen at " + format_pos(atk[0], atk[1]))
            return False

        cols[col] = ldiag[col + row] = rdiag[col - row + size - 1] = (row, col)

    print("Solution " + solution + " is valid")
    return True


class QuuensTest(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(check_solution_valid(queens("a1", 1), "a1", 1))
        self.assertTrue(check_solution_valid(queens("b4", 4), "b4", 4))
        self.assertTrue(check_solution_valid(queens("c7", 8), "c7", 8))


directions = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, 0), (1, -1), (1, 1)]


def parse_pos(pos):
    parsed_col = "abcdefghij".find(pos[0])
    parsed_row = "1234567890".find(pos[1])
    return parsed_row, parsed_col


def format_pos(row, col):
    return "abcdefghij"[col] + "1234567890"[row]


class QueensSolver:
    @property
    def board(self):
        return self._board

    @property
    def fixed_position(self):
        return self._fixed_position

    @property
    def size(self):
        return self._size

    def __init__(self, position, size):
        self._fixed_position = parse_pos(position)
        self._size = size
        self._board = []
        for i in range(size):
            self._board.append([0] * size)
        self.board[self.fixed_position[0]][self.fixed_position[1]] = 1

    def print_board(self):
        for row in self.board:
            for c in row:
                print(c, end="\t")
            print()
        print("=" * 60)

    def solve(self, col=0):
        if col == self.size:
            return True

        if col == self.fixed_position[0]:
            return self.solve(col + 1)

        for j in range(self.size):
            if self.is_safe(col,j):
                self.board[col][j] = 1
                if self.solve(col+1):
                    return True
                self.board[col][j] = 0

    def is_safe(self, row, col):
        if self.board[row][col] > 0:
            return False
        for direction in directions:
            r = row + direction[0]
            c = col + direction[1]
            while 0 <= r < self.size and 0 <= c < self.size:
                if self.board[r][c] > 0:
                    return False
                r += direction[0]
                c += direction[1]
        return True

    def get_queens(self):
        result = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j]:
                    result.append(format_pos(i, j))
        return result

def queens(position, size):
    solver = QueensSolver(position, size)
    solver.solve()
    return ",".join(solver.get_queens())


if __name__ == "__main__":
    unittest.main()
