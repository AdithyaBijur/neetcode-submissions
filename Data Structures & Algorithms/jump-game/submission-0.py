class Solution:
    def canJump(self, nums: List[int]) -> bool:
        j = len(nums) - 1
        if len(nums) <= 1:
            return True

        while j >= 0:
            i = j - 1
            while i >= 0:
                if nums[i] + i >= j:
                    j = i
                    break
                else:
                    i-=1
            if j == 0:
                return True
            if i < 0:
                return False
        
            

        


        