def getDistance(x,y):
    return abs(pow(x,2) + pow(y,2))
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            d = getDistance(point[0], point[1])
            if len(heap) == k and abs(heap[0][0]) > d:
                heapq.heappop(heap)
            if len(heap) < k:
                heapq.heappush(heap, (-d, point[0], point[1]))
            
        ans = []
        for i in range(len(heap)):
            node =  heapq.heappop(heap)
            ans.append([node[1],node[2]])
        
        return ans
            
            
            

        
        
