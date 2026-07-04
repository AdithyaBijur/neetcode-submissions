class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = 0
        
        curr = 0
        
        for c in customers:
            curr = max(curr, c[0])
            curr += c[1]
            waiting += curr  - c[0]
        
        return waiting / len(customers)