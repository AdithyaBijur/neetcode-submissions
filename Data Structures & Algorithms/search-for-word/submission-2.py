class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited = set()
        def dfs(i,j,k):
            visited.add((i,j))
            if k == len(word):
                return True
            
            nei = [[0,1],[1,0],[-1,0],[0,-1]]

            for n in nei:
                nx = i + n[0]
                ny = j + n[1]
                if nx >= 0 and ny >= 0 and nx < len(board) and ny < len(board[0]) and board[nx][ny] == word[k] and (nx,ny) not in visited:
                   
                    if dfs(nx,ny,k+1):
                        return True
                    # visited.remove((nx,ny))
            visited.remove((i,j))
                
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == word[0] and dfs(i,j,1):
                    return True
        
        return False