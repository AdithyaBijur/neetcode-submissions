from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        @cache
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            if buy:
                return max(dfs(i+1, False) - prices[i], dfs(i+1, True) )
            else:
                return max(prices[i] + dfs(i+2, True), dfs(i+1, False))

        return dfs(0, True)
        