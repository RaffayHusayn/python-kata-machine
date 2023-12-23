import unittest
import sys
sys.path.append("/Users/raffay/algo/python-kata-machine/src")
from ..src.BinarySearch import binary_search

class TestBinarySearch(unittest.TestCase):

    haystack  = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420];

    def test_binary_search(self):
        self.assertEqual(binary_search(self.haystack, 69), True)
        self.assertEqual(binary_search(self.haystack, 1336), False)
        self.assertEqual(binary_search(self.haystack, 69420), True)
        self.assertEqual(binary_search(self.haystack, 69421), False)
        self.assertEqual(binary_search(self.haystack, 1), True)
        self.assertEqual(binary_search(self.haystack, 0), False)

if __name__ == '__main__':
    print("running the tests from a script not importing as a module")
    unittest.main()