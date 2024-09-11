"""
Queue with two stacks.
Implement a queue with two stacks so that each queue operations
takes a constant amortized number of stack operations.
"""


class Queue_w_Stack:
    def __init__(self):
        # Python Arrays work as Stacks out of the box
        self.inbox = []
        self.outbox = []

    def enqueue(self, elem):
        # put element on top of the stack
        self.inbox.append(elem)

    def dequeue(self):
        if len(self.outbox) == 0:
            while len(self.inbox) > 0:
                # We add the last (popped) element from the inbox to the bottom of the outbox stack
                # So pop() for this stack outputs the first element (FIFO)
                self.outbox.append(self.inbox.pop())
        
        return self.outbox.pop()

   
q = Queue_w_Stack()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
print(q.dequeue())  # 1
print(q.dequeue())  # 2
print(q.dequeue())  # 3
print(q.dequeue())  # 4


# EZ PEZ
