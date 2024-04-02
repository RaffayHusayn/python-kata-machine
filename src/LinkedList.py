from typing import Optional
class Node:
    def __init__(self, data):
        self.data: int = data
        self.next: Optional[Node] = None

class LinkedList:
    '''
        it should have 
        1. append 2. prepend 3.show all 4.insert_at_index 5.delete_at_index 6.pop(delete the head) 
    '''

    def __init__(self):
        self.head = self.tail = None
        self.length = 0
    
    # insert a node before head 
    def prepend(self,data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # insert After the tail
    def append(self, data):
        new_node = Node(data)
        if self.length == 0:
            self.head = self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
        self.length += 1

    def insert_at(self, index, data ):
        if index <= self.length: 
            if index == 0 : self.prepend(data)
            elif index == self.length : self.append(data) 
            else:
                one_before = self.traverse(index-1)
                print(f'one before {one_before.data if one_before else None} one before next {one_before.next.data if one_before and one_before.next else None} one before next next {one_before.next.next.data if one_before and one_before.next and one_before.next.next else None}')
                new_node = Node(data)
                if one_before:
                    new_node.next = one_before.next 
                    one_before.next = new_node

    def traverse(self, index)-> Optional[Node]:
        current_node = self.head
        if index <= self.length:
            if current_node:
                current_node = current_node.next
        return current_node
    
    # Traverse all the nodes and return a list containing all in sequence
    def show_all(self):
        current_node = self.head
        all = []
        while current_node:
            all.append(current_node.data)
            current_node = current_node.next
        return all

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(4)
print(ll.show_all())
ll.insert_at(0,1)
print(ll.show_all())


