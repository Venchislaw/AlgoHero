# Queue data structure implementation using Linked List

from linked_list import LinkedListBasis, Node

class Queue(LinkedListBasis):
    def __init__(self, head):
        self.head = head
        self.first = head

    def enque(self, val):
        self.insert(val)
    
    def delete(self, val):
        super().delete(val)
        tmp = self.head
        while tmp:
            tmp = tmp.next
        self.first = tmp

    def deque(self):
        self.delete(self.first)

"""
head = Node(0)
queue = Queue(head)
queue.enque(1)
queue.enque(2)
queue.enque(3)
queue.enque(4)
queue.enque(5)
queue.enque(6)
queue.traverse()
queue.deque()
print("-"*60)
queue.traverse()
queue.deque()
queue.deque()
queue.deque()
queue.deque()
queue.deque()
print("-"*60)
queue.traverse()
"""