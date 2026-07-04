class UnionFind:
    def __init__(self):
        self.parent = {}
        self.length = {}
    
    def union(self,a,b):
        parent_a = self.find(a)
        parent_b = self.find(b)

        if parent_a == parent_b:
            return True
        
        length_a = self.length[parent_a]
        length_b = self.length[parent_b]

        if length_a <= length_b:
            self.length[parent_a] = 1 + length_b
            self.parent[parent_b] = parent_a 
        else:
            self.length[parent_b] = 1 + length_a
            self.parent[parent_a] = parent_b
        
        return False
            

    def find(self,node):
        if node not in self.parent:
            self.parent[node] = node
            self.length[node] = 0
            return node
        
        parent = self.parent[node]
        if parent == node:
            return node
        
        self.parent[node] = self.find(parent)
        return self.parent[node]

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind()
        for edge in edges:
            if uf.union(edge[0], edge[1]):
                return edge
        return []

        
        