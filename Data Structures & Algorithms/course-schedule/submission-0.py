class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:

        graph = collections.defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])

        visited = {}

        def dfs(node):
            if node in visited and visited[node] == 1:
                return False
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = 2
            return True

        for i in range(n):
            if i not in visited and not dfs(i):
                return False
        return True

        