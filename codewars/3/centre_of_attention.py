"""

https://www.codewars.com/kata/5324945e2ece5e1f32000370

"""
import unittest


class CentreOfAttentionTest(unittest.TestCase):
    def test_simple(self):
        image = Central_Pixels_Finder([1, 1, 4, 4, 4, 4, 2, 2, 2, 2,
                                       1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                                       1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
                                       1, 1, 1, 1, 1, 3, 2, 2, 2, 2,
                                       1, 1, 1, 1, 1, 3, 3, 3, 2, 2,
                                       1, 1, 1, 1, 1, 1, 3, 3, 3, 3], 10, 6)

        # Only one red pixel has the maximum depth of 3:
        red_ctr = [32]
        self.assertEqual(image.central_pixels(1), red_ctr)

        # Multiple blue pixels have the maximum depth of 2:
        blue_ctr = [16, 17, 18, 26, 27, 28, 38]
        self.assertEqual(sorted(image.central_pixels(2)), blue_ctr)

        # All the green pixels have depth 1, so they are all "central":
        green_ctr = [35, 45, 46, 47, 56, 57, 58, 59]
        self.assertEqual(sorted(image.central_pixels(3)), green_ctr)

        # Similarly, all the purple pixels have depth 1:
        purple_ctr = [2, 3, 4, 5]
        self.assertEqual(sorted(image.central_pixels(4)), purple_ctr)

        # There are no pixels with colour 5:
        non_existent_ctr = []
        self.assertEqual(image.central_pixels(5), non_existent_ctr)

        # Changing one pixel can make a big difference to the result:
        image.pixels[32] = 3
        self.assertEqual(sorted(image.central_pixels(1)), [11, 21, 41, 43])

class Image:
    def __init__(self, data, w, h):
        self.pixels = data
        self.width = w
        self.height = h

    def get_pixel(self, x, y):
        return self.pixels[self.width * y + x]

    def print_pixels(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.get_pixel(x, y), end="\t")
            print()
        print("=" * 50)


class Central_Pixels_Finder(Image):
    def __init__(self, data, w, h):
        super().__init__(data, w, h)
        self.depth = []
        self.directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


    def get_depth(self, x, y):
        return self.depth[self.width * y + x]

    def set_depth(self, x, y, value):
        self.depth[self.width * y + x] = value

    def print_depth(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.get_depth(x, y), end="\t")
            print()
        print("=" * 50)

    def get_edges(self, colour):
        edges = []
        for y in range(self.height):
            for x in range(self.width):
                if self.get_pixel(x, y) != colour:
                    continue

                if 0 == x or x == self.width - 1 or 0 == y or y == self.height - 1:
                    edges.append((x, y))
                    continue

                for direction in self.directions:
                    i = x + direction[0]
                    j = y + direction[1]
                    if i < 0 or i >= self.width or j < 0 or j >= self.height:
                        continue

                    if self.get_pixel(i, j) != colour:
                        edges.append((x, y))
                        break
        return edges

    def fill_area(self, q, colour):
        while q:
            x, y = q.pop(0)
            for direction in self.directions:
                i = x + direction[0]
                j = y + direction[1]
                if i < 0 or i >= self.width or j < 0 or j >= self.height:
                    continue
                if self.get_pixel(i, j) != colour:
                    continue

                d = self.get_depth(i, j)
                if d == -1 or d > self.get_depth(x,y) + 1:
                    self.set_depth(i, j, self.get_depth(x,y) + 1)
                    q.append((i, j))

    def get_pixels_with_max_depth(self, colour):
        max_depth = 0
        pixels = []
        for y in range(self.height):
            for x in range(self.width):
                if self.get_pixel(x, y) != colour:
                    continue
                if max_depth < self.get_depth(x, y):
                    max_depth = self.get_depth(x, y)
                    pixels = []
                if self.get_depth(x, y) == max_depth:
                    pixels.append(self.width * y + x)
        return pixels

    def central_pixels(self, colour):
        self.depth = [-1] * (self.width * self.height)
        q = self.get_edges(colour)
        for x, y in q:
            self.set_depth(x, y, 1)

        self.fill_area(q, colour)

        return self.get_pixels_with_max_depth(colour)


if __name__ == "__main__":
    unittest.main()