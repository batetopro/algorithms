import numpy as np


def possible(row, col, number):
    global grid
    if grid[row][col] != 0:
        return grid[row][col] == number
    for i in range(0, 9):
        if grid[row][i] == number:
            return False
    for i in range(0, 9):
        if grid[i][col] == number:
            return False
    x0 = (col // 3) * 3
    y0 = (row // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0 + i][x0 + j] == number:
                return False
    return True


def solve():
    global grid

    for row in range(0, 9):
        for col in range(0, 9):
            if grid[row][col] == 0:
                for number in range(1, 10):
                    if possible(row, col, number):
                        grid[row][col] = number
                        solve()
                        grid[row][col] = 0
                return

    print(np.matrix(grid))


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, ],
        [0, 2, 0, 9, 0, 0, 3, 8, 0, ],
        [0, 3, 0, 1, 0, 0, 7, 5, 0, ],
        [0, 4, 8, 0, 2, 0, 0, 0, 0, ],
        [0, 5, 0, 0, 0, 6, 0, 0, 0, ],
        [7, 6, 0, 5, 0, 0, 4, 1, 0, ],
        [4, 0, 0, 0, 0, 3, 0, 0, 0, ],
        [2, 0, 0, 8, 4, 5, 6, 7, 0, ],
        [0, 7, 5, 2, 0, 0, 0, 0, 0, ],
    ]
    solve()
