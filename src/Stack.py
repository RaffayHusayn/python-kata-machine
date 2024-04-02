# stack is basically last in first out
from typing import Optional
class Node:
    def __init__(self, val) :
        self.value: int = val
        self.previous: Optional[Node] = None

class Stack:
    def __init__(self):
        self.length = 0 
        self.head = None

    def push(self, val):
        """ 
            Steps:
            1. Create a new Node with the given value
            2. Point the new Node previous to the head
            3. Point the head to the new node
        """
        new_node = Node(val)
        new_node.previous = self.head
        self.head = new_node
        self.length += 1

    def pop(self):
        """
            steps:
            1. if head is None then I guess do nothing
            2. Store the value of head to an output node
            3. point head to head.previous
            4. return output node 
            5. Adjust length
        """
        if self.head == None:
            return None
        else:
            return_node = self.head
            self.head = self.head.previous 
            self.length -=1
            return return_node.value

    def show_all(self):
        all_nodes = []
        current = self.head
        while current != None:
            all_nodes.append(current.value)
            current = current.previous
        return all_nodes 