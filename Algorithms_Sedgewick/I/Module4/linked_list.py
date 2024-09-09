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

        while tmp.next.next and tmp.next.val != val:
            tmp = tmp.next
        
        
        tmp.next = tmp.next.next

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