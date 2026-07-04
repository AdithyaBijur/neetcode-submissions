from functools import cache
class Solution:
    def maxCoins(self, numss: List[int]) -> int:
        nums = [1] + numss + [1]
        print(nums)
        @cache
        def helper(i,j):
            print(i,j)
            if j - i <=1:
                return 0
            
            # if i > j or i < 0 or j >= len(nums):
            #     return 1
            
            ans = 0
            for k in range(i+1, j):
                ans = max(ans, nums[i] * nums[k] * nums[j] + helper(i,k) + helper(k,j))
            
            return ans
        
        return helper(0, len(nums)-1)
