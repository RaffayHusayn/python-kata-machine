'''
This file contains Depth First Search algorithms for Binary Tree Traversal.
It includes: 
1. PreOrder
2. InOrder
3. PostOrder
'''
from typing import Optional, List
class Node:
    def __init__(self, val):
        self.val: int = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None

# Creates a balanced binary tree
def create_binary_tree(input : List[int])-> Node|None:
    if len(input) == 0 : return None
    root = Node(input[0])
    queue = [root]
    index = 1

    while queue:
        new_node = queue.pop(0)

        if index < len(input):
            left_child = Node(input[index])
            new_node.left = left_child
            queue.append(left_child)
            index +=1
        
        if index < len(input):
            right_child = Node(input[index])
            new_node.right = right_child
            queue.append(right_child)
            index +=1

    return root

preorder_order= []
def preorder(node:Node|None):
    if node == None: return []

    preorder_order.append(node.val)
    preorder(node.left)
    preorder(node.right)
    return preorder_order

inorder_order = []
def inorder(node: Node|None):
    if node == None : return []

    inorder(node.left)
    inorder_order.append(node.val)
    inorder(node.right)
    return inorder_order

postorder_order = []
def postorder(node: Node| None):
    if node == None : return []  

    postorder(node.left)
    postorder(node.right)
    postorder_order.append(node.val)
    return postorder_order
