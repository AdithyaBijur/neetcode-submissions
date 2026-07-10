class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        i = 0
        j = 0
        k = 0
        ans = []
        print(nums)
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j  = i+1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                if nums[j] + nums[k] == target:
                    ans.append([nums[i], nums[j], nums[k]])
                if nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
                    while j <k and nums[j] == nums[j-1]:
                        j+=1

            
        return ans
        