class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        nei = [[0,1],[1,0],[-1,0],[0,-1]]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
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
                    if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        que.append([nx,ny])
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return max(0, level - 1)