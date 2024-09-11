"""
Stack Implementation via Linked List (I've never implemented such form before)
"""

from linked_list import LinkedListBasis, Node

# Stack Implementation.

class Stack(LinkedListBasis):
    def __init__(self, head):
        self.head = head

    def push(self, val):
        self.insert(val)
    
    def pop(self):
        self.delete(self.head.val)

    def is_empty(self):
        return self.head is not None

"""
head = Node(0)
stack = Stack(head)
stack.insert(1)
stack.insert(2)
stack.insert(3)
stack.insert(4)
stack.traverse()  # 01234
print("-----")
stack.pop()
stack.traverse()  # 0123
"""

# as we perform operations faster (by doing everything in the very beginning)
# our list is reversed

"""
Holly duck, I guess it's the best implementation of Linked List I've ever done in my Miserable Life ;)
Anyways, it works and It's duckin' brilliant!

I riced my UwUntu btw. It looks sick now!
"""
