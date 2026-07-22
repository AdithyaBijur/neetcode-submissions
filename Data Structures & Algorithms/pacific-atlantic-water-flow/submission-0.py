class Solution:
    def pacificAtlantic(self, grid: List[List[int]]) -> List[List[int]]:

        que = []
        nei = [[0,1],[1,0],[-1,0],[0,-1]]
        ans = [[set() for j in range(len(grid[0]))] for i in range(len(grid))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0:
                    que.append([i,j,0])
                    ans[i][j].add(0)
                if i == len(grid) - 1 or j == len(grid[0]) -1:
                    que.append([i,j,1])
                    ans[i][j].add(1)
                if i == 0 and j == len(grid[0]) - 1:
                    que.append([i,j,1])
                    ans[i][j].add(1)
                if j == 0 and i == len(grid) -1:
                    que.append([i,j,0])
                    ans[i][j].add(0)
 

        level = 0
        while que:
            level += 1
            n = len(que)
            for i in range(n):
                node = que.pop(0)
                for n in nei:
                    nx = node[0] + n[0]
                    ny = node[1] + n[1]
                    if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] >= grid[node[0]][node[1]]  and node[2] not in ans[nx][ny]:
                        ans[nx][ny].add(node[2])
                        que.append([nx,ny, node[2]])

        anss = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if len(ans[i][j]) == 2:
                    anss.append([i,j])
        return anss
        