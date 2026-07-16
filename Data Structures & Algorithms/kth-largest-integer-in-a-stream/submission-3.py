class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        self.k = k
        

    def add(self, val: int) -> int:

        if len(self.heap) == self.k and self.heap[0] < val:
            heapq.heappop(self.heap)
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        print(self.heap)
        return self.heap[0]
    



        
