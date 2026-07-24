class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        
        for i in range(0, len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for ind, row in enumerate(matrix):
            matrix[ind] = row[::-1]
        
        