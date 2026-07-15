# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            if node == None:
                return None
            if node.next == None:
                return node
            temp = node.next
            head = reverse(node.next)
            node.next.next = node
            node.next = None
            return head
            
            
        return reverse(head)