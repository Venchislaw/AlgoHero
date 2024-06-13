class Node:
    def __init__(self, value, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self, head):
        self.head = head

    def list_all(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.value)
            cur_node = cur_node.next
        return

    def get(self, value):
        cur_node = self.head
        while cur_node:
            if cur_node.value == value:
                return cur_node
            cur_node = cur_node.next

        return None

    def append(self, value):
        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next
        cur_node.next = Node(value)

        return self

    def remove(self, value):
        cur_node = self.head
        while cur_node.next:
            if cur_node.value == value:
                self.head = cur_node.next
                return self
            elif cur_node.next.value == value:
                cur_node.next = cur_node.next.next
                return self

            cur_node = cur_node.next
        return self

    def insert(self, value, index):
        i = 0
        cur_node = self.head

        while cur_node:
            if i+1 == index:
                dummy = cur_node.next
                cur_node.next = Node(value, cur_node.next)
                cur_node.next.next = dummy
                return self
            elif index == 0:
                dummy = self.head
                self.head = Node(value, dummy)
                return self
            i += 1
            cur_node = cur_node.next
        return self


node3 = Node(3, None)
node2 = Node(2, node3)
node1 = Node(1, node2)

linked_list = LinkedList(node1)

linked_list = linked_list.insert(4, 1)
linked_list.list_all()
