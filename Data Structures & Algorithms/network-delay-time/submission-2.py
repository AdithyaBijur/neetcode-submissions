class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph  = [[float("inf") for i in range(1 + n)] for j in range(1 + n)]
        distance = [float("inf") for i in range(1+n)]
        distance[k] = 0
        
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        

        heap = []
        heap.append((0,k))

        while heap:
            dist, node = heapq.heappop(heap)
            if dist > distance[node]:
                continue
            
            for nei, wt in graph[node]:
                if distance[nei] > dist + wt:
                    distance[nei] = dist + wt
                    heapq.heappush(heap,[distance[nei], nei])
                    
        
        ans =  max(distance[1:])
        if ans == float('inf'):
            return -1
        return ans