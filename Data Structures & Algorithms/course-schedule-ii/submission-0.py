class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:


        graph = collections.defaultdict(list)

        for p in prerequisites:
            graph[p[0]].append(p[1])

        visited = {}
        ans = []
        

        def dfs(node):
            if node in visited:
                if visited[node] == 1:
                    return False
                if visited[node] == 2:
                    return True       # already checked

    
            visited[node] = 1
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            
            visited[node] = 2
            ans.append(node)
            return True

        for i in range(n):
            if i not in visited and not dfs(i):
                return []
        return ans