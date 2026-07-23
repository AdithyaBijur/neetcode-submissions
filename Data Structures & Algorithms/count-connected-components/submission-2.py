class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)

        for p in edges:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])


        visited = {}
        

        def dfs(node):    
            visited[node] = 1
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        ans = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                ans += 1
        return ans