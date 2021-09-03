import unittest

from main import add

class Tests(unittest.TestCase):

    def test_pass(self):
        expected = 2
        actual = add(1, 1)
        self.assertEqual(expected, actual)

    def test_fail(self):
        expected = 3
        actual = add(1, 1)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
