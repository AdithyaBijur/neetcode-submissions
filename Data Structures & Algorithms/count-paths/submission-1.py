from functools import cache
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        @cache
        def dfs(i, j):
            if i == m-1 and j == n-1:
                return 1
            nei = [[0,1],[1,0]]

            ans = 0
            for ne in nei:
                nx = i + ne[0]
                ny = j + ne[1]
                if nx >=0 and nx < m and ny >= 0 and ny < n:
                    ans += dfs(nx, ny)
            
            return ans
        
        return dfs(0,0)