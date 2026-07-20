from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def dfs(i,j):
            if j == len(s) - 1:
                if s[i:j+1] in wordDict:
                    return True
                else:
                    return False
            if s[i:j+1] in wordDict:
                return dfs(j+1,j+1) or dfs(i, j+1)
            return dfs(i, j+1)

        return dfs(0,0) 
        