# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        i = list1
        j = list2

        head = ListNode()
        curr = head

        while i is not None and j is not None:
            if i.val <= j.val:
                curr.next = i
                temp = i.next
                i.next = None
                i = temp
            else:
                curr.next = j
                temp = j.next
                j.next = None
                j = temp
            curr = curr.next
            
        if i is not None:
            curr.next = i
        else:
            curr.next = j

        return head.next
                
        