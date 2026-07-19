from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def dfs(i):
            if i == len(s):
                return 1
            if s[i] < '1' or s[i] > '9':
                return 0

            if i+2 <= len(s) and int(s[i:i+2]) <= 26:
                return  dfs(i+1) + dfs(i+2)
            else:
                return dfs(i+1)
            
        return dfs(0)
        