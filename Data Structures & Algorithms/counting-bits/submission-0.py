from functools import cache
class Solution:
    def countBits(self, n: int) -> List[int]:
        
        @cache
        def dfs(n):
            if n == 1:
                return 1
            if n == 0:
                return 0
            
            nn = 1 << (n.bit_length() - 1)
            return 1 + dfs(n - nn)

        ans = []
        for i in range(n+1):
            ans.append(dfs(i))
        return ans