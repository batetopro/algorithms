"""

https://www.codewars.com/kata/551f23362ff852e2ab000037

"""
import unittest


class LongestSlideDownTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]), 23)
        self.assertEqual(longest_slide_down([
            [75],
            [95, 64],
            [17, 47, 82],
            [18, 35, 87, 10],
            [20, 4, 82, 47, 65],
            [19, 1, 23, 75, 3, 34],
            [88, 2, 77, 73, 7, 63, 67],
            [99, 65, 4, 28, 6, 16, 70, 92],
            [41, 41, 26, 56, 83, 40, 80, 70, 33],
            [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
            [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
            [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
            [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
            [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
            [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
        ]), 1074)

def longest_slide_down(pyramid):
    # sum of numbers from top to i'th number in current row
    best_path = [pyramid[0][0]]

    for row in pyramid[1:]:  # after first row
        # the leftmost number of current row
        new_path = [best_path[0] + row[0]]

        for i, num in enumerate(row[1:-1]):  # until rightmost number
            new_path.append(max(best_path[i], best_path[i + 1]) + row[i + 1])

        # the rightmost number of current row
        new_path.append(best_path[-1] + row[-1])

        best_path = new_path[:]

    return max(best_path)

if __name__ == "__main__":
    unittest.main()
