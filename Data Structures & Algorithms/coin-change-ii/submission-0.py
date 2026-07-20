from functools import cache
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def dfs(i, amount):
            if amount == 0:
                return 1
            if i == len(coins) or amount < 0:
                return 0
            
            return dfs(i, amount - coins[i]) + dfs(i+1, amount)
        
        return dfs(0, amount)