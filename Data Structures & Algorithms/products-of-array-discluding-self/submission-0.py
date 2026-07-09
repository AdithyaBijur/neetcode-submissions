class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1 for i in range(len(nums) + 1)]
        suffix = [1 for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            prefix[i+1]= prefix[i] * nums[i]
        
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        ans = [ 1 for i in range(len(nums))]

        for i in range(len(nums)):
            ans[i] = prefix[i] * suffix[i+1]
        
        return ans


        # 1 2 4 6
        # 1  1  2  8 48
        # 48 48 24 6 1