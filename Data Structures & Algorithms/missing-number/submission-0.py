class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        return abs(sum(nums) - len(nums) * (len(nums) + 1) // 2)

        