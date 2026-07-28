class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:


        distance = [[float('inf') for j in range(k+2)] for i in range(n)]
        print(distance)
        minK = [k for i in range(n)]
        distance[src][0] = 0

        graph = collections.defaultdict(list)

        for flight in flights:
            graph[flight[0]].append([flight[2], flight[1]])
        
        heap = [(0,0, src)]

        while heap:
            cost,stops,node = heapq.heappop(heap)
            if stops > k:
                continue
            if cost > distance[node][stops]:
                continue


            for nei in graph[node]:
                nei_cost = nei[0]
                print(stops + 1)
                if distance[nei[1]][stops+1] > nei_cost + cost:
                    minK = stops + 1
                    distance[nei[1]][stops+1] = nei_cost + cost
                    heapq.heappush(heap, (nei_cost + cost, stops+1, nei[1]))
        
        ans =  min(distance[dst])
        if ans == float('inf'):
            return -1
        return ans

        