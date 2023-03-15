"""

https://www.codewars.com/kata/561bed6a31daa8df7400000e

"""
import unittest


class SquareSumsTest(unittest.TestCase):
    def test_simple(self):
        for i in [15, 23, 25, 300]:
            actual = square_sums_row(i)
            # print(i, actual)
            a = actual[:-1]
            b = actual[1:]
            for x in zip(a, b):
                self.assertEqual(sum(x) ** .5 % 1, 0)
            actual.sort()
            self.assertEqual(actual, list(range(1, i + 1)), 'missing numbers')


def build_graph(n):
    graph = {v: set() for v in range(n + 1)}
    squares = {x*x for x in range(1, n + 1)}

    for v in range(1, n + 1):
        graph[0].add(v)
        graph[v].add(0)

        for u in range(v + 1, n + 1):
            if v + u in squares:
                graph[v].add(u)
                graph[u].add(v)

    return graph


def check_path(graph, node, path=None):
    if path is None:
        path = []

    if node in path:
        return False

    path.append(node)

    if len(graph) == len(path):
        return path

    for next_node in graph[node]:
        test = check_path(graph, next_node, path[:])
        if test:
            return test

    return False

def square_sums_row(n):
    graph = build_graph(n)
    path = check_path(graph, 0)
    return path[1:]

if __name__ == "__main__":
    unittest.main()
