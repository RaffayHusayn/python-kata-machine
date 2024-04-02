import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')

import unittest
from src.LinkedList import LinkedList, Node
from random import randint

class TestLinkedList(unittest.TestCase):
    def test_all_elements(self):
        new_list = LinkedList()
        test_array = []
        total_element_append = randint(5,15)
        total_element_prepend = randint(5,15)
        for i in range(total_element_append):
            new_list.append(i)
            test_array.append(i)
        for i in range(total_element_prepend):
            new_list.prepend(i)
            test_array.insert(0, i)
        self.assertEqual(new_list.show_all(), test_array)
        self.assertEqual(new_list.head.data if new_list.head else None, test_array[0])
        self.assertEqual(new_list.tail.data if new_list.tail else None, test_array[len(test_array)-1])
        
    def test_all_elements_empty(self):
        new_list = LinkedList()
        expected = []
        self.assertEqual(new_list.show_all(), expected)
        self.assertEqual(new_list.head, None)
        self.assertEqual(new_list.tail, None)

    def test_head_and_tail_one_element(self):
        new_list = LinkedList()
        expected = 2
        new_list.append(expected)
        self.assertEqual(new_list.head.data if new_list.head else None, expected )
        self.assertEqual(new_list.tail.data if new_list.tail else None, expected )

        new_list_2 = LinkedList()
        expected_2 = 3
        new_list_2.prepend(expected_2)
        self.assertEqual(new_list_2.head.data if new_list_2.head else None, expected_2)
        self.assertEqual(new_list_2.tail.data if new_list_2.tail else None, expected_2)



        






