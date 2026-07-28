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
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

            edges = []
            for i in range(0, len(points)):
                for j in range(i, len(points)):
                    edges.append([abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]), i, j])

            heapq.heapify(edges)

            dsu = UnionFind(len(points))

            ans = 0
            while edges:
                edge = heapq.heappop(edges)      
                if dsu.union(edge[1], edge[2]):
                    ans += edge[0]
            return ans





        