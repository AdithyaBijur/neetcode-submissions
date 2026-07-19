from functools import cache
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        @cache
        def dfs(i, flag):
            if flag and i >= len(nums) - 1:
                return 0
            if not flag and i >= len(nums):
                return 0
            return max(nums[i] + dfs(i+2, flag), dfs(i+1, flag))

        
        return max(dfs(0, True), dfs(1, False))

        