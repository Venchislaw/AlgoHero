# Old solution (root is the largest):
"""
class WeightedQuickUnion:
    def __init__(self, N):
        self.roots = [i for i in range(N)]

    def root(self, i):
        while i != self.roots[i]:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        return i

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)

        if p_root == q_root: return

        if p_root > q_root:
            self.roots[q_root] = p_root
        
        else:
            self.roots[p_root] = q_root

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def find(self, i):
        return self.root(i)  # in this implementation root has the greatest value
    

qckunion = WeightedQuickUnion(10)
qckunion.union(0, 5)

qckunion.union(6, 5)

qckunion.union(1, 2)
qckunion.union(7, 2)
qckunion.union(8, 3)
qckunion.union(3, 4)
qckunion.union(4, 9)
print(qckunion.roots)
print(qckunion.find(1))
"""

# New Solution using more memory.

class QuickUnionFind:
    def __init__(self, N):
        self.largest = [i for i in range(N)]
        self.sizes = [1 for _ in range(N)]
        self.roots = [i for i in range(N)]

    def root(self, i):
        while i != self.roots[i]:
            self.roots[i] = self.roots[self.roots[i]]
            i = self.roots[i]
        return i

    def union(self, p, q):
        root_p = self.root(p)
        root_q = self.root(q)

        if root_p == root_q:
            return
    
        if self.sizes[root_p] < self.sizes[root_q]:
            self.roots[root_p] = root_q
            self.sizes[root_q] += self.sizes[root_p]
            if self.largest[root_q] < self.largest[root_p]:
                self.largest[root_q] = self.largest[root_p]
        else:
            self.roots[root_q] = root_p
            self.sizes[root_p] += self.sizes[root_q]
            if self.largest[root_p] < self.largest[root_q]:
                self.largest[root_p] = self.largest[root_q]
            
        
    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
    def find(self, i):
        return self.largest[self.root(i)]


qckunion = QuickUnionFind(10)
qckunion.union(0, 5)

qckunion.union(6, 5)

qckunion.union(1, 2)
qckunion.union(7, 2)
qckunion.union(8, 3)
qckunion.union(3, 4)
qckunion.union(4, 9)
print(qckunion.roots)
print(qckunion.find(4))  # 9

# HOLLE... It works! Pog
