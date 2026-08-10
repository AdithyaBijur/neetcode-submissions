class UnionFind:

    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def union(self,a,b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a == par_b:
            return False

        if self.rank[par_a] > self.rank[par_b]:
            self.parent[par_b] = par_a
            self.rank[par_a] = max(self.rank[par_a], self.rank[par_b] + 1)
        else:
            self.parent[par_a] = par_b
            self.rank[par_b] = max(self.rank[par_b], self.rank[par_a] + 1)

        return True
        
                
    def find(self,a):
        if self.parent[a] == a:
            return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
        
        
class Solution:
    def kruskal(self, edges, include, avoid,n):

        edgess = []
        uf = UnionFind(n)
        ans = 0
        for i in edges:
            if i == include:
                ans += i[2]
                uf.union(i[0], i[1])
            elif i == avoid:
                continue
            else:
                edgess.append([i[2], i[0], i[1]])

        heapq.heapify(edgess)

        while len(edgess) > 0:
            edge = heapq.heappop(edgess)
            if uf.union(edge[1],edge[2]):
                ans += edge[0]
        
        if avoid != [] and uf.union(avoid[0], avoid[1]):
            return -1

        return ans
        
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        mst = self.kruskal(edges, [], [],n)
        critical = []
        pcritical = []
        index = -1
        for i in edges:
            index += 1
            imst = self.kruskal(edges,[], i,n)
            pmst = self.kruskal(edges,i, [],n)
            print(mst, imst)
            if imst == -1 or imst > mst:
                critical.append(index)
            elif pmst == mst:
                pcritical.append(index)
        return [critical,pcritical]
                
            

        
