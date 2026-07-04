class Solution:
    def solve(self, board: List[List[str]]) -> None:
        que  =[]
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'K'
                    if i == 0 or i == len(board) -1 or j == 0 or j == len(board[0]) -1:
                        que.append((i,j))
        
        
        print(board)
        while que:
            print(que)
            i,j = que.pop(0)
            board[i][j] = 'O'
            nei  = [[0,1],[1,0],[-1,0], [0, -1]]
            
            for ne in nei:
                nx = i + ne[0]
                ny = j + ne[1]
            
                if nx >=0 and ny >= 0 and nx < len(board) and ny < len(board[0]) and  board[nx][ny] == 'K':
                    board[nx][ny] = 'O'
                    que.append((nx,ny))
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'K':
                    board[i][j] = 'X'
