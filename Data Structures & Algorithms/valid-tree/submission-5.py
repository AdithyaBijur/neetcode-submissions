class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)

        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])

        def dfs(node, parent, visited):
            visited.add(node)
            for n in graph[node]:
                if n == parent:
                    continue
                if n in visited:
                    return False
                if not dfs(n, node, visited):
                    return False
            return True
        
        visited =set()
        if not dfs(0, -1, visited):
            return False
        for i in range(n):
            if i not in visited:
                return False
        return True
        