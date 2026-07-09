from functools import cache
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)
        s= set()
        for i in nums:
            s.add(i) 

        @cache
        def dp(n):
            if n not in s:
                return 0
            return 1 + dp(n-1)
        
        ans = 0

        for i in nums:
            ans = max(ans, dp(i))
        
        return ans
