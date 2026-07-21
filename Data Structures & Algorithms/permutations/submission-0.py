class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        seen = set()
        ans = []

        def dfs(pos, curr):

            if pos == len(nums):
                ans.append(curr[:])
                return
            
            for i in range(0, len(nums)):

                if i not in seen:
                    seen.add(i)
                    curr.append(nums[i])
                    dfs(pos+1, curr)
                    seen.remove(i)
                    curr.pop()
            
        dfs(0, [])
        return ans