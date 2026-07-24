class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        sorted_queries = sorted([(q,i) for i,q in enumerate(queries)])
        intervals.sort()

        i = 0
        heap = []

        ans = [-1 for i in range(len(queries))]

        for q, index in sorted_queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i+=1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if len(heap) != 0:
                interval =  heap[0]
                ans[index] = interval[0]#length
    
            
        return ans
