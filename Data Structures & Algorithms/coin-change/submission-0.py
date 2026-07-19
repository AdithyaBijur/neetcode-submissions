from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def dfs(i, amount):
            print(i, amount)
            if amount == 0:
                return 0
            if i == len(coins):
                return float('inf')
            ans = dfs(i+1, amount)
            curr = amount - coins[i]
            used = 1
            while curr >= 0:
                ans = min(ans, used + dfs(i+1, curr))
                curr -= coins[i]
                used+= 1
                

            return ans
        
        ans =  dfs(0, amount)
        if ans == float('inf'):
            return -1
        return ans
        