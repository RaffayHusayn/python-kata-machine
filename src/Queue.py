from typing import Optional
class Node:
    def __init__(self, val):
        self.value: int = val
        self.next: Optional[Node] = None 

class Queue:
    def __init__(self):
        self.length = 0
        self.head = self.tail = None
    
    def enqueue(self, val:int):
        new_node = Node(val)
        if self.head == None:
            self.head = self.tail = new_node
        else:
            if self.tail:
                self.tail.next = new_node
                self.tail = new_node
        self.length +=1

    def deque(self):
        if self.head == None:
            return None
        else:
            head = self.head
            self.head = self.head.next
            self.length -= 1
            return head.value

    def peek(self):
        return self.head.value if self.head else None

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.deque())
print(q.deque())
q.enqueue(4)
print(q.deque())
print(q.peek())

        







