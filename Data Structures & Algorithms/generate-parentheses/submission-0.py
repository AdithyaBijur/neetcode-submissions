class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        ans = []
        def dfs(open, close, curr):
            if open == 0 and close == 0:
                ans.append(curr)
            
            if open:
                dfs(open-1, close, curr + '(')
            if close > open:
                dfs(open, close-1, curr + ')')
        
        dfs(n,n, "")
        return ans