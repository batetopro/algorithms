"""

https://www.codewars.com/kata/52bef5e3588c56132c0003bc

"""
import unittest


class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n


class TreeByLevelsTest(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(tree_by_levels(None), [])
        self.assertEqual(tree_by_levels(
            Node(Node(None, Node(None, None, 4), 2), Node(Node(None, None, 5), Node(None, None, 6), 3), 1)),
                           [1, 2, 3, 4, 5, 6])


def tree_by_levels(root):
    if root is None:
        return []

    queue = [root]
    result = []

    while len(queue):
        node = queue.pop(0)
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


if __name__ == "__main__":
    unittest.main()