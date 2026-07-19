from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        @cache
        def helper(n):
            if n >= len(cost):
                return 0
            return cost[n] + min(helper(n+1), helper(n+2))
        
        return min(helper(0), helper(1))