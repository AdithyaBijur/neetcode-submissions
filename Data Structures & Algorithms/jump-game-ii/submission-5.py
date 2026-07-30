from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        jump = 0
        currMax = 0
        farthest = 0
        for i in range(0, len(nums) - 1):

            farthest = max(farthest, nums[i] + i)
            if currMax <= i:
                jump += 1
                currMax = farthest
        return jump

