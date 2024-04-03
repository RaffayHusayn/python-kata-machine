from typing import Optional, List
class Node:
    def __init__(self, val):
        self.val:int = val
        self.left: Optional[Node] =None 
        self.right: Optional[Node] =None

def create_binary_tree(input:List[int])->Node|None:
    if len(input) == 0: return None
    root = Node(input[0])
    queue = [root]
    index = 1

    while queue:
        new_node = queue.pop(0)

        if index < len(input):
            left_node = Node(input[index])
            new_node.left = left_node
            index +=1
            queue.append(left_node)

        if index < len(input):
            right_node = Node(input[index])
            new_node.right = right_node
            index +=1
            queue.append(right_node)
    return root

def bfs(root:Node|None):
    if not root: return []  
    queue = [root]
    bfs_order = []
    while queue:
        new_node = queue.pop(0)
        bfs_order.append(new_node.val)
        print(new_node.val)
        if new_node.left != None:
            queue.append(new_node.left)
        if new_node.right != None:
            queue.append(new_node.right)
    return bfs_order
        
input = [1,2,3,4,5,6,6,7]
tree = create_binary_tree(input)
bfs(None)