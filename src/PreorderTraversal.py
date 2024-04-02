from typing import Optional

class Node:
    def __init__(self, val):
        self.val = val
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
    

input_val = [1,2,3,4,5,6]
def create_tree(nodeVal:list[int]):
    head = Node(nodeVal[0])
    queue = [head]
    index = 1
    # queue is not empty we should still be running the loop
    while queue :
        node = queue.pop(0)

        if index < len(nodeVal):
            new_node = Node(nodeVal[index])
            node.left = new_node 
            queue.append(new_node)
            index +=1

        if index < len(nodeVal):
            new_node = Node(nodeVal[index])
            node.right = new_node 
            queue.append(new_node)
            index +=1
    return head 

# first_tree = create_tree(input_val)

def traverse(head):
    if head == None : return 

    print(head.val)
    traverse(head.left)
    traverse(head.right)
# traverse(first_tree)

def make_tree(input:list[int]):
    head = Node(input[0])
    queue = [head]
    index =1
    while queue:
        queue_node = queue.pop(0)

        # add the left child node
        if index < len(input):
            new_node = Node(input[index])
            queue_node.left = new_node
            queue.append(new_node)
            index +=1
        
        if index < len(input):
            new_node = Node(input[index])
            queue_node.right = new_node
            queue.append(new_node)
            index +=1
    return head    

def preorder(head):
    if head == None : return 

    print(head.val)
    preorder(head.left)
    preorder(head.right)

def inorder(head):
    if head == None : return 
    inorder(head.left)
    print(head.val)
    inorder(head.right)

def postorder(head):
    if head == None : return 
    postorder(head.left)
    postorder(head.right)
    print(head.val)

first_tree = make_tree(input_val)
print('WAlk')
preorder(first_tree)

def breath_first_search(head):
    head_node  = head
    queue = [head_node]
    while queue:
        new_node = queue.pop(0)
        print(new_node.val)
        if new_node.left != None:
            queue.append(new_node.left)
    
        if new_node.right != None:
            queue.append(new_node.right)
    
print('BFS')
breath_first_search(first_tree)