"""

https://www.codewars.com/kata/54cf7f926b85dcc4e2000d9d

"""
import unittest


class HuffmanEncodingTest(unittest.TestCase):
    def test_simple(self):
        def test_len(res):
            self.assertIsNotNone(res)
            self.assertEqual(len(res), 10)
        fs = frequencies("aaaabcc")
        test_len(encode(fs, "aaaabcc"))

        self.assertEqual(encode(fs, []), '')
        self.assertEqual(decode(fs, []), '')

        def test_enc_len(fs, strs, lens):
            def enc_len(s):
                return len(encode(fs, s))
            self.assertEqual(list(map(enc_len, strs)), lens)

        test_enc_len([('a', 1), ('b', 1)], ["a", "b"], [1, 1])
        test_enc_len([('a', 1), ('b', 1), ('c', 2)], ["a", "b", "c"], [2, 2, 1])

        s = "aaaabcc"
        fs = frequencies(s)
        self.assertEqual(sorted(fs), [("a", 4), ("b", 1), ("c", 2)])
        test_enc_len(fs, [s], [10])
        self.assertEqual(encode(fs, ""), "")
        self.assertEqual(decode(fs, ""), "")

        self.assertEqual(encode([], ""), None)
        self.assertEqual(decode([], ""), None)
        self.assertEqual(encode([('a', 1)], ""), None)
        self.assertEqual(decode([('a', 1)], ""), None)

    def test_enc_decode(self):
        messages = ["vt", "ins", "bszx", "vsmef", "ktiyvb", "nziwcrp"]
        for message in messages:
            freqs = frequencies(message)
            encoded = encode(freqs, message)
            self.assertEqual(decode(freqs, encoded), message)


class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        # symbol name (character)
        self.symbol = symbol

        # frequency of symbol
        self.freq = freq

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''

    def __lt__(self, nxt):
        return self.freq < nxt.freq

def build_huffman_tree(freqs):
    import heapq

    nodes = []
    for item in freqs:
        heapq.heappush(nodes, Node(item[0], item[1]))

    while len(nodes) > 1:
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        left.huff = "0"
        right.huff = "1"

        new_node = Node(
            symbol=left.symbol + right.symbol,
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        heapq.heappush(nodes, new_node)

    return nodes[0]

def iterate_huffman_codes(freqs):
    q = [(build_huffman_tree(freqs), "")]
    while len(q):
        node, code = q.pop(0)
        is_terminal = True
        if node.left:
            q.append((node.left, code + node.huff))
            is_terminal = False

        if node.right:
            q.append((node.right, code + node.huff))
            is_terminal = False

        if is_terminal:
            yield node.symbol, code + node.huff

def build_enc_codes(freqs):
    result = {}
    for symbol, code in iterate_huffman_codes(freqs):
        result[symbol] = code
    return result

def build_dec_codes(freqs):
    result = {}
    for symbol, code in iterate_huffman_codes(freqs):
        result[code] = symbol
    return result


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s):
    freqs = {}
    for c in s:
        if c not in freqs:
            freqs[c] = 0
        freqs[c] += 1
    return freqs.items()


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
def encode(freqs, s):
    if len (freqs) <= 1:
        return None

    codes = build_enc_codes(freqs)
    result = []
    for letter in s:
        result.append(codes[letter])
    return "".join(result)


# takes [ [str, int] ], str (with "0" and "1"); returns: str
def decode(freqs, bits):
    if len (freqs) <= 1:
        return None
    codes = build_dec_codes(freqs)
    message = []
    q = ""
    for b in bits:
        q += b
        if q in codes:
            message.append(codes[q])
            q = ""

    if q and q in codes:
        message.append(codes[q])
        q = ""

    return "".join(message)


if __name__ == "__main__":
    unittest.main()
