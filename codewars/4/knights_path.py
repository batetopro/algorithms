"""

https://www.codewars.com/kata/5664740e6072d2eebe00001b/

"""
import unittest


class KnightsPathTest(unittest.TestCase):
    def validate_tour(self, path, start, size):
        def legal(pos, size):
            row, col = pos
            return (0 <= row < size) and (0 <= col < size)

        def successors(pos, size, visited):
            row, col = pos
            all_candidates = [
                (row + 2, col + 1),
                (row + 2, col - 1),
                (row - 2, col + 1),
                (row - 2, col - 1),
                (row + 1, col + 2),
                (row + 1, col - 2),
                (row - 1, col + 2),
                (row - 1, col - 2)]

            return [
                move for move in all_candidates
                if legal(move, size) and not visited[move[0]][move[1]]]

        self.assertIsInstance(path, list, "Path expected to be a list")
        self.assertEqual(len(path), size * size, "Path is not the right size")
        self.assertEqual(path[0], start, "Path does not start at correct position")
        self.assertTrue(all(legal(pos, size) for pos in path), "Not all positions in path are legal")

        pos = path[0]
        visited = [[False for _ in range(size)] for _ in range(size)]
        valid_path = True
        for new_pos in path[1:]:
            visited[pos[0]][pos[1]] = True
            if new_pos not in successors(pos, size, visited):
                valid_path = False
                break

            pos = new_pos

        self.assertTrue(valid_path, "Invalid moves in tour")

        return True

    def test_simple(self):
        size = 6
        for start in ((0, 0), (2, 2), (5, 5)):
            path = knights_tour(start, size)
            self.validate_tour(path, start, size)


import heapq


directions = [(1,2), (1,-2), (2,1), (2,-1), (-1, 2), (-1, -2), (-2,1), (-2,-1)]


class KnightsTourBuilder:
    @property
    def board(self):
        return self._board

    @property
    def path(self):
        return self._path

    @property
    def size(self):
        return self._size

    def __init__(self, start, size):
        self._start = start
        self._path = []
        self._size = size
        self._board = []
        for k in range(self.size):
            self._board.append([0] * self.size)

    def print_board(self):
        for row in self.board:
            for c in row:
                print(c, end="\t")
            print()
        print("=" * self.size * 5)

    def is_empty(self, x, y):
        if x < 0 or x >= self.size: return False
        if y < 0 or y >= self.size: return False
        return self.board[x][y] == 0

    def count_free_neighbours(self, x, y):
        count = 0
        for d, direction in enumerate(directions):
            i = x + direction[0]
            j = y + direction[1]
            if self.is_empty(i, j):
                count += 1
        return count

    def run(self):
        x, y = self._start
        for depth in range(self.size * self.size):
            self.board[x][y] = depth + 1
            self.path.append((x,y))
            pq = []

            for d, direction in enumerate(directions):
                i = x + direction[0]
                j = y + direction[1]

                if not self.is_empty(i, j):
                    continue

                heapq.heappush(pq, (self.count_free_neighbours(i, j), d))

            if len(pq):
                count, d = heapq.heappop(pq)
                x += directions[d][0]
                y += directions[d][1]


        # self.print_board()

        return self.path


def knights_tour(start, size):
    """
    Finds a knight's tour from start position visiting every
    board position exactly once.

    A knight may make any "L" move which is valid in chess. That is:
    any rotation of "up 1 over 2" or "up 2 over 1". The problem
    description has a full explanation of valid moves.

    Arguments:
        start - (row, col) starting position on board.
        size - number of rows in the square board.

    Returns:
        List of positions beginning with the start position
        which constitutes a valid tour of the board; visiting
        each position exactly once.
    """
    builder = KnightsTourBuilder(start, size)
    return builder.run()

if __name__ == "__main__":
    unittest.main()

