"""

https://www.codewars.com/kata/5296bc77afba8baa690002d7/python

"""
import unittest


class SudokuSolverTest(unittest.TestCase):
    def test_simple(self):
        puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                  [6, 0, 0, 1, 9, 5, 0, 0, 0],
                  [0, 9, 8, 0, 0, 0, 0, 6, 0],
                  [8, 0, 0, 0, 6, 0, 0, 0, 3],
                  [4, 0, 0, 8, 0, 3, 0, 0, 1],
                  [7, 0, 0, 0, 2, 0, 0, 0, 6],
                  [0, 6, 0, 0, 0, 0, 2, 8, 0],
                  [0, 0, 0, 4, 1, 9, 0, 0, 5],
                  [0, 0, 0, 0, 8, 0, 0, 7, 9]]

        solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],
                    [6, 7, 2, 1, 9, 5, 3, 4, 8],
                    [1, 9, 8, 3, 4, 2, 5, 6, 7],
                    [8, 5, 9, 7, 6, 1, 4, 2, 3],
                    [4, 2, 6, 8, 5, 3, 7, 9, 1],
                    [7, 1, 3, 9, 2, 4, 8, 5, 6],
                    [9, 6, 1, 5, 3, 7, 2, 8, 4],
                    [2, 8, 7, 4, 1, 9, 6, 3, 5],
                    [3, 4, 5, 2, 8, 6, 1, 7, 9]]
        self.assertEqual(sudoku(puzzle), solution)


def possible(puzzle, row, col, number):
    if puzzle[row][col] != 0:
        return puzzle[row][col] == number
    for i in range(0, 9):
        if puzzle[row][i] == number:
            return False
    for i in range(0, 9):
        if puzzle[i][col] == number:
            return False
    x0 = (col // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if puzzle[y0 + i][x0 + j] == number:
                return False
    return True


def find_empty(puzzle):
    for row in range(0, 9):
        for col in range(0, 9):
            if puzzle[row][col] == 0:
                return row, col


def sudoku(puzzle):
    empty = find_empty(puzzle)
    if not empty:
        return puzzle

    for number in range(1, 10):
        if possible(puzzle, empty[0], empty[1], number):
            puzzle[empty[0]][empty[1]] = number
            if sudoku(puzzle):
                return puzzle
            puzzle[empty[0]][empty[1]] = 0

    return False



if __name__ == "__main__":
    unittest.main()
