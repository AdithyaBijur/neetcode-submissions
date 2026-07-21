class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ans = []
        def dfs(start, curr):
            if sum(curr) == target:
                ans.append(curr[:])
            if sum(curr) > target:
                return

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i, curr)
                curr.pop()  
            
        dfs(0, [])
        return ans
        