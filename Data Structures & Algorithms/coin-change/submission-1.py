from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(i, amount):
            if amount == 0:
                return 0
            if i == len(coins) or amount < 0:
                return float('inf')
            return  min(dfs(i+1, amount), 1 + dfs(i, amount - coins[i]))
        
        ans =  dfs(0, amount)
        if ans == float('inf'):
            return -1
        return ans
        