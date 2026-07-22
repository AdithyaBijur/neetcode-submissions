class Solution:
    def solve(self, grid: List[List[str]]) -> None:
        que = []
        nei = [[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i == 0 or j == 0 or i == len(grid) -1 or j == len(grid[0]) - 1) and grid[i][j] == 'O':
                    que.append([i,j])
                    grid[i][j] = 'Z'
 

        level = 0
        while que:
            level += 1
            n = len(que)
            for i in range(n):
                node = que.pop(0)
                for n in nei:
                    nx = node[0] + n[0]
                    ny = node[1] + n[1]
                    if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == 'O':
                        grid[nx][ny] = 'Z'
                        que.append([nx,ny])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'Z':
                    grid[i][j] = 'O'
                else:
                    grid[i][j] = 'X'