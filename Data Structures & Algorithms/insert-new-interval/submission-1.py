class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        i = 0
        while i < len(intervals):
            interval = intervals[i]
            if interval[0] < newInterval[0]:
                i+=1
            elif interval[0] == newInterval[0]:
                if interval[0] <= newInterval[0]:
                    i+=1
            else:
                break
            
        intervals.insert(i, newInterval)

       # 1,2 3,4    1,2 2,4.   1,5 2,3
        
        ans = []

        for inter in intervals:
            if not ans or inter[0] > ans[-1][1]:
                ans.append(inter)
            else:
                ans[-1][1] = max(ans[-1][1], inter[1])
            
        return ans