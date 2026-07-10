class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #row
        # print("here")
        for row in board:
            t = set()
            for i in row:
                if i in t:
                    return False
                if i != ".":
                    t.add(i)
        
        # print("here")

        #col

        for j in range(0, len(board[0])):
            t = set()
            for i in range(0, len(board)):
                print(t)
                if board[i][j] in t:
                    return False
                if board[i][j] != ".":
                    t.add(board[i][j])
        print("here")
        #box

        def check(row_start,col_start):
            t = set()
            for i in range(row_start, row_start+3):
                for j in range(col_start, col_start+3):
                    if board[i][j] in t:
                        return False
                    if board[i][j] != ".":
                        t.add(board[i][j])
            return True

        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                if not check(i,j):
                    return False
        return True

        