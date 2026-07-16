class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskDict = Counter(tasks)
        heap = []

        for key in taskDict:
            heap.append([-taskDict[key], key])
        heapq.heapify(heap)

        currTime = 0
        skip = {}
        taskC = len(tasks)
        
        while taskC > 0:
            print(heap)
            currTime += 1
            if len(heap) == 0:
                if currTime in skip:
                    heapq.heappush(heap,skip[currTime])
                    del(skip[currTime])
                continue
            
            task = heapq.heappop(heap)
            task[0] += 1
            taskC -= 1
            if task[0] != 0:
                skip[currTime + n] = task
            if currTime in skip:
                    heapq.heappush(heap, skip[currTime])
                    del(skip[currTime])
            
        
        return currTime
            
        