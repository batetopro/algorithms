import unittest


class RecoverSecretTest(unittest.TestCase):
    def test_simple(self):
        secret = "whatisup"
        triplets = [
            ['t', 'u', 'p'],
            ['w', 'h', 'i'],
            ['t', 's', 'u'],
            ['a', 't', 's'],
            ['h', 'a', 'p'],
            ['t', 'i', 's'],
            ['w', 'h', 's']
        ]
        self.assertEqual(recoverSecret(triplets), secret)


def recoverSecret(triplets):
    pass


if __name__ == "__main__":
    unittest.main()