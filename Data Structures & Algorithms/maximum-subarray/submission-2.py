class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        s = 0
        ans = 0

        for i in nums:
            s += i
            s = max(s, 0)
            ans = max(ans, s)
        
        if ans == 0:
            return max(nums)
        return ans