"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        d = {} #old to new

        if head == None:
            return None

        curr = head
        while curr:
            d[curr] = Node(curr.val)
            curr = curr.next
        
        currNew = d[head]
        currOld = head

        while currOld:
            if currOld.next:
                currNew.next = d[currOld.next]
            if currOld.random:
                currNew.random = d[currOld.random]
            currNew = currNew.next
            currOld = currOld.next
        
        return d[head]

