class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        def markZero(i,j):
            for col in range(0, len(matrix[0])):
                if matrix[i][col]!= -1:
                    matrix[i][col] = 0

            for row in range(0, len(matrix)):
                if matrix[row][j]!= -1:
                    matrix[row][j] = 0            
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][j] = -1
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if matrix[i][j] == -1:
                    markZero(i,j)
        
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                 if matrix[i][j] == -1:
                    matrix[i][j] = 0

