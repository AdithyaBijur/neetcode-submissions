class Solution:
    def findMin(self, nums: List[int]) -> int:
        low  =0 
        high = len(nums) - 1

        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            if nums[mid] <= nums[high]:
                ans = mid
                high -= 1
            else:
                low += 1
        
        return nums[ans]
