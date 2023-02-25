"""

https://www.codewars.com/kata/5856f3ecf37aec45e6000091

"""
import unittest


class CountConnectivityComponentsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(components('''\
+--+--+--+
|     |  |
+  +--+--+
|     |  |
+--+--+--+'''), [(4, 1), (1, 2)])

        self.assertEqual(components('''\
+--+--+--+
|  |     |
+  +--+--+
|  |  |  |
+--+--+--+'''), [(2, 2), (1, 2)])



        self.assertEqual(components('''\
+--+--+--+
|        |
+  +  +  +
|        |
+--+--+--+'''), [(6, 1)])

        self.assertEqual(components('''\
+--+--+--+
|  |  |  |
+--+--+--+
|  |  |  |
+--+--+--+'''), [(1, 6)])


        self.assertEqual(components('''\
+--+--+--+
|  |     |
+  +  +--+
|  |  |  |
+--+--+--+'''), [(3, 1), (2, 1), (1, 1)])

        self.assertEqual(components('''\
+--+--+--+
|  |     |
+  +  +--+
|        |
+--+--+--+'''), [(6, 1)])


def parse_grid(grid):
    lines = grid.splitlines()[1:-1]
    lines = [line[1:-1] for line in lines]

    v = 0
    for i in range(0, len(lines)):
        lines[i] = [c for c in lines[i]]
        if i % 2 == 1:
            for j in range(0, len(lines[i]), 3):
                if lines[i][j] == "-":
                    lines[i][j] = False
                    lines[i][j+1] = False
                else:
                    lines[i][j] = True
                    lines[i][j+1] = True
        else:
            for j in range(0, len(lines[i]), 3):
                if j + 2 < len(lines[i]):
                    if lines[i][j + 2] == "|":
                        lines[i][j + 2] = False
                    else:
                        lines[i][j + 2] = True
                lines[i][j] = v
                lines[i][j+1] = v
                v += 1

    graph = {k: [] for k in range(v)}

    for i in range(0, len(lines), 2):
        for j in range(0, len(lines[0]), 3):
            if i < len(lines) - 2 and lines[i+1][j]:
                graph[lines[i][j]].append(lines[i+2][j])
                graph[lines[i+2][j]].append(lines[i][j])
                # print(lines[i][j], lines[i+1][j], lines[i+2][j])

            if j < len(lines[0]) - 3 and lines[i][j+2]:
                graph[lines[i][j]].append(lines[i][j + 3])
                graph[lines[i][j + 3]].append(lines[i][j])
                # print(lines[i][j], lines[i][j+2], lines[i][j+3])

    return graph


def get_components(graph):
    result = [-1] * len(graph)
    for v in graph.keys():
        stack = [v]
        while stack:
            u = stack.pop()
            if result[u] >= 0:
                continue
            result[u] = v
            for w in graph[u]:
                stack.append(w)
    return result


def components(grid):
    graph = parse_grid(grid)
    graph_components = get_components(graph)
    # print(grid)
    # print(graph)
    # print(graph_components)

    counter = {}
    for v in graph_components:
        if v not in counter:
            counter[v] = 0
        counter[v] += 1

    result = {}
    for v, cnt in counter.items():
        if cnt not in result:
            result[cnt] = 0
        result[cnt] += 1

    return sorted(result.items(), reverse=True)


if __name__ == "__main__":
    unittest.main()
