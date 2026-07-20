from functools import cache
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        @cache
        def dfs(summ, i):
            if i == len(nums):
                if summ == 0:
                    return True
                return False
            
            return dfs(summ - nums[i], i+1) or dfs(summ, i+1)
        
        return dfs(sum(nums)//2, 0)
