# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        fast = head
        i = 0

        while i <= n:
            if fast == None:
                return head.next
            fast = fast.next
            i+=1

        slow = head

        while fast != None:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return head
        

        