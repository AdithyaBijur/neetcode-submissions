from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        
        @cache
        def dfs(i):
            if i == len(nums) -1:
                return 0

            ans = float("inf")
            for ind in range(i+1, min(i+nums[i]+1, len(nums))):
                ans = min(ans, 1 + dfs(ind))
            return ans

        return dfs(0)