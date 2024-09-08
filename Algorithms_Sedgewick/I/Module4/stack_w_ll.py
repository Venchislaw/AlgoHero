"""
Stack Implementation via Linked List (I've never implemented such form before)
"""

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    

class LinkedListBasis:
    def __init__(self, head):
        self.head = head
    
    # insert to the beginning
    def insert(self, val):
        list_ = self.head
        self.head = Node(val, list_)

    def delete(self, val):
        if val == self.head.val:
            self.head = self.head.next
            return
        
        tmp = self.head

        while tmp.next.val != val:
            tmp = tmp.next
        
        if tmp.next.next:
            tmp.next = tmp.next.next
        else:
            tmp.next = None

    # inversed traverse
    def traverse(self, head=None):
        if not head:
            head = self.head
        
        if not head.next:
            print(head.val)
            return

        self.traverse(head.next)
        print(head.val)

# Just some testing:
"""        
head = Node(1)
ll = LinkedListBasis(head)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.insert(6)
ll.traverse()  # 123456
print("-------")
ll.delete(5)
ll.traverse()  # 12346
print("-------")
ll.delete(6)
ll.traverse()  # 1234
print("-------")
ll.delete(1)
ll.traverse()  # 234
"""

# Stack Implementation.

class Stack(LinkedListBasis):
    def __init__(self, head):
        self.head = head

    def push(self, val):
        self.insert(val)
    
    def pop(self):
        self.delete(self.head.val)


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

# as we perform operations faster (by doing everything in the very beginning)
# our list is reversed

"""
Holly duck, I guess it's the best implementation of Linked List I've ever done in my Miserable Life ;)
Anyways, it works and It's duckin' brilliant!

I riced my UwUntu btw. It looks sick now!
"""