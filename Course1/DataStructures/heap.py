class Heap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while self.heap[i] < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2
        return self.heap

    def pop(self):
        # edge cases
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()

        value_popped = self.heap[1]

        i = len(self.heap) - 1
        self.heap[1] = self.heap[i]
        i = 1

        while i * 2 < len(self.heap):
            # right value:
            if (i * 2 + 1 < len(self.heap) and
                    (self.heap[i * 2 + 1] < self.heap[i * 2]
                     and self.heap[i] > self.heap[i * 2 + 1])):
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1
            # left value:
            elif self.heap[i] > self.heap[i * 2]:
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i *= 2
            else:
                break

        return value_popped


heap = Heap()
heap.push(1)
heap.push(3)
heap.push(2)
print(heap.push(0.5))

print(heap.pop())
print(heap.pop())
