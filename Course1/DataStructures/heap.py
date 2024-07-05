class Heap:
    def __init__(self):
        self.heap = [0]


    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while val < self.heap[i // 2]:
            self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

        return self


heap = Heap()
heap = heap.push(5)
heap = heap.push(3)
heap = heap.push(1)

print(heap.heap)
