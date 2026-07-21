class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        def dfs(start, curr, rem):
            if rem == 0:
                ans.append(curr[:])
            if rem < 0:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, curr, rem - nums[i])
                curr.pop()  
            
        dfs(0, [], target)
        return ans
        