class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        que = []
        nei = [[0,1],[1,0],[-1,0],[0,-1]]
        INF = 2147483647

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    que.append([i,j])
 

        level = 0
        while que:
            level += 1
            n = len(que)
            for i in range(n):
                node = que.pop(0)
                for n in nei:
                    nx = node[0] + n[0]
                    ny = node[1] + n[1]
                    if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == INF:
                        grid[nx][ny] = level
                        que.append([nx,ny])

