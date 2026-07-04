class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def hasCycle(node, visited, parent):
            nonlocal graph
            if node in visited:
                return True
                    
            visited[node] = 1
            
       
            for nei in graph[node]:
                if nei == parent:
                    continue
                if hasCycle(nei, visited, node):
                    return True
            visited[node] = 2
            return False
        
        visited = {}

        if hasCycle(0, visited, -1):
                    return False
        for i in range(n):
            if i not in visited:
                    return False
        return True


