class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        i = 0
        j = 0
        k = 0
        ans = []
        print(nums)
        while i < len(nums) - 2:
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
                    while nums[j] == nums[j-1] and j <k:
                        j+=1

            i+=1
            while  i < len(nums) and nums[i] == nums[i-1]:
                i+=1
            
        return ans
        