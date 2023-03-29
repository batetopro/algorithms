"""

https://www.codewars.com/kata/59fabc2406d5b638f200004a

"""
import unittest


class SpaceInvadersTest(unittest.TestCase):
    def test_simple(self):
        # test.describe('3 Example Tests')
        example_aliens = [
            [[3, 1, 2, -2, 2, 3, 6, -3, 7, 1]],
            [[5, 2, -2, 3, 1, 0, 4, 8, 3, -2, 5], [1, 4, -1, 0, 3, 6, 1, -3, 1, 2, -4]],
            [[4, 1, -7, -5, 1, 6, 3, -2, 1, 0, 2, 6, 5], [2, 0, 3, -4, 0, 2, -1, 5, -8, -3, -2, -5, 1],
             [1, 2, 0, -6, 4, 7, -2, 4, -4, 2, -5, 0, 4]]]
        example_positions = [[6, 4], [10, 2], [15, 6]]
        example_solutions = [
            [0, 2, 3, 4, 5, 9, 10, 13, 19, 22],
            [1, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 19, 20, 21, 26, 27, 30, 32, 36],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 27, 30, 31, 32, 35, 36, 38,
             40, 43, 45, 56, 58]]

        for aliens, pos, sol in zip(example_aliens, example_positions, example_solutions):
            self.assertEqual(blast_sequence(aliens, pos), sol)

    def test_compare(self):
        a = Alien(0, 0, 0, 5)
        b = Alien(1, 0, 0, -5)
        c = Alien(2, 0, 0, 3)

        self.assertLess(c,a)
        self.assertLess(c,b)
        self.assertLess(b,a)
        self.assertGreater(a,b)


class Alien:
    @property
    def idx(self):
        return self._idx

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def speed(self):
        return self._speed

    def __init__(self, idx, x, y, speed):
        self._idx = idx
        self._x = x
        self._y = y
        self._speed = speed

    def move(self, width):
        if self.speed > 0:
            pos = self.x + self.speed
            if pos >= width:
                self._x = width - (pos % width) - 1
                self._y += 1
                self._speed *= -1
            else:
                self._x = pos
        else:
            pos = self.x + self.speed
            if pos < 0:
                self._x = -1 * pos - 1
                self._y += 1
                self._speed *= -1
            else:
                self._x = pos

    def __lt__(self, other):
        if abs(self.speed) == abs(other.speed):
            return self.speed < other.speed
        return abs(self.speed) < abs(other.speed)

    def __str__(self):
        return str(self.speed)

    def __repr__(self):
        return str(self)


class Board:
    def print_data(self):
        for row in self.data:
            for c in row:
                print(c, end="\t")
            print()
        print("=" * 90)

    def __init__(self, aliens, position):
        self.turn = 0
        self.data = []
        self.aliens = dict()
        self.history = []
        self.shoot_column = position[1]
        for k in range(position[0] + 1):
            self.data.append([])
            for l in range(len(aliens[0])):
                self.data[-1].append([])

        idx = 0
        for i, row in enumerate(aliens):
            for j, c in enumerate(row):
                if c == 0:
                    continue
                alien = Alien(idx,j,i,c)
                self.aliens[idx] = alien
                self.data[i][j].append(alien)
                idx += 1

        # self.data[position[0]][position[1]] = "X"

        # self.print_data()

    def move_aliens(self):
        for alien in self.aliens.values():
            old_x, old_y = alien.x, alien.y
            alien.move(len(self.data[0]))
            for k, a in enumerate(self.data[old_y][old_x]):
                if a.idx == alien.idx:
                    self.data[old_y][old_x].pop(k)
                    break
            self.data[alien.y][alien.x].append(alien)
        # self.print_data()

    def shoot_aliens(self):
        for i in range(len(self.data)-1,-1,-1):
            if len(self.data[i][self.shoot_column]) > 0:
                a = sorted(self.data[i][self.shoot_column], reverse=True)

                for k, o in enumerate(self.data[a[0].y][a[0].x]):
                    if o.idx == a[0].idx:
                        self.data[a[0].y][a[0].x].pop(k)
                        break

                del self.aliens[a[0].idx]

                self.history.append(self.turn)
                break

    def are_aliens_winning(self):
        for i in range(len(self.data[0])):
            if len(self.data[len(self.data) - 1][i]) > 0:
                return True
        return False

    def are_earthlings_winning(self):
        return len(self.aliens) == 0

    def is_game_over(self):
        return self.are_earthlings_winning() or self.are_aliens_winning()

    def run(self):
        while not self.is_game_over():
            self.move_aliens()
            if not self.are_aliens_winning():
                self.shoot_aliens()
            self.turn += 1


def blast_sequence(aliens, position):
    board = Board(aliens, position)
    board.run()
    if board.are_earthlings_winning():
        return board.history
    else:
        return None

if __name__ == "__main__":
    unittest.main()
