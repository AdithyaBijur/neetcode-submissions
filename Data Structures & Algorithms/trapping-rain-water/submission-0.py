class Solution:
    def trap(self, height: List[int]) -> int:
        mleft = [0]
        mright = [0 for i in range(len(height) + 1)]

        maxx = 0

        for i in range(len(height)):
            maxx = max(maxx, height[i])
            mleft.append(maxx)

        maxx = 0

        for i in range(len(height)-1,-1,-1):
            maxx = max(maxx, height[i])
            mright[i] = maxx
        
        ans = 0
        for i in range(len(height)):
            ans += max(0, min(mleft[i], mright[i]) - height[i])

        print(mleft, mright)
        return ans
        