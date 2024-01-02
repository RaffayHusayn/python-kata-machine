import unittest
import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')

import random
from src.QuickSort import quick_sort_inplace, quick_sort_split_array, quick_sort_split_array_one_param
class QuickSort(unittest.TestCase):
    def create_random_list(self, size):
        l= []
        for i in range(size):
            l.append(random.randint(0,10002))
        return l

    def test_quick_sort_inplace(self):
        unsorted = self.create_random_list(40)
        self.assertEqual(quick_sort_inplace(unsorted,0 , len(unsorted)-1), sorted(unsorted))

    def test_quick_sort_split_array(self):
        unsorted = self.create_random_list(100)
        print(quick_sort_inplace(unsorted, 0 , len(unsorted)-1))
        self.assertEqual(quick_sort_split_array(unsorted, 0 , len(unsorted)-1), sorted(unsorted) )
        
    def test_quick_sort_split_array_one_param(self):
        unsorted = self.create_random_list(1000)
        self.assertEqual(quick_sort_split_array_one_param(unsorted), sorted(unsorted))



if __name__== '__main__':
    print('calling the file directly not as a module')
    unittest.main()


