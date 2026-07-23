class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        def isSmall(a, b):
            if a[0] > b[0]:
                return False
            if a[0] == b[0]:
                return a[1] < b[1]
            return True

        low = 0
        high = len(intervals)-1

        ans = high + 1
        while low <= high:
            mid = low + (high - low)//2
            if isSmall(intervals[mid],newInterval):
                low = mid + 1
            else:
                ans = mid
                high = mid - 1
        
        ind = ans
        print(ans)
        intervals.insert(ans, newInterval)
        print(intervals)

       # 1,2 3,4    1,2 2,4.   1,5 2,3
        
        ans = []

        for inter in intervals:
            if not ans or inter[0] > ans[-1][1]:
                ans.append(inter)
            else:
                ans[-1][1] = max(ans[-1][1], inter[1])
            
        return ans