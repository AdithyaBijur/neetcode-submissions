class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:


        def dfs(i,j):

            nei = [[0,1],[1,0], [0,-1],[-1,0]]

            for n in nei:
                nx = i + n[0]
                ny = j + n[1]
            
                if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == '1':
                    grid[nx][ny] = '0'
                    dfs(nx,ny)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    grid[i][j] = 0
                    ans += 1
                    dfs(i,j)
        return ans

        