class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        que = collections.deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    que.append((i,j))
        
        nei = [(0,1),(1,0), (0,-1),(-1,0)]
        level = 0
        
        while que:
            ll = len(que)
            level += 1
            for _ in range(ll):
                i,j = que.popleft()

                for ni,nj in nei:
                    nx = ni + i
                    ny = nj + j

                    if nx >=0 and ny >= 0 and nx < len(grid) and ny < len(grid[0]) and grid[nx][ny] == 2147483647:
                        grid[nx][ny] = level
                        que.append((nx,ny))
                    
            


        