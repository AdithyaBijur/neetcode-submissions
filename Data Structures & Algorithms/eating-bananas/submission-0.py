class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)


        def isPossible(num):

            ans = 0
            for i in piles:
                ans += math.ceil(i / num)
            
            return ans <= h

        ans = -1
        while low <= high:
            mid  = low + (high - low) //2 
            if isPossible(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        
        return ans


