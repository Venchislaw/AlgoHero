class WeightedQuickUnion:
    def __init__(self, N):
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
        
        if self.sizes[root_p] > self.sizes[root_q]:
            self.roots[root_q] = self.roots[root_p]
            self.sizes[root_p] += self.sizes[root_q]
        
        else:
            self.roots[root_p] = self.roots[root_q]
            self.sizes[root_q] += self.sizes[root_p]
        
    
    def connected(self, p, q):
        return self.root(p) == self.root(q)



class Percolation:
    def __init__(self, N):
        self.N = N
        self.grid = [[False for _ in range(N)] for _ in range(N)]  # Keeps track of open sites
        self.qu = WeightedQuickUnion(N * N + 2)  # N*N sites + 2 virtual sites
        self.virtual_top = N * N  # Virtual top site ID
        self.virtual_bottom = N * N + 1  # Virtual bottom site ID

        # Connect top row to virtual top site
        for i in range(N):
            self.qu.union(self.virtual_top, self.get_index(0, i))
        
        # Connect bottom row to virtual bottom site
        for i in range(N):
            self.qu.union(self.virtual_bottom, self.get_index(N-1, i))

    def get_index(self, row, col):
        return row * self.N + col
    
    def is_open(self, row, col):
        return self.grid[row][col]

    def open(self, row, col):
        if not self.is_open(row, col):
            self.grid[row][col] = True
            index = self.get_index(row, col)

            # Connect to open neighboring sites
            neighbors = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for r, c in neighbors:
                if 0 <= r < self.N and 0 <= c < self.N and self.is_open(r, c):
                    self.qu.union(index, self.get_index(r, c))
    
    def percolates(self):
        # Check if virtual top is connected to virtual bottom
        return self.qu.connected(self.virtual_top, self.virtual_bottom)

