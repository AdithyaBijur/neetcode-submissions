class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(start , curr):
            ans.append(curr[:])

            for i in range(start, len(nums)):
                curr.append(nums[i])
                dfs(i+1, curr)
                curr.pop()
            
        
            
        dfs(0, [])
        return ans