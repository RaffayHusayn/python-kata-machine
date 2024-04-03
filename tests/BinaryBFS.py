import sys
sys.path.append('/Users/raffay/algo/python-kata-machine')
import unittest

from src.BinaryBFS import create_binary_tree, bfs

class BinaryBFS(unittest.TestCase):

    def test_bfs(self):
        input_nodes_full = [1,2,3,4,5,100, 120, 111, 1]
        input_nodes_empty = []
        tree_full_root = create_binary_tree(input_nodes_full)
        tree_empty_root = create_binary_tree(input_nodes_empty)

        self.assertEqual(bfs(tree_full_root), [1,2,3,4,5,100, 120, 111, 1])
        self.assertEqual(bfs(tree_empty_root), [])

