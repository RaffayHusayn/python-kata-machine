import unittest
import random
import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')
from src.BubbleSort import bubble_sort, bubble_sort_real

class BubbleSort(unittest.TestCase):
    def create_random_list(self, size:int)-> list[int]:
        unsorted = []
        for i in range(size):
            unsorted.append(random.randint(0,1231))
        return unsorted
    def test_bubble_sort(self):
        unsorted_list = self.create_random_list(101)
        # self.assertEqual(bubble_sort(unsorted_list), sorted(unsorted_list))
        self.assertEqual(bubble_sort_real(unsorted_list), sorted(unsorted_list))

if __name__ == '__main__':
    print("running the tests by directly calling the file and running the code below to run the test cases")
    unittest.main()