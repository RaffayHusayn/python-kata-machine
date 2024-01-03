import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')
import unittest
import random

from src.Daily import quick_sort_1, quick_sort_2, bubble_sort, binary_search 

class Daily(unittest.TestCase):

    # staticmethod is one which doesn't take either self or cls(this will be classmethod)
    @staticmethod
    def create_random_list(size):
        random_list= []
        for i in range(size):
            random_list.append(random.randint(1, 1000))
        return random_list

    @staticmethod
    def element_search_python(haystack, needle):
        try:
            return haystack.index(needle)
        except:
            return -1
    
    def test_binary_search_1(self):
        haystack = sorted(self.create_random_list(1000))
        needle = random.randint(1,1500) # if the number is generated outside of 1000 then it won't be present
        message = "\n\n *************** Binary Search Test (1) failed ***************** \n\n"
        self.assertEqual(binary_search(haystack, needle), self.element_search_python(haystack, needle), message)
     
    def test_binary_search_empty_array_2(self):
        haystack = []
        message = "\n\n *************** Binary Search Test (2) failed ***************** \n\n"
        self.assertEqual(binary_search(haystack, 1), -1, message)

    def test_bubble_sort(self):
        unsorted_list = self.create_random_list(1000)
        sorted_list = sorted(unsorted_list)
        message = "\n\n *************** Bubble Sort Test (1) failed ***************** \n\n"
        self.assertEqual(bubble_sort(unsorted_list), sorted_list, message)

    def test_quick_sort_1(self):
        unsorted_list = self.create_random_list(1000)
        sorted_list = sorted(unsorted_list)
        message = "\n\n *************** Quick Sort Test (1) failed ***************** \n\n"
        self.assertEqual(quick_sort_1(unsorted_list), sorted_list, message)

    def test_quick_sort_2(self):
        unsorted_list = self.create_random_list(1000)
        sorted_list = sorted(unsorted_list)
        message = "\n\n *************** Quick Sort Test (2) failed ***************** \n\n"
        self.assertEqual(quick_sort_2(unsorted_list, 0, len(unsorted_list)-1), sorted_list, message)

if __name__ == '__main__':
    # this allows me to run `python -m tests.Daily`
    # instead of `python -m unittest tests.Daily`
    unittest.main()

    