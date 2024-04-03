import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')
import unittest

from src.BinaryDFS import create_binary_tree, preorder, inorder, postorder

class BinaryDFS(unittest.TestCase):

    tree_full = create_binary_tree([1,2,3,4,5,6,1,2,1])
    tree_empty = create_binary_tree([])

    def test_postorder(self):
        self.assertEqual(postorder(self.tree_full), [2,1,4,5,2,6,1,3,1])
        self.assertEqual(postorder(self.tree_empty), [])

    def test_inorder(self):
        self.assertEqual(inorder(self.tree_full), [2,4,1,2,5,1,6,3,1])
        self.assertEqual(inorder(self.tree_empty), [])

    def test_preorder(self):
        self.assertEqual(preorder(self.tree_full), [1,2,4,2,1,5,3,6,1])
        self.assertEqual(preorder(self.tree_empty), [])




