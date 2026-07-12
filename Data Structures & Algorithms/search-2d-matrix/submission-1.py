class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def getPos(ind):
            return [ind // len(matrix[0]), ind % len(matrix[0])]

        low = 0
        high = len(matrix) * len(matrix[0]) -1

        while low <= high:
            mid = low + (high - low) // 2
            pos = getPos(mid)
            print(pos[0], pos[1] ,mid)
            ele = matrix[pos[0]][pos[1]]
            if ele == target:
                return True
            elif target > ele:
                low += 1
            else:
                high -= 1
            
        return False