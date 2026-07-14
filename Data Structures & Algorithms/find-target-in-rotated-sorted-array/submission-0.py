class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(arr, target):
            print(arr, target)
            low  =0 
            high = len(arr) - 1
            while low <= high:
                mid = low + (high - low)//2
                if arr[mid] == target:
                    return mid
                elif target > arr[mid]:
                    low   = mid + 1
                else:
                    high = mid - 1
            
            return -1
        
        low  =0 
        high = len(nums) - 1

        ans = 0
        while low < high:
            mid = low + (high - low)//2
            if nums[mid] <= nums[high]:
                high = mid
            else:
                low = mid + 1
        
        minm =  high
        left = bs(nums[:minm], target)
        right =  bs(nums[minm:], target)
        if left == -1 and right == -1:
            return -1
        if left == -1:
            return  minm + right
        else:
            return  left

