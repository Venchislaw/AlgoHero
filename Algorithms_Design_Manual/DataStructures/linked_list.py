# first time I implemented everything with recursion


class ListNode:
    def __init__(self, val, next_):
        self.val = val
        self.next = next_
        

class LinkedList:
    def __init__(self, head):
        self.head = head
        
    def add(self, head, val):
        if not head:
            return ListNode(val, next_=None)
        
        else:
            head.next = self.add(head.next, val)
        
        return head
        
    def traverse(self, head):
        if not head:
            return
        else:
            print(head.val)
            self.traverse(head.next)
            
    
    def search(self, head, target):
        if not head:
            return None
        elif head.val == target:
            return head
        else:
            return self.search(head.next, target)
        
        

head = ListNode(0, None)
list_ = LinkedList(head)

for i in range(1, 5+1):
    list_.add(head, i)
    
list_.traverse(head)
print(list_.search(head, 5))