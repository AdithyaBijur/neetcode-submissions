import bisect
from functools import cache
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @cache
        def help(i):
            if i >= len(days):
                return 0
            return min(costs[0] + help(bisect.bisect_right(days,days[i]+ 0)),
            costs[1] + help(bisect.bisect_right(days,days[i]+ 6)),
            costs[2] + help(bisect.bisect_right(days,days[i]+ 29))) 


        return help(0)
        