class ListNode:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_
        

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = None
        
    def traverse(self):
        cur = self.head
        
        while cur.next:
            cur = cur.next
        self.tail = cur
    
    def traverse_print(self):
        cur = self.head
        
        while cur:
            print(cur.value)
            cur = cur.next
        self.tail = cur
    
            
    def insert_to_the_end(self, val):
        if not self.tail:
            self.traverse()
        
        self.tail.next = ListNode(value=val, next_=None)
        self.tail = ListNode(value=val, next_=None)
        
        
start_node = ListNode(value=1)
linked_list = LinkedList(start_node)
linked_list.traverse_print()
linked_list.insert_to_the_end(2)
linked_list.traverse_print()
