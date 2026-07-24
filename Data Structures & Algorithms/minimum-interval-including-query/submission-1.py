class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        queryIndex = collections.defaultdict(list)
        for q in range(len(queries)):
            queryIndex[queries[q]].append(q)
        
        queries.sort()
        intervals.sort()

        print(intervals, queries, queryIndex)

        i = 0
        heap = []

        ans = [-1 for i in range(len(queries))]

        for q in queries:
            while i < len(intervals) and intervals[i][0] <= q:
                heapq.heappush(heap, [intervals[i][1] - intervals[i][0] + 1, intervals[i][1]])
                i+=1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            if len(heap) != 0:
                interval =  heap[0]
                print(interval)
                for ind in queryIndex[q]:
                    ans[ind] = interval[0]#length
            
        return ans
