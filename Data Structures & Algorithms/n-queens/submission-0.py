class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        
        def isPossible(i,j, pos):


            for row in range(0, n):
                if [row, j] in pos:
                    return False

            for col in range(0, n):
                if [i, col] in pos:
                    return False
            
            ii = i
            jj = j
            while jj >= 0:
                if [ii, jj] in pos:
                    return False
                ii -= 1
                jj -= 1
            
            ii = i
            jj = j
            while jj < n and i > n:
                if [ii, jj] in pos:
                    return False
                ii += 1
                jj +=1 


            ii = i
            jj = j
            while jj < n and i >= 0:
                if [ii, jj] in pos:
                    return False
                ii -= 1
                jj += 1
            
            ii = i
            jj = j
            while jj >= 0 and i < n:
                if [ii, jj] in pos:
                    return False
                ii += 1
                jj -=1 

            return True

            


        ans = []
        def recur(row, pos):
            print(row, pos)
            if row == n:
                ans.append(pos[:])
                return
            
            for j in range(n):
                if isPossible(row,j, pos):
                    pos.append([row,j])
                    recur(row+1, pos)
                    pos.pop()
                
        recur(0, [])
        anss = []

        def generate(ans):
            mat = [['.' for i in range(n)] for j in range(n)]
            
            for pt in ans:
                mat[pt[0]][pt[1]] = 'Q'
            
            arr = []

            print(ans)

            for row in mat:
                arr.append(''.join(row))
            return arr
        
        for pos in ans:
            anss.append(generate(pos))
        
        return anss
            
        