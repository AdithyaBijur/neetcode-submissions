# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverse(node):
            if node is None or node.next is None:
                return node
            
            newHead = reverse(node.next)
            node.next.next = node
            node.next = None
            return newHead
            

        dummy = ListNode()
        dummy.next = head

        a = dummy
        b = dummy
        c = None

        while b is not None:
            i = 0
            while b.next and i < k:
                b= b.next
                i+=1
            if i < k:
                return dummy.next
            c = b.next
            b.next = None
            newHead = reverse(a.next)
            a.next.next = c
            temp = a.next
            a.next = newHead
            a = temp
            b = a


        return dummy.next

            



        