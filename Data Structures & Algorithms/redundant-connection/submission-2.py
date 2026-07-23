class UnionFind:

    def __init__(self, n):
        self.par = [i for i in range(n+1)]
        self.rank = [0 for i in range(n+1)]
    
    def union(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a == par_b:
            return False
        if self.rank[par_a] < self.rank[par_b]:
            self.par[par_a] = par_b
            self.rank[par_b] = max(1 + self.rank[par_a], self.rank[par_b])
        else:
            self.par[par_b] = par_a
            self.rank[par_a] = max(1 + self.rank[par_b], self.rank[par_a])
        # print(self.rank, self.par, a, b)
        return True
    
    def find(self, a):
        if self.par[a] == a:
            return a
        self.par[a] = self.find(self.par[a])
        return self.par[a]
        

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = 0
        for e in edges:
            n = max(n, max(e))    
        uf = UnionFind(n)

        red = []
        for edge in edges:
            if not uf.union(edge[0], edge[1]):
                red.append(edge)
            
        return red[-1]
        
        