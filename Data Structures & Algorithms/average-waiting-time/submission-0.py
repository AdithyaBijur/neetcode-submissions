class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting = 0
        
        curr = 0
        i = 0

        while i < len(customers):
            if customers[i][0] <= curr:
                waiting += customers[i][1] + (curr - customers[i][0])
                curr += customers[i][1]
                i+=1
            else:
                curr += 1
        
        
        return waiting / len(customers)