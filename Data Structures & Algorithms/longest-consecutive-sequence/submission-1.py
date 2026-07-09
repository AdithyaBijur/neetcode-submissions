from functools import cache
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dp = collections.defaultdict(int)
        s= set()
        for i in nums:
            s.add(i)

        ans = 0

        for i in nums:
            if i - 1 in s:
                continue
            j = i + 1
            while j in s:
                j += 1
            ans = max(ans, j -i)
        
        return ans