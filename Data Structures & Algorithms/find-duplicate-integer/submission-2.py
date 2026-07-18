class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == i+1:
                i+= 1
                continue
            if nums[num - 1] == num:
                return num
            
            nums[i] = nums[num - 1] 
            nums[num - 1] = num
        
        print(nums)
        