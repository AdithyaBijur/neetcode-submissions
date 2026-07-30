from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        
        i = 0
        maxJump = nums[0]
        jump = 0

        while i < len(nums) - 1:
            farthest = i
            ind = i
            for j in range(i+1, min(maxJump+1, len(nums))):
                farthest = max(farthest, nums[j] + j)
                if farthest == nums[j] + j:
                    ind = j
            i = maxJump
            jump += 1
            maxJump = farthest
        return jump
