"""

https://www.codewars.com/kata/58c5577d61aefcf3ff000081/

"""
import unittest


class RailFenceCipherTest(unittest.TestCase):
    def test_encode(self):
        self.assertEqual(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3), "WECRLTEERDSOEEFEAOCAIVDEN")
        self.assertEqual(encode_rail_fence_cipher("Hello, World!", 3), "Hoo!el,Wrdl l")
        self.assertEqual(encode_rail_fence_cipher("Hello, World!", 4), "H !e,Wdloollr")
        self.assertEqual(encode_rail_fence_cipher("", 3), "")

    def test_decode(self):
        self.assertEqual(decode_rail_fence_cipher("H !e,Wdloollr", 4), "Hello, World!")
        self.assertEqual(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3), "WEAREDISCOVEREDFLEEATONCE")
        self.assertEqual(decode_rail_fence_cipher("", 3), "")


EMPTY_CELL = "_"
MARKER_CELL = "*"


def encode_rail_fence_cipher(string, n):
    rails = [[EMPTY_CELL for _ in range(len(string))] for __ in range(n)]
    go_down = False
    row, col = 0, 0

    for i, char in enumerate(string):
        rails[row][col] = char
        col += 1
        if row == 0 or row == n - 1:
            go_down = not go_down
        if go_down:
            row += 1
        else:
            row -= 1

    result = []
    for r in rails:
        for c in r:
            if c == EMPTY_CELL:
                continue
            result.append(c)

    return "".join(result)


def decode_rail_fence_cipher(string, n):
    rails = [[EMPTY_CELL for _ in range(len(string))] for __ in range(n)]
    go_down = False
    row, col = 0, 0

    for i in range(len(string)):
        rails[row][col] = MARKER_CELL

        col += 1
        if row == 0 or row == n - 1:
            go_down = not go_down
        if go_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(n):
        for j in range(len(string)):
            if rails[i][j] != MARKER_CELL:
                continue
            if index < len(string):
                rails[i][j] = string[index]
                index += 1

    result = []
    go_down = False
    row, col = 0, 0
    for i in range(len(string)):
        if rails[row][col] != MARKER_CELL:
            result.append(rails[row][col])
        col += 1
        if row == 0 or row == n - 1:
            go_down = not go_down
        if go_down:
            row += 1
        else:
            row -= 1

    return "".join(result)





if __name__ == "__main__":
    unittest.main()
