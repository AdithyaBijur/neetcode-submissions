class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        nums = sorted(candidates)
        ans = []
        def dfs(start, rem, curr):
            if rem == 0:
                ans.append(curr[:])
                return
            if rem < 0:
                return
            
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                
                curr.append(nums[i])
                dfs(i+1, rem - nums[i], curr)
                curr.pop()
            
            return 
        
        dfs(0, target, [])
        return ans
