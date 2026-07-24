class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:[x[1], x[0]]) # sort by ending
        
        finish = intervals[0][1]
        removed = 0
        for interval in intervals[1:]:
            start = interval[0]
            end = interval[1]
            if start >= finish:
                finish = end
            else:
                removed += 1



        return removed
