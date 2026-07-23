"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        events = []
        for i in intervals:
            events.append([i.start, 1])
            events.append([i.end, 0])

        events.sort()

        cnt = 0
        ans = 0
        print(events)
        for i in events:
            if i[1] == 0:
                cnt -= 1
            else:
                cnt += 1
            ans = max(ans, cnt)
        return ans
