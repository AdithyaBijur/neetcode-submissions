class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heap.append(-i)
        heapq.heapify(heap)

        while len(heap) > 1:
            print(heap)
            one = abs(heapq.heappop(heap))
            two = abs(heapq.heappop(heap))
            three = one - two
            if three > 0:
                heapq.heappush(heap, -three)
        
        if len(heap) > 0:
            return abs(heap[0])
        else:
            return 0
