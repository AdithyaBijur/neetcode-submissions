# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random
from itertools import count


class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap = []   
        k = len(lists)
        counter = count()

        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, next(counter), node))

        dummy = ListNode()
        curr = dummy
        while len(heap) > 0:
            node = heapq.heappop(heap)
            if node[2].next:
                heapq.heappush(heap, (node[2].next.val, next(counter),  node[2].next))
            node[2].next = None
            curr.next = node[2]
            curr = curr.next
            
        return dummy.next




