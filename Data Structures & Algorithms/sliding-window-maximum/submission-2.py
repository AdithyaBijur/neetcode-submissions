class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
            d = deque()
            if k >= len(nums):
                return [max(nums)]
            for i in range(k):
                while d and nums[d[-1]] <= nums[i]:
                        d.pop()
                d.append(i)
            
            ans = []
            ans.append(nums[d[0]])
            for i in range(k, len(nums)):
                while d and nums[d[-1]] <= nums[i]:
                        d.pop()
                d.append(i)
                while d and d[0] <= i -k:
                    print(d,i)
                    d.popleft()
                ans.append(nums[d[0]])
            return ans
