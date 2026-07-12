class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        padded_heights = [0] + heights + [0]
        sl = [0 for i in range(len(padded_heights))]
        sr = [0 for i in range(len(padded_heights))]

        stack = []

        for i in range(len(padded_heights)):
            while stack and padded_heights[stack[-1]] > padded_heights[i]:
                sr[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        stack = []
        for i in range(len(padded_heights) -1 ,-1, -1):
            while stack and padded_heights[stack[-1]] > padded_heights[i]:
                sl[stack[-1]] = i
                stack.pop()
            stack.append(i)
        
        ans = 0
        for i in range(1, len(heights)+1):
            ans = max(ans, heights[i-1] * (sr[i] - sl[i]-1))
        
        return ans