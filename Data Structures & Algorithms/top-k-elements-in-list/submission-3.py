class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = collections.defaultdict(int)

        for i in nums:
            count[i] += 1
        
        heap = []

        for i in count:
            while len(heap) >= k and heap[0][0] < count[i]:
                heapq.heappop(heap)
            
            if len(heap) < k:
                heapq.heappush(heap, (count[i], i))
        
        ans = []

        while heap:
            ans.append(heapq.heappop(heap)[1])

        return ans
        