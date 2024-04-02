import unittest
import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')

from src.MergeSort import merge_sort
class MergeSort(unittest.TestCase):
    def test_merge_sort_empty(self):
        unsorted_1= []
        unsorted_2= [100,99,61,22,11,1,-10,-100000]
        unsorted_3= [1,2,3,4,5,6,7,8,-100000]
        self.assertEqual(merge_sort(unsorted_1), sorted(unsorted_1))
        self.assertEqual(merge_sort(unsorted_2), sorted(unsorted_2))
        self.assertEqual(merge_sort(unsorted_3), sorted(unsorted_3))


if __name__== '__main__':
    print('calling the file directly not as a module')
    unittest.main()


