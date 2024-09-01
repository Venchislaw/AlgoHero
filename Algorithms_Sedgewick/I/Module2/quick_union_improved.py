class WeightedQuickUnion:
    def __init__(self, N) -> None:
        self.tree_sizes = [1 for _ in range(N)]  # monitors tree size
        self.roots = [i for i in range(N)]

    def root(self, i) -> int:
        while self.roots[i] != i:
            # paths compression
            self.roots[i] = self.roots[self.roots[i]]
            # root tmp update
            i = self.roots[i]
        
        return i

    def union(self, p, q) -> None:
        root_p = self.root(p)
        root_q = self.root(q)

        # if nodes are connected already
        if root_p == root_q:
            return
        
        # connect smaller tree to the larger (to avoid imbalanced trees)
        if self.tree_sizes[root_p] < self.tree_sizes[root_q]:
            self.roots[root_p] = root_q
            self.tree_sizes[root_q] += self.tree_sizes[root_p]
        else:
            self.roots[root_q] = root_p
            self.tree_sizes[root_p] += self.tree_sizes[root_q]

    def connected(self, p, q):
        return self.root(p) == self.root(q)
    
# Same test cases as for QuickFind


qckunion = WeightedQuickUnion(10)
qckunion.union(0, 5)

qckunion.union(6, 5)
qckunion.union(1, 2)
qckunion.union(7, 2)
qckunion.union(8, 3)
qckunion.union(3, 4)
qckunion.union(4, 9)

print(qckunion.connected(0, 6))  # expected: True; output: True
print(qckunion.roots)  # [0, 1, 1, 8, 8, 0, 0, 1, 8, 8]

print(qckunion.root(4))  # 8

# And this is brilliant
# Gem