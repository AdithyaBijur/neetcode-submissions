class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        m = 0
        ans = 0
        for i in range(len(prices)-1,-1,-1):
            m = max(m, prices[i])
            ans = max(ans, m - prices[i])
        
        return ans

