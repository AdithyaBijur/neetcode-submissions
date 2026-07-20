from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        @cache
        def dfs(i,j):
            nei = [[0,1], [1,0], [0,-1], [-1,0]]
            ans = 1
            for n in nei:
                nx = i + n[0]
                ny = j + n[1]
                if nx >= 0 and ny >= 0 and nx < len(matrix) and ny < len(matrix[0]) and matrix[nx][ny] > matrix[i][j]:
                    ans = max(ans, 1 + dfs(nx,ny))
                
            return ans
        
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans, dfs(i,j))
            
        return ans